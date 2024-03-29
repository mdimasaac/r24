import pandas as pd
import streamlit as st
from streamlit import session_state as ss
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def empty_space(n):
    i = 0
    while i < n:
        st.write("")
        i+=1

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
    df["tanggal"] = pd.to_datetime(df["tanggal"])
    return df

def jadwal_shalat():
    d_jam = fetch_from_gspread("jadwal_shalat")
    d_jam = d_jam[d_jam["tanggal"].dt.date == datetime.today().date()].reset_index(drop = True)
    if len(d_jam) != 0:
        text = (str(d_jam["tanggal"].dt.strftime('%A, %b %d')[0]))
        title = '<div style="text-align: center; font-size: 24px; font-style: italic;">'+text+'</div>'
        st.markdown(title,unsafe_allow_html=True)
        empty_space(2)
        for i,j in zip(range(1,7),d_jam.columns[1:7]):
            value = str(d_jam.iloc[:,i][0])
            label = j.title()
            # st.write(big_text,text)
            c = st.container(border = True)
            c.metric(label=label, value=value)
