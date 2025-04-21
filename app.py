# app.py

import streamlit as st
from fee_tables import fee_rates_bmi, fee_rates_pvi, fee_rates_vni

st.set_page_config(page_title="Tính phí bảo hiểm xe", layout="centered")

st.title("🚗 Tính phí bảo hiểm xe")

company = st.selectbox("Chọn công ty bảo hiểm", ["BMI", "PVI", "VNI"])
value = st.number_input("Giá trị xe (VND)", min_value=100_000_000, step=10_000_000)
year = st.text_input("Năm sản xuất (VD: 2022)")
part_theft = st.checkbox("Thêm quyền lợi mất cắp bộ phận (chỉ áp dụng cho PVI)")

if st.button("Tính phí"):
    try:
        year_key = str(year).strip()

        if company == "BMI":
            rate = fee_rates_bmi.get(year_key)
        elif company == "PVI":
            rate = fee_rates_pvi.get(year_key)
        elif company == "VNI":
            rate = fee_rates_vni.get(year_key)
        else:
            rate = None

        if not rate:
            st.error("Không tìm thấy tỷ lệ cho năm sản xuất này.")
        else:
            total_fee = value * rate
            if company == "PVI" and part_theft:
                total_fee *= 1.2  # nhân thêm 20%

            st.success(f"✅ Phí bảo hiểm ước tính: {total_fee:,.0f} VND")

    except Exception as e:
        st.error(f"Lỗi: {e}")
