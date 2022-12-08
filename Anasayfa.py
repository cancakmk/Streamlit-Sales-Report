import streamlit as st

st.header("📁 Dosya Seçiniz : ")

uploaded_file = st.file_uploader("")
st.session_state["xlsxFile"] = uploaded_file

if uploaded_file is not None:
    st.warning(' ✅ Rapor Sayfasına Geçebilirsiniz')
else:
    st.warning('Lütfen dosya seçiniz...')

