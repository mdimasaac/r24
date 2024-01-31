import streamlit as st
from streamlit import session_state as ss
import gspread
import pandas as pd
# st.set_page_config(layout="wide")
from sumbangan_makanan import sumbangan_makanan
from pendampingan_ust import pendampingan_ust
from jobdesk import jobdesk
from jadwal_shalat import jadwal_shalat

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

t1,t2,t3,t4,t5,t6,t7,t8,t9 = st.tabs(options)
with t1:
    empty_space(2)
    cols = st.columns([1.2,.1,1])
    with cols[0]:
        jadwal_shalat()
    with cols[2]:
        title = '<div style="text-align: center; font-size: 24px; font-style: italic;">Login</div>'
        st.markdown(title,unsafe_allow_html=True)
        empty_space(2)
        c = st.container(border = True)
        password = ""
        user = c.selectbox("Select User",["Jamaah","Admin"])
        if user == "Jamaah":
            ss.admin = False
        elif user == "Admin":
            password_admin = c.text_input("Masukkan password (khusus Admin)", type="password", key = "Admin")
            if c.button("Submit password", key = "button_admin"):
                if password_admin == "satesomay":
                    st.success("Berhasil login sebagai admin. Silakan pilih menu di atas untuk navigasi ke halaman lainnya.")
                    ss.admin = True
                else:
                    st.error("Password salah. Hubungi admin untuk login sebagai admin, atau pilih menu di atas untuk masuk sebagai Jamaah.")
                    ss.admin = False
            c.write("(Jamaah tidak perlu mengisi password)")
with t2:
    jobdesk()
with t3:
    st.write("Page Sumbangan Kurma - coming soon")
with t4:
    sumbangan_makanan(ss.admin)
with t5:
    st.write("Page Piket Ikhwan - coming soon")
with t6:
    st.write("Page Piket Akhwat - coming soon")
with t7:
    st.write("Page Penjemputan Makanan - coming soon")
with t8:
    st.write("Page Imam Tarawih - coming soon")
with t9:
    pendampingan_ust(ss.admin)