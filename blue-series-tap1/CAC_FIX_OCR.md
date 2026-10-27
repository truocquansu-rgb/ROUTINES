# Các fix OCR – Blue Series Tập 1: Tư Duy Đọc Hiểu

- File gốc: `goc.md` (bản OCR nguyên trạng).
- File đã sửa: `Blue_Series_Tap1_da_sua_OCR.md`.

## 1. Dọn tự động (toàn file)

| Loại | Số lượng |
|---|---|
| Bỏ dòng watermark "ooo", "## ooo TSA ooo", "looo", đuôi "ooo TSA/STUDY ooo"; nối lại câu bị watermark cắt đôi | ~100 dòng, 17 chỗ nối |
| Bỏ thẻ `<sub>`/`<sup>` bọc chữ thường (lỗi OCR chữ nhỏ cuối dòng); giữ chỉ số thật như CO<sub>2</sub>, m<sup>2</sup> | 474 |
| `$\mathrm{CO}_2$` → CO<sub>2</sub> | 8 |
| Ð (eth) → Đ | 10 |
| ◯ → ○ | 2 |
| Bỏ dòng watermark trong bảng (`P20STUDY`, `TSA`) | 9 |
| Thêm dòng tiêu đề "Đúng / Sai" cho bảng Đúng–Sai bị mất tiêu đề; bỏ dòng "Đúng Sai" lạc phía trên bảng | 9 / 5 |
| Bỏ chân trang lọt vào nội dung ("Tập 1/4: Tư Duy Đọc Hiểu", "51 Thầy Đào Anh Phúc – Zalo…") | 3 |

## 2. Sửa thủ công theo dòng (879 chỗ)

Gồm: sai dấu/chính tả do OCR, phương án 2 cột bị trộn thứ tự (tách lại thành từng dòng A-B-C-D), phương án dính vào dòng câu hỏi, "## " gắn nhầm vào lời thoại/phương án, tiêu đề chủ đề dính vào tên bài, "-" thay cho ".", mục lục.
Số dòng dưới đây là số dòng của bản trung gian sau bước 1 (sau khi bỏ watermark), không phải của file gốc.

| Dòng | Cũ | Mới |
|---|---|---|
| 1 | Tài liu luyn | Tài liệu luyện |
| 3 | TU DUY DC HIU | TƯ DUY ĐỌC HIỂU |
| 5 | TÂP1 | TẬP 1 |
| 22 | ĐỌC HIỆU | ĐỌC HIỂU |
| 55 | ĐỌC HIỀU | ĐỌC HIỂU |
| 177 | được phẩm | dược phẩm |
| 177 | giám tồn thất | giảm tổn thất |
| 206 | đầu cọ | dầu cọ |
| 220 | statellite | satellite |
| 240 | đồi hỏi | đòi hỏi |
| 302 | từ vải tuần xuống vải giây | từ vài tuần xuống vài giây |
| 340 | Tạo số cái | Tạo sổ cái |
| 378 | thức đẩy | thúc đẩy |
| 420 | công ty lón | công ty lớn |
| 420 | rào cần | rào cản |
| 448 | vải bản các chợ | vải bán các chợ |
| 490 | cuộc đồi | cuộc đời |
| 490 | ấm cứng trong lòng, bổ hết nối lo sợ | ấm cúng trong lòng, bỏ hết nỗi lo sợ |
| 528 | Lòng một nhọc | Lòng mệt nhọc |
| 528 | Tâm hồng giản dị được nghi ngoại yên tỉnh | Tâm hồn giản dị được nghỉ ngơi yên tĩnh |
| 534 | về về đẹp | về vẻ đẹp |
| 534 | vật và là | vất vả là |
| 534 | thô đệt | thô dệt |
| 568 | tỉnh thần | tinh thần |
| 626 | răng tre | rặng tre |
| 626 | Đôi môi đồ như sãm máu | Đôi môi đỏ như sẫm máu |
| 815 | cắm hoàn toàn | cấm hoàn toàn |
| 815 | ra khởi | ra khỏi |
| 815 | Nuôi cây tế bào | Nuôi cấy tế bào |
| 815 | ứng hộ | ủng hộ |
| 873 | Nuôi cây tế bào | Nuôi cấy tế bào |
| 916 | ứng hộ | ủng hộ |
| 916 | nhân mạnh | nhấn mạnh |
| 916 | phần đối | phản đối |
| 916 | độ tin cây | độ tin cậy |
| 928 | nhanh<sub>hơn?</sub> | nhanh hơn? |
| 948 | tư duy cực cực đoan | tư duy cực đoan |
| 1019 | nguyên tắc 3R phương pháp thay thế | nguyên tắc 3R

phương pháp thay thế |
| 1021 | tàn nhẫn tiến bộ | tàn nhẫn

tiến bộ |
| 1023 | tranh cãi chưa có hồi kết cân bằng | tranh cãi chưa có hồi kết

cân bằng |
| 1025 | đạo đức và khoa học cấu trúc | đạo đức và khoa học

cấu trúc |
| 1037 | chuyến sang | chuyển sang |
| 1037 | chuyển bay | chuyến bay |
| 1077 | Mình đã sổng | Mình đã sống |
| 1085 | quyết liệt đen bên | quyết liệt đến bên |
| 1085 | Đen gần trưa | Đến gần trưa |
| 1085 | đã chút hơi thở | đã trút hơi thở |
| 1119 | kiểm thêm | kiếm thêm |
| 1119 | cẩm | cảm |
| 1119 | thì thẩm | thì thầm |
| 1119 | hoàng sợ | hoảng sợ |
| 1133 | Khoảnh khác | Khoảnh khắc |
| 1133 | trong giác mơ | trong giấc mơ |
| 1133 | giắc mơ | giấc mơ |
| 1133 | thì thẩm | thì thầm |
| 1147 | Cửa số | Cửa sổ |
| 1155 | lại lại đầy | lại đầy |
| 1197 | thì thẩm | thì thầm |
| 1197 | kiểm thêm | kiếm thêm |
| 1200 | Sự kiện trì | Sự kiên trì |
| 1280 | người của cha | người cha |
| 1288 | nội bật | nổi bật |
| 1294 | chuyến sang | chuyển sang |
| 1294 | chuyển bay | chuyến bay |
| 1304 | ## CHỦ ĐỀ 5 NGHỊCH | ## CHỦ ĐỀ 5

## NGHỊCH |
| 1366 | phần ứng | phản ứng |
| 1459 | Câu 12. [P20 STUDY]   | ## Câu 12. [P20 STUDY] |
| 1492 | Cửa số | Cửa sổ |
| 1514 | Nhiệt độ Áp suất | Nhiệt độ

Áp suất |
| 1516 | môi trường Chi phí | môi trường

Chi phí |
| 1518 | xúc tác Loại dung môi | xúc tác

Loại dung môi |
| 1659 | dân thần lệ quỷ | dâm thần lệ quỷ |
| 1675 | Sử giả | Sứ giả |
| 1689 | Dĩ Thành thiết lập pháp luật để quản lí Sự công bằng trong cách xử lí của Dĩ chúng quỷ. Thành. | Dĩ Thành thiết lập pháp luật để quản lí chúng quỷ.

Sự công bằng trong cách xử lí của Dĩ Thành. |
| 1691 | Khẳng định quyền uy tuyệt đối của Dĩ Khả năng kiềm chế ma quỷ của nhân Thành đối với thế giới. vật chính. | Khẳng định quyền uy tuyệt đối của Dĩ Thành đối với thế giới.

Khả năng kiềm chế ma quỷ của nhân vật chính. |
| 1703 | sợ hải | sợ hãi |
| 1703 | quỹ | quỷ |
| 1703 | kiểm chế | kiềm chế |
| 1703 | lời mòi | lời mời |
| 1703 | nề phục | nể phục |
| 1703 | Lê Ngô nhận | Lê Ngộ nhận |
| 1711 | Hành Động | Hành động |
| 1711 | ma quỹ | ma quỷ |
| 1711 | sợ hải | sợ hãi |
| 1711 | Đến mòi | Đến mời |
| 1711 | Vén mảnh ra chào đón người cuối ngựa thanh song, kể hầu đầy tới rộn rip. | Vén mành ra chào đón người cưỡi ngựa thanh song, kẻ hầu đầy tớ rộn rịp. |
| 1711 | để thò | để thờ |
| 1739 | điều gì? Sự nghiêm khắc tuyệt đối trong việc Mong muốn biến chúng quỷ thành trị tội và phạt chúng quỷ. những thần linh bảo vệ dân. Khả năng kiểm soát và thống trị âm Mong muốn cải tạo chúng quỷ. linh. | điều gì?

Sự nghiêm khắc tuyệt đối trong việc trị tội và phạt chúng quỷ.

Mong muốn biến chúng quỷ thành những thần linh bảo vệ dân.

Khả năng kiểm soát và thống trị âm linh.

Mong muốn cải tạo chúng quỷ. |
| 1745 | Sự tàn bạo và độc đoán trong cách cai<sub>trị</sub> <sub>của</sub> <sub>ông.</sub> Khẳng định sự luật nghiêm minh và<sub>không</sub> <sub>khoan</sub> <sub>nhượng.</sub> | Sự tàn bạo và độc đoán trong cách cai trị của ông.

Khẳng định sự luật nghiêm minh và không khoan nhượng. |
| 1747 | Mong muốn gây sợ hãi để củng cố Cách thức truyền thống để xử lí những quyền uy cá nhân. kẻ vi phạm luật lệ. | Mong muốn gây sợ hãi để củng cố quyền uy cá nhân.

Cách thức truyền thống để xử lí những kẻ vi phạm luật lệ. |
| 1781 | là gì? Chủ đề nhân cách con người. Chủ đề xã hội. Chủ đề nhân quả trong niềm tin Chủ đề về tình người. phương Đông. | là gì?

Chủ đề nhân cách con người.

Chủ đề xã hội.

Chủ đề nhân quả trong niềm tin phương Đông.

Chủ đề về tình người. |
| 1799 | văn bản: Truyện tiểu thuyết. Truyện đồng thoại. Truyện thần thoại. Truyện truyền kỳ. | văn bản:

Truyện tiểu thuyết.

Truyện đồng thoại.

Truyện thần thoại.

Truyện truyền kỳ. |
| 1803 | văn bản trên? Sử dụng đan xen đa dạng phương thức biểu đạt. Sử dụng từ ngữ có yếu tố tâm linh. Sử dụng yếu tố kì ảo. Sử dụng | văn bản trên?

Sử dụng đan xen đa dạng phương thức biểu đạt.

Sử dụng từ ngữ có yếu tố tâm linh.

Sử dụng yếu tố kì ảo.

Sử dụng |
| 1811 | Sử dụng những từ ngữ biểu hiện ý <sub>ế</sub> Sử dụng câu hỏi thể hiện ý nghi ngờ,<sub>chất</sub> <sub>vấn.</sub> | Sử dụng những từ ngữ biểu hiện ý […] (chữ bị mất khi chuyển đổi, cần đối chiếu bản gốc)

Sử dụng câu hỏi thể hiện ý nghi ngờ, chất vấn. |
| 1813 | khẳng định. Sử dụng | khẳng định.

Sử dụng |
| 1819 | chúng quý | chúng quỷ |
| 1819 | kết đẳng | kết đảng |
| 1861 | câu"ai | câu "ai |
| 1955 | quản thể | quần thể |
| 1995 | <tr><td colspan="2">TSA'</td></tr> |  |
| 1999 | kháng kháng sinh? So sánh Ẩn dụ Điệp ngữ Hoán dụ | kháng kháng sinh?

So sánh

Ẩn dụ

Điệp ngữ

Hoán dụ |
| 2003 | biện pháp tu từ nào? Nhân hóa <sub>So</sub> <sub>sánh</sub> Thậm xưng Đối lập | biện pháp tu từ nào?

Nhân hóa

So sánh

Thậm xưng

Đối lập |
| 2007 | là gì? Đưa ra lý thuyết khoa học về hiện tượng kháng kháng sinh. Giới thiệu khái quát vấn đề, nhấn mạnh tính cấp bách và phạm vi ảnh hưởng. So sánh tình hình kháng kháng sinh tại Việt Nam với thế giới. Phân tích | là gì?

Đưa ra lý thuyết khoa học về hiện tượng kháng kháng sinh.

Giới thiệu khái quát vấn đề, nhấn mạnh tính cấp bách và phạm vi ảnh hưởng.

So sánh tình hình kháng kháng sinh tại Việt Nam với thế giới.

Phân tích |
| 2035 | nguyên tắc nào? So sánh - đối chiếu Nguyên nhân - kết quả Vấn đề - phân tích - giải pháp Thời gian - không gian | nguyên tắc nào?

So sánh - đối chiếu

Nguyên nhân - kết quả

Vấn đề - phân tích - giải pháp

Thời gian - không gian |
| 2039 | là gì? Tự sự Miêu tả Nghị luận Biểu cảm | là gì?

Tự sự

Miêu tả

Nghị luận

Biểu cảm |
| 2043 | kháng kháng sinh? Đoạn 6-7 (về tác động đến hệ sinh Đoạn 2-3 (về cơ chế kháng thuốc) thái) Đoạn 10 (về dự báo của WHO) Đoạn 11 (về nguyên tắc sử dụng kháng sinh) | kháng kháng sinh?

Đoạn 6-7 (về tác động đến hệ sinh thái)

Đoạn 2-3 (về cơ chế kháng thuốc)

Đoạn 10 (về dự báo của WHO)

Đoạn 11 (về nguyên tắc sử dụng kháng sinh) |
| 2118 | mặt tàn phần | mặt tàn phấn |
| 2118 | khiến đôi khi rõ những | khiến đôi khi rỏ những |
| 2126 | quang trọng | quan trọng |
| 2134 | ngồi cuống chiều gió | ngồi cuối chiều gió |
| 2140 | trước đến Bạch Mã | trước đền Bạch Mã |
| 2160 | ura chuộng | ưa chuộng |
| 2160 | riêu của | riêu cua |
| 2160 | Ăn quả đã | Ăn quà đã |
| 2223 | là? Nghị luận kết hợp với tự sự. Tự sự kết hợp với miêu tả, nghị luận. Biểu cảm, thuyết minh kết hợp với Miêu tả thuần túy. miêu tả, tự sự. | là?

Nghị luận kết hợp với tự sự.

Tự sự kết hợp với miêu tả, nghị luận.

Biểu cảm, thuyết minh kết hợp với miêu tả, tự sự.

Miêu tả thuần túy. |
| 2241 | thống. Chủ đề ẩm thực Hà Nội. Chủ đề ẩm thực. Chủ đề dân gian. | thống.

Chủ đề ẩm thực Hà Nội.

Chủ đề ẩm thực.

Chủ đề dân gian. |
| 2245 | văn bản? Đề tài ẩm thực Hà Nội. Đề tài thức quà mặn. Đề tài ẩm thực. Đề tài | văn bản?

Đề tài ẩm thực Hà Nội.

Đề tài thức quà mặn.

Đề tài ẩm thực.

Đề tài |
| 2249 | văn bản trên Tản văn. Phóng sự. Kí sự. Tuỳ bút. | văn bản trên:

Tản văn.

Phóng sự.

Kí sự.

Tuỳ bút. |
| 2253 | (chọn nhiều đáp án đúng) Tập trung | (chọn nhiều đáp án đúng)

Tập trung |
| 2253 | rõ rang. Thể hiện | rõ ràng.

Thể hiện |
| 2253 | sự vật. Sử dụng | sự vật.

Sử dụng |
| 2253 | rõ rang. Trình bày | rõ ràng.

Trình bày |
| 2253 | cảm xúc cá nhân. Kết hợp | cảm xúc cá nhân.

Kết hợp |
| 2253 | tính chất nghệ thuật. Sử dụng | tính chất nghệ thuật.

Sử dụng |
| 2271 | ## Bàn luận | Bàn luận |
| 2279 | để nước chả | để nướng chả |
| 2444 | cắm một phần | cấm một phần |
| 2545 | ứng hộ | ủng hộ |
| 2629 | Ấn dụ | Ẩn dụ |
| 2629 | Tương phần | Tương phản |
| 2647 | Cần cần thận với dữ liệu khoa học trọng | Cần cẩn thận với dữ liệu khoa học trong |
| 2727 | lạc trí và mỗi Đông | lạc trí và môi Đông |
| 2731 | hệ trong như thế | hệ trọng như thế |
| 2749 | gây gây như | gây gấy như |
| 2769 | Đoàn [ | Đoạn [ |
| 2769 | <tr><td colspan="2">TSA</td></tr> |  |
| 2771 | Câu 2. [P20 STUDY] | ## Câu 2. [P20 STUDY] |
| 2775 | cứu văn | cứu vãn |
| 2775 | ra khởi | ra khỏi |
| 2783 | nôi gai da như lên con sót | nổi gai da như lên cơn sốt |
| 2852 | Việc Đông úp mặt vào hai bàn tay và<sub>bấm</sub> <sub>chặt</sub> <sub>thái</sub> <sub>dương.</sub> Thái độ bất động của Đông khi nghe<sub>tin</sub> <sub>về</sub> <sub>Lí.</sub> | Việc Đông úp mặt vào hai bàn tay và bấm chặt thái dương.

Thái độ bất động của Đông khi nghe tin về Lí. |
| 2854 | Câu trả lời "tuỳ các đồng chí thôi" của<sub>Đông.</sub> Việc Đông lau mặt vội vàng khi có<sub>khách</sub> <sub>đến.</sub> | Câu trả lời "tuỳ các đồng chí thôi" của Đông.

Việc Đông lau mặt vội vàng khi có khách đến. |
| 2860 | Đề tài gia đình. Đề tài người phụ nữ. | Đề tài gia đình.

Đề tài người phụ nữ. |
| 2862 | Đề tài trách nhiệm của con người với Đề tài hôn nhân. gia đình. | Đề tài trách nhiệm của con người với gia đình.

Đề tài hôn nhân. |
| 2894 | ## Triết lý | Triết lý |
| 2896 | tuỷ các | tuỳ các |
| 2896 | chọn nhằm | chọn nhầm |
| 2900 | truyện ngắn Hệ thống nhân vật. Chi tiết kì ảo. Ngôn ngữ trần thuật. Lời | truyện ngắn?

Hệ thống nhân vật.

Chi tiết kì ảo.

Ngôn ngữ trần thuật.

Lời |
| 2934 | trong vườn” Hoán dụ Ước lệ Điển tích điển cố Ẩn dụ | trong vườn”?

Hoán dụ

Ước lệ

Điển tích điển cố

Ẩn dụ |
| 2938 | trích đoạn sau: Một buổi chiều | trích đoạn sau:

Một buổi chiều |
| 2938 | Bỗng Đông hỏi: – Nhạc | Bỗng Đông hỏi:

– Nhạc |
| 2940 |  Phong cách ngôn ngữ nghệ thuật. Phong cách ngôn ngữ chính luận. Phong cách ngôn ngữ hành chính – Phong cách ngôn ngữ sinh hoạt. công vụ. | 

Phong cách ngôn ngữ nghệ thuật.

Phong cách ngôn ngữ chính luận.

Phong cách ngôn ngữ hành chính – công vụ.

Phong cách ngôn ngữ sinh hoạt. |
| 2946 |  Phong cách ngôn ngữ nghệ thuật. Phong cách ngôn ngữ chính luận. Phong cách ngôn ngữ hành chính – Phong cách ngôn ngữ sinh hoạt. công vụ. | 

Phong cách ngôn ngữ nghệ thuật.

Phong cách ngôn ngữ chính luận.

Phong cách ngôn ngữ hành chính – công vụ.

Phong cách ngôn ngữ sinh hoạt. |
| 2952 | tôi trạng | tội trạng |
| 2956 | tác phẩm: Ngôn ngữ nói. Ngôn ngữ viết. Ngôn ngữ nói ở dạng viết. Ngôn ngữ viết ở dạng nói. | tác phẩm:

Ngôn ngữ nói.

Ngôn ngữ viết.

Ngôn ngữ nói ở dạng viết.

Ngôn ngữ viết ở dạng nói. |
| 2986 | chưa cắt. ít hôm | chưa cắt. Ít hôm |
| 3048 | buộc tôi họa sĩ đã lừa đối | buộc tội họa sĩ đã lừa dối |
| 3141 | phải đúng trước | phải đứng trước |
| 3141 | lắp đi lắp lại | lặp đi lặp lại |
| 3141 | gần rời lại | gần rồi lại |
| 3141 | kể chuyên | kể chuyện |
| 3141 | phần ánh | phản ánh |
| 3151 | điển canh | điếm canh |
| 3171 | Ưa ra cả máu | Ứa ra cả máu |
| 3201 | vẹt đê | vệt đê |
| 3201 | rời bổ | rời bỏ |
| 3201 | bổ trách nhiệm | bỏ trách nhiệm |
| 3204 | Con đại hồng thủy | Cơn đại hồng thủy |
| 3204 | truy đuôi | truy đuổi |
| 3224 | rò vào chân tôi đang buông thống | rờ vào chân tôi đang buông thõng |
| 3224 | Trời oì | Trời ơi |
| 3224 | hết rú lên | hét rú lên |
| 3224 | xuống hồng chụp | xuống hòng chụp |
| 3224 | thẳng con | thằng con |
| 3355 | sáng nay trước mũi | sáng ngay trước mũi |
| 3357 | ## [6] | [6] |
| 3395 | được tăng bởi | được tặng bởi |
| 3395 | có ngân đồng | có ngàn đồng |
| 3421 | đột ngọt khởi giác ngủ | đột ngột khỏi giấc ngủ |
| 3421 | bồi âm thanh | bởi âm thanh |
| 3421 | Tổ ra sợ hải | Tỏ ra sợ hãi |
| 3421 | khinh bǐ | khinh bỉ |
| 3421 | cần thận | cẩn thận |
| 3481 | “mây trắng còn bay” Tiểu thuyết chiến tranh Truyện ngắn Truyện kí Hồi kí | “Mây trắng còn bay”:

Tiểu thuyết chiến tranh

Truyện ngắn

Truyện kí

Hồi kí |
| 3503 | nội khái quát | nội dung khái quát |
| 3509 | mong ngónh | mong ngóng |
| 3515 | hai anh em? Ẩn dụ So sánh Tương phản Nhân hóa | hai anh em?

Ẩn dụ

So sánh

Tương phản

Nhân hóa |
| 3527 | kiện định | kiên định |
| 3527 | yếu dưới | yếu đuối |
| 3527 | Lữ trẻ trong xóm trên chọc | Lũ trẻ trong xóm trêu chọc |
| 3527 | ganh tỉ | ganh tị |
| 3527 | trường thành | trưởng thành |
| 3569 | vạch cửa | vạch cứa |
| 3569 | Vải giọt nước ấm roi | Vài giọt nước ấm rơi |
| 3569 | gầy sợp | gầy sọp |
| 3569 | dang đở | dang dở |
| 3573 | văn bản? Chủ đề gia đình. Chủ đề tình yêu thương trong gia đình. Chủ đề tình cảm gia đình thời hậu chiến. Chủ đề | văn bản?

Chủ đề gia đình.

Chủ đề tình yêu thương trong gia đình.

Chủ đề tình cảm gia đình thời hậu chiến.

Chủ đề |
| 3577 | là gì? Những tổn thương tâm lý trong tuổi thơ. Những kỷ niệm đẹp được ghi nhớ mãi trong lòng. Những trải nghiệm đau buồn trong tuổi thơ của nhân vật. Những | là gì?

Những tổn thương tâm lý trong tuổi thơ.

Những kỷ niệm đẹp được ghi nhớ mãi trong lòng.

Những trải nghiệm đau buồn trong tuổi thơ của nhân vật.

Những |
| 3581 | văn bản trên? Truyện đồng thoại Truyện kí Truyện ngắn Truyện vừa | văn bản trên?

Truyện đồng thoại

Truyện kí

Truyện ngắn

Truyện vừa |
| 3599 | ## Ai biểu xấu?! | Ai biểu xấu?! |
| 3631 | tổ ra | tỏ ra |
| 3631 | chú không | chứ không |
| 3631 | cuộc đồi | cuộc đời |
| 3637 | cắt da cắt thịt So sánh. Hoán dụ. Ẩn dụ. Tượng trưng. | cắt da cắt thịt.

So sánh.

Hoán dụ.

Ẩn dụ.

Tượng trưng. |
| 3673 | đau đón | đau đớn |
| 3673 | muốn khởi thực tại | muốn thoát khỏi thực tại |
| 3673 | vị dám khảo | vị giám khảo |
| 3673 | màu thuẫn | mâu thuẫn |
| 3673 | đến đo | đắn đo |
| 3673 | Sự có gắng che giấy | Sự cố gắng che giấu |
| 3701 | yếu tổ | yếu tố |
| 3730 | công việc? Sự kiên nhẫn Khả năng quản lý nhân sự Tính cầu toàn Sự nghiêm túc | công việc?

Sự kiên nhẫn

Khả năng quản lý nhân sự

Tính cầu toàn

Sự nghiêm túc |
| 3736 | Thành Biển | Thần Biển |
| 3736 | hạn phúc | hạnh phúc |
| 3756 | phần ứng | phản ứng |
| 3756 | sóng gần | sóng gầm |
| 3756 | con giân dữ | cơn giận dữ |
| 3756 | tức giân nhất | tức giận nhất |
| 3756 | <tr><td colspan="2">P20STUDY</td></tr> |  |
| 3760 | Kafka sử dụng? Nghệ thuật nhận thức lại Dạng thức nhại huyền thoại Phương thức truyền kì hoá Phương thức ẩn dụ hoá | Kafka sử dụng?

Nghệ thuật nhận thức lại

Dạng thức nhại huyền thoại

Phương thức truyền kì hoá

Phương thức ẩn dụ hoá |
| 3818 | chính ông ông lại | chính ông lại |
| 3846 | quân áo tả tơi | quần áo tả tơi |
| 3848 | Tâm Hội cười | Tâm Hôi cười |
| 3866 | về bà hai | về bà Hai |
| 3872 | quyền góp | quyên góp |
| 3872 | Tâm Hội ứng hộ | Tâm Hôi ủng hộ |
| 3872 | tỉnh khiết | tinh khiết |
| 3872 | ứng hộ thẩm lặng | ủng hộ thầm lặng |
| 3912 | áo 2 dây dây | áo 2 dây |
| 3918 | bậu của | bậu cửa |
| 3920 | ngơời | người |
| 3922 | cầm xúc | cảm xúc |
| 3922 | Chửi đồng | Chửi đổng |
| 3922 | phần nộ | phẫn nộ |
| 3922 | đồng cầm | đồng cảm |
| 3926 | văn bản trên Văn học hiện thực. Văn học hiện thực phê phán Truyện kí. Truyện ngắn. | văn bản trên:

Văn học hiện thực.

Văn học hiện thực phê phán.

Truyện kí.

Truyện ngắn. |
| 3930 | văn bản Đề tài sự xuống cấp trong đạo đức làm từ thiện. Đề tài làm từ thiện. Đề tài kinh tế. Đề tài | văn bản:

Đề tài sự xuống cấp trong đạo đức làm từ thiện.

Đề tài làm từ thiện.

Đề tài kinh tế.

Đề tài |
| 3934 | xã hội? Thực trạng tình trạng thiên tai lũ lụt của một số tỉnh thành nước ta. Sự phân hóa giàu nghèo ngày càng rõ rệt trong xã hội hiện đại. Thực trạng làm từ thiện theo xu hướng. Thực trạng về | xã hội?

Thực trạng tình trạng thiên tai lũ lụt của một số tỉnh thành nước ta.

Sự phân hóa giàu nghèo ngày càng rõ rệt trong xã hội hiện đại.

Thực trạng làm từ thiện theo xu hướng.

Thực trạng về |
| 3958 | ## - Thế mà | \- Thế mà |
| 3992 | Thắng Gù | Thằng Gù |
| 3992 | thẳng Gù | thằng Gù |
| 3992 | trên chọc | trêu chọc |
| 3992 | khiển | khiến |
| 3992 | cảng cúi | càng cúi |
| 3992 | khởi nhóm | khỏi nhóm |
| 3992 | phần ứng mạnh mê | phản ứng mạnh mẽ |
| 4002 | Gù của lảng | Gù lảng |
| 4032 | chúng mây oì | chúng mày ơi |
| 4032 | thể thế | thế thế |
| 4032 | thẳng Gù | thằng Gù |
| 4032 | lung gù để kiểm tiền | lưng gù để kiếm tiền |
| 4095 | ác thật! | Ác thật! |
| 4095 | sâu khấu | sân khấu |
| 4099 | ## -  | \-  |
| 4107 | ## -  | \-  |
| 4115 | ## -  | \-  |
| 4145 | có chuyên | có chuyện |
| 4145 | được đúng trên | được đứng trên |
| 4145 | ha hå | ha hả |
| 4145 | về lo âu | vẻ lo âu |
| 4145 | nghi ngoi | nghỉ ngơi |
| 4145 | <tr><td colspan="3">P20STUDY</td></tr> |  |
| 4177 | rời khóc | rồi khóc |
| 4177 | Đúng thần người ra như phổng | Đứng thần người ra như phỗng |
| 4189 | Kép Tư Bền? Ẩn dụ. Hoán dụ. Điển tích điển cố. Tương phản. | Kép Tư Bền?

Ẩn dụ.

Hoán dụ.

Điển tích điển cố.

Tương phản. |
| 4207 | những<sub>ổ</sub> | những […] |
| 4211 | thủ pháp nghệ thuật nào? Ẩn dụ. Tương phản. Đối lập. Tăng cấp. | thủ pháp nghệ thuật nào?

Ẩn dụ.

Tương phản.

Đối lập.

Tăng cấp. |
| 4231 | ## [2] Đêm mưa. | [2] Đêm mưa. |
| 4261 | đỡ để | đỡ đẻ |
| 4261 | nguy kích | nguy kịch |
| 4261 | Thắng Cún cần trở | Thằng Cún cản trở |
| 4261 | không hè chẩn chù | không hề chần chừ |
| 4293 | uốt lướt thước | ướt lướt thướt |
| 4293 | về bền | về bến |
| 4293 | ngăn ngặt | ngằn ngặt |
| 4293 | Bày tổ lòng biết on suốt đồi | Bày tỏ lòng biết ơn suốt đời |
| 4355 | Hà Thị B | Hà Thị E |
| 4363 | chứng mình xem! - Trường bản | chứng minh xem! - Trưởng bản |
| 4365 | Đền chiều chẳng vác | Đến chiều chàng vác |
| 4365 | lông nhìm | lông nhím |
| 4369 | ## [3] | [3] |
| 4371 | dùng cảm | dũng cảm |
| 4373 | ## E trả lời: | E trả lời: |
| 4403 | Hua tát | Hua Tát |
| 4405 | tủng thực | trung thực |
| 4423 | Hà Thị B | Hà Thị E |
| 4425 | chân dung B | chân dung E |
| 4435 | sẵn được con lợn lời | săn được con lợn lòi |
| 4435 | khó kiểm nhất | khó kiếm nhất |
| 4435 | bộ lão | bô lão |
| 4479 | con lợn lời | con lợn lòi |
| 4479 | đồ lừ ngày máu | đỏ lừ ngầu máu |
| 4479 | Có về ngoài | Có vẻ ngoài |
| 4567 | hai mươi máy tuổi | hai mươi mấy tuổi |
| 4567 | dữ đội khi biết chỉ sắp đi | dữ dội khi biết chị sắp đi |
| 4567 | ghế tai sát môi thẳng bé | ghé tai sát môi thằng bé |
| 4573 | nó với mình | nó nói với mình |
| 4601 | tàu trở gà trở vịt | tàu chở gà chở vịt |
| 4661 | Để tài | Đề tài |
| 4743 | chống chénh | chống chếnh |
| 4743 | cát bại | cát bụi |
| 4799 | трẻo | trẻo |
| 4799 | hiểm hơi | hiếm hoi |
| 4799 | xóa nhà ranh giới | xóa nhòa ranh giới |
| 4799 | khoảng khắc | khoảnh khắc |
| 4843 | tâm sự vớ mẹ | tâm sự với mẹ |
| 4859 | lỗi sống | lối sống |
| 4867 | Ba đồi | Ba đời |
| 4867 | xung hô | xưng hô |
| 4867 | Con rễ | Con rể |
| 4867 | nép sống | nếp sống |
| 4897 | nhờ và làm phiên | nhờ vả làm phiền |
| 4897 | Tâm sự c Pair mở, cảm thấy thoái mái | Tâm sự cởi mở, cảm thấy thoải mái |
| 5039 | xấu hồ vì bị phát hiện và rời hồi hạn, cảm thấy hồ then | xấu hổ vì bị phát hiện và rồi hối hận, cảm thấy hổ thẹn |
| 5039 | ý tử. | ý tứ. |
| 5039 | Tình tế | Tinh tế |
| 5039 | Vội xã rời đi để không gây phiên | Vội vã rời đi để không gây phiền |
| 5045 | (3 . | (3) . |
| 5051 | tình cò | tình cờ |
| 5051 | đào bói | đào bới |
| 5051 | mẫu khoai | mẩu khoai |
| 5051 | hối hạn | hối hận |
| 5115 | ạng Tú | Ông Tú |
| 5117 | ạng Tú | Ông Tú |
| 5131 | ạng bà | Ông bà |
| 5133 | ạng bà | Ông bà |
| 5135 | Gặp mắt sáng | Cặp mắt sáng |
| 5161 | Đúng |  |
| 5163 | <tr><td colspan="3">TSA</td></tr> | <tr><td></td><td>Đúng</td><td>Sai</td></tr> |
| 5163 | guom | gươm |
| 5163 | giảng | giàng |
| 5163 | lưới | lưỡi |
| 5163 | khởi thiên tai | khỏi thiên tai |
| 5199 | kể thù | kẻ thù |
| 5199 | kê thù | kẻ thù |
| 5199 | to mò | tò mò |
| 5199 | câu chuyên | câu chuyện |
| 5245 | những vẫn | nhưng vẫn |
| 5259 | cái cât | cái cây |
| 5269 | Để tài | Đề tài |
| 5277 | chủ Nam | chú Năm |
| 5279 | hàng hát | hăng hái |
| 5279 | đua anh | đưa anh |
| 5279 | kĩ niệm thân | kỉ niệm thân |
| 5281 | xuống lên | xuồng lên |
| 5283 | đêm mua ngoài | đêm mưa ngoài |
| 5285 | tiếng môi và tiếng trống | tiếng mõ và tiếng trống |
| 5285 | hỏi Đồng khởi | hồi Đồng khởi |
| 5331 | cầm giác choàng tỉnh đột ngọt | cảm giác choàng tỉnh đột ngột |
| 5331 | an ůi, che chờ | an ủi, che chở |
| 5331 | cái cầm nhọn hoát ra đặc trung | cái cằm nhọn hoắt ra đặc trưng |
| 5391 | ménh mông | mênh mông |
| 5391 | hiện rời tan | hiện rồi tan |
| 5391 | ma quy | ma quỷ |
| 5391 | đau đón | đau đớn |
| 5395 | trên: Đề tài kháng chiến. Đề tài niềm tin chiến đấu. Đề tài khát vọng cống hiến cho đất Đề tài người chiến sĩ cách mạng. nước. | trên:

Đề tài kháng chiến.

Đề tài niềm tin chiến đấu.

Đề tài khát vọng cống hiến cho đất nước.

Đề tài người chiến sĩ cách mạng. |
| 5411 | tiếng mõi | tiếng mõ |
| 5411 | hỏi Đồng khởi | hồi Đồng khởi |
| 5413 | Tương phản. <sub>So</sub> <sub>sánh.</sub> Điệp từ. Đối. | Tương phản.

So sánh.

Điệp từ.

Đối. |
| 5421 | ## [2] | [2] |
| 5425 | ## Con cáo | Con cáo |
| 5431 | bên tả , | bên tả, |
| 5438 | ## [6] | [6] |
| 5442 | Nguyễn Dữ, chuyện | Nguyễn Dữ, Chuyện |
| 5490 | ứng hộ | ủng hộ |
| 5490 | phần tác dụng | phản tác dụng |
| 5490 | vô nhân | võ nhân |
| 5490 | cáo chữ không | cáo chứ không |
| 5526 | văn bản trên? Truyện thần thoại Tiểu thuyết lịch sử Truyện truyền kì Truyện ngắn hiện đại | văn bản trên?

Truyện thần thoại

Tiểu thuyết lịch sử

Truyện truyền kì

Truyện ngắn hiện đại |
| 5554 | khóc;nhưng | khóc; nhưng |
| 5554 | người công còn gì chống đở | người không còn gì chống đỡ |
| 5560 | khỏi cho ngọn lửa | khơi cho ngọn lửa |
| 5566 | sự ngáo trở sẩy ra | sự ngáng trở xảy ra |
| 5566 | nững sự | những sự |
| 5566 | giắt nàng | dắt nàng |
| 5566 | rồn đến chàng như một lớp sống vào bờ | dồn đến chàng như một lớp sóng vào bờ |
| 5566 | Nhửng kỷ niệm | Những kỷ niệm |
| 5566 | rõ rệ. | rõ rệt. |
| 5570 | ## Mai khẽ | Mai khẽ |
| 5574 | khỏ biết | khổ biết |
| 5576 | đến lần với | đến lẫn với |
| 5576 | tàn ác với chàng | tàn ác với nàng |
| 5580 | Nàng giờ tay | Nàng giơ tay |
| 5580 | yên.Vân | yên. Vân |
| 5582 | nổi tủi nhục | nỗi tủi nhục |
| 5582 | Khi Mai đứng nói | Khi Mai ngừng nói |
| 5586 | trên thân hồng | trên than hồng |
| 5618 | hối hạn | hối hận |
| 5618 | cay đẳng | cay đắng |
| 5664 | lò suời | lò sưởi |
| 5706 | Hắn xẻn từ | Hắn xén từ |
| 5718 | 2016 Câu 1. [P20 STUDY] | 2016

## Câu 1. [P20 STUDY] |
| 5754 | sự một môi và muốn giải tòa con giận | sự mệt mỏi và muốn giải tỏa cơn giận |
| 5822 | Đề tài sự thấu <sub>hiểu</sub> Đề tài tình yêu Đề tài gia đình Đề tài hậu chiến | Đề tài sự thấu hiểu

Đề tài tình yêu

Đề tài gia đình

Đề tài hậu chiến |
| 5836 | trứng gà bóc tóc | trứng gà bóc, tóc |
| 5840 | đầy ấp | đầy ắp |
| 5856 | com dim | con dim |
| 5870 | cuối gầm mặt | cúi gằm mặt |
| 5892 | phục nó Bởi | phục nó. Bởi |
| 5900 | Đúng Sai |  |
| 5902 | <td colspan="3">P20STUDY</td> | <td></td><td>Đúng</td><td>Sai</td> |
| 5902 | sẵn hổ | săn hổ |
| 5910 | như mùa hộ mệnh | như bùa hộ mệnh |
| 5918 | khiển | khiến |
| 5918 | sẵn | săn |
| 5918 | hồ | hổ |
| 5918 | tham ra chuyển | tham gia chuyến |
| 5918 | sắp áp tới | sắp ập tới |
| 5925 | sẵn | săn |
| 5925 | hồ | hổ |
| 5925 | trái tìm | trái tim |
| 5997 | hạ nhục cá mình | hạ nhục cả mình |
| 6009 | các các | các cô |
| 6025 | bồng hông | bông hồng |
| 6061 | câu coi | cậu coi |
| 6061 | về ngoài | vẻ ngoài |
| 6061 | lừa đối | lừa dối |
| 6061 | của câu đã lừa dối câu | của cậu đã lừa dối cậu |
| 6061 | hành tỉnh | hành tinh |
| 6077 | oàng từ bé | oàng tử bé |
| 6077 | rời hoàng | rồi hoàng |
| 6077 | câu phụ nhận | cậu phủ nhận |
| 6077 | của câu khi câu đã rời khởi hành tỉnh | của cậu khi cậu đã rời khỏi hành tinh |
| 6093 | về bề ngoài | vẻ bề ngoài |
| 6103 | và và | và |
| 6153 | trống rỗng vào đau | trống rỗng và đau |
| 6171 | ở bên kia sông | Ở bên kia sông |
| 6213 | bồng vụt | bỗng vụt |
| 6269 | cổ tình bổ mặc | cố tình bỏ mặc |
| 6269 | cũng cố | củng cố |
| 6269 | bị dưới nước | bị đuối nước |
| 6269 | Câu truyền được kể theo trực thời gian | Câu chuyện được kể theo trục thời gian |
| 6269 | bến các để tìm gặp chỉ Thắm | bến Cốc để tìm gặp chị Thắm |
| 6299 | khoảng khắc đẹp dễ | khoảnh khắc đẹp đẽ |
| 6299 | phai mò | phai mờ |
| 6299 | Một măng nhỏ | Một mảng nhỏ |
| 6299 | Lói viết | Lối viết |
| 6299 | cuộc đồi | cuộc đời |
| 6305 | hối hạn | hối hận |
| 6305 | chỉ Thắm | chị Thắm |
| 6305 | sông oì | sông ơi |
| 6311 | Tôi làm(2) | Tôi làm (2) |
| 6395 | đăng trí | đãng trí |
| 6395 | Cải oì | Cải ơi |
| 6471 | Nguyễn Phúc ánh | Nguyễn Phúc Ánh |
| 6471 | châu âu | châu Âu |
| 6475 | châu âu | châu Âu |
| 6475 | mặt xám lại Chúng | mặt xám lại. Chúng |
| 6475 | Buổi tôí | Buổi tối |
| 6483 | Phăng an xong | Phăng ăn xong |
| 6485 | nhũng cô gắng | những cố gắng |
| 6487 | những môí bất hòa | những mối bất hòa |
| 6491 | Phăng vể kinh | Phăng về kinh |
| 6495 | châu âu | châu Âu |
| 6495 | vua Gia long | vua Gia Long |
| 6541 | Phẳng | Phăng |
| 6541 | chuyển đi | chuyến đi |
| 6547 | tin cây | tin cậy |
| 6591 | Câu chuyên | Câu chuyện |
| 6591 | ứng hộ | ủng hộ |
| 6591 | triệu Nguyễn là một triệu đại | triều Nguyễn là một triều đại |
| 6624 | người đọc các thấy rõ những tac phẩm | người đọc càng thấy rõ những tác phẩm |
| 6636 | thấu hiếu | thấu hiểu |
| 6664 | Do Áp lực | Do áp lực |
| 6668 | văn học tiền thời | văn học tiền chiến |
| 6680 | giả đối | giả dối |
| 6680 | nhận vật | nhân vật |
| 6680 | tránh khởi | tránh khỏi |
| 6686 | Don quichottee | Don Quichotte |
| 6694 | gã gần dở | gã gàn dở |
| 6694 | Lói viết | Lối viết |
| 6760 | giỡ gạch | dỡ gạch |
| 6760 | chị Duyên nói | chị Duyện nói |
| 6794 | con mưa | cơn mưa |
| 6794 | kiểm ăn | kiếm ăn |
| 6794 | tỉnh lặng | tĩnh lặng |
| 6794 | dua nhau | đua nhau |
| 6824 | kiểm sống | kiếm sống |
| 6824 | Duyên chỉ là | Duyện chỉ là |
| 6824 | tượng trung | tượng trưng |
| 6905 | Frank Kafka | Franz Kafka |
| 6943 | bọ chết | bọ chét |
| 6943 | cứi xuống | cúi xuống |
| 6943 | được dụng lên | được dựng lên |
| 6955 | Tuyết vọng và ngày ngô | Tuyệt vọng và ngây ngô |
| 7016 | việc làm.Mất | việc làm. Mất |
| 7032 | lập lại | lặp lại |
| 7051 | giải các quyết khó khăn | giải quyết các khó khăn |
| 7079 | mạnh mê | mạnh mẽ |
| 7079 | tổ ra | tỏ ra |
| 7079 | Grete đàn trở nên | Grete dần trở nên |
| 7137 | tổ ra | tỏ ra |
| 7141 | Câu 10. [P20 STUDY] | ## Câu 10. [P20 STUDY] |
| 7216 | bậc tấm | bậc tám |
| 7216 | kiểm sống | kiếm sống |
| 7216 | tầu thuốc với giá một rút | tẩu thuốc với giá một rúp |
| 7216 | <tr><td colspan="3">○○○——○○○</td></tr> |  |
| 7218 | phổng đá | phỗng đá |
| 7218 | Cầm dài | Cằm dài |
| 7408 | sung tức | sung túc |
| 7408 | buộc tôi | buộc tội |
| 7408 | va chậm | va chạm |
| 7452 | từ bổ | từ bỏ |
| 7452 | buộc tôi | buộc tội |
| 7474 | ## CHỦ ĐỀ 42 NẾU | ## CHỦ ĐỀ 42

## NẾU |
| 7522 | lòng Faraday | lồng Faraday |
| 7522 | khởi sét | khỏi sét |
| 7576 | con bão | cơn bão |
| 7576 | bằng dăm | bằng dặm |
| 7576 | boi dưới | bơi dưới |
| 7576 | thấy chóp trước khi nghe sám | thấy chớp trước khi nghe sấm |
| 7592 | Tình hướng | Tình huống |
| 7642 | gập ba | gấp ba |
| 7735 | ## PHƯƠNG PHÁP CHỮA BỆNH MỚI BẰNG CỘNG CHỦ ĐỀ 44 HƯỞNG ÂM THANH | ## CHỦ ĐỀ 44

## PHƯƠNG PHÁP CHỮA BỆNH MỚI BẰNG CỘNG HƯỞNG ÂM THANH |
| 7929 | thiểu ánh nắng | thiếu ánh nắng |
| 7961 | quản thể | quần thể |
| 7981 | # KỸ NĂNG MỀM | ## CHỦ ĐỀ 46

# KỸ NĂNG MỀM |
| 7983 | CHỦ ĐỀ 46 |  |
| 7987 | kSỹ năng | kỹ năng |
| 8046 | đời hồi | đòi hỏi |
| 8052 | dàitrong | dài trong |
| 8102 | khan hiểm | khan hiếm |
| 8167 | %các | % các |
| 8173 | rào cần | rào cản |
| 8207 | (2 vào | (2) vào |
| 8221 | ## Ảnh hưởng | Ảnh hưởng |
| 8237 | # E-LEARNING | ## CHỦ ĐỀ 48

# E-LEARNING |
| 8239 | CHỦ ĐỀ 48 |  |
| 8275 | mạnh mê | mạnh mẽ |
| 8305 | Nền tầng | Nền tảng |
| 8311 | đảm mây | đám mây |
| 8333 | tương tácvà | tương tác và |
| 8367 | TRUYỀN THỐNG HÀNH TRÌNH | TRUYỀN THỐNG - HÀNH TRÌNH |
| 8395 | ngũ than | ngũ thân |
| 8405 | díp | dịp |
| 8405 | khiển | khiến |
| 8405 | khởi đời sống | khỏi đời sống |
| 8409 | đoạn văn sau: Đến đầu | đoạn văn sau:

Đến đầu |
| 8413 | của áo dài có | của áo dài có mối liên hệ như thế nào? (chọn nhiều đáp án đúng) |
| 8415 | mối liên hệ như thế nào? (chọn nhiều đáp án đúng) |  |
| 8437 | díp | dịp |
| 8696 | e đề | e dè |
| 8720 | phần đối | phản đối |
| 8728 | nuôi cây | nuôi cấy |
| 8808 | nghi trưa | nghỉ trưa |
| 8834 | ứng hộ | ủng hộ |
| 8886 | thành " công nhân | thành "công nhân |
| 8928 | lưu trữ chức không | lưu trữ chứ không |
| 9040 | đoạn văn sau: Hygge | đoạn văn sau:

Hygge |
| 9046 | rực rõ và màu sắc sắc sõ là đặc trung | rực rỡ và màu sắc sặc sỡ là đặc trưng |
| 9140 | Nam cực).Thật | Nam cực). Thật |
| 9140 | đe dọa.Điều | đe dọa. Điều |
| 9166 | bề lưu trữ | bể lưu trữ |
| 9166 | khí quyền | khí quyển |
| 9166 | Rừng nhiệt đối đúng thứ 5 | Rừng nhiệt đới đứng thứ 5 |
| 9166 | Vùng đất bằng tuyệt vĩnh cứu | Vùng đất băng tuyết vĩnh cửu |
| 9204 | cổ biển | cỏ biển |
| 9204 | Cổ biển | Cỏ biển |
| 9204 | chấp nơi | khắp nơi |
| 9220 | bàn cò | bàn cờ |
| 9342 | thới quen | thói quen |
| 9342 | Nước đúng đầu | Nước đứng đầu |
| 9385 | nghiêm khắt | nghiêm khắc |
| 9515 | (8) ,cuối | (8) , cuối |
| 9519 | nội dun bài | nội dung bài |
| 9547 | kinh $\mathbf { t } \acute { \hat { \mathbf { e } } } ,$ | kinh tế, |
| 9569 | nước kiểm | nước kiềm |
| 9609 | mất dàn | mất dần |
| 9609 | loại bổ | loại bỏ |
| 9609 | khối phục | khôi phục |
| 9704 | hư hổng | hư hỏng |
| 9704 | bị dùng hoạt động | bị dừng hoạt động |
| 9704 | <tr><td colspan="3">P20 |  |
| 9705 | STUDY</td></tr> |  |
| 9739 | Giáo su | Giáo sư |
| 9739 | Fãhraeus | Fåhraeus |
| 9791 | khác du lịch | khác là du lịch |
| 9817 | nghi dưỡng | nghỉ dưỡng |
| 9843 | nghị dưỡng | nghỉ dưỡng |
| 9849 | nghi dưỡng | nghỉ dưỡng |
| 9849 | hướng lợi | hưởng lợi |
| 9899 | tiktok…để | tiktok… để |
| 9907 | anh Cường thể bán | anh Cường có thể bán |
| 9971 | ùn ú | ùn ứ |
| 9971 | đúng đến | đúng đắn |
| 10026 | # DIGITAL DETOX | ## CHỦ ĐỀ 62

# DIGITAL DETOX |
| 10028 | CHỦ ĐỀ 62 |  |
| 10072 | thoát khởi | thoát khỏi |
| 10116 | tỉnh thần | tinh thần |
| 10252 | ký nguyên | kỷ nguyên |
| 10252 | gọi ý | gợi ý |
| 10252 | kỳ nguyên | kỷ nguyên |
| 10252 | không lồ | khổng lồ |
| 10356 | Tơ nhận | Tơ nhện |
| 10356 | tơ nhận | tơ nhện |
| 10450 | va chậm | va chạm |
| 10450 | Va chậm | Va chạm |
| 10450 | dây chuyển | dây chuyền |
| 10474 | va chậm | va chạm |
| 10474 | Va chậm | Va chạm |
| 10474 | dây chuyển | dây chuyền |
| 10502 | gáp đôi | gấp đôi |
| 10674 | sản xuấ nông | sản xuất nông |
| 10700 | tỉnh thần | tinh thần |
| 10716 | Tôi ưu hóa | Tối ưu hóa |
| 10716 | màu thuẫn | mâu thuẫn |
| 10746 | roi vào | rơi vào |
| 10746 | đời hồi | đòi hỏi |
| 10778 | Tình thần | Tinh thần |
| 10778 | mạnh mê | mạnh mẽ |
| 10778 | Đề cao về đẹp | Đề cao vẻ đẹp |
| 10834 | bãy | bẫy |
| 10834 | Bãy | Bẫy |
| 10840 | Ni-tơ Kali Phốt-pho Magie | Ni-tơ

Kali

Phốt-pho

Magie |
| 10888 | phần ứng | phản ứng |
| 10888 | thù dịch | thù địch |
| 10904 | TỪHOA | TỪ HOA |
| 11068 | đẹp dễ | đẹp đẽ |
| 11151 | thẩm họa | thảm họa |
| 11179 | huyện thoại | huyền thoại |
| 11243 | người dân? Xã hội số. Chính phủ số. Kinh tế số. Cả ba | người dân?

Xã hội số.

Chính phủ số.

Kinh tế số.

Cả ba |
| 11353 | Mary Picford | Mary Pickford |
| 11355 | phần biệt | phân biệt |
| 11361 | một hương mới | một hướng mới |
| 11365 | nghỉ ngoi | nghỉ ngơi |
| 11371 | Bà phần chia | Bà phân chia |
| 11379 | sang hương khác | sang hướng khác |
| 11423 | roi vào tình cảnh bề tắc | rơi vào tình cảnh bế tắc |
| 11423 | nóng hồi | nóng hổi |
| 11423 | ứng hộ | ủng hộ |
| 11423 | kiện trì | kiên trì |
| 11491 | Sắ Dựa | Dựa |
| 11507 | Đ đã thấy | Đi đã thấy |
| 11509 | Bà bào: | Bà bảo: |
| 11517 | trong đoạn trích? Không có người thân chăm sóc Phải làm việc vất vả để kiếm sống Sức khỏe yếu và không thể tiếp tục công Tất cả các đáp án trên việc | trong đoạn trích?

Không có người thân chăm sóc

Phải làm việc vất vả để kiếm sống

Sức khỏe yếu và không thể tiếp tục công việc

Tất cả các đáp án trên |
| 11523 | cho con trai." Sai Đúng | cho con trai."

Sai

Đúng |
| 11527 | vì lý do gì? Bà làm việc chậm chạp và vụng về Bà thường xuyên bị ốm Bà đòi tiền công cao Bà không biết | vì lý do gì?

Bà làm việc chậm chạp và vụng về

Bà thường xuyên bị ốm

Bà đòi tiền công cao

Bà không biết |
| 11545 | bị đổi chủ? Vì bà lão làm việc không hiệu quả Vì bà lão quá lẩm cẩm, chậm chạp Vì bà lão yêu cầu mức lương cao Vì bà lão | bị đổi chủ?

Vì bà lão làm việc không hiệu quả

Vì bà lão quá lẩm cẩm, chậm chạp

Vì bà lão yêu cầu mức lương cao

Vì bà lão |
| 11551 | cần thận | cẩn thận |
| 11551 | than phiên | than phiền |
| 11551 | bé trẻ | bế trẻ |
| 11636 | từ Trung Quốc? Điện tử Ô tô Máy tính Nông nghiệp | từ Trung Quốc?

Điện tử

Ô tô

Máy tính

Nông nghiệp |
| 11640 | " Giả sử | "Giả sử |
| 11640 | nhiều nhất" Sai Đúng | nhiều nhất"

Sai

Đúng |
| 11644 | Thái Lan? Giá dầu toàn cầu tăng mạnh Biến động kinh tế toàn cầu và căng thẳng địa chính trị Đồng baht mạnh lên nhanh hơn dự kiến Ngân hàng | Thái Lan?

Giá dầu toàn cầu tăng mạnh

Biến động kinh tế toàn cầu và căng thẳng địa chính trị

Đồng baht mạnh lên nhanh hơn dự kiến

Ngân hàng |
| 11648 | năm 2025? Chính sách | năm 2025?

Chính sách |
| 11702 | năm 2025? Nhóm thu nhập cao Nhóm thu nhập trung bình Nhóm thu nhập thấp Nhóm làm việc | năm 2025?

Nhóm thu nhập cao

Nhóm thu nhập trung bình

Nhóm thu nhập thấp

Nhóm làm việc |
| 11742 | của của chúng ta | của chúng ta |
| 11789 | hơn (3) Câu 4. [P20 STUDY] | hơn (3)

## Câu 4. [P20 STUDY] |
| 11791 | xe ô tô? Động cơ Bánh xe Ghế ngồi Thân xe | xe ô tô?

Động cơ

Bánh xe

Ghế ngồi

Thân xe |
| 11797 | vòng thom | vòng thơm |
| 11821 | năm 1952? Thời gian tiến hành thí nghiệm. Thành phần các chất tham gia thí nghiệm. Số lần thực hiện thí nghiệm. Thiếu | năm 1952?

Thời gian tiến hành thí nghiệm.

Thành phần các chất tham gia thí nghiệm.

Số lần thực hiện thí nghiệm.

Thiếu |
| 11825 | sau đây? Khổ [5] Khổ [6] Khổ [7] Khổ [8] | sau đây?

Khổ [5]

Khổ [6]

Khổ [7]

Khổ [8] |
| 11829 | ngạc nhiên? Vì sulfur không tồn tại trên Trái Đất. Vì amino acid chứa sulfur quá phức tạp. Vì sulfur là phổ biến trên Trái Đất thời ban đầu. Vì | ngạc nhiên?

Vì sulfur không tồn tại trên Trái Đất.

Vì amino acid chứa sulfur quá phức tạp.

Vì sulfur là phổ biến trên Trái Đất thời ban đầu.

Vì |
| 11833 | là gì? Sử dụng nhiều thí nghiệm mô phỏng bằng các máy móc hiện đại. Phân tích nhiều hóa thạch và so sánh các hóa thạch. Phối hợp với các nghiên cứu về sự sống trong vũ trụ. Tiếp cận | là gì?

Sử dụng nhiều thí nghiệm mô phỏng bằng các máy móc hiện đại.

Phân tích nhiều hóa thạch và so sánh các hóa thạch.

Phối hợp với các nghiên cứu về sự sống trong vũ trụ.

Tiếp cận |
| 11837 | bôông bêênh | bông bênh |
| 11843 | ## Tùng tùng | Tùng tùng |
| 11847 | man máC. | man mác. |
| 11849 | ## - Đã ra | \- Đã ra |
| 11871 | đượC. | được. |
| 11879 | là gì? Miêu tả các môn võ cổ truyền Miêu tả một hội thi đấu võ cổ truyền Giới thiệu về các võ sĩ nổi tiếng Kể | là gì?

Miêu tả các môn võ cổ truyền

Miêu tả một hội thi đấu võ cổ truyền

Giới thiệu về các võ sĩ nổi tiếng

Kể |
| 11899 | là gì? Có nhiều đoàn võ với các sở trường khác nhau. Các võ sĩ chỉ đấu kiếm mà không đầu quyền. Sự chuẩn bị chu đáo cho buổi biểu diễn võ. Thể hiện | là gì?

Có nhiều đoàn võ với các sở trường khác nhau.

Các võ sĩ chỉ đấu kiếm mà không đấu quyền.

Sự chuẩn bị chu đáo cho buổi biểu diễn võ.

Thể hiện |
| 11903 | túng thiếu? Người khố đơn. Ông “loa”. Võ sĩ. Các cụ già. | túng thiếu?

Người khố đơn.

Ông “loa”.

Võ sĩ.

Các cụ già. |
| 11907 | là gì? Võ sĩ biểu diễn. Người dẫn chương trình. Người cầm trịch và gõ trống. Người | là gì?

Võ sĩ biểu diễn.

Người dẫn chương trình.

Người cầm trịch và gõ trống.

Người |
| 11911 | giải thưởng? Khổ [5] Khổ [6] Khổ [7] Khổ [8] | giải thưởng?

Khổ [5]

Khổ [6]

Khổ [7]

Khổ [8] |
| 11915 | không được sử dụng? Nhân hóa. Nói quá. Cảm thán. So sánh. | không được sử dụng?

Nhân hóa.

Nói quá.

Cảm thán.

So sánh. |
| 11919 | ở khổ [10] Khổ [1] và [4] Khổ [2] và [3] Khổ [5] và [7] Khổ [8] và [9] | ở khổ [10]?

Khổ [1] và [4]

Khổ [2] và [3]

Khổ [5] và [7]

Khổ [8] và [9] |
| 11923 | lò lạ? Vì nó thể lệ quá phức tạp. Vì có thể gây thương tích nặng. Vì ít võ sĩ có thể thi đấu. Vì | lò lạ?

Vì nó thể lệ quá phức tạp.

Vì có thể gây thương tích nặng.

Vì ít võ sĩ có thể thi đấu.

Vì |
| 11929 | là mươi tám | là mười tám |
| 11929 | Đoàn vô bên Phú Gia có mặt đồ gay và tròng mất cũng đồ lịm | Đoàn võ bên Phú Gia có mặt đỏ gay và tròng mắt cũng đỏ lịm |
| 11929 | độ lón | độ lớn |
| 11929 | biểu diễn vỡ | biểu diễn võ |
| 11943 | lao động lao động | lao động |
| 11951 | ”Chính sách | “Chính sách |
| 12003 | rời sau đó | rồi sau đó |
| 12003 | Đề Việt Nam | Để Việt Nam |
| 12003 | khiển | khiến |
| 12035 | đoạn văn “Bài báo | đoạn văn:

“Bài báo |
| 12069 | bên cạnh- nó | bên cạnh. Nó |
| 12073 | ngờ vực- Hắn | ngờ vực. Hắn |
| 12073 | mồ hồi mồ kê | mồ hôi mồ kê |
| 12075 | Phụt Viên sỏi bay vút lên ngọn cây, Tên | Phụt! Viên sỏi bay vút lên ngọn cây. Tên |
| 12079 | bậy quái Mải | bậy quá! Mải |
| 12081 | giữa đường- Khi | giữa đường. Khi |
| 12085 | sững lại? buột | sững lại, buột |
| 12089 | Phải. đúng là | Phải, đúng là |
| 12093 | \- đứng im Mi mà | \- Đứng im! Mi mà |
| 12095 | đi động | di động |
| 12095 | theo mình. để đánh lừa | theo mình. Để đánh lừa |
| 12097 | bắt rồi Chạy | bắt rồi! Chạy |
| 12099 | giò heo- Nguyễn | giò heo. Nguyễn |
| 12101 | tau. đứa nào | tau. Đứa nào |
| 12103 | phía cầu Tụi | phía cầu. Tụi |
| 12103 | kêu lên- “Hai | kêu lên: “Hai |
| 12107 | hai chần | hai chân |
| 12107 | chung quanh, \_ một vài người cúi lén nhặt-Nguyễn | chung quanh, một vài người cúi lén nhặt. Nguyễn |
| 12109 | ## - Gớm | \- Gớm |
| 12117 | con cu xanh? Đang uống cà phê. Đang rình bắt chim. Đang trò chuyện với mật thám. Đang | con cu xanh?

Đang uống cà phê.

Đang rình bắt chim.

Đang trò chuyện với mật thám.

Đang |
| 12135 | Nghiêng qua nghiêng lại rất nhanh. Vội vã, hấp tấp. Không giữ được thăng bằng. Choáng | Nghiêng qua nghiêng lại rất nhanh.

Vội vã, hấp tấp.

Không giữ được thăng bằng.

Choáng |
| 12141 | ngò ngò | ngờ ngợ |
| 12141 | sẵn chim | săn chim |
| 12141 | cảnh giác nửa | cảnh giác nữa |
| 12141 | Lượng | Lượm |
| 12141 | tổng quản lý | tống quản lý |
| 12141 | căm thấy | cảm thấy |
| 12141 | hoảng sọ mà bình cảnh báo cho đồng đội chạy toát | hoảng sợ mà bình tĩnh cảnh báo cho đồng đội chạy thoát |
| 12145 | bị bắt? Khổ [9]. Khổ [11]. Khổ [14]. Đáp án khác. | bị bắt?

Khổ [9].

Khổ [11].

Khổ [14].

Đáp án khác. |
| 12157 | cầu Bao Vinh” Đúng Sai | cầu Bao Vinh”

Đúng

Sai |
| 12161 | lúc bấy giờ? Sự sợ hãi và thờ ơ. Sự đồng cảm. Sự phản kháng âm thầm. Sự bất lực. | lúc bấy giờ?

Sự sợ hãi và thờ ơ.

Sự đồng cảm.

Sự phản kháng âm thầm.

Sự bất lực. |
| 12165 | kẹo gừng? Vì muốn trừng phạt chúng. Vì muốn tìm thêm truyền đơn. Vì cho rằng Tư-dát nằm trong số đó Vì | kẹo gừng?

Vì muốn trừng phạt chúng.

Vì muốn tìm thêm truyền đơn.

Vì cho rằng Tư-dát nằm trong số đó.

Vì |
| 12171 | Lượng | Lượm |
| 12365 | tâm trạng nhân vật? Tương phản. So sánh. Ẩn dụ. Đối thoại. | tâm trạng nhân vật?

Tương phản.

So sánh.

Ẩn dụ.

Đối thoại. |
| 12395 | những không thể phần kháng | nhưng không thể phản kháng |
| 12395 | <tr><td colspan="3">TSA</td></tr> |  |
| 12395 | thất cổ mà chết đi cho rời | thắt cổ mà chết đi cho rồi |
| 12395 | khởi đau khổ | khỏi đau khổ |
| 12395 | bắt cháy" để độ các con | bắt chấy" để dỗ các con |
| 12395 | ngày thơ | ngây thơ |
| 12395 | bắt công trong xã hội đầy con người | bất công trong xã hội đẩy con người |
| 12409 | dính lung | dính lưng |
| 12409 | lỗm ngồm | lổm ngổm |
| 12417 | (3) ,, | (3) .” |
| 12423 | người yếu thế.” Đúng Sai | người yếu thế.”

Đúng

Sai |
| 12501 | Độ PH | Độ pH |
| 12509 | thẩm vào | thấm vào |
| 12509 | nước mưa đo đặc điểm | nước mưa do đặc điểm |
| 12531 | vai trò lón | vai trò lớn |
| 12607 | mỗ năm | mỗi năm |
| 12709 | nghiệm trọng | nghiêm trọng |
| 12721 | tảo đệ hạn chế | tảo để hạn chế |
| 12771 | chỉ ý nghĩa ca vic là con ngưòi trong th gii s hóa và m ra nhng kh năng mà các th h trưc ch | chỉ có thể mơ ước. |
| 12773 | có thể mơ ước. |  |
| 12765 | Người Lương Hà | Người Lưỡng Hà |
| 12765 | mục nước song | mực nước sông |
| 12765 | hàng thập ký | hàng thập kỷ |
| 12795 | nhất &#x27;like | nhấn &#x27;like |
| 12795 | lắp đầy | lấp đầy |
| 12853 | Lương Hà | Lưỡng Hà |
| 12867 | ## ĐOẠN TRÍCH BÀI LUẬN CHỖ ĐỨNG CỦA CHỦ ĐỀ 84 CHÚNG TA TRONG VŨ TRỤ | ## CHỦ ĐỀ 84

## ĐOẠN TRÍCH BÀI LUẬN CHỖ ĐỨNG CỦA CHÚNG TA TRONG VŨ TRỤ |
| 12917 | thẳng đúng | thẳng đứng |
| 12917 | bóng đồ | bóng đổ |
| 12955 | 100 triệu đặm | 100 triệu dặm |
| 12955 | mục sồi | mực sồi |
| 12985 | Trái đât | Trái đất |
| 13092 | dùng để chỉ: Cái đầu của con mèo Mâm cơm của gia đình Cái bát đựng cơm Nồi cơm nguội | dùng để chỉ:

Cái đầu của con mèo

Mâm cơm của gia đình

Cái bát đựng cơm

Nồi cơm nguội |
| 13096 | rõ nhất? Tham ăn và ích kỷ Có ý thức và biết điều Kiêu căng và khó tính Thật thà và chân chất | rõ nhất?

Tham ăn và ích kỷ

Có ý thức và biết điều

Kiêu căng và khó tính

Thật thà và chân chất |
| 13102 | Hai anh chỉ đều rất đối | Hai anh chị đều rất đói |
| 13102 | anh đuôi con mèo làm thẳng cu thức giác | anh đuổi con mèo làm thằng cu thức giấc |
| 13102 | anh cu đuôi con mèo | anh cu đuổi con mèo |
| 13102 | không tất được | không tát được |
| 13102 | chỉ cu | chị cu |
| 13102 | chỉ đã | chị đã |
| 13110 | mâm com | mâm cơm |
| 13110 | lừa thẳng cu | lừa thằng cu |
| 13136 | giàu có dư giả nồng nực bức bối | giàu có dư giả

nồng nực bức bối |
| 13138 | kẻ phá hoại chính niềm vui giản dị | kẻ phá hoại chính

niềm vui giản dị |
| 13142 | cãi vã hiện thực đen tối | cãi vã

hiện thực đen tối |
| 13148 | nghèo khổ cùng cực nguyên nhân tình cờ | nghèo khổ cùng cực

nguyên nhân tình cờ |
| 13189 | # TẬP TÍNH VẬT NUÔI | ## CHỦ ĐỀ 86

# TẬP TÍNH VẬT NUÔI |
| 13191 | ## CHỦ ĐỀ 86 |  |
| 13193 | thoải má cho | thoải mái cho |
| 13237 | hoang đã | hoang dã |
| 13237 | Săn môi | Săn mồi |
| 13237 | không tổ lòng biết on | không tỏ lòng biết ơn |
| 13269 | ngoại lại | ngoái lại |
| 13269 | vô on | vô ơn |
| 13269 | thú cung | thú cưng |
| 13269 | ngời xuống | ngồi xuống |
| 13323 | bước qua tính cách thân thiện | bước qua

tính cách thân thiện |
| 13331 | ## " TRẬN CHIẾN CUỐI CÙNG TẠI THUNG LŨNG CHỦ ĐỀ 87 DEVIL'S CANYON" | ## CHỦ ĐỀ 87

## "TRẬN CHIẾN CUỐI CÙNG TẠI THUNG LŨNG DEVIL'S CANYON" |
| 13436 | khối từ ống khói | khói từ ống khói |
| 13436 | tránh khôi | tránh khỏi |
| 13436 | nứt nề | nứt nẻ |
| 13436 | dấu tranh | đấu tranh |
| 13454 | " Trận Chiến | "Trận Chiến |
| 13486 | hành tỉnh | hành tinh |
| 13486 | sử mệnh | sứ mệnh |
| 13492 | hành tỉnh | hành tinh |
| 13492 | Tìm kiểm | Tìm kiếm |
| 13492 | con lốc xoáy | cơn lốc xoáy |
| 13498 | hành tỉnh | hành tinh |
| 13498 | kéo khởi | kéo khỏi |
| 13498 | triệu đặt | triệu dặm |
| 13498 | không lò | khổng lồ |
| 13514 | hành tỉnh | hành tinh |
| 13514 | Kể trôi đạt | Kẻ trôi dạt |
| 13518 | Hành tỉnh | Hành tinh |
| 13536 | hành tỉnh | hành tinh |
| 13536 | Kepler là khả năng | Kepler có khả năng |
| 13562 | (4 ) | (4) |
| 13576 | # VAI TRÒ CỦA DỮ LIỆU | ## CHỦ ĐỀ 89

# VAI TRÒ CỦA DỮ LIỆU |
| 13578 | CHỦ ĐỀ 89 |  |
| 13610 | cầu nổi | cầu nối |
| 13747 | bản than | bản thân |
| 13767 | khó khan | khó khăn |
| 13787 | cuời nảy lên dành dạch | cười nảy lên đành đạch |
| 13787 | Trình không sừng sốt | Trinh không sửng sốt |
| 13787 | dàn thấy cổ úr nghẹn | dần thấy cổ ứ nghẹn |
| 13805 | sướng lấm! | sướng lắm! |
| 13805 | đầm địa | đầm đìa |
| 13805 | Giả đối ôi là giả đối | Giả dối ôi là giả dối |
| 13831 | về đẹp | vẻ đẹp |
| 13831 | học giới | học giỏi |
| 13831 | mĩa mai | mỉa mai |
| 13831 | Được rời! | Được rồi! |
| 13831 | giống điệu | giọng điệu |
| 13847 | 1 409 tỷ | 1,409 tỷ |
| 13931 | nghiệm trọng | nghiêm trọng |
| 14003 | đoạn văn sau: Nền tảng | đoạn văn sau:

Nền tảng |
| 14041 | cắm TikTok | cấm TikTok |
| 14051 | tính chính xác của | tính chính xác của nghiên cứu về thị trường thương mại điện tử? |
| 14053 | nghiên cứu về thị trường thương mại điện tử? |  |
| 14087 | ## SỰ RA ĐỜI CỦA BỨC ẢNH ĐỘNG ĐẦU TIÊN CHỦ ĐỀ 93 TRÊN THẾ GIỚI | ## CHỦ ĐỀ 93

## SỰ RA ĐỜI CỦA BỨC ẢNH ĐỘNG ĐẦU TIÊN TRÊN THẾ GIỚI |
| 14099 | mỗi phức phơi sáng | mỗi bức phơi sáng |
| 14125 | nhắc khởi đất | nhấc khỏi đất |
| 14159 | hạ bộ | hạ bệ |
| 14163 | đoạn văn sau: Sau khi | đoạn văn sau:

Sau khi |
| 14249 | Vĩnh Mexico | Vịnh Mexico |
| 14253 | (chọn nhiều | (chọn nhiều đáp án đúng) |
| 14255 | đáp án đúng) |  |
| 14275 | kínhvà | kính và |
| 14295 | tan bằng | tan băng |
| 14390 | mỗi bụng | mỡ bụng |
| 14414 | đoạn văn sau: Để khắc phục | đoạn văn sau:

Để khắc phục |
| 14434 | gần bồi các | gần bởi các |
| 14518 | dịch tế học | dịch tễ học |
| 14544 | "con sót" | "cơn sốt" |
| 14544 | đời hồi | đòi hỏi |
| 14582 | # HỌA SĨ DƯƠNG BÍCH LIÊN | ## CHỦ ĐỀ 97

# HỌA SĨ DƯƠNG BÍCH LIÊN |
| 14584 | CHỦ ĐỀ 97 |  |
| 14636 | vừa gọi cảm | vừa gợi cảm |
| 14668 | Dương Bích Liên? Đúng Sai | Dương Bích Liên? |
| 14670 | <table><tr><td>Tất cả | <table><tr><td></td><td>Đúng</td><td>Sai</td></tr><tr><td>Tất cả |
| 14776 | Ức, Canada | Úc, Canada |
| 14782 | kháp Việt Nam | khắp Việt Nam |
| 14786 | đoạn văn sau: Trung Nguyên | đoạn văn sau:

Trung Nguyên |
| 14866 | ra khởi nhà | ra khỏi nhà |
| 14922 | (3) .Giải pháp | (3) . Giải pháp |
| 14984 | bao nhiêu? 37 m² và cao 173 cm. 73 m² và cao 137 cm. 173 m² và cao 37 cm. 137 m² và cao 73 cm. | bao nhiêu?

37 m² và cao 173 cm.

73 m² và cao 137 cm.

173 m² và cao 37 cm.

137 m² và cao 73 cm. |
| 15002 | Chuột mẹ bỏ rơi con. Chuột đực | Chuột mẹ bỏ rơi con.

Chuột đực |
| 15004 | mỗi tuần. Chuột di cư | mỗi tuần.

Chuột di cư |
| 15006 | Bạo lực bùng phát khắp nơi không có Chuột cái trở nên căng thẳng và hung lý do rõ ràng. dữ. | Bạo lực bùng phát khắp nơi không có lý do rõ ràng.

Chuột cái trở nên căng thẳng và hung dữ. |
| 15022 | bộ long | bộ lông |
| 15044 | quản thể | quần thể |
| 4353 | TIỆC XÒA | TIỆC XÒE |
| 11 | mở lôi | mở lối |
| 13 | tranh cải | tranh cãi |
| 16 | Chuyện Tưởng Dạ Xoa | Chuyện Tướng Dạ Xoa |
| 17 | khùng hoàng | khủng hoảng |
| 18 | Văn quả Hà Nội | Vẫn quà Hà Nội |
| 31 | Thắng gù | Thằng gù |
| 34 | Tiệc xòa | Tiệc xòe |
| 35 | một mó mộng | một mớ mộng |
| 36 | Ga xếp | Ga xép |
| 44 | Trái tìm hồ | Trái tim hổ |
| 45 | Hoàng từ bé | Hoàng tử bé |
| 46 | sông oì | sông ơi |
| 47 | Cải oì! | Cải ơi! |
| 49 | Vàng lừa | Vàng lửa |
| 50 | Hây đọc lời ai điều | Hãy đọc lời ai điếu |
| 62 | lá chấn | lá chắn |
| 66 | ký nguyên | kỷ nguyên |
| 67 | nghi ngoi của người tây ban nha | nghỉ ngơi của người Tây Ban Nha |
| 68 | ký nguyên | kỷ nguyên |
| 69 | hạn phúc của người dan mạch | hạnh phúc của người Đan Mạch |
| 70 | bề chứa Carbon | bể chứa carbon |
| 75 | chia khóa | chìa khóa |
| 76 | nghi dưỡng | nghỉ dưỡng |
| 77 | nền tăng số | nền tảng số |
| 79 | ki nguyên | kỉ nguyên |
| 80 | Tơ nhận | Tơ nhện |
| 82 | thế ký XXI | thế kỷ XXI |
| 86 | về atlantis | về Atlantis |
| 94 | rợi ánh sáng | rọi ánh sáng |
| 97 | dữ đội | dữ dội |
| 105 | phần ánh | phản ánh |
| 106 | devil's canyon | Devil's Canyon |
| 109 | sung suống | sung sướng |
| 114 | tranh cải | tranh cãi |

## 3. Không sửa (lỗi nội dung của sách, không phải lỗi OCR) – cần GV xem

- CĐ 71 (Singapore): đoạn ngữ liệu trùng với bài âm nhạc của CĐ 63.
- Mục lục có hai mục "PHẦN 3".
- Một số phương án bị lặp (vd. CĐ 6 Câu 18; CĐ 66 Câu 3, Câu 8).
- Một số chỗ văn bản bị cắt cụt ngay trong sách.
- CĐ 6 Câu 15 có chữ không đọc được, đánh dấu "[…]".
- Nhiều chủ đề không có tiêu đề "CHỦ ĐỀ N" riêng (bắt đầu thẳng bằng tên bài / đoạn [1]): 17, 18, 20, 22–26, 28, 29, 31, 35, 36, 38, 43, 45, 47, 51–55, 58, 61, 70, 73, 75, 76, 90–92, 94. Chưa thêm tiêu đề.
- CĐ "nông nghiệp hữu cơ" Câu 21, phương án A: "Vì nó nông nghiệp công nghiệp…" (có lẽ là "Vì nền…"), để nguyên.
