# Sinh PDF LaTeX gửi HS Buổi 1 (bài tập phản xạ PX1–PX6) từ buoi1_spec.py. Bản HS: không có key, không có ý giảng.
import os, re, shutil, subprocess, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, ROOT)
from buoi1_spec import PX
from anh_chuyen_de import so_hinh

TEMPLATE = '/root/.claude/skills/synced/ef69f53a-273f-41a3-ad97-c64ccbfacd43_45acc2b8-d2ef-448f-99cf-f15468c28e37/tsa-exam-creator/assets/latex_hs/main_template.tex'
BUILD = os.path.join(HERE, 'latex')
CHUYEN_DE = 'Chuyên đề Cân bằng hóa học'
TITLE = ('BUỔI 1: CÂN BẰNG ĐỘNG, Kc VÀ Q', 'Bài tập phản xạ PX1 -- PX6')
PDF_NAME = 'Buổi 1 - Bài tập phản xạ PX1-PX6.pdf'
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
    L = [r'\Needspace{5cm}', r'\tablecaption{%s}{%s}' % (label, tx(cap)), r'{\small', r'\begin{center}',
         r'\renewcommand{\arraystretch}{1.3}', r'\begin{tabular}{|%s|}' % '|'.join('c' * n), r'\hline',
         r'\rowcolor{pastelBlue}', ' & '.join(r'\textbf{%s}' % tx(c) for c in rows[0]) + r' \\', r'\hline']
    for r in rows[1:]:
        L += [' & '.join(tx(c) for c in r) + r' \\', r'\hline']
    return '\n'.join(L + [r'\end{tabular}', r'\end{center}', '}'])


def build():
    os.makedirs(os.path.join(BUILD, 'Phan thi'), exist_ok=True)
    os.makedirs(os.path.join(BUILD, 'image'), exist_ok=True)
    out, hs_no = [r'\lessonsection{Bài tập phản xạ PX1--PX6}'], {}
    for px in PX:
        # Đánh lại số hình theo thứ tự xuất hiện trong bản HS
        figs = [b['fig'] for b in px['passage'] if isinstance(b, dict) and 'fig' in b]
        for f in figs:
            hs_no[f] = len(hs_no) + 1
        def renum(s):
            for f in figs:
                s = s.replace('Hình %d' % FIG[f][1], 'Hình %d' % hs_no[f])
            return s
        out.append(r'\pxtitle{%s}' % tx(px['title']))
        out.append(r'\begin{readingpassage}[Ngữ liệu lạ]')
        for b in px['passage']:
            if isinstance(b, str):
                out.append(tx(renum(b)) + '\n')
            elif 'fig' in b:
                f = b['fig']; shutil.copy(os.path.join(ROOT, f), os.path.join(BUILD, 'image'))
                _, _, ten, nguon, _ = FIG[f]
                out.append(r'\begin{center}\includegraphics[width=0.45\textwidth,height=9cm,keepaspectratio]{image/%s}\end{center}' % os.path.basename(f))
                out.append(r'\figcaption{%d}{%s (Nguồn: %s)}' % (hs_no[f], tx(ten), tx(nguon)))
            else:
                out.append(table(b['rows'], b['label'], b['cap']))
        out.append(r'\end{readingpassage}')
        # Giữ 'Câu hỏi:' cùng trang với ý (1) và khoảng trống của nó
        out.append(r'\Needspace{%d\baselineskip}' % (px['questions'][0]['n'] + 8))
        out.append(r'\qhead')
        out.append(r'\begin{enumerate}[label={}, leftmargin=0.5em, itemsep=4pt]')
        for k, q in enumerate(px['questions'], 1):
            out.append(r'\Needspace{%d\baselineskip}' % (q['n'] + 4))
            out.append(r'\item \textbf{(%d)} %s \answerlines{%d}' % (k, tx(renum(q['q'])), q['n']))
        out.append(r'\end{enumerate}')
    out.append(r'\vfill\hfill \textit{(Nguồn: Nguyễn Nghĩa Đô biên soạn)}')
    open(os.path.join(BUILD, 'Phan thi', 'buoi1.tex'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

    m = open(TEMPLATE, encoding='utf-8').read()
    m = m.replace(r'\textbf{Chuyên đề Sóng}', r'\textbf{%s}' % CHUYEN_DE)
    m = m.replace(r'\lessontitle{BUỔI N: <TÊN BUỔI>}{ĐỀ 1: <...> -- ĐỀ 2: <...> -- ĐỀ 3: <...>}',
                  r'\lessontitle{%s}{%s}' % (tx(TITLE[0]), TITLE[1]))
    m = m.replace(r'\input{Phan thi/buoiN}', r'\input{Phan thi/buoi1}')
    open(os.path.join(BUILD, 'main1.tex'), 'w', encoding='utf-8').write(m)
    if os.path.exists(os.path.join(ROOT, 'image', 'LOGO.jpg')):
        shutil.copy(os.path.join(ROOT, 'image', 'LOGO.jpg'), os.path.join(BUILD, 'image'))

    for _ in range(2):
        r = subprocess.run(['xelatex', '-interaction=nonstopmode', 'main1.tex'], cwd=BUILD, capture_output=True, text=True)
    if not os.path.exists(os.path.join(BUILD, 'main1.pdf')):
        print(r.stdout[-3000:]); sys.exit(1)
    shutil.copy(os.path.join(BUILD, 'main1.pdf'), os.path.join(HERE, PDF_NAME))
    with zipfile.ZipFile(os.path.join(HERE, 'Buoi1_Bai_tap_phan_xa_Overleaf.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        for d, _, fs in os.walk(BUILD):
            for f in fs:
                if f.endswith(('.tex', '.png', '.jpg')):
                    p = os.path.join(d, f); z.write(p, os.path.relpath(p, BUILD))
    print(os.path.join(HERE, PDF_NAME))


if __name__ == '__main__':
    build()
