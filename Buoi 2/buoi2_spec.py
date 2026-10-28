# -*- coding: utf-8 -*-
"""
Buổi 2 — Le Chatelier qua Q/Kc (PX7–PX10)
Chuyên đề Cân bằng hóa học · TSA ĐHBK Hà Nội
"""

TITLE = 'CHUYÊN ĐỀ CÂN BẰNG HÓA HỌC'
LESSON = 'BUỔI 2: LE CHATELIER QUA Q/Kc (PX7–PX10)'
HEAD = 'CÂN BẰNG HÓA HỌC'

# ──────────────────────────────────────────────
# INTRO — nối từ Buổi 1 (PX6 kết thúc: Q < Kc → thuận, Q > Kc → nghịch)
# ──────────────────────────────────────────────
INTRO = [
    'Buổi trước, ta đã biết cách đọc hai con số Q và Kc: '
    'Q < Kc thì hệ chạy thuận, Q > Kc thì hệ chạy nghịch, Q = Kc thì cân bằng. '
    'Câu hỏi tiếp theo là: khi ta tác động vào hệ đang cân bằng '
    '(nén, thay đổi nhiệt độ, thêm xúc tác), Q và Kc thay đổi thế nào, '
    'và hệ đi về đâu?',

    'Buổi này chia ba nhóm tác động:\n'
    '• Nhóm D (PX7–PX8): tác động làm lệch Q trong khi Kc đứng yên '
    '(vì nhiệt độ không đổi) — nén/giãn thể tích và thêm khí trơ.\n'
    '• Nhóm E (PX9): tác động duy nhất dời được Kc — thay đổi nhiệt độ.\n'
    '• Nhóm F (PX10): xúc tác — không đổi Q, không đổi Kc.',
]

# ──────────────────────────────────────────────
# PX7 — Nén/giãn thể tích (hệ khí) → Q lệch Kc
# ──────────────────────────────────────────────
PX7 = {
    'title': 'PX7. Nén/giãn thể tích — Q lệch Kc',

    'theory': (
        'Khi nén hệ khí (giảm thể tích), nồng độ MỌI chất khí đều tăng theo cùng hệ số k. '
        'Q mới = Q cũ × k^(Δn), với Δn = (tổng hệ số sản phẩm khí) − (tổng hệ số chất đầu khí).\n\n'
        '• Δn < 0 (ít mol khí phía sản phẩm hơn): nén → Q giảm → Q < Kc → chạy thuận '
        '(hệ "co" về phía ít mol khí).\n'
        '• Δn > 0: nén → Q tăng → Q > Kc → chạy nghịch.\n'
        '• Δn = 0: nén → Q không đổi → KHÔNG chuyển dịch.\n\n'
        'Giãn thể tích cho kết quả ngược lại.'
    ),

    'vd': [
        'N₂(g) + 3H₂(g) ⇌ 2NH₃(g): Δn = 2 − 4 = −2. '
        'Nén → Q giảm → chạy thuận → tăng % NH₃. '
        'Đây là lí do nhà máy Haber chạy ở 200 bar.',
        'H₂(g) + I₂(g) ⇌ 2HI(g): Δn = 2 − 2 = 0. '
        'Nén không ảnh hưởng cân bằng — phần trăm HI lúc cân bằng giữ nguyên.',
    ],

    'reflex': [
        'Đọc đề thấy "nén" hoặc "tăng áp suất bằng giảm thể tích" → nghĩ ngay: tính Δn.',
        'Δn = 0 → nén/giãn không chuyển dịch (bẫy kinh điển).',
    ],

    'trap': [
        'Tưởng nén luôn làm cân bằng chuyển dịch '
        '(thực ra Δn = 0 thì Q không đổi, cân bằng đứng yên).',
        'Nhầm Δn: quên chỉ đếm mol KHÍ '
        '(chất rắn/lỏng nguyên chất không có trong Q nên không đếm).',
    ],

    'figs': [],

    'passage': [
        'Xét hai phản ứng cân bằng trong bình kín có piston ở cùng nhiệt độ:',
        'Phản ứng (I): N₂(g) + 3H₂(g) ⇌ 2NH₃(g)    Δn = 2 − 4 = −2',
        'Phản ứng (II): H₂(g) + I₂(g) ⇌ 2HI(g)    Δn = 2 − 2 = 0',
        'Cả hai hệ đều đang ở trạng thái cân bằng (Q = Kc). '
        'Sau đó, piston được đẩy vào để giảm thể tích bình còn một nửa '
        '(nồng độ mọi chất khí tăng gấp đôi).',
        {'cap': 'Nồng độ trước và sau khi nén (giảm V còn 1/2)',
         'label': '2.1',
         'rows': [
             ['Phản ứng', 'Trước nén: Q = Kc', 'Sau nén: Q mới', 'So sánh Q mới với Kc', 'Chiều chuyển dịch'],
             ['(I) N₂ + 3H₂ ⇌ 2NH₃', 'Q = Kc', 'Q × 2^(−2) = Kc/4', 'Q mới < Kc', 'Thuận'],
             ['(II) H₂ + I₂ ⇌ 2HI', 'Q = Kc', 'Q × 2^(0) = Kc', 'Q mới = Kc', 'Không chuyển dịch'],
         ]},
        'Giải thích: khi nồng độ mọi chất nhân đôi (k = 2), '
        'Q mới = Q cũ × k^Δn. Với phản ứng (I), Δn = −2 nên Q mới = Kc × 2^(−2) = Kc/4 < Kc. '
        'Với phản ứng (II), Δn = 0 nên Q mới = Kc × 2^0 = Kc.',
    ],

    'questions': [
        {
            'q': 'Phản ứng (I): sau khi nén còn 1/2 thể tích, '
                 'Q mới bằng bao nhiêu lần Kc? Hệ chạy chiều nào?',
            'n': 4,
            'ans': 'Q mới = Kc/4. Hệ chạy thuận.',
            'exp': 'Nồng độ mọi chất nhân 2. '
                   'Q mới = [NH₃]²/([N₂][H₂]³) → tử nhân 2² = 4, mẫu nhân 2⁴ = 16. '
                   'Q mới = Q cũ × 4/16 = Kc/4 < Kc → chạy thuận.',
        },
        {
            'q': 'Phản ứng (II): sau khi nén còn 1/2 thể tích, '
                 'Q mới thay đổi thế nào? Cân bằng có chuyển dịch không?',
            'n': 4,
            'ans': 'Q mới = Kc. Cân bằng không chuyển dịch.',
            'exp': 'Nồng độ mọi chất nhân 2. '
                   'Q mới = [HI]²/([H₂][I₂]) → tử nhân 2² = 4, mẫu nhân 2² = 4. '
                   'Q mới = Q cũ × 4/4 = Kc → cân bằng giữ nguyên.',
        },
        {
            'q': 'Phản ứng 2SO₂(g) + O₂(g) ⇌ 2SO₃(g) đang cân bằng trong bình có piston. '
                 'Nén bình còn 1/3 thể tích. Tính Δn và cho biết cân bằng chuyển dịch theo chiều nào.',
            'n': 5,
            'ans': 'Δn = 2 − 3 = −1. Chạy thuận.',
            'exp': 'k = 3 (nồng độ nhân 3). Q mới = Q cũ × 3^(−1) = Kc/3 < Kc → chạy thuận '
                   '(tạo thêm SO₃, giảm tổng mol khí).',
        },
        {
            'q': 'Một bạn nói: "Nén bình chứa H₂ + I₂ ⇌ 2HI sẽ tạo thêm HI '
                 'vì áp suất tăng thì hệ chuyển dịch về phía ít mol khí." '
                 'Phân tích sai lầm trong lập luận này.',
            'n': 5,
            'ans': 'Sai. Δn = 0 nên nén không chuyển dịch cân bằng.',
            'exp': 'Phản ứng có 2 mol khí mỗi bên (Δn = 0). '
                   'Khi nén, tử và mẫu của Q cùng nhân hệ số bằng nhau → Q không đổi → '
                   'cân bằng không chuyển dịch. '
                   'Quy tắc "chuyển về phía ít mol khí" chỉ đúng khi Δn ≠ 0.',
        },
    ],
}

# ──────────────────────────────────────────────
# PX8 — Thêm khí trơ → tùy điều kiện
# ──────────────────────────────────────────────
PX8 = {
    'title': 'PX8. Thêm khí trơ — Q có đổi không?',

    'theory': (
        'Khí trơ (Ar, Ne, He...) không phản ứng → không xuất hiện trong Q. '
        'Nhưng khí trơ CÓ THỂ làm Q thay đổi gián tiếp, tùy điều kiện:\n\n'
        '• Thêm khí trơ, giữ V không đổi: nồng độ các chất phản ứng không đổi → '
        'Q không đổi → KHÔNG chuyển dịch.\n'
        '• Thêm khí trơ, giữ P không đổi: khí trơ chiếm thể tích → V tăng → '
        'nồng độ mọi chất giảm → Q thay đổi tùy Δn (giống giãn thể tích).\n\n'
        'Đây chính là chỗ Le Chatelier "đoán sai" nếu chỉ nhớ '
        '"thêm khí trơ không ảnh hưởng" mà không phân biệt V hay P không đổi.'
    ),

    'vd': [
        'Bình kín cứng (V cố định) chứa N₂ + 3H₂ ⇌ 2NH₃ đang cân bằng. '
        'Bơm thêm Ar → áp suất tổng tăng, nhưng V không đổi → '
        'nồng độ N₂, H₂, NH₃ giữ nguyên → Q giữ nguyên → không chuyển dịch.',
        'Bình có piston (P cố định) cùng phản ứng. Bơm thêm Ar → '
        'piston dãn ra để giữ P → V tăng → nồng độ mọi chất giảm → '
        'Q thay đổi theo Δn = −2 → chạy nghịch.',
    ],

    'reflex': [
        'Đọc đề thấy "thêm khí trơ" → hỏi ngay: V hay P không đổi?',
        'V không đổi → Q không đổi → không chuyển dịch (luôn đúng, mọi phản ứng).',
        'P không đổi → tương đương giãn thể tích → xét Δn.',
    ],

    'trap': [
        'Tưởng "thêm khí trơ luôn không ảnh hưởng cân bằng" '
        '(thực ra chỉ đúng khi V không đổi; P không đổi thì cân bằng CÓ THỂ chuyển dịch).',
        'Nhầm "áp suất tổng tăng" với "nén": thêm khí trơ ở V không đổi '
        'tăng P tổng nhưng áp suất riêng phần các chất phản ứng KHÔNG đổi → Q giữ nguyên.',
    ],

    'figs': ['Buoi 2/image/hinh_1_2.png'],

    'passage': [
        'Phản ứng N₂(g) + 3H₂(g) ⇌ 2NH₃(g) đang cân bằng ở 450 °C. '
        'Hai bình A và B chứa cùng hỗn hợp cân bằng ban đầu. '
        'Sau đó, bơm thêm một lượng Ar bằng nhau vào cả hai bình:',
        '• Bình A: bình kín cứng (thể tích không đổi).',
        '• Bình B: bình có piston tự do (áp suất tổng không đổi).',
        {'cap': 'Thay đổi sau khi thêm Ar vào hai bình',
         'label': '2.2',
         'rows': [
             ['Đại lượng', 'Bình A (V không đổi)', 'Bình B (P không đổi)'],
             ['Thể tích', 'Không đổi', 'Tăng (piston dãn ra)'],
             ['Áp suất tổng', 'Tăng', 'Không đổi'],
             ['[N₂], [H₂], [NH₃]', 'Không đổi', 'Giảm (V tăng)'],
             ['Q', 'Không đổi (= Kc)', '?'],
             ['Chuyển dịch', 'Không', '?'],
         ]},
        'Biết Δn = 2 − 4 = −2 cho phản ứng trên.',
    ],

    'questions': [
        {
            'q': 'Tính Q mới của bình B sau khi thêm Ar, biết thể tích tăng gấp đôi. '
                 'Cân bằng trong bình B chuyển dịch theo chiều nào?',
            'n': 5,
            'ans': 'Q mới = Kc × 2^(−(−2)) = 4Kc > Kc. Chạy nghịch.',
            'exp': 'V tăng gấp 2 → nồng độ mọi chất giảm còn 1/2 (k = 1/2). '
                   'Q mới = Q cũ × (1/2)^Δn = Kc × (1/2)^(−2) = 4Kc > Kc → '
                   'hệ chuyển dịch theo chiều nghịch (phân hủy NH₃, tăng tổng mol khí).',
        },
        {
            'q': 'Giải thích vì sao trong bình A, dù áp suất tổng tăng sau khi bơm Ar, '
                 'cân bằng vẫn không chuyển dịch.',
            'n': 4,
            'ans': 'V không đổi → nồng độ các chất phản ứng không đổi → Q không đổi.',
            'exp': 'Ar không có trong biểu thức Q. Ở V không đổi, [N₂], [H₂], [NH₃] giữ nguyên → '
                   'Q = [NH₃]²/([N₂][H₂]³) không đổi → Q vẫn = Kc → cân bằng không chuyển dịch. '
                   'Áp suất tổng tăng nhưng áp suất riêng phần của N₂, H₂, NH₃ đều không đổi.',
        },
        {
            'q': 'Nếu phản ứng trong bình B là H₂(g) + I₂(g) ⇌ 2HI(g) thay vì tổng hợp NH₃, '
                 'thêm Ar ở P không đổi có làm cân bằng chuyển dịch không? Vì sao?',
            'n': 4,
            'ans': 'Không chuyển dịch.',
            'exp': 'Δn = 2 − 2 = 0. Khi V tăng, Q mới = Kc × k^(−0) = Kc → '
                   'Q không đổi → cân bằng giữ nguyên. '
                   'Với Δn = 0, thêm khí trơ không ảnh hưởng dù ở V hay P không đổi.',
        },
        {
            'q': 'Trong nhà máy Haber, khí Ar từ không khí tích lũy dần trong vòng tuần hoàn. '
                 'Nhà máy chạy ở áp suất không đổi (~200 bar). '
                 'Giải thích vì sao Ar tích lũy làm giảm hiệu suất tổng hợp NH₃.',
            'n': 5,
            'ans': 'Ar chiếm thể tích, pha loãng N₂ và H₂, làm Q tăng.',
            'exp': 'Ở P không đổi, Ar tích lũy → chiếm phần thể tích → '
                   'nồng độ (áp suất riêng phần) N₂ và H₂ giảm → '
                   'mẫu Q giảm nhiều hơn tử → Q tăng → Q tiến gần hoặc vượt Kc → '
                   'chiều thuận bị hạn chế → % NH₃ lúc cân bằng giảm. '
                   'Đó là lí do nhà máy phải xả bỏ (purge) định kì.',
        },
    ],
}

# ──────────────────────────────────────────────
# PX9 — Thay đổi nhiệt độ → Kc thay đổi
# ──────────────────────────────────────────────
PX9 = {
    'title': 'PX9. Thay đổi nhiệt độ — tác động duy nhất dời Kc',

    'theory': (
        'Nhiệt độ là tác động DUY NHẤT thay đổi Kc.\n\n'
        '• Phản ứng tỏa nhiệt (ΔH < 0): tăng T → Kc giảm. '
        'Lúc này Q (vẫn bằng Kc cũ) > Kc mới → Q > Kc → chạy nghịch.\n'
        '• Phản ứng thu nhiệt (ΔH > 0): tăng T → Kc tăng. '
        'Q (= Kc cũ) < Kc mới → Q < Kc → chạy thuận.\n\n'
        'Mẹo nhớ: coi nhiệt như một "chất" — phản ứng tỏa nhiệt thì nhiệt nằm phía sản phẩm, '
        'tăng T như "thêm sản phẩm" → Q > Kc → nghịch. '
        'Nhưng CƠ CHẾ THẬT là Kc thay đổi (không phải Q thay đổi trước).'
    ),

    'vd': [
        'N₂ + 3H₂ ⇌ 2NH₃ (ΔH = −91,8 kJ, tỏa nhiệt): '
        'tăng T → Kc giảm → % NH₃ giảm. Bảng 1 Đề 2: 450 °C cho 27% NH₃ nhưng 550 °C chỉ còn 14,6%.',
        'N₂O₄(g) ⇌ 2NO₂(g) (ΔH = +57 kJ, thu nhiệt): '
        'tăng T → Kc tăng → tạo thêm NO₂ (nâu) → hỗn hợp sẫm màu hơn.',
    ],

    'reflex': [
        'Đọc đề thấy "thay đổi nhiệt độ" → nghĩ ngay: đây là tác động dời Kc, khác hẳn nén hay thêm khí trơ.',
        'Tỏa nhiệt + tăng T → Kc giảm → nghịch. Thu nhiệt + tăng T → Kc tăng → thuận.',
    ],

    'trap': [
        'Tưởng tăng T luôn tăng tốc chiều thuận (thực ra chỉ tăng tốc cả hai chiều; '
        'chiều nào được ưu tiên phụ thuộc ΔH).',
        'Nhầm: xúc tác cũng thay đổi Kc (thực ra xúc tác KHÔNG đổi Kc — xem PX10).',
    ],

    'figs': ['Buoi 2/image/hinh_1_3.png'],

    'passage': [
        'Hệ cân bằng N₂O₄(g) ⇌ 2NO₂(g) có ΔH = +57,2 kJ là ví dụ trực quan: '
        'N₂O₄ không màu, NO₂ nâu đỏ. Khi thay đổi nhiệt độ, '
        'màu hỗn hợp thay đổi cho thấy vị trí cân bằng dịch chuyển.',
        {'cap': 'Hằng số cân bằng Kc của phản ứng N₂O₄ ⇌ 2NO₂ theo nhiệt độ',
         'label': '2.3',
         'rows': [
             ['Nhiệt độ (°C)', 'Kc (mol/L)', 'Màu hỗn hợp'],
             ['0', '0,0013', 'Gần như không màu'],
             ['25', '0,0047', 'Vàng nhạt'],
             ['50', '0,016', 'Nâu nhạt'],
             ['100', '0,14', 'Nâu đậm'],
         ]},
        'Một thí nghiệm: hai ống nghiệm chứa cùng hỗn hợp N₂O₄/NO₂ ở 25 °C '
        '(Kc = 0,0047 mol/L). Ống (a) được nhúng vào nước đá (0 °C), '
        'ống (b) được nhúng vào nước nóng (50 °C).',
    ],

    'questions': [
        {
            'q': 'Khi nhúng ống (a) vào nước đá, Kc thay đổi thế nào? '
                 'Q và Kc mới so sánh ra sao? Hệ chạy chiều nào?',
            'n': 5,
            'ans': 'Kc giảm từ 0,0047 xuống 0,0013. Q (= 0,0047) > Kc mới → chạy nghịch.',
            'exp': 'Phản ứng thu nhiệt (ΔH > 0): giảm T → Kc giảm. '
                   'Ngay sau khi làm lạnh, nồng độ các chất chưa kịp đổi nên Q vẫn = Kc cũ = 0,0047. '
                   'Mà Kc mới = 0,0013 → Q > Kc → chạy nghịch → NO₂ giảm → hỗn hợp nhạt màu.',
        },
        {
            'q': 'Khi nhúng ống (b) vào nước nóng 50 °C, '
                 'giải thích bằng Q/Kc vì sao hỗn hợp sẫm màu hơn.',
            'n': 5,
            'ans': 'Kc tăng từ 0,0047 lên 0,016. Q < Kc mới → chạy thuận → thêm NO₂ nâu.',
            'exp': 'Thu nhiệt + tăng T → Kc tăng. Q (= 0,0047) < Kc mới (= 0,016) → '
                   'hệ chuyển dịch theo chiều thuận → tạo thêm NO₂ → hỗn hợp nâu đậm hơn.',
        },
        {
            'q': 'Phản ứng tổng hợp NH₃: N₂ + 3H₂ ⇌ 2NH₃ (ΔH = −91,8 kJ). '
                 'Nhà máy Haber chạy ở 450 °C dù % NH₃ lúc cân bằng giảm so với 350 °C. '
                 'Vì sao không hạ xuống 350 °C?',
            'n': 5,
            'ans': 'Ở 350 °C, tốc độ phản ứng quá chậm.',
            'exp': 'Giảm T → Kc tăng (tỏa nhiệt) → % NH₃ cân bằng cao hơn (35,7% vs 17,3% ở 200 bar). '
                   'Nhưng tốc độ giảm mạnh, hệ mất rất lâu mới tiến đến cân bằng → '
                   'năng suất thực tế thấp hơn. Nhà máy chọn 450 °C là sự tối ưu hóa '
                   'giữa phần trăm chuyển hóa và tốc độ đạt cân bằng.',
        },
        {
            'q': 'Một bạn nói: "Tăng nhiệt độ làm Kc của MỌI phản ứng tăng." '
                 'Nhận xét đúng hay sai? Cho ví dụ phản bác nếu sai.',
            'n': 4,
            'ans': 'Sai.',
            'exp': 'Tăng T chỉ làm Kc tăng với phản ứng thu nhiệt (ΔH > 0). '
                   'Với phản ứng tỏa nhiệt (ΔH < 0), tăng T làm Kc giảm. '
                   'Ví dụ: NH₃ tổng hợp (tỏa nhiệt), tăng T → Kc giảm → % NH₃ giảm.',
        },
    ],
}

# ──────────────────────────────────────────────
# PX10 — Xúc tác: tăng tốc, không đổi Kc, không đổi Q
# ──────────────────────────────────────────────
PX10 = {
    'title': 'PX10. Xúc tác — nhanh hơn nhưng đích đến giữ nguyên',

    'theory': (
        'Xúc tác làm tốc độ phản ứng thuận VÀ nghịch cùng tăng → '
        'hệ ĐẾN CÂN BẰNG nhanh hơn, nhưng VỊ TRÍ cân bằng (Kc) không đổi.\n\n'
        '• Phần trăm chuyển hóa lúc cân bằng không đổi.\n'
        '• Xúc tác không xuất hiện trong Q (không bị tiêu hao).\n'
        '• Ý nghĩa công nghiệp: xúc tác cho phép hệ đạt cân bằng ở nhiệt độ THẤP HƠN '
        '(nơi Kc thuận lợi), mà vẫn đủ nhanh.'
    ),

    'vd': [
        'Xúc tác Fe trong Haber: cho phép chạy ở 450 °C mà đủ nhanh, '
        'thay vì 600 °C (nơi Kc giảm mạnh, % NH₃ thấp).',
        'Enzyme trong cơ thể: urease tăng tốc phân hủy urea lên 10¹⁴ lần, '
        'nhưng lượng sản phẩm lúc cân bằng giữ nguyên.',
    ],

    'reflex': [
        'Đọc đề thấy "thêm xúc tác" → nghĩ ngay: Kc không đổi, Q không đổi, '
        'chỉ đến cân bằng nhanh hơn.',
        'Đọc đề hỏi "phần trăm chuyển hóa thay đổi thế nào khi thêm xúc tác" → '
        'trả lời: không đổi (nếu hệ đã đạt cân bằng).',
    ],

    'trap': [
        'Tưởng xúc tác làm tăng hiệu suất / phần trăm sản phẩm '
        '(thực ra chỉ tăng TỐC ĐỘ đạt cân bằng, Kc giữ nguyên).',
        'Tưởng xúc tác chỉ tăng tốc chiều thuận '
        '(thực ra tăng tốc CẢ HAI chiều như nhau).',
    ],

    'figs': ['Buoi 2/image/hinh_1_4.png'],

    'passage': [
        'Phản ứng phân hủy H₂O₂: 2H₂O₂(aq) → 2H₂O(l) + O₂(g) diễn ra rất chậm ở nhiệt độ phòng. '
        'Thêm MnO₂ (chất xúc tác) làm phản ứng xảy ra mãnh liệt, sủi bọt O₂ dữ dội.',
        'Tuy nhiên, lượng O₂ thu được lúc phản ứng kết thúc (cân bằng) KHÔNG phụ thuộc '
        'có hay không có MnO₂ — chỉ thời gian đạt cân bằng thay đổi.',
        {'cap': 'So sánh có/không xúc tác: phản ứng 2SO₂ + O₂ ⇌ 2SO₃ ở 450 °C',
         'label': '2.4',
         'rows': [
             ['Điều kiện', 'Thời gian đạt cân bằng', '% SO₃ lúc cân bằng', 'Kc'],
             ['Không xúc tác', '~vài tuần', '97,5%', '1,7 × 10⁶'],
             ['Có V₂O₅ (xúc tác)', '~vài giây', '97,5%', '1,7 × 10⁶'],
         ]},
        'Trong quy trình tiếp xúc sản xuất H₂SO₄, xúc tác V₂O₅ giúp phản ứng đạt cân bằng '
        'trong vài giây thay vì vài tuần, '
        'trong khi phần trăm SO₃ lúc cân bằng và Kc hoàn toàn không thay đổi.',
    ],

    'questions': [
        {
            'q': 'Dựa vào Bảng 2.4, so sánh % SO₃ lúc cân bằng có và không có xúc tác. '
                 'Giải thích vì sao Kc giữ nguyên.',
            'n': 4,
            'ans': '% SO₃ như nhau (97,5%). Kc không đổi vì nhiệt độ không đổi.',
            'exp': 'Kc chỉ phụ thuộc nhiệt độ (PX9). Xúc tác không thay đổi nhiệt độ '
                   '→ Kc giữ nguyên → vị trí cân bằng giữ nguyên → % SO₃ không đổi. '
                   'Xúc tác chỉ rút ngắn thời gian đạt cân bằng từ vài tuần xuống vài giây.',
        },
        {
            'q': 'Trong nhà máy Haber, nếu dùng xúc tác tốt hơn (giả sử tăng tốc gấp 10 lần '
                 'so với Fe), phần trăm NH₃ lúc cân bằng có tăng không? '
                 'Lợi ích thực sự của xúc tác mới là gì?',
            'n': 5,
            'ans': '% NH₃ lúc cân bằng không tăng.',
            'exp': 'Kc không đổi (cùng nhiệt độ) → % NH₃ cân bằng giữ nguyên. '
                   'Lợi ích thực sự: xúc tác mới cho phép hạ nhiệt độ vận hành '
                   '(ví dụ từ 450 °C xuống 350 °C) mà phản ứng vẫn đủ nhanh. '
                   'Ở 350 °C, Kc lớn hơn → % NH₃ cân bằng cao hơn (35,7% vs 17,3%). '
                   'Xúc tác giúp "mở khóa" vùng nhiệt độ có Kc thuận lợi.',
        },
        {
            'q': 'Một bạn nói: "Xúc tác chỉ tăng tốc chiều thuận nên tạo thêm sản phẩm." '
                 'Sai ở đâu?',
            'n': 4,
            'ans': 'Sai. Xúc tác tăng tốc CẢ HAI chiều.',
            'exp': 'Xúc tác hạ năng lượng hoạt hóa của cả chiều thuận và chiều nghịch '
                   'như nhau → tốc độ hai chiều cùng tăng → '
                   'hệ đến cân bằng nhanh hơn nhưng VỊ TRÍ cân bằng không đổi → '
                   'lượng sản phẩm lúc cân bằng giữ nguyên.',
        },
        {
            'q': 'Xét hệ N₂ + 3H₂ ⇌ 2NH₃ CHƯA đạt cân bằng (Q < Kc). '
                 'Nếu thêm xúc tác Fe vào lúc này, nồng độ NH₃ tăng hay giảm '
                 'so với trường hợp không có xúc tác (đợi lâu để tự đạt cân bằng)?',
            'n': 5,
            'ans': 'Nồng độ NH₃ cuối cùng như nhau.',
            'exp': 'Q < Kc → hệ đang chạy thuận (tạo NH₃). '
                   'Có xúc tác: đạt cân bằng nhanh hơn → NH₃ tăng nhanh đến giá trị cân bằng. '
                   'Không xúc tác: cũng đạt cân bằng nhưng chậm hơn → NH₃ tăng chậm đến CÙNG giá trị. '
                   'Đích đến (Kc) là như nhau, chỉ thời gian khác.',
        },
    ],
}

# ──────────────────────────────────────────────
# Gom PX
# ──────────────────────────────────────────────
PX = [PX7, PX8, PX9, PX10]

# ──────────────────────────────────────────────
# DEBATE — 3 câu tranh biện cuối buổi
# ──────────────────────────────────────────────
DEBATE = [
    {
        'q': 'Hệ đang cân bằng ở nhiệt độ cao. Ta vừa hạ nhiệt độ, vừa nén thể tích. '
             'Hai tác động này "cùng chiều" hay "ngược chiều" đối với phản ứng tỏa nhiệt có Δn < 0? '
             'Có thể dự đoán chắc chắn hệ chạy chiều nào không?',
        'hint': 'Hạ T → Kc tăng (tỏa nhiệt) → thuận. Nén → Q giảm (Δn < 0) → thuận. '
                'Hai tác động cùng chiều → chắc chắn chạy thuận. '
                'Nhưng nếu một phản ứng mà hạ T → thuận, nén → nghịch (Δn > 0)? '
                'Lúc đó không chắc chắn — phụ thuộc mức độ từng tác động.',
    },
    {
        'q': '"Le Chatelier nói hệ luôn chống lại tác động. Vậy nếu thêm N₂ vào '
             'hệ N₂ + 3H₂ ⇌ 2NH₃, hệ phải tiêu thụ N₂ để chống lại. '
             'Nhưng sau khi cân bằng mới thiết lập, [N₂] vẫn cao hơn ban đầu. '
             'Vậy hệ chống lại có hiệu quả không?"',
        'hint': 'Hệ chạy thuận, tiêu thụ một phần N₂ đã thêm, nhưng không bao giờ '
                'tiêu thụ hết. [N₂] mới > [N₂] cũ là bình thường. '
                '"Chống lại" không có nghĩa "triệt tiêu hoàn toàn" — nó chỉ là '
                'Q đang < Kc nên hệ chạy thuận cho đến khi Q = Kc mới. '
                'Cách nói Q/Kc chính xác hơn: hệ không "chống lại" mà đơn giản '
                'là chạy về phía Q = Kc.',
    },
    {
        'q': '"Trong nhà máy Haber, nếu phát minh được xúc tác siêu tốt '
             '(phản ứng đạt cân bằng gần như tức thì), liệu có thể bỏ hẳn '
             'áp suất cao 200 bar và chạy ở 1 bar không?"',
        'hint': 'Xúc tác siêu tốt → đến cân bằng cực nhanh, NHƯNG Kc không đổi. '
                'Ở 450 °C, 1 bar (100 kPa): % NH₃ cân bằng rất thấp (<5%). '
                'Xúc tác không cứu được Kc nhỏ ở T cao + P thấp. '
                'Vẫn cần áp suất cao để Q < Kc lớn hơn (nén → ưu tiên thuận với Δn < 0). '
                'Xúc tác mở khóa hạ T (nơi Kc lớn), không mở khóa hạ P.',
    },
]

# ──────────────────────────────────────────────
# Tóm tắt Buổi 2 (dùng cho gen_docx)
# ──────────────────────────────────────────────
SUMMARY = (
    'Buổi 2 khép lại nguyên lí Le Chatelier bằng ngôn ngữ Q/Kc:\n'
    '• PX7–PX8: hai cách làm Q lệch Kc (nén/giãn thể tích, thêm khí trơ) — '
    'Kc đứng yên vì nhiệt độ không đổi.\n'
    '• PX9: nhiệt độ là tác động duy nhất dời Kc.\n'
    '• PX10: xúc tác không đổi Q, không đổi Kc — chỉ đến cân bằng nhanh hơn.\n\n'
    'Buổi sau: kiểm tra + chữa bài (5 đề TSA).'
)
