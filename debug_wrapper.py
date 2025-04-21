
import streamlit as st
import traceback

def run_with_debug(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        st.error("❌ Đã xảy ra lỗi:")
        st.code(traceback.format_exc(), language="python")
        raise e
