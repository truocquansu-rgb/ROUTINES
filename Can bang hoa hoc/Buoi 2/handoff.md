# Handoff — Soạn giáo án Buổi 2: Le Chatelier qua Q/Kc (PX7–PX11)

Phiên mới bắt đầu từ đây. Đọc file này trước khi làm bất cứ gì.

---

## Bối cảnh chuyên đề

Chuyên đề TSA "Cân bằng hóa học" gồm 3 buổi, dạy học sinh chuẩn bị thi TSA (ĐHBK Hà Nội).

```
BUỔI 1 ✅ DONE — Cân bằng động, Kc và Q (PX1–PX6)
BUỔI 2 ← BẠN LÀM CÁI NÀY — Le Chatelier qua Q/Kc (PX7–PX11)
BUỔI 3 — Kiểm tra + chữa bài (5 đề TSA, đã/đang soạn riêng ở Buoi 3/)
```

Buổi 2 **không có đề kiểm tra**. Bài tập nằm trong các PX (passage + câu hỏi tự luyện, giống Buổi 1).

---

## Nhiệm vụ cụ thể

1. Viết file `buoi2_spec.py` theo đúng format `Buoi 1/buoi1_spec.py` (đọc file đó trước)
2. Nội dung: PX7–PX11, lý thuyết + passage + câu hỏi có đáp án + giải thích
3. Viết scripts `gen_docx.py` và `gen_tex_hs.py` (tham khảo `Buoi 1/gen_docx.py` và `Buoi 1/gen_tex_hs.py`)
4. Dùng ảnh có sẵn trong `Buoi 2/image/` (4 file: hinh_1_2.png → hinh_1_5.png)

---

## Format buoi_spec.py (BẮT BUỘC theo đúng Buổi 1)

```python
TITLE = 'CHUYÊN ĐỀ CÂN BẰNG HÓA HỌC'
LESSON = 'BUỔI 2: LE CHATELIER QUA Q/Kc (PX7–PX11)'
HEAD = 'CÂN BẰNG HÓA HỌC'

INTRO = [...]  # Đoạn mở đầu nối từ Buổi 1

PX = [
    {
        'title': 'PX7. ...',
        'theory': '...',           # Lý thuyết ngắn, gọn
        'vd': ['...'],             # Ví dụ thực tế
        'reflex': ['...', '...'],  # Phản xạ khi đọc đề TSA
        'trap': ['...', '...'],    # Bẫy / lỗi hay gặp
        'figs': ['Buoi 2/image/hinh_1_N.png'],  # Ảnh nếu có
        'passage': [               # Ngữ liệu bài tập
            'Đoạn văn...',
            {'cap': '...', 'label': '2.N',  # Bảng số liệu
             'rows': [[...], [...]]},
        ],
        'questions': [
            {'q': '...', 'n': 4, 'ans': '...', 'exp': '...'},
            ...
        ],
    },
    ...
]

DEBATE = [...]  # 2–3 câu tranh biện cuối buổi
```

**Các trường quan trọng:**
- `theory`: lý thuyết ngắn, dùng khung Q/Kc (KHÔNG dùng "hệ chống lại tác động")
- `vd`: ví dụ đời thực / công nghiệp
- `reflex`: quy tắc rút gọn kiểu "Đọc đề thấy ... thì nghĩ ngay: ..."
- `trap`: lỗi nhầm điển hình kiểu "Tưởng ... (thực ra ...)"
- `passage`: ngữ liệu + bảng số liệu, mọi số dùng trong câu hỏi phải có ở đây
- `questions`: mỗi câu có `q` (đề), `n` (số dòng trống PDF HS), `ans` (đáp án), `exp` (giải thích)
- `figs`: path ảnh tương đối từ gốc `Can bang hoa hoc/`
- Bảng trong passage: dict `{'cap': ..., 'label': '2.N', 'rows': [[header], [row1], ...]}`
- Hình trong passage: dict `{'fig': 'Buoi 2/image/hinh_1_N.png'}`
- Công thức: tuple `('LaTeX', 'plaintext fallback')` — dùng trong `'formula'` hoặc trong `'example'`

---

## Nội dung 5 phản xạ Buổi 2 (PX7–PX11)

### Triết lý cốt lõi

Buổi 1 kết thúc ở PX6: Q < Kc → chạy thuận, Q > Kc → chạy nghịch. Buổi 2 dùng CHÍNH khung Q/Kc đó để giải thích MỌI tác động Le Chatelier. **Không dạy Le Chatelier kiểu "hệ chống lại tác động bên ngoài"** — dạy bằng cách: tác động → Q thay đổi thế nào so với Kc → hệ chạy chiều nào để Q quay về Kc.

### Nhóm D: Tác động làm lệch Q (Kc không đổi, vì nhiệt độ không đổi)

**PX7. Thêm/bớt chất → Q lệch Kc**
- Thêm chất đầu → Q giảm → Q < Kc → chạy thuận
- Thêm sản phẩm → Q tăng → Q > Kc → chạy nghịch
- Bớt sản phẩm (lấy ra liên tục) → Q < Kc → chạy thuận (giải thích lò nung vôi PX3, nhà máy NH₃)
- **Ngoại lệ quan trọng:** thêm chất RẮN nguyên chất → không xuất hiện trong Q → Q không đổi → KHÔNG chuyển dịch
- Passage gợi ý: hệ CaCO₃(s) ⇌ CaO(s) + CO₂(g) — thêm CaCO₃ thì Q không đổi, mâu thuẫn với suy đoán "thêm chất đầu thì chạy thuận"

**PX8. Nén/giãn thể tích (hệ khí) → Q lệch Kc**
- Nén (giảm V) → nồng độ mọi chất tăng → Q thay đổi tùy tổng số mũ tử/mẫu:
  - Nếu tổng mol khí sản phẩm < tổng mol khí chất đầu → Q tăng → chạy nghịch (giảm mol khí)... NHƯNG cần giải thích qua Q, không qua "hệ chống lại"
  - Chính xác: nén → tất cả nồng độ nhân cùng hệ số → Q thay đổi theo (hệ số)^(Δn) với Δn = tổng hệ số sản phẩm − tổng hệ số chất đầu
- Nếu Δn = 0 (VD: H₂ + I₂ ⇌ 2HI) → nén không đổi Q → KHÔNG chuyển dịch
- Passage gợi ý: so sánh N₂+3H₂⇌2NH₃ (Δn = −2) với H₂+I₂⇌2HI (Δn = 0) khi nén

**PX9. Thêm khí trơ → tùy điều kiện**
- Thêm khí trơ ở V không đổi → nồng độ các chất phản ứng không đổi → Q không đổi → KHÔNG chuyển dịch
- Thêm khí trơ ở P không đổi → V tăng → nồng độ mọi chất giảm → Q thay đổi tùy Δn (giống giãn thể tích)
- Đây là chỗ Le Chatelier "đoán sai" nếu chỉ nhớ "thêm khí trơ không ảnh hưởng" mà không phân biệt V hay P không đổi
- Passage gợi ý: bảng số liệu so sánh 2 trường hợp

### Nhóm E: Tác động dời Kc (nhiệt độ thay đổi)

**PX10. Thay đổi nhiệt độ → Kc thay đổi → cân bằng mới**
- Đây là tác động DUY NHẤT thay đổi Kc
- Phản ứng tỏa nhiệt (ΔH < 0): tăng T → Kc giảm → Q > Kc mới → chạy nghịch
- Phản ứng thu nhiệt (ΔH > 0): tăng T → Kc tăng → Q < Kc mới → chạy thuận
- Mẹo nhớ: coi nhiệt như một "chất" — tỏa nhiệt thì nhiệt nằm phía sản phẩm, tăng T như "thêm nhiệt" → Q > Kc → nghịch. Nhưng cơ chế THẬT là Kc thay đổi, không phải Q.
- Passage gợi ý: Bảng 1 trong Đề 2 (% NH₃ theo T và P) hoặc bảng tương tự; hệ NO₂/N₂O₄ đổi màu theo nhiệt độ
- Nối với Buổi 1: PX4 nói "Kc chỉ phụ thuộc nhiệt độ" — giờ thấy rõ: đổi T thì Kc khác, cân bằng khác

### Nhóm F: Xúc tác

**PX11. Xúc tác — tăng tốc cả hai chiều, không đổi Kc, không đổi Q**
- Xúc tác làm v(thuận) và v(nghịch) cùng tăng → hệ ĐẾN cân bằng nhanh hơn, nhưng VỊ TRÍ cân bằng (Kc) không đổi
- Phần trăm chuyển hóa lúc cân bằng không đổi
- Ý nghĩa công nghiệp: xúc tác Fe trong Haber cho phép chạy ở 450 °C mà vẫn đủ nhanh, thay vì phải lên 600 °C (nơi Kc giảm mạnh, % NH₃ thấp)
- Passage gợi ý: so sánh "có/không xúc tác" — cùng Kc nhưng thời gian đạt cân bằng khác xa

---

## Ảnh có sẵn trong Buoi 2/image/

| File | Gợi ý nội dung (cần mở xem để xác nhận) |
|---|---|
| hinh_1_2.png | Có thể là đồ thị/sơ đồ liên quan Le Chatelier |
| hinh_1_3.png | — |
| hinh_1_4.png | — |
| hinh_1_5.png | — |

**Mở ảnh xem trước khi gán vào PX.** Nếu cần thêm ảnh, gợi ý cho người dùng tìm (không tự tạo ảnh).

---

## Kết nối với Buổi 1

Buổi 1 kết thúc bằng:
- PX6: Q < Kc → thuận, Q > Kc → nghịch, Q = Kc → cân bằng
- TSA section nói: "Buổi sau học tiếp PX7–PX11: các tác động làm lệch Q và làm dời Kc"
- DEBATE Buổi 1: 3 câu tranh biện (cân bằng đã dừng? Q vs Kc? Kc lớn = nhanh?)

INTRO Buổi 2 nên nối từ đó: "Buổi trước biết cách đọc Q và Kc. Giờ hỏi: khi ta tác động vào hệ (thêm chất, nén, đổi nhiệt độ), Q và Kc thay đổi thế nào, và hệ đi về đâu?"

Nhóm PX Buổi 2:
```
D. Tác động nào thay đổi Q mà Kc đứng yên? PX7, PX8, PX9.
E. Tác động nào thay đổi luôn Kc? PX10.
F. Xúc tác thì sao? PX11.
```

---

## Quy tắc văn phong (BẮT BUỘC)

File gốc: `Can bang hoa hoc/Ghi chu van phong.md`

- "chuyển dịch theo chiều thuận / chuyển dịch theo chiều nghịch" — KHÔNG BAO GIỜ dùng "dịch" đứng một mình
- Tối thiểu "dịch chuyển" (vẫn dịch chuyển, không dịch chuyển)
- Không ghi "(số liệu mô phỏng)" hay tương tự
- "giống suy đoán" thay vì "đúng như tưởng"
- "bị áp dụng sai" thay vì "bị áp sai"

---

## Tóm tắt cấu trúc PX Buổi 1 (để giữ nhất quán)

| PX | Tên | Passage | Câu hỏi |
|---|---|---|---|
| PX1 | Phản ứng hai chiều không bao giờ hết chất đầu | HI ⇌ H₂+I₂, 445 °C, 2 bình + đốt CH₄ | 5 câu |
| PX2 | Lượng chất đứng yên, phản ứng vẫn chạy | N₂+3H₂⇌2NH₃, Bảng 1.1 số mol theo t, thí nghiệm D₂ | 5 câu |
| PX3 | Chất vào/ra trong Kc | 4 phản ứng viết Kc, lò nung vôi, Kc(b)=0,0025 | 5 câu |
| PX4 | Tính Kc bằng bảng ICE | PCl₅⇌PCl₃+Cl₂ (2 TN), CO+H₂O⇌CO₂+H₂ | 4 câu |
| PX5 | Kc cho biết đích đến, không cho biết tốc độ | Bảng 1.2 (4 phản ứng, Kc), H₂+O₂ không nổ, NO khí quyển | 4 câu |
| PX6 | So Q với Kc để biết chiều phản ứng | H₂+I₂⇌2HI, Bảng 1.3 (4 bình X/Y/Z/W) | 5 câu |

Mỗi PX Buổi 2 nên có 4–5 câu hỏi, tổng Buổi 2 khoảng 20–25 câu.

---

## Git

- Branch: `claude/eager-ride-3hqm6o`
- Push: `git push -u origin claude/eager-ride-3hqm6o`
- Commit attribution: xem cuối commit message

---

## Checklist trước khi giao

- [ ] `buoi2_spec.py` viết xong, chạy import không lỗi
- [ ] 5 PX (PX7–PX11), mỗi PX có theory/vd/reflex/trap/passage/questions
- [ ] Mọi số liệu trong câu hỏi đều có trong passage
- [ ] Passage có bảng số liệu hoặc hình
- [ ] Văn phong: "chuyển dịch" không "dịch", không "(số liệu mô phỏng)"
- [ ] Giải thích Le Chatelier qua Q/Kc, KHÔNG qua "hệ chống lại tác động"
- [ ] DEBATE có 2–3 câu tranh biện
- [ ] gen_docx.py và gen_tex_hs.py chạy được, xuất file đúng
- [ ] Commit + push
