# Đề 1. Khi Le Chatelier "đoán sai"

Bài về nhà sau Buổi 2 · chữa ở Buổi 3 · M3 · Trạng thái: có idea, chưa có prompt Gemini.

## Idea (D2)

Số liệu đã giải lại bằng code (Kc kiểm ngược đúng ở mọi trạng thái cân bằng mới).

```
1. Khi Le Chatelier "đoán sai"
Chủ đề: Giới hạn của phát biểu dạng lời của nguyên lí Le Chatelier và cách dùng Q, Kc để đoán đúng (Hóa học)
Loại: B (lý thuyết kèm số liệu thí nghiệm) · Tier: M3 (500–600 từ + 2 bảng) · Kiểu cấu trúc: 11 — Giải quyết Mâu thuẫn/Nghịch lý ◉ | 7 — Nghiên cứu thực nghiệm → Kết quả → Phân tích ○

* Mục tiêu: HS thấy câu "cân bằng chuyển dịch theo chiều làm giảm tác động" có thể dẫn tới dự đoán sai khi tác động không làm đổi nồng độ các chất trong biểu thức Kc theo cách tưởng; HS tự lập bảng ba thời điểm (cân bằng ban đầu, ngay sau tác động, cân bằng mới), tính Q và so với Kc để ra kết luận đúng.

* Dàn ý triển khai (7 ý):
  1. Phát biểu dạng lời của nguyên lí Le Chatelier và hai cách hiểu phổ biến của học sinh: "tăng áp suất thì dịch về phía ít phân tử khí", "thêm chất nào thì hệ tiêu thụ bớt chất đó".
  2. Công cụ kiểm tra: Q tính bằng đúng công thức của Kc nhưng dùng nồng độ ngay sau tác động; Q < Kc thì chạy thuận, Q > Kc thì chạy nghịch, Q = Kc thì không dịch. Chỉ nhiệt độ làm đổi Kc. Nồng độ chất rắn không có mặt trong Kc.
  3. Tình huống A, thêm khí trơ argon vào bình chứa N₂O₄(g) ⇌ 2NO₂(g), Kc = 0,036 ở nhiệt độ T; cân bằng ban đầu [N₂O₄] = 0,100 M, [NO₂] = 0,060 M.
     A1. Bình cứng (thể tích không đổi): áp suất tổng tăng nhưng [N₂O₄], [NO₂] không đổi nên Q = Kc, cân bằng không dịch (dù "áp suất tăng").
     A2. Xi-lanh pít-tông tự do (áp suất không đổi): khí argon làm thể tích tăng gấp đôi, ngay sau đó [N₂O₄] = 0,050 M, [NO₂] = 0,030 M, Q = 0,018 < Kc, cân bằng dịch thuận; cân bằng mới [N₂O₄] ≈ 0,0449 M, [NO₂] ≈ 0,0402 M.
  4. Tình huống B, pha loãng dung dịch Fe³⁺(aq) + SCN⁻(aq) ⇌ FeSCN²⁺(aq) (màu đỏ máu), Kc = 100 ở 25 °C; cân bằng ban đầu [Fe³⁺] = [SCN⁻] = 0,020 M, [FeSCN²⁺] = 0,040 M. Thêm nước gấp đôi thể tích: ngay sau đó 0,010 / 0,010 / 0,020 M, Q = 200 > Kc, cân bằng dịch nghịch; máy đo màu ghi [FeSCN²⁺] cân bằng mới ≈ 0,017 M, thấp hơn 0,020 M (giá trị nếu chỉ do pha loãng). Không chất nào được "thêm vào", nhưng cân bằng vẫn dịch.
  5. Tình huống C, chất rắn: NH₄HS(s) ⇌ NH₃(g) + H₂S(g), Kc = 1,44·10⁻⁴ ở 25 °C, Kc = [NH₃][H₂S]; trong bình kín có dư NH₄HS, [NH₃] = [H₂S] = 0,012 M. Thêm 10 g NH₄HS rắn: Q không đổi, cân bằng không dịch, dù "thêm chất đầu".
  6. Bảng tổng hợp ba tình huống (Bảng 2): tác động | dự đoán theo câu chữ Le Chatelier | Q so với Kc | kết quả thực.
  7. Kết luận: phát biểu dạng lời chỉ là cách nói ngắn; khi tác động không làm đổi nồng độ đúng như tưởng (khí trơ, pha loãng, chất rắn), cần lập bảng ba thời điểm và tính Q.

* Bảng dự kiến:
  - Bảng 1: Nồng độ (M) ở ba thời điểm cho tình huống A1, A2, B: cột Tình huống | Chất | Cân bằng ban đầu | Ngay sau tác động | Cân bằng mới. Một số ô để trống cho câu hỏi khai thác (ô cân bằng mới của A2 và B).
  - Bảng 2: tổng hợp ba tình huống như ý 6 (cột "kết quả thực" có thể để trống một phần cho câu hỏi).

* Lỗi nhầm lẫn điển hình:
  L1. Thêm khí trơ làm áp suất tổng tăng nên cân bằng dịch về phía ít phân tử khí (bỏ qua việc nồng độ các chất phản ứng không đổi khi thể tích không đổi).
  L2. Pha loãng làm mọi nồng độ giảm như nhau nên cân bằng không dịch (bỏ qua số mũ, hay số "hạt", ở tử và mẫu khác nhau).
  L3. Thêm chất rắn (chất đầu) thì cân bằng dịch thuận.
  L4. Nhầm "áp suất tổng" với nồng độ từng chất trong biểu thức Kc.
  L5. Kết luận "nguyên lí Le Chatelier sai" thay vì "phát biểu dạng lời bị áp sai"; hoặc cho rằng Kc đổi khi pha loãng hay thêm khí trơ.

* Câu hỏi TSA gợi ý:
  * "Bạn A nói: thêm argon vào bình cứng làm áp suất tăng nên cân bằng dịch về phía N₂O₄. Dựa vào Bảng 1, nhận định này đúng hay sai?"
  * "Tính Q ngay sau khi pha loãng ở tình huống B và cho biết chiều dịch chuyển." (Q = 200)
  * "Nếu chỉ do pha loãng, [FeSCN²⁺] phải là bao nhiêu? Số liệu máy đo cho thấy điều gì?"
  * "Ở tình huống A2, nếu thay argon bằng N₂O₄ cùng số mol thì hệ dịch theo chiều nào?" (tình huống mới, M3)
  * "Ghép mỗi tác động (thêm Ar bình cứng, thêm Ar áp suất không đổi, pha loãng, thêm NH₄HS rắn, tăng nhiệt độ) với Q, Kc sau tác động."
```

## Gợi ý hình ảnh

| Hình | Đặt ở | Caption | Từ khóa tìm ảnh |
|---|---|---|---|
| Hình 1 | Sau ý 3 (tình huống A) | Hình 1: Thêm khí trơ vào bình cứng (trái) và vào xi-lanh có pít-tông tự do (phải). | `inert gas added constant volume constant pressure equilibrium diagram`, `adding argon equilibrium piston diagram` |
| Hình 2 | Sau ý 4 (tình huống B) | Hình 2: Dung dịch FeSCN²⁺ trước và sau khi pha loãng gấp đôi. | `iron thiocyanate equilibrium dilution color`, `FeSCN2+ blood red solution test tube` |

- Hình 1 dễ không tìm được đúng ý; có thể nhờ Gemini vẽ mới theo mô tả: hai bình, bên trái bình cứng có thêm hạt Ar, bên phải xi-lanh pít-tông bị đẩy lên.
- Mỗi hình ghi đúng 1 nguồn; ảnh Việt hóa ghi thêm "(Việt hóa)".
