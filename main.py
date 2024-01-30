import streamlit as st
from streamlit import session_state as ss
import gspread
import pandas as pd
st.set_page_config(layout="wide")
from sumbangan_makanan import sumbangan_makanan
from pendampingan_ust import pendampingan_ust
from jobdesk import jobdesk

def write_title():
    title = '<div style="text-align: center; font-size: 40px;">Project: Ramadhan 2024 Al-Falah IWKZ</div>'
    subtitle = '<div style="text-align: center; font-size: 18px;">Form Kontribusi & Partisipasi Ramadhan (Persiapan, Kajian, Buka Puasa, Tarawih, Itikaf, dll)</div>'
    st.markdown(title, unsafe_allow_html=True)
    st.markdown(subtitle, unsafe_allow_html=True)

def empty_space(n):
    i = 0
    while i < n:
        st.write("")
        i+=1

write_title()
empty_space(5)
if "admin" not in ss:
    ss.admin = False

options = ["Login Page","Jobdesk Panitia","Sumbangan Kurma",
           "Sumbangan Makanan","Piket Ikhwan","Piket Akhwat",
           "Jemput Makanan","Imam Tarawih","Pendampingan Ustadz"]

# choice = st.sidebar.selectbox("Menu",options, key = '1')
choice = st.tabs(options)
if (choice == "Login Page"):
    password = ""
    
    user = st.selectbox("Select User",["Jamaah","Admin"])
    if user == "Jamaah":
        ss.admin = False
    elif user == "Admin":
        password_admin = st.text_input("Masukkan password", type="password", key = "Admin")
        if st.button("Submit password", key = "button_admin"):
            if password_admin == "satesomay":
                st.success("Berhasil login sebagai admin. Silakan pilih menu di sebelah kiri untuk navigasi ke halaman lainnya.")
                ss.admin = True
            else:
                st.error("Password salah. Hubungi admin untuk login sebagai admin, atau pilih menu di sebelah kiri untuk login sebagai Jamaah.")
                ss.admin = False

elif (choice == "Sumbangan Makanan"):
    sumbangan_makanan(ss.admin)

elif (choice == "Pendampingan Ustadz"):
    pendampingan_ust(ss.admin)

elif (choice == "Jobdesk Panitia"):
    jobdesk()
