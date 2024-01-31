import streamlit as st
from streamlit import session_state as ss
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from streamlit_card import card

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
    return df

def insert_to_gspread(sheet_name,new_row):
    ws = connect_to_gspread(sheet_name)
    ws.append_row(new_row)

def manajemen_konsumsi():
    empty_space(5)
    title = '<div style="text-align: center; font-size: 24px; font-style: italic;">Job Desk: Manajemen Konsumsi</div>'
    st.markdown(title,unsafe_allow_html=True)
    st.divider()
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim A (2 orang atau lebih):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.caption("- Komunikasi dengan Ibu-Ibu, Bapak-Bapak, dan jamaah lainnya yang bersedia/berminat untuk mendonasikan menu makan untuk buka puasa")
    st.write("- Mencatat info detail donatur makanan ke app/google sheet")
    st.write("- Update status dengan ketua ramadhan")
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim B (2 orang):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Janjian dengan tim penjemput makanan: siapa yang jemput di hari apa, jemput di mana, kontak dengan donatur, dll")
    st.write("- Memanage supply kurma dan air; memastikan masih ada cukup supply untuk buka puasa setiap harinya")
    st.write("- Komunikasi dengan tim belanja & logistik jika harus beli kurma dadakan")
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim C (1-2 orang):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Stay setelah tarawih, untuk belanja menu makan sahur keesokan harinya")
    st.write("- Bisa bekerja sama dengan piket ikhwan untuk bagi tugas menjemput/beli makanan sahur (RisA)")

def manajemen_ustadz():
    empty_space(5)
    title = '<div style="text-align: center; font-size: 24px; font-style: italic;">Job Desk: Manajemen Ustadz</div>'
    st.markdown(title,unsafe_allow_html=True)
    st.divider()
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim A (1 orang):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Komunikasi dengan Ustadz terkait jadwal kajian selama Ramadhan & tema/judul kajian")
    st.write("- Update status ustadz dengan tim imam tarawih (jika ust ingin iftar/tarawih di tempat lain)")
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim B (2 orang atau lebih):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Atur/bagi jadwal pendampingan ustadz")
    st.write("- Antar ustadz kalau beliau mau jalan-jalan, atau buka puasa di masjid lain")

def piket_ikhwan():
    empty_space(5)
    title = '<div style="text-align: center; font-size: 24px; font-style: italic;">Job Desk: Piket Ikhwan</div>'
    st.markdown(title,unsafe_allow_html=True)
    st.divider()
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim A (2 orang atau lebih):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Komunikasi dengan contact person donatur makanan buka puasa")
    st.write("- Koordinasi mengisi jadwal penjemputan makanan setiap harinya")
    st.write("- Menjemput makanan buka puasa dari alamat donatur (jika butuh penjemputan)")
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim B (2 orang):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Hadir di acara buka puasa, datang sekitar 20 menit sebelum adzan maghrib untuk membagikan air & kurma")
    st.write("- Ikut hadir di acara Iftar di IWKZ dan membantu distribusi makanan")
    st.write("- Membersihkan tiker dan piring sisa makanan; menghimbau jamaah yang buka puasa supaya ikut membantu beres-beres")
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 26px;font-style: bold;">🗹 Tim Lakik (5+ orang):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Cuci piring setelah tarawih")
    st.write("- Belanja RisA setelah tarawih untuk makanan sahur keesokan harinya")

def piket_akhwat():
    empty_space(5)
    title = '<div style="text-align: center; font-size: 24px; font-style: italic;">Job Desk: Piket Akhwat</div>'
    st.markdown(title,unsafe_allow_html=True)
    st.divider()
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim A (3 orang atau lebih):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Komunikasi dengan donatur makanan buka puasa & tim penjemputan makanan, memastikan makanan mendarat di masjid sebelum maghrib")
    st.write("- Hadir sekitar 1 jam (?) sebelum adzan maghrib untuk portioning")
    st.write("- Menyiapkan air & kurma di bagian akhwat")
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim B (2 orang atau lebih):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Persiapan tiker & distribusi makanan untuk makan besar")
    st.write("- Merapihkan setelah makanan selesai & menghimbau jamaah untuk ikut bantu beres-beres")
    st.write("- (Optional) membungkus sisa makanan untuk dibawa pulang jamaah, karena masjid tidak ada kulkas besar untuk menyimpan isi makanan")
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim C (1-2 orang):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- staubsaugen setelah acara makan besar, atau")
    st.write("- Suruh yang ikhwan buat staubsaugen, supaya akhwat pulangnya nggak kemaleman")

def belanja_logistik():
    empty_space(5)
    title = '<div style="text-align: center; font-size: 24px; font-style: italic;">Job Desk: Belanja Logistik</div>'
    st.markdown(title,unsafe_allow_html=True)
    st.divider()
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim A (1-2 orang):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Manage stok peralatan makan plastik & plastik bungkus: beli (online) jika dibutuhkan")
    st.write("- Manage stok sabun cuci tangan, tisu toilet & tisu wudhu: beli (online?) jika dibutuhkan")
    st.write("- Manage stok sabun cuci piring, spons, lap kering dst: beli (online) jika dibutuhkan")
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim B (2 orang):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Membantu tim manajemen konsumsi untuk membeli kurma (jika dibutuhkan)")
    st.write("- Membantu tim kerja bakti untuk membeli peralatan bersih-bersih (jika dibutuhkan)")
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim C (1-2 orang):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Support bagian transportasi (jika dibutuhkan)")

def zakat_dan_bendahara():
    empty_space(5)
    title = '<div style="text-align: center; font-size: 24px; font-style: italic;">Job Desk: Zakat & Bendahara</div>'
    st.markdown(title,unsafe_allow_html=True)
    st.divider()
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim A (1 orang - taken):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Mengatur keuangan ramadhan")
    st.write("- Mengatur perizinan memakai dana untuk keperluan ramadhan")
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim B (4 orang - 2 Ikhwan 2 Akhwat):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Hadir offline di Masjid untuk penerimaan zakat fitrah dari jamaah (terutama 10 hari terakhir)")
    st.write("- Mencatat pembayaran zakat fitrah dan menyimpan uang pembayaran zakat fitrah")
    st.write("- Menghimbau/mengingatkan jamaah di hari-hari terakhir mengenai pembayaran zakat fitrah (offline dan online)")
    st.write("- Menyalurkan dana zakat fitrah ke badan penyaluran zakat fitrah di Indonesia (?)")

def acara_dan_publikasi():
    empty_space(5)
    title = '<div style="text-align: center; font-size: 24px; font-style: italic;">Job Desk: Acara & Publikasi</div>'
    st.markdown(title,unsafe_allow_html=True)
    st.divider()
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim A (n orang):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- coming soon")
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim B (n orang):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- coming soon")

def kerja_bakti():
    empty_space(5)
    title = '<div style="text-align: center; font-size: 24px; font-style: italic;">Job Desk: Kerja Bakti</div>'
    st.markdown(title,unsafe_allow_html=True)
    st.divider()
    empty_space(3)
    undertitle = '<div style="text-align: left; font-size: 24px;">🗹 Tim Besar (n orang):</div>'
    st.markdown(undertitle,unsafe_allow_html=True)
    st.write("- Lap basah jendela masjid (sisi dalam) + Fensterbank")
    st.write("- Staubsaugen seluruh interior masjid")
    st.write("- Pel dan bersihkan tempat wudhu ikhwan & akhwat")
    st.write("- Pel dan bersihkan toilet ikhwan & akhwat")
    st.write("- Bersihkan Garderobe; buang barang yang tidak diperlukan")
    st.write("- Rapikan lemari hitam ikhwan dekat tempat wudhu")
    st.write("- Rapikan lemari tempat perlengkapan dekat dapur")
    st.write("- Rapikan Quran terutama; susun berdasarkan tipe Quran & ukuran")
    st.write("- Rapikan lemari kantin; atur susunan barang")
    st.write("- Sortir barang di dapur; singkirkan bahan makanan yang tidak dipakai")
    st.write("- Sortir barang ramadhan yang sudah dibelanjakan (piring plastik, gelas plastik, tisu dll)")
    st.write("- dan lainnya")

def jobdesk():
    empty_space(2)
    title = '<div style="text-align: center; font-size: 40px; font-style: italic;">Panitia Ramadhan</div>'
    st.markdown(title,unsafe_allow_html=True)
    
    c1,c2 = st.columns(2)
    width = "310px"
    height = "200px"
    with c1:
        card(
        title="Manajemen Konsumsi",
        text="",
        image="https://media4.giphy.com/media/0iIDiDhE5dAxXkbRXx/giphy.gif",
        styles={"card": {"width":width,"height": height}}
        )
        card(
        title="Piket Ikhwan",
        text="",
        image="https://i.makeagif.com/media/10-28-2017/jxtpGP.gif",
        styles={"card": {"width":width,"height": height}}
        )
        card(
        title="Zakat & Bendahara",
        text="",
        image="https://i.pinimg.com/originals/53/b8/fd/53b8fd488b6fd22304640355fb6dfff4.gif",
        styles={"card": {"width":width,"height": height}}
        )
        card(
        title="Acara & Publikasi",
        text="",
        image="https://boolatplay.com/picture/1640765779.gif",
        styles={"card": {"width":width,"height": height}}
        )
    with c2:
        card(
        title="Manajemen Ustadz",
        text="",
        image="https://media4.giphy.com/media/l2QZXQdfq03PutABy/giphy.gif",
        styles={"card": {"width":width,"height": height}}
        )
        card(
        title="Piket Akhwat",
        text="",
        image="https://img.huffingtonpost.com/asset/5e444ca9210000f600e94ec1.gif?ops=scalefit_720_noupscale",
        styles={"card": {"width":width,"height": height}}
        )
        card(
        title="Belanja Logistik",
        text="",
        image="https://hips.hearstapps.com/roadandtrack/assets/16/38/1474651362-sep-23-2016-13-22-13.gif",
        styles={"card": {"width":width,"height": height}}
        )
        card(
        title="Kerja Bakti",
        text="",
        image="https://i.pinimg.com/originals/75/10/1d/75101d1055ac951dc0e2bc352e499327.gif",
        styles={"card": {"width":width,"height": height}}
        )

    tim_list = []
    values = ["Manajemen Konsumsi","Manajemen Ustadz","Piket Ikhwan",
                "Piket Akhwat","Belanja Logistik","Kerja Bakti",
                "Acara & Publikasi","Zakat & Bendahara"]
    panitia = st.selectbox("Detail Kepanitiaan",values,placeholder="Pilih Tim Panitia:")
    t3_1,t0,t3_2 = st.columns([1,.2,1])
    with t3_1:
        nama = st.text_input("Nama:")
        kontak = str(st.text_input("Kontak (Whatsapp):", value = "+49"))
    with t3_2:
        if panitia in ["Manajemen Konsumsi","Piket Akhwat","Belanja Logistik"]:
            tim_list = ["Tim A","Tim B","Tim C"]
        elif panitia in ["Piket Ikhwan"]:
            tim_list = ["Tim A","Tim B","Tim Lakik"]
        elif panitia in ["Manajemen Ustadz"]:
            tim_list = ["Tim A","Tim B"]
        elif panitia in ["Zakat & Bendahara"]:
            tim_list = ["Tim B"]
        elif panitia in ["Kerja Bakti"]:
            tim_list = ["Tim Besar"]
        elif panitia in ["Acara & Publikasi"]:
            tim_list = ["Tim A Ikhwan","Tim B Ikhwan","Tim A Akhwat","Tim B Akhwat"]
        tim = st.selectbox("Pilih tim:", tim_list)
        empty_space(1)
        if st.button("Masukkan saya ke tim!", key="panitia",use_container_width=True):
            new_row = [panitia,nama,kontak,tim]
            insert_to_gspread("panitia",new_row)
            df = fetch_from_gspread("panitia")
            
    empty_space(1)
    if panitia == "Manajemen Konsumsi":
        manajemen_konsumsi()
    elif panitia == "Manajemen Ustadz":
        manajemen_ustadz()
    elif panitia == "Piket Ikhwan":
        piket_ikhwan()
    elif panitia == "Piket Akhwat":
        piket_akhwat()
    elif panitia == "Belanja Logistik":
        belanja_logistik()
    elif panitia == "Zakat & Bendahara":
        zakat_dan_bendahara()
    elif panitia == "Acara & Publikasi":
        acara_dan_publikasi()
    elif panitia == "Kerja Bakti":
        kerja_bakti()

    empty_space(5)
    df = fetch_from_gspread("panitia")
    st.divider()
    title = '<div style="text-align: center; font-size: 36px; font-style: italic;">Struktur Kepanitiaan</div>'
    st.markdown(title,unsafe_allow_html=True)
    empty_space(3)
    if st.button("Refresh data"):
        df = fetch_from_gspread("panitia")
    bendahara_list = df[df["panitia"] == "Zakat & Bendahara"].sort_values(by= "tim")
    piket_ikhwan_list = df[df["panitia"] == "Piket Ikhwan"].sort_values(by= "tim")
    piket_akhwat_list = df[df["panitia"] == "Piket Akhwat"].sort_values(by= "tim")
    logistik_list = df[df["tim"] == "Belanja Logistik"].sort_values(by= "tim")
    kerja_bakti_list = df[df["panitia"] == "Kerja Bakti"].sort_values(by= "tim")
    publikasi_list = df[df["panitia"] == "Acara & Publikasi"].sort_values(by= "tim")
    konsumsi_list = df[df["panitia"] == "Manajemen Konsumsi"].sort_values(by= "tim")
    
    st.write('''#### *Ketua Ramadhan:*''')
    st.write("Arsyan Mohamad Virio Andreyana | +49 1523 7363067")
    empty_space(3)
    st.write('''#### *Wakil Ketua:*''')
    wakil = ["Ilham Muhammad | +49 1792 851483","Kevin Pratama | +49 1523 8593490"]
    for i in wakil:
        st.write(i)
    empty_space(3)
    st.write('''#### *Zakat & Bendahara:*''')
    if len(bendahara_list) != 0:
        for i,j,k in zip(bendahara_list["nama"],bendahara_list["kontak"],bendahara_list["tim"]):
            st.write(k+" | "+i+" | "+str(j))
    empty_space(3)
    st.write('''#### *Piket Ikhwan:*''')
    if len(piket_ikhwan_list) != 0:
        for i,j,k in zip(piket_ikhwan_list["nama"],piket_ikhwan_list["kontak"],piket_ikhwan_list["tim"]):
            st.write(k+" | "+i+" | "+str(j))
    empty_space(3)
    st.write('''#### *Piket Akhwat:*''')
    if len(piket_akhwat_list) != 0:
        for i,j,k in zip(piket_akhwat_list["nama"],piket_akhwat_list["kontak"],piket_akhwat_list["tim"]):
            st.write(k+" | "+i+" | "+str(j))
    empty_space(3)
    st.write('''#### *Manajemen Konsumsi:*''')
    if len(konsumsi_list) != 0:
        for i,j,k in zip(konsumsi_list["nama"],konsumsi_list["kontak"],konsumsi_list["tim"]):
            st.write(k+" | "+i+" | "+str(j))
    empty_space(3)
    st.write('''#### *Belanja Logistik:*''')
    if len(logistik_list) != 0:
        for i,j,k in zip(logistik_list["nama"],logistik_list["kontak"],logistik_list["tim"]):
            st.write(k+" | "+i+" | "+str(j))
    empty_space(3)
    st.write('''#### *Kerja Bakti:*''')
    if len(kerja_bakti_list) != 0:
        for i,j,k in zip(kerja_bakti_list["nama"],kerja_bakti_list["kontak"],kerja_bakti_list["tim"]):
            st.write(k+" | "+i+" | "+str(j))
    empty_space(3)
    st.write('''#### *Acara & Publikasi:*''')
    if len(publikasi_list) != 0:
        for i,j,k in zip(publikasi_list["nama"],publikasi_list["kontak"],publikasi_list["tim"]):
            st.write(k+" | "+i+" | "+str(j))
    empty_space(3)
    