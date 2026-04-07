from langchain_core.tools import tool

# ============================================================
# MOCK DATA — Dữ liệu giả lập hệ thống du lịch
# Lưu ý: Giá cả có logic (VD: cuối tuần đắt hơn, hạng cao hơn đắt hơn)
# Sinh viên cần đọc hiểu data để debug test cases.
# ============================================================

FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1_450_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2_800_000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1_200_000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1_350_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1_100_000, "class": "economy"},
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1_600_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1_300_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3_200_000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1_300_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780_000, "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650_000, "class": "economy"},
    ],
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1_800_000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1_200_000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650_000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250_000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350_000, "area": "An Thượng", "rating": 4.7},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3_500_000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1_500_000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800_000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200_000, "area": "Dương Đông", "rating": 4.5},
    ],
    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2_800_000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1_400_000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550_000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 180_000, "area": "Quận 1", "rating": 4.6},
    ],
}

@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Tìm kiếm chuyến bay giữa 2 thành phố.
    Tham số:
    - origin: Thành phố xuất phát
    - destination: Thành phố đích
    Đầu ra: Danh sách các chuyến bay phù hợp. Trả về hãng máy bay, giờ bay và giá vé.
    Nếu không có chuyến bay phù hợp, nhận thông báo không có chuyến nào.
    """
    flight_key = (origin, destination)
    relevant_flights = FLIGHTS_DB.get(flight_key, [])
    if not relevant_flights:
        reversed_flight_key = (destination, origin)
        relevant_flights = FLIGHTS_DB.get(reversed_flight_key, [])
        if not relevant_flights:
            return f"Không tìm thấy chuyến bay từ {origin} đến {destination}"
        else:
            results = [f"Không tìm thấy chuyến bay từ {origin} tới {destination}, ý bạn là từ {destination} tới {origin}?"
                       f"Đây là danh sách các chuyến bay từ {destination} đến {origin}:"]
    else:
        results = [f"Danh sách các chuyến bay từ {origin} tới {destination}:"]

    for idx, flight in enumerate(relevant_flights, start=1):
        results.append(
            f"{idx}. {flight['airline']} | "
            f"{flight['departure']} - {flight['arrival']} | "
            f"Hạng: {flight['class']} | "
            f"Giá: {flight['price']:,} VND"
        )

    return "\n".join(results)

@tool
def search_hotels(city: str, max_price_per_night: int = 9999999) -> str:
    """
    Tìm kiếm các khách sạn phù hợp tại một thành phố, lọc theo giá tối đa mỗi đêm.
    Tham số:
    - city: Tên thành phố cần tìm khách sạn.
    - max_price_per_night: Giá tối đa mỗi đêm
    Đầu ra: Trả về danh sách các khách sạn phù hợp (tên, số sao và giá khu vực). Sắp xếp theo rating.
    """
    nearby_hotels = HOTELS_DB.get(city, [])
    relevant_hotels = []

    for hotel in nearby_hotels:
        if hotel.get("price_per_night") <= max_price_per_night:
            relevant_hotels.append(hotel)

    if len(relevant_hotels) == 0:
        return f"Không tìm thấy khách sạn tại {city} với giá dưới {max_price_per_night}/đêm. Hãy thử tăng ngân sách."

    relevant_hotels = sorted(
        relevant_hotels,
        key=lambda hotel: hotel.get("rating", 0),
        reverse=True
    )

    results = [f"Danh sách khách sạn tại {city} có giá dưới {max_price_per_night:,} VND/đêm:"]

    for idx, hotel in enumerate(relevant_hotels, start=1):
        results.append(
            f"{idx}. {hotel['name']} | "
            f"{hotel['stars']} sao | "
            f"Khu vực: {hotel['area']} | "
            f"Rating: {hotel['rating']} | "
            f"Giá: {hotel['price_per_night']:,} VND/đêm"
        )

    return "\n".join(results)

@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách còn lại sau khi trừ các khoản chi phí.
    Tham số:
    - total_budget: ngân sách ban đầu (VNĐ)
    - expenses: Chuỗi mô tả các chi phí, mỗi khoản được cách nhau bởi dấu phẩy. Định dạng là: tên khoản:số tiền.
    Ví dụ: vé_máy_bay:890000,khách_sạn:650000
    Trả về chi tiết các khoản chi phí và số tiền còn lại.
    Nếu vượt quá ngân sách, cảnh bảo rõ số tiền thiếu.
    """

    @tool
    def calculate_budget(total_budget: int, expenses: str) -> str:
        """
        Tính toán ngân sách còn lại sau khi trừ các khoản chi phí.
        Tham số:
        - total_budget: ngân sách ban đầu (VNĐ)
        - expenses: Chuỗi mô tả các chi phí, mỗi khoản được cách nhau bởi dấu phẩy. Định dạng là: tên khoản:số tiền.
        Ví dụ: vé_máy_bay:890000,khách_sạn:650000
        Trả về chi tiết các khoản chi phí và số tiền còn lại.
        Nếu vượt quá ngân sách, cảnh bảo rõ số tiền thiếu.
        """
        if total_budget < 0:
            return "Ngân sách ban đầu không hợp lệ."

        expenses = expenses.strip()
        if not expenses:
            return (
                f"Ngân sách ban đầu: {total_budget:,} VND\n"
                f"Tổng chi phí: 0 VND\n"
                f"Ngân sách còn lại: {total_budget:,} VND"
            )

        parsed_expenses = []
        total_expense = 0

        items = [item.strip() for item in expenses.split(",") if item.strip()]

        for item in items:
            if ":" not in item:
                return (
                    f"Khoản chi '{item}' không đúng định dạng. "
                    f"Vui lòng dùng dạng tên_khoản:số_tiền."
                )

            name, amount_str = item.split(":", 1)
            name = name.strip()
            amount_str = amount_str.strip()

            if not name:
                return "Tên khoản chi không được để trống."

            try:
                amount = int(amount_str)
            except ValueError:
                return f"Số tiền của khoản '{name}' không hợp lệ: '{amount_str}'."

            if amount < 0:
                return f"Số tiền của khoản '{name}' không được là số âm."

            parsed_expenses.append((name, amount))
            total_expense += amount

        remaining_budget = total_budget - total_expense

        results = [f"Ngân sách ban đầu: {total_budget:,} VND", "Chi tiết chi phí:"]

        for idx, (name, amount) in enumerate(parsed_expenses, start=1):
            results.append(f"{idx}. {name}: {amount:,} VND")

        results.append(f"Tổng chi phí: {total_expense:,} VND")

        if remaining_budget >= 0:
            results.append(f"Ngân sách còn lại: {remaining_budget:,} VND")
        else:
            results.append(
                f"Vượt ngân sách {-remaining_budget:,} VND. "
                f"Hãy giảm chi tiêu hoặc tăng ngân sách."
            )

        return "\n".join(results)
