# Handoff — Chuyên đề Cân bằng hóa học (3 buổi)

Phiên tiếp theo bắt đầu từ đây. Đọc file này trước khi làm bất cứ gì.

---

## Giáo án tổng thể — Chuyên đề Cân bằng hóa học (3 buổi)

### Triết lý chuyên đề
Chuyên đề TSA KH&GQVĐ về cân bằng hóa học, dạy cho học sinh chuẩn bị thi TSA (ĐHBK Hà Nội). Mỗi buổi gồm lý thuyết + phản xạ (PX) + passage + câu hỏi tự luyện. Đề kiểm tra dùng ngữ liệu thực tế (nhà máy, thí nghiệm, y học) kèm bảng số liệu, sơ đồ. Skill: `anthropic-skills:tsa-exam-creator`.

### Cấu trúc 3 buổi

```
BUỔI 1 ✅ DONE — Cân bằng động, Kc và Q (PX1–PX6)
BUỔI 2 ❌ CHƯA XÂY — Le Chatelier qua Q/Kc (PX7–PX11)
  ↓ BTVN sau Buổi 2: Đề 1 (M3–4) + Đề 2 (M3) + Đề 3 (M3–4)
BUỔI 3 — 30 phút đầu: Đề 4 (M2) + Đề 5 (M2), sau đó chữa cả 5 đề
```

### Buổi 1 — Cân bằng động, Kc và Q ✅ DONE

**Thư mục:** `Can bang hoa hoc/Buoi 1/`
**File chính:** `buoi1_spec.py` (spec Python chứa toàn bộ nội dung), `gen_docx.py` (xuất docx GV), `gen_tex_hs.py` (xuất PDF LaTeX HS)
**Output đã có:** SOURCE docx, docx GV, PDF HS, zip Overleaf

**Nội dung:** 6 phản xạ chia 3 nhóm:
- **A. Phản ứng có chạy hết không?**
  - PX1: Phản ứng hai chiều không bao giờ hết chất đầu (passage: HI ⇌ H₂+I₂ ở 445 °C)
  - PX2: Lượng chất đứng yên, phản ứng vẫn chạy — cân bằng động (passage: N₂+3H₂ ⇌ 2NH₃, Bảng 1.1 số mol theo thời gian)
- **B. Hệ dừng lại ở đâu? (Kc)**
  - PX3: Hằng số cân bằng Kc — con số cho biết hệ "thích" chiều nào
  - PX4: Kc chỉ phụ thuộc nhiệt độ
  - PX5: Chất rắn và chất lỏng nguyên chất không xuất hiện trong biểu thức Kc
- **C. Lúc này hệ chạy chiều nào? (Q)**
  - PX6: So sánh Q với Kc để biết hệ chạy chiều nào

**Mỗi PX gồm:** lý thuyết ngắn → ví dụ thực tế → phản xạ (quy tắc rút gọn khi đọc đề) → bẫy (lỗi hay gặp) → passage + câu hỏi tự luyện (có đáp án + giải thích).

### Buổi 2 — Le Chatelier qua Q/Kc ❌ CHƯA XÂY

**Thư mục:** `Can bang hoa hoc/Buoi 2/` — hiện chỉ có `image/` (4 ảnh: hinh_1_2.png → hinh_1_5.png)
**Chưa có:** spec (tương tự `buoi1_spec.py`), docx, PDF, gen scripts

**Nội dung dự kiến:** 5 phản xạ (PX7–PX11), dạy Le Chatelier KHÔNG qua "nguyên lí dịch chuyển" mà qua khung Q/Kc:
- PX7–PX9: Các tác động làm lệch Q (thêm/bớt chất, nén/giãn, pha loãng) → Q ≠ Kc → hệ chạy chiều nào
- PX10: Tác động dời Kc (thay đổi nhiệt độ) → cân bằng mới
- PX11: Xúc tác — không đổi Kc, không đổi Q, chỉ đổi tốc độ

**Không có đề kiểm tra trong buổi 2.** Bài tập nằm trong PX (tương tự Buổi 1).

**Nhiệm vụ xây Buổi 2:**
1. Viết spec `buoi2_spec.py` theo format `buoi1_spec.py` (PX7–PX11, mỗi PX có theory/vd/reflex/trap/passage/questions)
2. Các passage cần bảng số liệu hoặc sơ đồ — dùng ảnh trong `Buoi 2/image/`
3. Gen docx GV + PDF LaTeX HS (scripts tương tự Buổi 1)
4. Lý thuyết bám khung Q/Kc: mọi tác động giải thích qua Q thay đổi so với Kc, KHÔNG dùng "hệ chống lại tác động" kiểu phát biểu cũ

### BTVN sau Buổi 2 — 3 đề (M3–M4)

Học sinh làm ở nhà, nộp trước Buổi 3:
- **Đề 1** "Khi Le Chatelier đoán sai" (M3–4) — ✅ DONE, 6 câu, D5 đã xong
- **Đề 2** "Nhà máy NH₃: mỗi lượt chỉ khoảng 15% vẫn có lãi" (M3) — 🔄 10 câu lọc D4, chờ chốt final list
- **Đề 3** "Hemoglobin–CO–buồng oxy cao áp" (M3–4) — ❌ chưa bắt đầu

### Buổi 3 — Kiểm tra + Chữa bài

**30 phút đầu:** Làm tại lớp 2 đề ngắn (M2, ôn lại Buổi 1+2):
- **Đề 4** "Từ hồ muối Ai Cập đến Kc" (M2) — ❌ có idea+prompt, chưa chạy Gemini
- **Đề 5** "Nhật ký lò tổng hợp methanol" (M2) — ❌ có idea+prompt, chưa chạy Gemini

**Phần còn lại:** Chữa cả 5 đề (Đề 1–3 BTVN + Đề 4–5 vừa làm).

### Thứ tự ưu tiên công việc còn lại

1. **Đề 2:** Người dùng chốt final list → D5 → docx
2. **Đề 3:** Idea → ngữ liệu → prompt Gemini → D4 → D5 → docx
3. **Đề 4 & 5:** Chạy Gemini (prompt đã có trong `De 4-5 - idea va prompt Gemini.md`) → D4 → D5 → docx
4. **Buổi 2:** Viết spec PX7–PX11 → gen docx + PDF

---

## Trạng thái chi tiết từng đề

### Đề 1 — "Khi Le Chatelier đoán sai" ✅
- Ngữ liệu: `De 1 - ngu lieu.md`
- D4 bộ câu: `De 1 - D4 bo cau.md` (6 câu cuối cùng, đã qua D5)
- Docx SOURCE (ngữ liệu + câu hỏi + đáp án): chạy `python3 gen_de1_docx.py`
- Ảnh đã chèn: `image/de1_hinh1.png` (FeSCN pha loãng, P20 STUDY), `image/de1_hinh2.png` (khí trơ A1/A2, Shutterstock)
- **DONE.** Chỉ chờ xuất docx teacher format nếu cần.

### Đề 2 — "Nhà máy NH₃: mỗi lượt chỉ khoảng 15% vẫn có lãi" 🔄
- Ngữ liệu + 10 câu đã lọc D4: **`De 2 - D4 bo cau.md`** (file duy nhất cần đọc)
- Sơ đồ Haber loop: `image/de2_hinh1.png` (tiếng Việt, ghi 200 atm — ngữ liệu ghi 200 bar, cần note)
- Prompt Gemini gốc: `De 2 - prompt Gemini.md`
- Idea gốc: `De 2 - idea.md`

**BƯỚC KẾ TIẾP:**
1. **Người dùng chốt final list câu hỏi** — duyệt 10 câu trong `De 2 - D4 bo cau.md`, có thể bỏ/thêm/swap/chỉnh
2. Sau khi chốt → **D5 check toàn diện** (GĐ1 nội dung /10 → GĐ2 hình thức /10)
3. Xuất docx SOURCE (gen script tương tự `gen_de1_docx.py`)

### Đề 3 — "Hemoglobin–CO–buồng oxy cao áp" ❌
- Chưa bắt đầu. Cần: idea → ngữ liệu → prompt Gemini → D4 → D5.

### Đề 4 — "Từ hồ muối Ai Cập đến Kc" (M2) ❌
- Idea + prompt: `De 4 - idea va prompt Gemini.md` hoặc `De 4-5 - idea va prompt Gemini.md`
- Chưa có output Gemini.

### Đề 5 — "Nhật ký lò tổng hợp methanol" (M2) ❌
- Idea + prompt: `De 5 - idea va prompt Gemini.md` hoặc `De 4-5 - idea va prompt Gemini.md`
- Chưa có output Gemini.

---

## Quy tắc cần nhớ

### Flow D4 (đã update skill)
```
Gemini 15 câu → Claude lọc 7–10 (Bước 1–2) → Người dùng chốt final list (Bước 2b) → D5
```
**Không chạy D5 khi người dùng chưa xác nhận danh sách câu.**

### Văn phong CBHH (file `Ghi chu van phong.md`)
- "chuyển dịch theo chiều thuận/nghịch" (không bao giờ dùng "dịch" đứng một mình)
- Không ghi "(số liệu mô phỏng)"
- Xem full quy tắc trong `Can bang hoa hoc/Ghi chu van phong.md`

### Ảnh sơ đồ Đề 2
- `de2_hinh1.png` ghi **200 atm** trên sơ đồ, ngữ liệu ghi **200 bar**
- 1 atm ≈ 1,013 bar → sai số nhỏ, nhưng cần note trong caption hoặc ngữ liệu khi xuất đề chính thức
- Nguồn: EnerTherm Engineering, chỉnh sửa bởi P20 STUDY

### Gen docx
- Dùng python-docx, xem mẫu `gen_de1_docx.py`
- Ảnh chèn bằng `r.add_picture(img_path, width=Cm(13))`
- IMG dict map số hình → file path

### Git
- Branch: `claude/eager-ride-3hqm6o`
- Push: `git push -u origin claude/eager-ride-3hqm6o`
- Commit attribution: `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`

---

## Skill TSA
- Invoke: `anthropic-skills:tsa-exam-creator`
- D4 reference: `references/loc_15_con_7_10.md` (đã thêm Bước 2b — người dùng chốt)
- D5 reference: `references/check_toan_dien.md`
- Docx teacher format: `references/de_note_level_key.md` + docx skill
