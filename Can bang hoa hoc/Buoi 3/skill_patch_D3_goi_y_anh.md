# Patch skill D3 — Thêm mục "Gợi ý ảnh/sơ đồ"

**File cần sửa:** `references/prompt_gemini_15.md` trong skill `tsa-exam-creator`
**Vị trí:** Thêm mục mới **trước** mục "Sau khi viết prompt", cuối file.

---

## Nội dung thêm vào

```markdown
## Gợi ý ảnh / sơ đồ cho ngữ liệu (TÁCH RIÊNG, không vào prompt Gemini)

Sau khi in prompt, Claude **gợi ý 1–3 ảnh/sơ đồ** phù hợp với ngữ liệu để người dùng tự tìm. Mục này KHÔNG dán vào prompt Gemini — chỉ in riêng bên ngoài code block.

Format gợi ý:

💡 Ảnh/sơ đồ gợi ý cho đề này:
1. [Loại hình: sơ đồ / ảnh chụp / đồ thị / infographic] — [mô tả ngắn, ví dụ: "sơ đồ vòng tuần hoàn Haber loop, có nhãn tháp xúc tác, bình ngưng tụ, máy nén"]
   → Từ khóa tìm: [gợi ý keyword tiếng Anh để search Google Images / Shutterstock]
   → Vai trò trong đề: [câu nào có thể khai thác hình này]
2. ...

Nguyên tắc:
- Ưu tiên sơ đồ quy trình / thiết bị nếu ngữ liệu có mô tả quy trình
- Ưu tiên ảnh thí nghiệm / hiện tượng thực tế nếu ngữ liệu có mô tả thí nghiệm
- Ghi rõ nhãn tiếng Anh cần dịch nếu ảnh nguồn sẽ có chữ Anh
- Nhắc người dùng ghi nguồn ảnh khi tìm được
```

---

## Mục "Sau khi viết prompt" — sửa thêm 1 dòng

Thêm dòng **"In gợi ý ảnh/sơ đồ bên ngoài code block (mục trên)."** vào giữa:

```markdown
## Sau khi viết prompt
- In prompt trong 1 code block để người dùng copy.
- In gợi ý ảnh/sơ đồ bên ngoài code block (mục trên).   ← DÒNG MỚI
- Nhắc người dùng dán output Gemini lại → chuyển sang D4.
```
