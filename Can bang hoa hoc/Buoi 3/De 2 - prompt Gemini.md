# Đề 2. Nhà máy NH₃: prompt Gemini 15 câu

Tier: M3 · Ngữ liệu đã sửa từ output Gemini (10 fix A1/cường điệu/thiếu dữ kiện) · Lỗi L1–L5 từ idea.

## Prompt (copy nguyên khối dưới đây, kèm ảnh sơ đồ Haber loop)

```
Bạn là người ra đề TSA (Đánh giá Tư duy, ĐHBK Hà Nội), phần Tư duy Khoa học / Giải quyết vấn đề.

NGỮ LIỆU:

NHÀ MÁY NH₃: MỖI LƯỢT CHỈ KHOẢNG 15% VẪN CÓ LÃI

[1] Phản ứng tổng hợp ammonia: N₂(g) + 3H₂(g) ⇌ 2NH₃(g), ΔH = −91,8 kJ. Chiều thuận tỏa nhiệt và làm giảm tổng số mol khí. Trong công nghiệp, phản ứng diễn ra ở 400–450 °C, áp suất 150–200 bar, với xúc tác sắt (Fe).

[2] Hạ nhiệt độ làm phần trăm NH₃ lúc cân bằng tăng (Bảng 1), nhưng tốc độ phản ứng giảm mạnh: ở 350 °C, tốc độ chỉ bằng 1/8 so với 450 °C. Nhà máy chọn 450 °C vì đó là điểm thỏa hiệp giữa phần trăm chuyển hóa và tốc độ đạt cân bằng. Áp suất cao làm tăng phần trăm NH₃ nhưng đòi hỏi máy nén công suất lớn và thiết bị chịu áp dày hơn, nên thường dừng ở khoảng 200 bar.

Bảng 1: Phần trăm NH₃ (%) lúc cân bằng theo nhiệt độ và áp suất (hỗn hợp nạp N₂ : H₂ = 1 : 3).

| Nhiệt độ | 100 bar | 200 bar | 300 bar | Tốc độ tương đối |
|---|---|---|---|---|
| 350 °C | 35,7 | 47,5 | 54,2 | 1 |
| 450 °C | 17,3 | 27,0 | 33,6 | 8 |
| 550 °C | 8,4 | 14,6 | 19,5 | 40 |

[3] Khí đi qua tháp xúc tác nhanh nên không kịp đạt cân bằng: mỗi lượt chỉ khoảng 15% N₂ và H₂ chuyển thành NH₃.

[4] Sơ đồ vòng tổng hợp (Hình 1): khí ra khỏi tháp được làm lạnh, NH₃ hóa lỏng và tách ra ở bình ngưng tụ; N₂ và H₂ chưa phản ứng được máy nén tuần hoàn đưa trở lại tháp cùng khí mới. Việc liên tục lấy NH₃ ra giữ Q luôn nhỏ hơn Kc ở đầu vào tháp, nên chiều thuận luôn được ưu tiên.

Hình 1: Sơ đồ vòng tổng hợp NH₃: tháp xúc tác, làm lạnh, tách NH₃ lỏng, tuần hoàn khí và nhánh xả khí trơ. Nguồn: EnerTherm Engineering, chỉnh sửa bởi P20 STUDY.

[5] Khí trơ tích lũy: Ar (từ không khí) và CH₄ (từ khí thiên nhiên) không phản ứng và không hóa lỏng nên tích tụ dần trong vòng tuần hoàn. Ở áp suất tổng không đổi, khí trơ chiếm thể tích làm loãng N₂ và H₂, khiến phần trăm NH₃ lúc cân bằng giảm (Bảng 3). Nhà máy phải xả bỏ (purge) một phần nhỏ khí tuần hoàn để giữ hàm lượng khí trơ dưới ngưỡng, đồng thời chấp nhận mất theo một ít N₂ và H₂.

Bảng 3: Phần trăm NH₃ (%) lúc cân bằng theo phần trăm khí trơ trong khí nạp (450 °C, 200 bar, N₂ : H₂ = 1 : 3).

| Khí trơ (%) | 0 | 5 | 10 | 20 |
|---|---|---|---|---|
| NH₃ (%) | 27,0 | 24,4 | 22,0 | 17,6 |

[6] Hiệu suất tổng thể: với 15% chuyển hóa mỗi lượt và tuần hoàn liên tục, tổng phần trăm nguyên liệu chuyển thành NH₃ phụ thuộc tỉ lệ xả. Công thức gần đúng:

Tổng chuyển hóa = 0,15 / [1 − 0,85 × (1 − tỉ lệ xả)]

Xả 1% khí tuần hoàn thì khoảng 95% nguyên liệu được chuyển thành NH₃; xả 2% còn khoảng 90%; xả 5% còn khoảng 78%.

[7] Tỉ lệ nạp: phần trăm NH₃ lúc cân bằng lớn nhất khi nạp đúng tỉ lệ hợp thức 1 : 3 (Bảng 2). Dư N₂ hay dư H₂ đều làm giảm phần trăm NH₃, trái với suy đoán "thêm chất đầu thì luôn được nhiều sản phẩm hơn".

Bảng 2: Phần trăm NH₃ (%) lúc cân bằng theo tỉ lệ nạp H₂ : N₂ (450 °C, 200 bar).

| H₂ : N₂ | 1 : 1 | 2 : 1 | 3 : 1 | 4 : 1 | 6 : 1 |
|---|---|---|---|---|---|
| NH₃ (%) | 19,0 | 25,6 | 27,0 | 26,3 | 23,0 |

Nguồn: P20 STUDY sưu tầm và tổng hợp

Đọc ngữ liệu trên và trả lời các câu hỏi sau đây:

GHI CHÚ DỊCH NHÃN HÌNH (Hình 1, sơ đồ vòng tổng hợp):
Fresh feed → Khí mới (N₂ + 3H₂)
Reactor → Tháp xúc tác Fe (450 °C, 200 bar)
Separator → Bình ngưng tụ
Recycle compressor → Máy nén tuần hoàn
Purge → Xả khí trơ 5%
Liquid ammonia / Product → NH₃ lỏng
Recycle stream → Khí chưa phản ứng

NHIỆM VỤ: viết đúng 15 câu hỏi theo ma trận sau, tier độ khó đề M3.

| Dạng | Mức 1 | Mức 2 | Mức 3–4 | Tổng |
|------|-------|-------|---------|------|
| MCQ | 1 | 2 | 1 | 4 |
| Đúng/Sai | 1 | 1 | 1 | 3 |
| Điền khuyết | 0 | 2 | 1 | 3 |
| Ghép đôi | 1 | 0 | 2 | 3 |
| Kéo thả | 0 | 0 | 2 | 2 |
| TỔNG | 3 | 4 | 8 | 15 |

LỖI NHẦM LẪN ĐIỂN HÌNH (dùng làm nguyên liệu cho phương án nhiễu):
L1. Tưởng nhà máy chọn 450 °C vì ở đó phần trăm NH₃ lúc cân bằng cao nhất (thực ra cao nhất ở nhiệt độ thấp; 450 °C là thỏa hiệp với tốc độ).
L2. Tưởng xúc tác Fe làm tăng phần trăm NH₃ lúc cân bằng.
L3. Tưởng chuyển hóa 15% mỗi lượt nghĩa là nhà máy chỉ dùng được 15% nguyên liệu (bỏ qua tuần hoàn).
L4. Tưởng khí trơ không phản ứng thì không ảnh hưởng gì (bỏ qua việc làm loãng ở áp suất tổng không đổi).
L5. Tưởng nạp càng dư N₂ (hoặc H₂) thì càng nhiều NH₃.

RÀNG BUỘC:
1. Mọi số liệu, công thức dùng trong câu hỏi phải có trong ngữ liệu hoặc bảng. Câu cần công thức không hiển nhiên thì ghi công thức ngay trong đề câu.
2. Các câu độc lập: đáp án hoặc kết quả tính của câu này không được xuất hiện trong đề câu khác.
3. Phương án nhiễu xây từ lỗi L1–L5; mỗi nhiễu phải đúng theo một cách đọc lệch ngữ liệu, không nhiễu ngớ ngẩn.
4. Câu mức 3–4 không trả lời được bằng cách tìm chữ trong bài: phải có tính toán, so sánh điều kiện, suy ngược hoặc áp nguyên lý vào dữ liệu mới.
5. MCQ: 4 phương án dài xấp xỉ nhau, đáp án đúng không phải phương án dài nhất; phương án sai không dùng từ tuyệt đối (hoàn toàn, luôn luôn, không bao giờ).
6. Đúng/Sai: 4 mệnh đề, không toàn Đúng hoặc toàn Sai. Ghép đôi: 4–6 cặp, mỗi ý Cột B dùng đúng 1 lần. Kéo thả: kho có ≥2 từ nhiễu cùng chủ đề. Điền khuyết: ghi rõ đơn vị và quy tắc làm tròn, mỗi ô 1 đáp án.
7. Văn phong khoa học, khách quan. Không dùng dấu gạch ngang dài (—) hay mũi tên (→) thay từ nối trong câu chữ. "Dịch" khi nói về cân bằng không bao giờ đứng một mình; tối thiểu "dịch chuyển", đủ nhất là "chuyển dịch theo chiều thuận/nghịch".

FORMAT MỖI CÂU (bắt buộc, không bỏ dòng nào):
Câu [N]. [Dạng câu] | Độ khó [x,x]/5 | Mức tư duy [1/2/3/4] | [Kỹ năng nâng cao nếu mức ≥3] | [Lỗi khai thác: L?]
[Nội dung câu hỏi + phương án]
▸ Đáp án: [...]
▸ Giải thích: [căn cứ ở đoạn/bảng nào; MCQ giải thích cả 3 nhiễu sai vì sao; Đúng/Sai giải thích từng mệnh đề; Kéo thả không cần giải thích]

Dạng câu chỉ dùng 1 trong: Trắc nghiệm 4 lựa chọn / Đúng–Sai / Điền khuyết / Ghép đôi / Kéo thả.
Kỹ năng nâng cao chỉ dùng 1 trong: Mô hình hóa & Tỷ lệ / Bài toán ngược & Điều kiện biên / Chẩn đoán & Khắc phục / Giả định tình huống / Tối ưu hóa đa mục tiêu / Phân tích dữ liệu chéo.

CUỐI CÙNG: bảng tổng hợp | Câu | Dạng | Độ khó | Mức | Kỹ năng | Lỗi L | Đáp án | và 1 dòng tự đếm số câu theo từng dạng, từng mức để đối chiếu ma trận.
```

## Checklist trước khi dán
- [ ] Kèm ảnh sơ đồ Haber loop (file gốc EnerTherm Engineering hoặc bản đã chỉnh sửa)
- [ ] Tier M3
- [ ] Ngữ liệu 7 ý + 3 bảng + 1 sơ đồ, purge 5%→78% đã có
- [ ] Không có "(số liệu mô phỏng)"
- [ ] Văn phong: không "Tuy nhiên" mở câu, không cường điệu, không văn báo chí
- [ ] "chuyển dịch theo chiều thuận/nghịch" (không "dịch" đứng một mình)
