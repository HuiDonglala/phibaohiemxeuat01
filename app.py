
import streamlit as st
from fee_tables import calculate_vehicle_fee, format_currency
from debug_wrapper import run_with_debug

def main():
    st.set_page_config(page_title="Báo phí bảo hiểm xe", layout="centered")
    st.title("🚗 Công cụ báo phí bảo hiểm xe")

    st.markdown("Nhập thông tin xe để tính phí bảo hiểm:")

    # Nhập thông tin cần thiết
    company = st.selectbox("Chọn công ty bảo hiểm", ["VNI", "BMI", "PVI", "TNDS"])
    vehicle_type = st.text_input("Loại xe (VD: Xe chở người, Xe tải...)")
    purpose = st.text_input("Mục đích sử dụng (VD: Không KDVT, KDVT)")
    value = st.number_input("Giá trị xe (VND)", min_value=100_000_000, step=10_000_000)
    months = st.number_input("Thời hạn bảo hiểm (tháng)", min_value=1, max_value=36, value=12)
    product_code = st.text_input("Mã sản phẩm (nếu có, cách nhau bởi dấu phẩy)")

    if st.button("Tính phí"):
        result = calculate_vehicle_fee(
            company=company,
            vehicle_type=vehicle_type,
            purpose=purpose,
            value=value,
            months=months,
            product_codes=[p.strip() for p in product_code.split(",")] if product_code else []
        )
        if result is not None:
            st.success(f"✅ Phí bảo hiểm: {format_currency(result)} VND")
        else:
            st.warning("Không tìm thấy mức phí phù hợp với thông tin đã nhập.")

# Bọc app bằng công cụ debug
run_with_debug(main)
