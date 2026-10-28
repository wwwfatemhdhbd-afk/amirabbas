import streamlit as st

st.title("فرم نظرسنجی")

# فیلدهای ورودی در مرورگر
name = st.text_input("نام خود را وارد کنید:")
last_name = st.text_input("نام خانوادگی خود را وارد کنید:")
father_name = st.text_input("نام پدر خود را وارد کنید:")

# دکمه ارسال
if st.button("ارسال پاسخ‌ها"):
    if name and last_name and father_name:
        st.success("پاسخ‌های شما با موفقیت دریافت شد!")
        st.write("---")
        st.write(f"نام: {name}")
        st.write(f"نام خانوادگی: {last_name}")
        st.write(f"نام پدر: {father_name}")
        st.write("پیام شما دریافت شد. متشکرم.")
    else:
        st.warning("لطفاً همه فیلدها را پر کنید.")
