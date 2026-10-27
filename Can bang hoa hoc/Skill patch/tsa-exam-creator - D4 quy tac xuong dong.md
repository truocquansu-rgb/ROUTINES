# Bản vá skill tsa-exam-creator: quy tắc xuống dòng khi xuất bộ câu D4

## 1. SKILL.md, mục "D4 — Check sản phẩm Gemini + lọc 15 → 7–10 câu", thêm bước 5:

5. Xuống dòng chính xác: mặc định xuất docx, mỗi phương án/mệnh đề/ý giải thích một paragraph; nếu xuất .md hoặc chat thì giữa mọi dòng có một dòng trống (chi tiết: `references/loc_15_con_7_10.md`, mục "Quy tắc xuống dòng")

## 2. references/loc_15_con_7_10.md, chèn trước dòng "Sau đó chuyển D5 (check toàn diện).":

### Quy tắc xuống dòng khi xuất bộ câu (BẮT BUỘC)

Lỗi đã gặp: xuất bộ câu ra file .md với mỗi ý trên một dòng đơn. Khi người dùng mở bằng trình xem Markdown, các dòng đơn bị gộp thành một đoạn liền (câu dẫn, A/B/C/D, đáp án, giải thích dính vào nhau), không đọc được.

- Mặc định xuất bộ câu D4 ra **docx** (format A13): mỗi phương án A/B/C/D, mỗi mệnh đề Đúng–Sai (bảng 3 cột), mỗi cặp ghép đôi (bảng Cột A/Cột B), kho kéo thả, "▸ Đáp án", "▸ Giải thích" và **từng ý giải thích** là một paragraph riêng. Render thử docx sang PDF/ảnh để kiểm xuống dòng trước khi gửi.
- Nếu xuất ra **.md** hoặc in trong chat: giữa MỌI dòng phải có **một dòng trống** (dòng metadata, câu dẫn, từng phương án, từng mệnh đề, đáp án, từng ý giải thích). Không dựa vào xuống dòng đơn. Bảng ghép đôi, Đúng–Sai viết bằng bảng Markdown.
- Giải thích MCQ: mỗi phương án sai giải thích trên một dòng riêng ("A sai: …", "B sai: …"). Giải thích Đúng–Sai và Ghép đôi: mỗi mệnh đề/cặp một dòng.
