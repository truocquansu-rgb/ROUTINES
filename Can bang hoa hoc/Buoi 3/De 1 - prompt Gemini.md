# Đề 1. Prompt Gemini viết 15 câu (D3)

```
Bạn là người ra đề TSA (Đánh giá Tư duy, ĐHBK Hà Nội), phần Tư duy Khoa học / Giải quyết vấn đề. Đối tượng: học sinh lớp 11 đã học nguyên lí Le Chatelier theo cách so sánh Q với Kc (bảng ba thời điểm: cân bằng ban đầu, ngay sau tác động, cân bằng mới). Học sinh CHƯA được dạy về khí trơ, pha loãng dung dịch và thêm chất rắn: đây là phần các em phải tự suy ra từ ngữ liệu.

NGỮ LIỆU (giữ nguyên, không sửa):
**[1]** Nguyên lí Le Chatelier thường được học sinh nhớ dưới dạng hai câu ngắn: "tăng áp suất thì cân bằng dịch chuyển về phía ít phân tử khí" và "thêm chất nào thì hệ tiêu thụ bớt chất đó". Hai câu này chỉ là cách nói gọn của một quy tắc định lượng. Gọi Q là tỉ số tính bằng đúng công thức của Kc nhưng thay vào nồng độ ngay sau tác động. Nếu Q < Kc, cân bằng chuyển dịch theo chiều thuận; nếu Q > Kc, cân bằng chuyển dịch theo chiều nghịch; nếu Q = Kc, cân bằng không dịch chuyển. Kc chỉ thay đổi khi nhiệt độ thay đổi, và nồng độ chất rắn không có mặt trong biểu thức Kc.

**[2]** Tình huống A. Một hỗn hợp khí đang ở trạng thái cân bằng N₂O₄(g) ⇌ 2NO₂(g) ở nhiệt độ T, với Kc = [NO₂]²/[N₂O₄] = 0,036, [N₂O₄] = 0,100 M và [NO₂] = 0,060 M. Người ta thêm khí argon (Ar), một khí không phản ứng với N₂O₄ và NO₂, theo hai cách. Cách A1: hỗn hợp chứa trong bình cứng, thể tích không đổi; sau khi thêm Ar, áp suất tổng trong bình tăng. Cách A2: hỗn hợp chứa trong xi-lanh có pít-tông chuyển động tự do nên áp suất tổng giữ không đổi; lượng Ar thêm vào làm thể tích khí tăng gấp đôi.

*Hình 1: Thêm khí trơ Ar vào bình cứng (A1) và vào xi-lanh có pít-tông tự do (A2).*

**[3]** Tình huống B. Một dung dịch chứa cân bằng Fe³⁺(aq) + SCN⁻(aq) ⇌ FeSCN²⁺(aq); màu đỏ máu của dung dịch do ion FeSCN²⁺ tạo ra. Ở 25 °C, Kc = [FeSCN²⁺]/([Fe³⁺][SCN⁻]) = 100. Ban đầu [Fe³⁺] = [SCN⁻] = 0,020 M và [FeSCN²⁺] = 0,040 M. Người ta thêm nước cất để thể tích dung dịch tăng gấp đôi, rồi dùng máy đo màu theo dõi nồng độ FeSCN²⁺ đến khi số đo ổn định.

*Hình 2: Dung dịch chứa FeSCN²⁺ trước và sau khi pha loãng gấp đôi.*

**[4]** Tình huống C. Một bình kín ở 25 °C chứa dư NH₄HS rắn, có cân bằng NH₄HS(s) ⇌ NH₃(g) + H₂S(g) với Kc = [NH₃][H₂S] = 1,44·10⁻⁴; lúc cân bằng [NH₃] = [H₂S] = 0,012 M. Người ta cho thêm 10 g NH₄HS rắn vào bình, giữ nguyên nhiệt độ và thể tích.

**Bảng 1:** *Nồng độ (M) các chất ở ba thời điểm.*

| Tình huống | Chất | Cân bằng ban đầu | Ngay sau tác động | Cân bằng mới |
|---|---|---|---|---|
| A1 | N₂O₄ | 0,100 | 0,100 | |
| A1 | NO₂ | 0,060 | 0,060 | |
| A2 | N₂O₄ | 0,100 | 0,050 | 0,0449 |
| A2 | NO₂ | 0,060 | 0,030 | 0,0402 |
| B | Fe³⁺ | 0,020 | 0,010 | 0,0130 |
| B | SCN⁻ | 0,020 | 0,010 | 0,0130 |
| B | FeSCN²⁺ | 0,040 | 0,020 | 0,0170 |
| C | NH₃ | 0,012 | 0,012 | |
| C | H₂S | 0,012 | 0,012 | |

**Bảng 2:** *Dự đoán của một nhóm học sinh khi chỉ dựa vào phát biểu dạng lời của nguyên lí Le Chatelier.*

| Tác động | Dự đoán của nhóm học sinh |
|---|---|
| Thêm Ar vào bình cứng (A1) | Áp suất tổng tăng nên cân bằng chuyển dịch về phía ít phân tử khí, tức chiều nghịch |
| Thêm Ar ở áp suất không đổi (A2) | Áp suất tổng không đổi nên cân bằng không dịch chuyển |
| Pha loãng dung dịch (B) | Mọi nồng độ cùng giảm một nửa nên cân bằng không dịch chuyển |
| Thêm NH₄HS rắn (C) | Thêm chất đầu nên cân bằng chuyển dịch theo chiều thuận |
| Rút bớt NO₂ khỏi bình cứng ở tình huống A (trước khi thêm Ar) | Mất bớt sản phẩm nên cân bằng chuyển dịch theo chiều thuận để tạo lại NO₂ |

**Nguồn: P20 STUDY sưu tầm và tổng hợp**

HÌNH ẢNH ĐI KÈM (đã Việt hóa, không cần dịch):
- Hình 1: hai bình A1 (nắp cố định) và A2 (pít-tông tự do), trước và sau khi thêm Ar; chấm đỏ = N₂O₄, cam = NO₂, xanh = Ar.
- Hình 2: hai ống nghiệm dung dịch FeSCN²⁺, trước và sau khi pha loãng gấp đôi.

NHIỆM VỤ: viết đúng 15 câu hỏi theo ma trận sau, tier độ khó đề M3.
| Dạng | Mức 1 | Mức 2 | Mức 3–4 | Tổng |
|------|-------|-------|---------|------|
| Trắc nghiệm 4 lựa chọn | 1 | 2 | 1 | 4 |
| Đúng–Sai | 1 | 1 | 1 | 3 |
| Điền khuyết | 0 | 2 | 1 | 3 |
| Ghép đôi | 1 | 0 | 2 | 3 |
| Kéo thả | 0 | 0 | 2 | 2 |
| TỔNG | 3 | 4 | 8 | 15 |

ĐỊNH HƯỚNG NỘI DUNG CÂU HỎI:
- Mức 2: tính Q ngay sau tác động từ Bảng 1 và so với Kc; điền ô trống cột "Cân bằng mới" của A1 và C; đánh giá từng dự đoán trong Bảng 2 (đúng hay sai, vì sao).
- Mức 3–4 dùng tình huống MỚI không có trong ngữ liệu, ví dụ: ở cách A2 thay Ar bằng N₂O₄ với cùng số mol khí thêm vào; pha loãng dung dịch B gấp 3 thay vì gấp 2; bơm thêm H₂S vào bình C; dùng số đo máy đo màu để kiểm tra giả thuyết "pha loãng không làm cân bằng dịch chuyển"; xếp một tác động lạ vào nhóm "làm lệch Q" hay "không làm lệch Q".
- Với mọi tình huống mới có tính số, tự giải đầy đủ trong phần giải thích (công thức, thay số, kết quả, làm tròn) để người duyệt kiểm lại.
- Câu Ghép đôi gợi ý: Cột A là các tác động (thêm Ar bình cứng, thêm Ar áp suất không đổi, pha loãng gấp đôi, thêm NH₄HS rắn, tăng nhiệt độ); Cột B là kết quả mô tả bằng Q và Kc, mỗi ý Cột B khác nhau và dùng đúng 1 lần.

LỖI NHẦM LẪN ĐIỂN HÌNH (dùng làm nguyên liệu cho phương án nhiễu):
L1. Thêm khí trơ làm áp suất tổng tăng nên cân bằng dịch chuyển về phía ít phân tử khí (bỏ qua việc nồng độ các chất phản ứng không đổi khi thể tích không đổi).
L2. Pha loãng làm mọi nồng độ giảm như nhau nên cân bằng không dịch chuyển (bỏ qua số mũ và số chất ở tử, mẫu khác nhau).
L3. Thêm chất rắn (chất đầu) thì cân bằng chuyển dịch theo chiều thuận.
L4. Nhầm áp suất tổng với nồng độ từng chất trong biểu thức Kc.
L5. Kết luận "nguyên lí Le Chatelier sai" thay vì "phát biểu dạng lời bị áp dụng sai"; hoặc cho rằng Kc đổi khi pha loãng hay thêm khí trơ.

RÀNG BUỘC:
1. Mọi số liệu, công thức dùng trong câu hỏi phải có trong ngữ liệu hoặc bảng; số liệu cho tình huống mới phải ghi đủ ngay trong đề câu. Câu cần công thức không hiển nhiên thì ghi công thức ngay trong đề câu.
2. Các câu độc lập: đáp án hoặc kết quả tính của câu này không được xuất hiện trong đề câu khác (ví dụ Q = 200 của tình huống B chỉ là đáp án của đúng một câu).
3. Phương án nhiễu xây từ lỗi L1–L5; mỗi nhiễu phải đúng theo một cách đọc lệch ngữ liệu, không nhiễu ngớ ngẩn.
4. Câu mức 3–4 không trả lời được bằng cách tìm chữ trong bài: phải có tính toán, so sánh điều kiện, suy ngược hoặc áp nguyên lý vào tình huống mới.
5. MCQ: 4 phương án dài xấp xỉ nhau, đáp án đúng không phải phương án dài nhất; phương án sai không dùng từ tuyệt đối (hoàn toàn, luôn luôn, không bao giờ).
6. Đúng–Sai: 4 mệnh đề, 2 Đúng 2 Sai, thứ tự Đ/S không lặp giữa các câu Đúng–Sai. Ghép đôi: 4–6 cặp, mỗi ý Cột B dùng đúng 1 lần, không ghi "có ý thừa". Kéo thả: kho có ít nhất 2 từ nhiễu cùng chủ đề. Điền khuyết: ghi rõ đơn vị và quy tắc làm tròn bằng chữ, mỗi ô 1 đáp án.
7. Câu dẫn chuẩn: Đúng–Sai "Các nhận định sau đúng hay sai?"; Điền "Điền từ/cụm từ (không quá 2 tiếng) hoặc số (làm tròn đến ...) vào chỗ trống:"; Ghép đôi "Ghép mỗi ý ở Cột A với một ý ở Cột B."; Kéo thả "Kéo các cụm từ trong kho vào chỗ trống cho phù hợp:".
8. Văn phong khoa học, khách quan. Dấu phẩy thập phân (0,036). Không dùng dấu gạch ngang dài (—), không dùng mũi tên (→) thay từ nối trong câu chữ (được dùng trong phương trình hóa học). Không mở câu bằng "Đây là", "Tuy nhiên", "Vì vậy", "Như vậy".
9. Khi nói về cân bằng, không dùng chữ "dịch" đứng một mình: viết "dịch chuyển" hoặc "chuyển dịch theo chiều thuận/nghịch".

FORMAT MỖI CÂU (bắt buộc, không bỏ dòng nào):
Câu [N]. [Dạng câu] | Độ khó [x,x]/5 | Mức tư duy [1/2/3/4] | [Kỹ năng nâng cao nếu mức ≥3] | [Lỗi khai thác: L?]
[Nội dung câu hỏi + phương án]
▸ Đáp án: [...]
▸ Giải thích: [căn cứ ở đoạn/bảng nào; MCQ giải thích cả 3 nhiễu sai vì sao; Đúng–Sai giải thích từng mệnh đề; Kéo thả không cần giải thích]

Dạng câu chỉ dùng 1 trong: Trắc nghiệm 4 lựa chọn / Đúng–Sai / Điền khuyết / Ghép đôi / Kéo thả.
Kỹ năng nâng cao chỉ dùng 1 trong: Mô hình hóa & Tỷ lệ / Bài toán ngược & Điều kiện biên / Chẩn đoán & Khắc phục / Giả định tình huống / Tối ưu hóa đa mục tiêu / Phân tích dữ liệu chéo.

CUỐI CÙNG: bảng tổng hợp | Câu | Dạng | Độ khó | Mức | Kỹ năng | Lỗi L | Đáp án | và 1 dòng tự đếm số câu theo từng dạng, từng mức để đối chiếu ma trận.
```
