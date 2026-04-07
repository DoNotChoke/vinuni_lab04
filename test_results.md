# TravelBuddy — Trợ lý Du lịch Thông minh

> Gõ `quit` để thoát

---

## Hội thoại mẫu

### 1) Chào hỏi ban đầu

**Bạn:**  
Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.

**TravelBuddy đang suy nghĩ...**  
Trả lời trực tiếp

**TravelBuddy:**  
Chào bạn! Rất vui được giúp bạn lên kế hoạch du lịch. Bạn có ý tưởng về điểm đến nào chưa? Hoặc bạn muốn tham khảo một số địa điểm nổi tiếng ở Việt Nam như Hà Nội, Đà Nẵng, Hội An hay TP.HCM? Hãy cho mình biết thêm thông tin về sở thích của bạn nhé!

---

### 2) Tìm chuyến bay từ Hà Nội tới Đà Nẵng

**Bạn:**  
Hãy tìm cho tôi các chuyến bay từ Hà Nội tới Đà Nẵng

**TravelBuddy đang suy nghĩ...**

**Gọi tool:**
```python
search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
```

**Kết quả:** Trả lời trực tiếp

**TravelBuddy:**  
Dưới đây là danh sách các chuyến bay từ Hà Nội tới Đà Nẵng:

1. **Vietnam Airlines** — **06:00 - 07:20**  
   Hạng: `economy`  
   Giá: **1,450,000 VND**

2. **Vietnam Airlines** — **14:00 - 15:20**  
   Hạng: `business`  
   Giá: **2,800,000 VND**

3. **VietJet Air** — **08:30 - 09:50**  
   Hạng: `economy`  
   Giá: **890,000 VND**

4. **Bamboo Airways** — **11:00 - 12:20**  
   Hạng: `economy`  
   Giá: **1,200,000 VND**

Nếu bạn cần thêm thông tin về khách sạn hoặc tính toán ngân sách cho chuyến đi, hãy cho tôi biết nhé!

---

### 3) Tư vấn chuyến đi Phú Quốc 2 đêm với ngân sách 5 triệu

**Bạn:**  
Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, tổng chi phí là 5 triệu. Hãy tư vấn cho tôi

**TravelBuddy đang suy nghĩ...**

**Gọi tool:**
```python
search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 1500000})
calculate_budget({'total_budget': 5000000, 'expenses': 'vé_máy_bay:1350000,khách_sạn:1600000'})
```

**Kết quả:** Trả lời trực tiếp

**TravelBuddy:**  
Dưới đây là thông tin cho chuyến đi của bạn từ Hà Nội đến Phú Quốc:

#### Chuyến bay
- **VietJet Air**: `10:00 - 12:15`  
  Hạng: `economy`  
  Giá: **1,350,000 VND**

#### Khách sạn
- **Lahana Resort** — 3 sao  
  Khu vực: Dương Đông  
  Rating: 4.0  
  Giá: **800,000 VND/đêm**

- **Sol by Meliá** — 4 sao  
  Khu vực: Bãi Trường  
  Rating: 4.2  
  Giá: **1,500,000 VND/đêm**

#### Tính toán chi phí
- **Vé máy bay:** 1,350,000 VND (VietJet Air)
- **Khách sạn:** 800,000 VND × 2 đêm = 1,600,000 VND (Lahana Resort)

**Tổng chi phí:**  
1,350,000 + 1,600,000 = **2,950,000 VND**

#### Kết luận
Với ngân sách **5,000,000 VND**, bạn còn dư **2,050,000 VND** sau khi chi trả cho vé máy bay và khách sạn. Bạn có thể xem xét nâng cấp khách sạn hoặc thêm các hoạt động giải trí khác trong chuyến đi.

Nếu bạn cần thêm thông tin hoặc đặt dịch vụ, hãy cho tôi biết nhé!

---

### 4) Yêu cầu đặt khách sạn

**Bạn:**  
Tôi muốn đặt khách sạn

**TravelBuddy đang suy nghĩ...**  
Trả lời trực tiếp

**TravelBuddy:**  
Bạn có thể cho mình biết thông tin cụ thể hơn về chuyến đi của bạn được không? Cụ thể là bạn muốn đặt khách sạn ở thành phố nào, thời gian lưu trú và ngân sách tối đa mỗi đêm là bao nhiêu?

---

### 5) Câu hỏi ngoài phạm vi

**Bạn:**  
Giải giúp tôi bài tập lập trình Python Linked List

**TravelBuddy đang suy nghĩ...**  
Trả lời trực tiếp

**TravelBuddy:**  
Tôi là chatbot phục vụ du lịch nên không thể trả lời câu hỏi của bạn.

---

### 6) Kết thúc

**Bạn:**  
`quit`
