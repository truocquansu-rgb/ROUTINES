# Đề 2. Nhà máy NH₃: mỗi lượt chỉ khoảng 15% vẫn có lãi

Bài về nhà sau Buổi 2 · chữa ở Buổi 3 · M3 · Trạng thái: có idea, chưa có ngữ liệu và prompt Gemini.

## Idea (D2)

Số liệu bảng là **mô phỏng khí lý tưởng**, tính bằng code từ một Kp neo ở 450 °C (Kp ≈ 6,1·10⁻⁵ bar⁻², ΔH = −91,8 kJ theo SGK, hỗn hợp N₂ : H₂ = 1 : 3), nên các bảng nhất quán với nhau. Giá trị thật của nhà máy (khí thực ở áp suất cao) lệch vài phần trăm. Ngữ liệu không ghi chú "mô phỏng".

```
2. Nhà máy NH₃: mỗi lượt chỉ khoảng 15% vẫn có lãi
Chủ đề: Vòng tổng hợp ammonia, cân bằng và tối ưu điều kiện vận hành (Hóa học)
Loại: B (quy trình công nghiệp kèm số liệu) · Tier: M3 (500–600 từ + 2–3 bảng + 1 sơ đồ) · Kiểu cấu trúc: 5 — Quy trình → Phản ứng → Tuần hoàn & Tối ưu ◉ | 23 — Tối ưu hóa theo Điều kiện biên ○

* Mục tiêu: HS dùng Kc, Q và nguyên lí Le Chatelier để giải thích vì sao nhà máy chọn 400–450 °C, 150–200 bar, xúc tác Fe, và vì sao chấp nhận mỗi lượt qua tháp chỉ chuyển hóa khoảng 15% nhưng tổng thể vẫn gần như hết nguyên liệu nhờ tách NH₃ và tuần hoàn khí.

* Dàn ý triển khai (7 ý):
  1. Phản ứng N₂(g) + 3H₂(g) ⇌ 2NH₃(g), ΔH = −91,8 kJ; chiều thuận tỏa nhiệt và làm giảm số mol khí. Điều kiện công nghiệp: 400–450 °C, 150–200 bar, xúc tác Fe.
  2. Mâu thuẫn nhiệt độ: hạ nhiệt độ thì phần trăm NH₃ lúc cân bằng tăng (Bảng 1) nhưng tốc độ phản ứng giảm mạnh (Bảng 1, cột tốc độ tương đối); 450 °C là điểm cân bằng giữa hiệu suất và tốc độ. Áp suất cao làm tăng phần trăm NH₃ nhưng tốn chi phí máy nén và thiết bị chịu áp, nên dừng ở khoảng 200 bar.
  3. Thực tế khí đi qua tháp xúc tác rất nhanh nên không kịp đạt cân bằng: mỗi lượt chỉ khoảng 15% N₂ và H₂ chuyển thành NH₃.
  4. Vòng tuần hoàn (sơ đồ): khí ra khỏi tháp được làm lạnh, NH₃ hóa lỏng và tách ra ở bình tách; N₂ và H₂ chưa phản ứng được máy nén tuần hoàn đưa trở lại tháp cùng khí mới. Việc liên tục lấy NH₃ ra giữ Q luôn nhỏ hơn Kc ở đầu vào tháp.
  5. Khí trơ (Ar từ không khí, CH₄ từ khí thiên nhiên) không phản ứng, không hóa lỏng, nên tích tụ dần trong vòng tuần hoàn. Ở áp suất tổng không đổi, khí trơ làm loãng N₂ và H₂, khiến phần trăm NH₃ lúc cân bằng giảm (Bảng 3). Nhà máy phải xả bỏ (purge) một phần nhỏ khí tuần hoàn, chấp nhận mất theo một ít N₂ và H₂.
  6. Tổng thể: với 15% mỗi lượt và tuần hoàn, nếu xả 1% khí tuần hoàn thì khoảng 95% nguyên liệu được chuyển thành NH₃; xả 2% còn khoảng 90%; xả 5% còn khoảng 78% (công thức: tổng chuyển hóa = 0,15 / [1 − 0,85 × (1 − tỉ lệ xả)]).
  7. Tỉ lệ nạp N₂ : H₂: phần trăm NH₃ lúc cân bằng lớn nhất khi nạp đúng tỉ lệ 1 : 3; dư N₂ hay dư H₂ đều làm giảm (Bảng 2). Điều này trái với suy đoán "thêm chất đầu thì luôn được nhiều sản phẩm hơn".

* Bảng dự kiến (mô phỏng):
  - Bảng 1: % NH₃ lúc cân bằng theo nhiệt độ và áp suất (nạp 1 : 3), kèm tốc độ tương đối (mô phỏng, chọn để minh họa xu hướng):
    | Nhiệt độ | 100 bar | 200 bar | 300 bar | Tốc độ tương đối |
    | 350 °C | 35,7 | 47,5 | 54,2 | 1 |
    | 450 °C | 17,3 | 27,0 | 33,6 | 8 |
    | 550 °C | 8,4 | 14,6 | 19,5 | 40 |
  - Bảng 2: % NH₃ lúc cân bằng theo tỉ lệ nạp H₂ : N₂ ở 450 °C, 200 bar: 1 : 1 → 19,0; 2 : 1 → 25,6; 3 : 1 → 27,0; 4 : 1 → 26,3; 6 : 1 → 23,0.
  - Bảng 3: % NH₃ lúc cân bằng theo phần trăm khí trơ trong khí nạp ở 450 °C, 200 bar: 0% → 27,0; 5% → 24,4; 10% → 22,0; 20% → 17,6.
  - Sơ đồ vòng tổng hợp: khí mới → máy nén → tháp xúc tác Fe → thiết bị làm lạnh → bình tách (NH₃ lỏng ra) → máy nén tuần hoàn → quay lại tháp; nhánh xả khí trơ.

* Lỗi nhầm lẫn điển hình:
  L1. Tưởng nhà máy chọn 450 °C vì ở đó phần trăm NH₃ lúc cân bằng cao nhất (thực ra cao nhất ở nhiệt độ thấp; 450 °C là thỏa hiệp với tốc độ).
  L2. Tưởng xúc tác Fe làm tăng phần trăm NH₃ lúc cân bằng.
  L3. Tưởng chuyển hóa 15% mỗi lượt nghĩa là nhà máy chỉ dùng được 15% nguyên liệu (bỏ qua tuần hoàn).
  L4. Tưởng khí trơ không phản ứng thì không ảnh hưởng gì (bỏ qua việc làm loãng ở áp suất tổng không đổi).
  L5. Tưởng nạp càng dư N₂ (hoặc H₂) thì càng nhiều NH₃.

* Câu hỏi TSA gợi ý:
  * "Dựa vào Bảng 1, vì sao nhà máy không vận hành ở 350 °C dù phần trăm NH₃ lúc cân bằng cao hơn?" (Trade-off)
  * "Việc hóa lỏng và tách NH₃ ra khỏi khí tuần hoàn ảnh hưởng thế nào đến Q ở đầu vào tháp?" (Q < Kc, chuyển dịch theo chiều thuận)
  * "Tính phần trăm tổng chuyển hóa khi tỉ lệ xả là 3%." (dùng công thức trong ngữ liệu; kết quả ≈ 85%, đã tính: 0,15 / (1 − 0,85 × 0,97) = 0,855)
  * "Nếu ngừng xả khí trơ trong nhiều ngày, sản lượng NH₃ mỗi lượt thay đổi thế nào? Dựa vào Bảng 3."
  * "Một kỹ sư đề xuất nạp dư N₂ gấp đôi để tăng NH₃. Dùng Bảng 2 để phản biện."
```

## Gợi ý hình ảnh

| Hình | Đặt ở | Caption | Ghi chú |
|---|---|---|---|
| Hình 1 | Sau ý 4 | Hình 1: Sơ đồ vòng tổng hợp NH₃: tháp xúc tác, làm lạnh, tách NH₃ lỏng, tuần hoàn khí và nhánh xả khí trơ. | Dùng ảnh gốc tes.com (đã lưu trong zip) làm mẫu cho Gemini vẽ lại; **thêm nhánh xả khí trơ** (ảnh mẫu chưa có). Nguồn: tham khảo Lmbroomfield, tes.com |

Từ khóa tìm thêm mẫu sơ đồ: `Haber process recycle loop purge diagram`, `ammonia synthesis loop flow diagram`.

Lệnh vẽ lại (đính kèm ảnh mẫu):
```
Using the attached image only as a layout reference, draw a new clean schematic, flat 2D, white background, black lines, no logo:
fresh gas inlet "Khí mới (N₂ + 3H₂)" → "Máy nén" → reactor column "Tháp xúc tác Fe (450 °C, 200 bar)" → "Thiết bị làm lạnh" → "Bình tách" with liquid outlet at the bottom "NH₃ lỏng" → gas outlet at the top "Khí chưa phản ứng" → "Máy nén tuần hoàn" → back to the reactor inlet.
Add a small side branch from the recycle line labeled "Xả khí trơ (Ar, CH₄)".
Below the diagram: N₂(g) + 3H₂(g) ⇌ 2NH₃(g), ΔH = −91,8 kJ. Correct subscripts.
```
