# Handoff — Soạn giáo án Buổi 2: Le Chatelier qua Q/Kc (PX7–PX10)

Phiên mới bắt đầu từ đây. Đọc file này trước khi làm bất cứ gì.

---

## Bối cảnh chuyên đề

Chuyên đề TSA "Cân bằng hóa học" gồm 3 buổi, dạy học sinh chuẩn bị thi TSA (ĐHBK Hà Nội).

```
BUỔI 1 ✅ DONE — Cân bằng động, Kc và Q (PX1–PX6)
BUỔI 2 ← BẠN LÀM CÁI NÀY — Le Chatelier qua Q/Kc (PX7–PX10)
BUỔI 3 — Kiểm tra + chữa bài (5 đề TSA, đã/đang soạn riêng ở Buoi 3/)
```

Buổi 2 **không có đề kiểm tra**. Bài tập nằm trong các PX (passage + câu hỏi tự luyện, giống Buổi 1).

---

## Bài học từ phiên A (quan trọng, đọc kĩ)

Phiên A chạy thử trên branch `claude/relaxed-rubin-0upeik` và phát hiện:

**PX7 gốc (thêm/bớt chất) BỊ BỎ vì trùng kiến thức Buổi 1:**
- PX3 Buổi 1 đã dạy: chất rắn nguyên chất không có trong Kc → thêm CaCO₃ thì Q không đổi.
- PX3 Buổi 1 đã dạy: lò nung vôi dùng quạt hút CO₂ → Q < Kc → chạy thuận.
- Nếu giữ PX7 (thêm/bớt chất) → trùng gần hết, HS sẽ thấy giảng lại.

**Đánh số lại: PX8→PX7, PX9→PX8, PX10→PX9, PX11→PX10. Buổi 2 còn 4 PX.**

---

## Trạng thái file hiện tại

| File | Trạng thái |
|---|---|
| `buoi2_spec.py` | ✅ Đã có, 4 PX (PX7–PX10), import OK |
| `gen_docx.py` | ✅ Đã có, chạy OK, xuất 2 file docx |
| `gen_tex_hs.py` | ❌ Chưa có (cần tạo nếu muốn PDF LaTeX HS) |
| `Buổi 2. Le Chatelier qua Q-Kc.docx` | ✅ Bản HS |
| `Buổi 2. [SOURCE] Le Chatelier qua Q-Kc.docx` | ✅ Bản GV |

---

## 4 phản xạ Buổi 2 (PX7–PX10)

### Triết lý cốt lõi

Buổi 1 kết thúc ở PX6: Q < Kc → chạy thuận, Q > Kc → chạy nghịch. Buổi 2 dùng CHÍNH khung Q/Kc đó để giải thích MỌI tác động Le Chatelier. **Không dạy Le Chatelier kiểu "hệ chống lại tác động bên ngoài"** — dạy bằng cách: tác động → Q thay đổi thế nào so với Kc → hệ chạy chiều nào để Q quay về Kc.

### Nhóm D: Tác động làm lệch Q (Kc không đổi, vì nhiệt độ không đổi)

**PX7. Nén/giãn thể tích — Q lệch Kc**
- Nén (giảm V) → nồng độ mọi chất tăng → Q thay đổi theo k^Δn
- Δn < 0: nén → Q giảm → chạy thuận
- Δn > 0: nén → Q tăng → chạy nghịch
- **Δn = 0 (VD: H₂ + I₂ ⇌ 2HI) → nén không đổi Q → KHÔNG chuyển dịch**
- Passage: so sánh N₂+3H₂⇌2NH₃ (Δn = −2) với H₂+I₂⇌2HI (Δn = 0) khi nén
- Ảnh: hinh_1_5.png (xi-lanh nén khí NO₂)

**PX8. Thêm khí trơ → tùy điều kiện**
- V không đổi → Q không đổi → KHÔNG chuyển dịch
- P không đổi → V tăng → tương đương giãn thể tích → xét Δn
- Chỗ Le Chatelier "đoán sai" nếu chỉ nhớ "thêm khí trơ không ảnh hưởng"
- Passage: bảng so sánh 2 bình (V cố định vs P cố định)

### Nhóm E: Tác động dời Kc (nhiệt độ thay đổi)

**PX9. Thay đổi nhiệt độ — tác động duy nhất dời Kc**
- Tỏa nhiệt (ΔH < 0): tăng T → Kc giảm → Q > Kc → nghịch
- Thu nhiệt (ΔH > 0): tăng T → Kc tăng → Q < Kc → thuận
- Passage: N₂O₄ ⇌ 2NO₂ đổi màu theo nhiệt độ, bảng Kc theo T
- Ảnh: hinh_1_2.png + hinh_1_3.png (ống NO₂ và CH₃COONa đổi màu ở nóng/lạnh)

### Nhóm F: Xúc tác

**PX10. Xúc tác — nhanh hơn nhưng đích đến giữ nguyên**
- v(thuận) và v(nghịch) cùng tăng → đến cân bằng nhanh hơn, Kc không đổi
- Phần trăm chuyển hóa lúc cân bằng không đổi
- Passage: so sánh có/không V₂O₅ trong quy trình sản xuất H₂SO₄

---

## Ảnh trong Buoi 2/image/

| File | Nội dung | Dùng ở |
|---|---|---|
| hinh_1_2.png | 3 ống NO₂/N₂O₄: nước đá → nhạt, 25°C → cam, nước nóng → nâu đậm | PX9 |
| hinh_1_3.png | 3 ống CH₃COONa + phenolphthalein: đổi màu theo nhiệt độ | PX9 |
| hinh_1_4.png | 3 ống CH₃COONa: thêm tinh thể/thêm CH₃COOH → đổi màu | Thừa (old PX7 đã bỏ) |
| hinh_1_5.png | Xi-lanh nén khí NO₂: 3 trạng thái nén | PX7 |

---

## Kết nối với Buổi 1

Buổi 1 kết thúc bằng:
- PX6: Q < Kc → thuận, Q > Kc → nghịch, Q = Kc → cân bằng
- TSA section nói: "Buổi sau học tiếp PX7–PX11: các tác động làm lệch Q và làm dời Kc"

INTRO Buổi 2 nối từ đó: "Buổi trước biết cách đọc Q và Kc. Giờ hỏi: khi ta tác động vào hệ (nén, thay đổi nhiệt độ, thêm xúc tác), Q và Kc thay đổi thế nào, và hệ đi về đâu?"

Nhóm PX Buổi 2:
```
D. Tác động nào thay đổi Q mà Kc đứng yên? PX7, PX8.
E. Tác động nào thay đổi luôn Kc? PX9.
F. Xúc tác thì sao? PX10.
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

## Checklist

- [x] `buoi2_spec.py` viết xong, chạy import không lỗi
- [x] 4 PX (PX7–PX10), mỗi PX có theory/vd/reflex/trap/passage/questions
- [x] Mọi số liệu trong câu hỏi đều có trong passage
- [x] Passage có bảng số liệu hoặc hình
- [x] Văn phong: "chuyển dịch" không "dịch", không "(số liệu mô phỏng)"
- [x] Giải thích Le Chatelier qua Q/Kc, KHÔNG qua "hệ chống lại tác động"
- [x] DEBATE có 3 câu tranh biện
- [x] gen_docx.py chạy được, xuất file đúng (bản HS + bản GV [SOURCE])
- [ ] gen_tex_hs.py (chưa tạo)
- [ ] Commit + push
