import streamlit as st
from streamlit import session_state as ss
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from streamlit_card import card
from datetime import datetime



def empty_space(n):
    i = 0
    while i < n:
        st.write("")
        i+=1

def hari():
    z1,z2,z3,z4,z5,z6,z7 = st.columns(7)
    with z1:
        st.subheader("Senin")
    with z2:
        st.subheader("Selasa")
    with z3:
        st.subheader("Rabu")
    with z4:
        st.subheader("Kamis")
    with z5:
        st.subheader("Jumat")
    with z6:
        st.subheader("Sabtu")
    with z7:
        st.subheader("Ahad")
    st.divider()

def connect_to_gspread(sheet_name):
    credentials = {
    "type": st.secrets["type"],
    "project_id": st.secrets["project_id"],
    "private_key_id": st.secrets["private_key_id"],
    "private_key": st.secrets["private_key"],
    "client_email": st.secrets["client_email"],
    "client_id": st.secrets["client_id"],
    "auth_uri": st.secrets["auth_uri"],
    "token_uri": st.secrets["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["client_x509_cert_url"],
    "universe_domain": st.secrets["universe_domain"]
    }
    cred = ServiceAccountCredentials.from_json_keyfile_dict(credentials)
    gc = gspread.authorize(cred)
    sheet_id = st.secrets["sheet_id"]
    spreadsheet = gc.open_by_key(sheet_id)
    ws = spreadsheet.worksheet(sheet_name)
    return ws

def fetch_from_gspread(sheet_name):
    ws = connect_to_gspread(sheet_name)
    sheet = ws.get_all_records()
    df = pd.DataFrame(sheet)
    df["tanggal"] = df["tanggal"].astype("int32")
    return df

def insert_to_gspread(sheet_name,new_row):
    ws = connect_to_gspread(sheet_name)
    ws.append_row(new_row)

def container(df,n):
    c = st.container(border = True)
    d = df[df["tanggal"] == n]
    masehi = ""
    if n+10 <=31:
        masehi = str(n+10)+"-Maret"
    else:
        masehi = str(n)+"-April"
    c.write(str(n) + "-Ramadhan")
    c.write("("+masehi+")")
    c.write("___")
    for i in range(len(d)):
        c.write("nama: "+str(d.iloc[i,1]))
        c.write("menu: "+str(d.iloc[i,2]))
        c.write("porsi: "+str(d.iloc[i,3]))
        c.write("jemput: "+str(d.iloc[i,6]))
        c.write("___")

def cards(df,n):
    d = df[df["tanggal"] == n][["date","nama","menu","porsi","dijemput"]]
    d["date"] = pd.to_datetime(d["date"])
    image = ""
    st.write(d["date"].values.tolist()[0])
    st.write(type(d["date"].values.tolist()[0]))
    # if d["date"].values().date() == datetime.today().date():
    #     image = "https://media4.giphy.com/media/0iIDiDhE5dAxXkbRXx/giphy.gif"
    # else:
    #     image = ""
    a,b = st.columns([1,2])
    with a:
        width = "160px"
        height = "125px"
        card(
        title=str(n),
        text="Ramadhan",
        image=image,
        styles={"card": {"width":width,"height": height}}
        )
    with b:
        empty_space(5)
        c = st.container(border = True)
        c.table(d[["nama","menu","porsi","dijemput"]])

def sumbangan_makanan(admin):
    empty_space(2)
    title = '<div style="text-align: center; font-size: 30px; font-style: italic;">Sumbangan Makanan Buka Puasa</div>'
    st.markdown(title,unsafe_allow_html=True)
    empty_space(5)
    title1,t0,title2 = st.columns([1,.2,1])
    with title1:
        st.subheader("Login sebagai admin:")
        st.write("- bisa lihat kalender dan isinya")
        st.write("- bisa eintragen nama dan detail ke kalender")
        st.write("- bisa buka tabel isi detail info (lihat di bagian bawah)")
    with title2:
        st.subheader("Login sebagai jamaah:")
        st.write("- bisa lihat kalender dan isinya")

    st.divider()
    empty_space(3)
    if "divider" not in ss:
        ss.divider = False
    list_tanggal = []
    for i in range(31):
        t1 = str(i+1)+" Ramadhan / "
        if i+11 <=31:
            t2 = str(i+11)+" Maret"
        else:
            t2 = str(i-20)+" April"
        list_tanggal.append(t1+t2)
    if admin:
        untertitle = '<div style="text-align: center; font-size: 30px; font-style: italic;">--- Eintragen nama dan detail info ---</div>'
        st.markdown(untertitle,unsafe_allow_html=True)
        empty_space(3)
        
        o1,o0,o2 = st.columns([1,.2,1])
        with o1:
            nama = st.text_input("Nama")
        with o2:
            kontak = st.text_input("Kontak (WA)")
        empty_space(2)
        o1,o0,o2 = st.columns([1,.2,1])
        with o1:
            menu = st.text_input("Menu")
        with o2:
            porsi = st.slider("Porsi",1,100)
        empty_space(2)
        o1,o0,o2 = st.columns([1,.2,1])
        with o1:
            alamat = st.text_input("Alamat")
        with o2:
            dijemput = st.selectbox("Dijemput di rumah?",["iya","tidak"])
        empty_space(2)
        o1,o0,o2 = st.columns([1,.2,1])
        with o1:
            tanggal = st.selectbox("Mau masak untuk hari apa / tanggal berapa?",list_tanggal)
        with o2:
            empty_space(2)
            submit = st.button("Submit",key="sumbangan_makanan",use_container_width=True) 
            
        if submit:
            dateval = tanggal.split("/")[1].strip().replace("Maret","03").replace("April","04").replace(" ","/")+"/2024"
            new_row = [dateval,int(tanggal.split(" ")[0]),nama,menu,porsi,kontak,alamat,dijemput]
            insert_to_gspread("sumbangan_makanan",new_row)
            df = fetch_from_gspread("sumbangan_makanan")
            ss.divider = True

    empty_space(2)
    st.divider()
    if st.toggle("Fetch actual data",key="sumbangan_makanan_1"):
        df = fetch_from_gspread("sumbangan_makanan")
        ss.divider = True
    else:
        ss.divider = False
    empty_space(5)
    # hari()

    for n in range(31):
        cards(df,n)
        # try:
        #     # container(df,n)
        #     cards(df,n)
        # except:
        #     pass

    if admin:
        if st.toggle("Show full data",key="sumbangan_makanan_2"):
            df_show = fetch_from_gspread("sumbangan_makanan").iloc[1:]
            st.table(df_show)

    # # pekan 1
    # a1,a2,a3,a4,a5,a6,a7 = st.columns(7)
    # cols_1_7 = [a1,a2,a3,a4,a5,a6,a7]
    # for i,n in zip(cols_1_7,range(1,8,1)):
    #     with i:
    #         try:
    #             container(df,n)
    #         except:
    #             pass
    # if ss.divider:
    #     st.divider()

    # # pekan 2
    # a8,a9,a10,a11,a12,a13,a14 = st.columns(7)
    # cols_8_14 = [a8,a9,a10,a11,a12,a13,a14]
    # for i,n in zip(cols_8_14,range(8,15,1)):
    #     with i:
    #         try:
    #             container(df,n)
    #         except:
    #             pass
    # if ss.divider:
    #     st.divider()

    # # pekan 3
    # a15,a16,a17,a18,a19,a20,a21 = st.columns(7)
    # cols_15_21 = [a15,a16,a17,a18,a19,a20,a21]
    # for i,n in zip(cols_15_21,range(15,22,1)):
    #     with i:
    #         try:
    #             container(df,n)
    #         except:
    #             pass
    # if ss.divider:
    #     st.divider()

    # # pekan 4
    # a22,a23,a24,a25,a26,a27,a28 = st.columns(7)
    # cols_22_28 = [a22,a23,a24,a25,a26,a27,a28]
    # for i,n in zip(cols_22_28,range(22,29,1)):
    #     with i:
    #         try:
    #             container(df,n)
    #         except:
    #             pass
    # if ss.divider:
    #     st.divider()

    # # pekan 5
    # a29,a30,a31,e4,e5,e6,e7 = st.columns(7)
    # cols_29_31 = [a29,a30,a31]
    # for i,n in zip(cols_29_31,range(29,32,1)):
    #     with i:
    #         try:
    #             container(df,n)
    #         except:
    #             pass
    # if ss.divider:
    #     st.divider()
    
    
    