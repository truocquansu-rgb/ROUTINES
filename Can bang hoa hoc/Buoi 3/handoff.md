# Handoff — Chuyên đề Cân bằng hóa học, Buổi 3

Phiên tiếp theo bắt đầu từ đây. Đọc file này trước khi làm bất cứ gì.

---

## Trạng thái hiện tại

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
