# Sinh PDF LaTeX gửi HS Buổi 1 (bài giảng đầy đủ theo khung chuyên đề Sóng) từ buoi1_spec.py. Bản HS: không có đáp án.
import os, re, shutil, subprocess, sys, zipfile
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, ROOT)
import buoi1_spec as S
from anh_chuyen_de import so_hinh

TEMPLATE = '/root/.claude/skills/synced/ef69f53a-273f-41a3-ad97-c64ccbfacd43_45acc2b8-d2ef-448f-99cf-f15468c28e37/tsa-exam-creator/assets/latex_hs/main_template.tex'
BUILD = os.path.join(HERE, 'latex')
CHUYEN_DE = 'Chuyên đề Cân bằng hóa học'
PDF_NAME = 'Buổi 1 - Cân bằng động, Kc và Q.pdf'
ZIP_NAME = 'Buoi1_Can_bang_dong_Kc_va_Q_Overleaf.zip'
FIG = so_hinh()

SUB = dict(zip('₀₁₂₃₄₅₆₇₈₉', '0123456789'))
SUP = dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺', '0123456789-+'))


def tx(s):
    s = s.replace('\\', r'\textbackslash{}')
    for a, b in (('&', r'\&'), ('%', r'\%'), ('#', r'\#'), ('_', r'\_')):
        s = s.replace(a, b)
    s = re.sub('[₀-₉]+', lambda m: '$_{%s}$' % ''.join(SUB[c] for c in m.group()), s)
    s = re.sub('[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+', lambda m: '$^{%s}$' % ''.join(SUP[c] for c in m.group()), s)
    for a, b in (('⇌', r'$\rightleftharpoons$'), ('→', r'$\rightarrow$'), ('−', r'$-$'),
                 ('×', r'$\times$'), ('≈', r'$\approx$'), ('≠', r'$\neq$'), ('·', r'$\cdot$'), ('′', r"$'$")):
        s = s.replace(a, b)
    s = s.replace('$$', '')
    s = re.sub(r'"([^"]*)"', r"``\1''", s)
    return s


def table(rows, label, cap):
    n = len(rows[0])
    longest = [max(len(r[j]) for r in rows) for j in range(n)]
    if sum(longest) > 70:
        tot = sum(longest); spec = '|'.join(r'>{\raggedright\arraybackslash}p{%.2f\textwidth}' % (0.9 * l / tot) for l in longest)
    else:
        spec = '|'.join('c' * n)
    L = [r'\Needspace{5cm}', r'\tablecaption{%s}{%s}' % (label, tx(cap)), r'{\small', r'\begin{center}',
         r'\renewcommand{\arraystretch}{1.3}', r'\begin{tabular}{|%s|}' % spec, r'\hline',
         r'\rowcolor{pastelBlue}', ' & '.join(r'\textbf{%s}' % tx(c) for c in rows[0]) + r' \\', r'\hline']
    for r in rows[1:]:
        L += [' & '.join(tx(c) for c in r) + r' \\', r'\hline']
    return '\n'.join(L + [r'\end{tabular}', r'\end{center}', '}'])


def figures(paths, used):
    w = {1: 0.6, 2: 0.47, 3: 0.31}[len(paths)]
    if len(paths) == 1:
        iw, ih = Image.open(os.path.join(ROOT, paths[0])).size
        w = 0.9 if iw > 2 * ih else w  # hình ngang (đồ thị hai khung) cần rộng mới đọc được
    L = [r'\Needspace{7cm}', r'\begin{center}']
    for k, f in enumerate(paths):
        shutil.copy(os.path.join(ROOT, f), os.path.join(BUILD, 'image')); used.add(os.path.basename(f))
        _, n, ten, nguon, _ = FIG[f]
        L.append(r'\begin{minipage}[t]{%.2f\textwidth}\centering' % w)
        L.append(r'\includegraphics[width=\linewidth,height=6cm,keepaspectratio]{image/%s}' % os.path.basename(f))
        L.append(r'\figcaption{%d}{%s}' % (n, tx(ten)))
        L.append(r'\vspace{-6pt}{\scriptsize\textit{Nguồn: %s}}' % tx(nguon))
        L.append(r'\end{minipage}' + (r'\hfill' if k < len(paths) - 1 else ''))
    return '\n'.join(L + [r'\end{center}'])


def fig_ref(t):
    return re.sub(r'\{H:([^}]+)\}', lambda m: str(FIG[m.group(1)][1]), t)


def build():
    os.makedirs(os.path.join(BUILD, 'Phan thi'), exist_ok=True)
    os.makedirs(os.path.join(BUILD, 'image'), exist_ok=True)
    used, out = set(), []
    out.append(r'\lessonsection{1. Khởi động}')
    k = S.KHOI_DONG; out.append(table(k['rows'], k['label'], k['cap']))
    for lab, txt in S.INTRO:
        out.append(r'\begin{notebox}%s%s\end{notebox}' % (r'\textbf{%s}' % tx(lab) if lab else '', tx(txt)))
    out.append(r'\lessonsection{%s}' % tx(S.TSA['title']))
    out += [tx(t) + '\n' for t in S.TSA['text']]
    out.append(r'\begin{itemize}[leftmargin=1.5em, itemsep=1pt]')
    out += [r'\item \textbf{%s}' % tx(g) for g in S.TSA['groups']]
    out.append(r'\end{itemize}')
    out.append(tx(S.TSA['after']) + '\n')
    out.append(r'\lessonsection{%s}' % tx(S.PX_HEAD))
    for px in S.PX:
        out.append(r'\pxtitle{%s}' % tx(px['title']))
        out.append(r'\textbf{Lý thuyết:} %s' % tx(px['theory']) + '\n')
        if 'formula' in px:
            num, den = px['formula']
            out.append(r'\[ K_c = \dfrac{%s}{%s} \]' % (num, den))
        for v in px['vd']:
            out.append(r'\textbf{VD:} %s' % tx(v) + '\n')
        figs = px.get('figs', [])
        for row in (figs if figs and isinstance(figs[0], list) else [figs] if figs else []):
            out.append(figures(row, used))
        out.append(r'\begin{reflexbox}')
        for rf in px['reflex']:
            head, tail = rf.split('thì nghĩ ngay:', 1)
            out.append(r'\item \textbf{%s} %s' % (tx(head + 'thì nghĩ ngay:'), tx(tail.strip())))
        out.append(r'\end{reflexbox}')
        traps = px['trap']
        body = tx(traps[0]) if len(traps) == 1 else r'\\ '.join('(%s) %s' % ('abcd'[i], tx(t)) for i, t in enumerate(traps))
        out.append(r'\begin{trapbox}%s\end{trapbox}' % body)
        if isinstance(px['passage'][0], dict):
            out.append(r'\Needspace{9cm}')  # Needspace không có tác dụng bên trong tcolorbox breakable
        out.append(r'\begin{readingpassage}[Ngữ liệu lạ]')
        for b in px['passage']:
            if isinstance(b, str):
                out.append(tx(fig_ref(b)) + '\n')
            elif 'fig' in b:
                out.append(figures([b['fig']], used))
            else:
                out.append(table(b['rows'], b['label'], b['cap']))
        out.append(r'\end{readingpassage}')
        out.append(r'\Needspace{6\baselineskip}')
        out.append(r'\qhead')
        out.append(r'\begin{enumerate}[label={}, leftmargin=0.5em, itemsep=6pt]')
        for i, q in enumerate(px['questions'], 1):
            out.append(r'\item \textbf{(%d)} %s' % (i, tx(fig_ref(q['q']))))
        out.append(r'\end{enumerate}')
    open(os.path.join(BUILD, 'Phan thi', 'buoi1.tex'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

    m = open(TEMPLATE, encoding='utf-8').read()
    m = m.replace(r'\textbf{Chuyên đề Sóng}', r'\textbf{%s}' % CHUYEN_DE)
    m = m.replace(r'\lessontitle{BUỔI N: <TÊN BUỔI>}{ĐỀ 1: <...> -- ĐỀ 2: <...> -- ĐỀ 3: <...>}',
                  r'\lessontitle{%s}{%s}' % (tx(S.HEAD), tx(S.LESSON)))
    m = m.replace(r'\input{Phan thi/buoiN}', r'\input{Phan thi/buoi1}')
    open(os.path.join(BUILD, 'main1.tex'), 'w', encoding='utf-8').write(m)
    if os.path.exists(os.path.join(ROOT, 'image', 'LOGO.jpg')):
        shutil.copy(os.path.join(ROOT, 'image', 'LOGO.jpg'), os.path.join(BUILD, 'image')); used.add('LOGO.jpg')
    for f in os.listdir(os.path.join(BUILD, 'image')):
        if f not in used:
            os.remove(os.path.join(BUILD, 'image', f))

    for _ in range(2):
        r = subprocess.run(['xelatex', '-interaction=nonstopmode', 'main1.tex'], cwd=BUILD, capture_output=True, text=True)
    if not os.path.exists(os.path.join(BUILD, 'main1.pdf')):
        print(r.stdout[-3000:]); sys.exit(1)
    shutil.copy(os.path.join(BUILD, 'main1.pdf'), os.path.join(HERE, PDF_NAME))
    with zipfile.ZipFile(os.path.join(HERE, ZIP_NAME), 'w', zipfile.ZIP_DEFLATED) as z:
        for d, _, fs in os.walk(BUILD):
            for f in fs:
                if f.endswith(('.tex', '.png', '.jpg')):
                    p = os.path.join(d, f); z.write(p, os.path.relpath(p, BUILD))
    print(os.path.join(HERE, PDF_NAME))


if __name__ == '__main__':
    build()
