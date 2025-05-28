import streamlit as st
from zaman_modulu import zaman_modulu

st.set_page_config(page_title="Proje Yönetimi Simülasyonu", layout="wide")
st.title("📅 Proje Yönetimi Web Uygulaması")

menu = st.sidebar.radio("Modül Seçimi", ["Zaman Planlama Modülü"])

if menu == "Zaman Planlama Modülü":
    zaman_modulu()
