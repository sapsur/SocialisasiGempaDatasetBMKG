import streamlit as st
import pandas as pd
import folium
import geopandas
import leafmap.foliumap as leafmap
import plotly_express as px
from streamlit_option_menu import option_menu

df1 = pd.read_csv("gempagempi.csv")
df = df1.loc[:, ("tanggal", "waktu", "latitude", "longitude", "kedalaman", "magnitudo", "daerah")]
m = leafmap.Map(location=[ -0.78927, 113.921327], tiles="Cartodb dark_matter", zoom_start=4)
jml_gempa = df['daerah'].unique()
contact_options = jml_gempa

with st.sidebar:
    selected = option_menu('Explore!',
    ['Main Menu','Tabel Data','Grafik Gempa','Heatmap','Titik Gempa'],
    default_index=0)

if (selected == 'Main Menu'):
    st.markdown("<h1 style='text-align: center;' >Media Sosialisasi Bencana Gempa Bumi</h1>", unsafe_allow_html=True)
    st.subheader("Tahukah kamu?")
    st.caption("Gempa bumi adalah getaran atau guncangan yang terjadi di permukaan bumi akibat pelepasan energi dari bawah permukaan secara tiba-tiba yang menciptakan gelombang seismik. Gempa bumi biasa disebabkan oleh pergerakan kerak bumi atau lempeng bumi. Selain itu gempa bumi juga bisa disebabkan oleh letusan gunung api.")
    st.caption("Menurut Direktorat Vulkanologi dan Mitigasi Bencana Geologi (DVMBG) Departemen Energi dan Sumber Daya Mineral (ESDM) menyatakan wilayah di Indonesia yang rawan gempa dan tsunami diantarannya Aceh, Sumatera Utara, Sumatera Barat, Bengkulu, Lampung, Banten, Jateng, Jogjakarta, Jatim, Bali, Nusa Tenggara Barat, Nusa Tenggara Timur, Sulut, Sulteng, Sulsel, Maluku Uatara, Maluku Selatan, Biak, Yapen dan Fak-Fak di Papua serta Balikpapan.")
    st.caption("Selama tahun 2022 kejadian gempa bumi yang mengakibatkan dampak besar adalah gempa bumi Cianjur tanggal 21 November 2022 dengan magnitudo (M 5,6), episenter terletak di darat pada kedalaman 10 km. Kejadian gempa bumi Cianjur mengakibatkan 635 meninggal, 1.083 orang luka-luka dan mengakibatkan terjadinya bahaya ikutan (retakan tanah, likuefaksi dan gerakan tanah).")
    st.caption("<h3>Maka dari itu penting bagi kita untuk mengetahui cara menghadapi Gempa bumi</h3>", unsafe_allow_html=True)
    st.caption("<h2>Metode 1, Berlutut dan Berpegangan (Untuk di Dalam Ruangan)</h2>", unsafe_allow_html=True)
    st.image("metode1.jpg")
    st.caption("Berlutut dan rendahkan badan, Cari tempat berlindung, Berlindunglah di bawah meja yang kokoh atau perabot lain. Usahakan menjauhi kaca, jendela, pintu dan dinding, serta benda-benda yang rawan jatuh seperti lampu gantung atau perabot lain. Tetaplah di dalam hingga Anda aman keluar. Berpegangan, Berpeganganlah pada apa pun benda yang Anda jadikan tempat berlindung dan tunggu sampai getarannya mereda. Tetaplah berada di tempat yang aman dan Tetaplah di dalam ruangan sampai guncangan berhenti dan sudah aman untuk keluar dari bangunan")
    st.caption("<h2>Metode 2, Segitiga Kehidupan (Untuk di Dalam Ruangan)</h2>", unsafe_allow_html=True)
    st.image("metode2.jpg")
    st.caption("Gunakan metode segitiga kehidupan sebagai alternatif teknik berlutut, berlindung, dan berpegangan. Carilah struktur bangunan atau perabot terdekat. Teori segitiga kehidupan menyatakan bahwa orang yang berlindung di sebelah, bukan di bawah, perabot rumah seperti sofa sering kali dilindungi oleh kekosongan atau ruang yang tercipta ketika tertimpa runtuhan bertumpuk. Secara teori, bangunan yang runtuh akan jatuh menimpa sofa atau meja dan meremukkannya sedikit, namun meninggalkan sejumlah celah kosong di dekatnya. Meringkuklah dalam posisi fetal (seperti janin dalam kandungan) di samping struktur bangunan atau perabot.")
    st.caption("<h2>Metode 3, Bertahan Hidup Menghadapi Gempa Bumi di Luar Ruangan</h2>", unsafe_allow_html=True)
    st.image("metode3.jpg")
    st.caption("Tetap berada di luar ruangan sampai guncangan berhenti. Jangan mencoba aksi heroik seperti menyelamatkan seseorang atau memasuki suatu bangunan. Tetap di luar, dengan kemungkinan tertimpa bangunan yang runtuh semakin kecil, adalah pilihan terbaik. Jauhi bangunan, penerangan jalan, dan kabel listrik. Hal-hal ini merupakan risiko utama jika berada di luar ruangan saat gempa bumi atau salah satu gempa susulan sedang berlangsung. Jika berada dalam kendaraan, berhenti sesegera mungkin dan tetaplah di dalam. Hindari berhenti di dekat bangunan, pepohonan, jalan layang, dan kabel listrik. Jika Anda berada dekat dengan badan air yang besar, bersiaplah menghadapi kemungkinan tsunami. Tsunami terjadi ketika gempa bumi menimbulkan gangguan bawah air yang ekstrim, sehingga mengirimkan ombak dahsyat ke arah pantai dan tempat tinggal manusia.")
    st.caption("<h3>Bencana Gempa bumi terjadi secara tidak terduga, oleh karena itu, alangkah baiknya kita Mempersiapkan Diri dengan salah satu cara yaitu membuat Rumah Anti Gempa, berikut 4 desain rumah tahan gempa sesuai anjuran BNPB</h3>", unsafe_allow_html=True)
    st.caption("<h2>1. Growing House</h2>", unsafe_allow_html=True)
    st.image("rumah1.jpg")
    st.caption("Desain rumah ini merupakan karya mahasiswa UGM sebagai rumah yang bisa mengantisipas datangnya banjir serta tahan gempa. Desain rumah ini merupakan sebuah karya yang memenangkan sebuah sayembara desain yang diselenggarakan oleh negara Jepang. Konsep ini sendiri terbagi menjadi tiga tahapan, yakni home for all, space for all, life for future. Tiga tahapan tersebut masing-masing memiliki makna. Tujuannya adalah mendesain sebuah bangunan rumah yang menambah ruang di dalamnya untuk beraktivitas tanpa mengurangi fungsi utamanya. Bagian luar rumah juga dimaksimalkan untuk aktivitas lain seperti berkebun, olahraga, dan bermain.")
    st.caption("<h2>2. Dome</h2>", unsafe_allow_html=True)
    st.image("rumah2.jpg")
    st.caption("Rumah dengan ciri khas dinding dan atap yang saling menyatu ini diyakini memiliki tingkat ketahanan tinggi terhadap gempa bumi. Rumah dome karya Prof. Nizam, M.Sc, Ph.D ini memiliki ketahan juga terhadap angin kencang yang kuat. Kunci utama dari rumah ini menerapkan konstruksi yang kokoh serta penggunaan material bangunan yang ringan. Karena konstruksi kokoh dan material yang ringan, rumah ini tidak akan mudah goyang saat gempa bumi dan angin kencang. Rumah ini sendiri sudah diterapkan sebagai rumah mitigasi bencana. Letaknya ada di Dusun Nglepen, Prambanan, Kabupaten Sleman.")
    st.caption("<h2>3. Barrataga (Bangunan Rumah Rakyat Tahan Gempa)</h2>", unsafe_allow_html=True)
    st.image("rumah3.jpg")
    st.caption("Rumah ini tampak memiliki nuansa tradisional, namun siapa yang menyangka jika Barrataga adalah rumah yang tahan terhadap gempa bumi. Rancangan ini digagas oleh pakar Rekayasa Kegempaan Universitas Islam Indonesia (UII) Yogyakarta, yakni Prof. Ir. Sarwidi. Filosofi dari rumah ini sendiri adalah “menyelamatkan diri”, sebagai respon atas gempa bumi yang melanda Jogja pada tahun 2006 silam. Rangkat dari Barrataga terdiri dari beton kolom, balok tepi atas, balok bawah, kemudian balok lantai yang dihubungkan dengan simpul Barrataga agar tidak patah saat gempa melanda. Aspek yang paling kuat dari bangunan ini adalah penguatan besi tulangan yang mengait satu sama lain. Menurut Sarwidi, rumah ini akan semakin kuat terhadap gempa jika menggunakan kayu atau bambu untuk bagian besi tulangannya.")
    st.caption("<h2>4. Risha (Rumah Instan Sederhana Sehat)</h2>", unsafe_allow_html=True)
    st.image("rumah4.jpg")
    st.caption("Risha merupakan rumah instan beton bongkar pasang yang bisa dibangun dalam waktu singkat serta telah terbukti tahan terhadap gempa bumi. Proses pembangunan rumah ini tidak menggunakan semen dan bata, tapi menggabungkan setiap panel beton dengan menggunakan baut. Desain rumah ini menjadi solusi bagi masyarakat yang memiliki penghasilan rendah, menjadi korban bencana, dan rumah darurat. Walau begitu rumah ini tetap memiliki kualitas yang baik selayaknya rumah lain secara umum.")

if (selected == 'Tabel Data'):
    st.markdown("<h1 style='text-align: center;' >Tabel Data</h1>", unsafe_allow_html=True)
    st.table(df)

if (selected == 'Grafik Gempa'):
    st.markdown("<h1 style='text-align: center;' >Grafik Gempa</h1>", unsafe_allow_html=True)
    st.markdown("<h3><center>Visualisasi Gempa Bumi dalam beberapa Kasus", unsafe_allow_html=True)

    st.caption("<br><h3><center>Kasus 1. Besarnya Gempa di beberapa daerah berdasarkan Waktu</center>", unsafe_allow_html=True)
    daerah = st.selectbox("Pilih Daerah yang tersedia", jml_gempa)
    fig = px.line(df[df['daerah'] == daerah], x = "waktu", y = "magnitudo", title = daerah)
    st.plotly_chart(fig)
    st.caption("Pada Kasus ini, user memilih Daerah yang akan di analisis, kemudian Program akan menampilkan Waktu muncul nya Gempa yang terjadi dengan Kekuatan Magnitudo nya.")

    st.caption("<br><h3><center>Kasus 2. Magnitudo Gempa yang paling sering Terjadi</center>", unsafe_allow_html=True)
    df2 = df.groupby('magnitudo').size().reset_index(name='Count')
    fig1 = px.bar(df2, x = 'magnitudo', y='Count')
    st.plotly_chart(fig1)
    st.caption("Pada Kasus ini, Menampilkan Jumlah Magnitudo yang sering Terjadi. Dari hasil tersebut, Besarnya gempa yang terjadi Rata-rata sebesar 3.1 SR")

    st.caption("<br><h3><center>Kasus 3. Gempa yang paling dekat dengan Permukaan beserta keterangan Magnitudo nya</center>", unsafe_allow_html=True)
    df3 = df.nsmallest(10, 'kedalaman')
    fig2 = px.bar(df3, x = 'kedalaman', y = 'daerah', color='magnitudo')
    st.plotly_chart(fig2)
    st.caption("Pada Kasus ini, Menampilkan Kedalaman Gempa yang paling dekat dengan Permukaan. Kemudian ditampilkan juga Besarnya Magnitudo pada Kedalaman tersebut. Dari data yang di dapat, Magnitudo yang paling besar dengan Kedalaman yang paling dekat terdapat di Pulau Jawa dengan kedalaman 5 KM dan Magnitudo 3.9 SR")

    st.caption("<br><h3><center>Kasus 4. Waktu pada Gempa Terbesar yang pernah Terjadi</center>", unsafe_allow_html=True)
    df4 = df.nlargest(10, 'magnitudo')
    fig3 = px.line(df4, x='waktu', y='magnitudo')
    st.plotly_chart(fig3)
    st.caption("Pada Kasus ini, Menampilkan Kapan saja Waktu saat terjadinya Gempa Paling Besar. Dari data yang di dapat, Gempa yang paling besar yaitu 6.1 SR terjadi pada pukul 9:49:42 Pagi hari.")

    st.caption("<br><h3><center>Kasus 5. Total Gempa yang terjadi di beberapa Daerah pada 20 November - 09 Desember</center>", unsafe_allow_html=True)
    df5 = df.groupby('daerah').size().reset_index(name='Count')
    fig4 = px.bar(df5, x = 'daerah', y='Count')
    st.plotly_chart(fig4)
    st.caption("Pada Kasus ini, Menampilkan Total Gempa yang terjadi di beberapa Daerah. Dari informasi yang di dapat, Gempa yang paling banyak terjadi yaitu di Pulau Jawa dengan total 367 kali Gempa.")

if (selected == 'Heatmap'):
    st.markdown("<h3 style='text-align: center;' >Gempa 20 November - 9 Desember 2022 di Indonesia</h3>", unsafe_allow_html=True)
    m.add_heatmap(
        df,
        latitude="latitude",
        longitude="longitude",
        value="magnitudo",
        name="Heat map",
        radius=15,
    )
    m.to_streamlit(height=600)


if (selected == 'Titik Gempa'):
    st.markdown("<h1 style='text-align: center;' >Titik Gempa</h1>", unsafe_allow_html=True)
    geometry = geopandas.points_from_xy(df.longitude, df.latitude)
    geo_df = geopandas.GeoDataFrame(df[["tanggal", "waktu", "latitude", "longitude", "kedalaman", "magnitudo", "daerah"]], geometry=geometry)
    geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in geo_df.geometry]
    tempat = st.selectbox('Provinsi yang ingin dipilih', contact_options)
    if "load_state" not in st.session_state:
        st.session_state.load_state = False

    if "load_state" or st.session_state.load_state:
        st.session_state.load_state = True
        rslt_geo_df = geo_df.loc[geo_df["daerah"]==tempat]
        geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in rslt_geo_df.geometry]
        if tempat == 'Java, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Pulau Jawa</h1>", unsafe_allow_html=True)
        elif tempat == 'Seram, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Pulau Seram</h1>", unsafe_allow_html=True)
        elif tempat == 'Bali Region, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Pulau Bali</h1>", unsafe_allow_html=True)
        elif tempat == 'Flores Region, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Flores, Nusa Tenggara Timur</h1>", unsafe_allow_html=True)
        elif tempat == 'Halmahera, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Pulau Halmahera</h1>", unsafe_allow_html=True)
        elif tempat == 'Irian Jaya Region, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Sekitar Papua</h1>", unsafe_allow_html=True)
        elif tempat == 'Irian Jaya, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Papua</h1>", unsafe_allow_html=True)
        elif tempat == 'Minahassa Peninsula, Sulawesi':
            st.markdown("<h1 style='text-align: center;' >Semenanjung Minahasa</h1>", unsafe_allow_html=True)
        elif tempat == 'Near North Coast of Irian Jaya':
            st.markdown("<h1 style='text-align: center;' >Pantai Utara Papua</h1>", unsafe_allow_html=True)
        elif tempat == 'North of Halmahera, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Halmahera Utara</h1>", unsafe_allow_html=True)
        elif tempat == 'Northern Sumatra, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Sumatera Utara</h1>", unsafe_allow_html=True)
        elif tempat == 'South of Bali, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Bali Selatan</h1>", unsafe_allow_html=True)
        elif tempat == 'Southern Sumatra, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Sumatera Selatan</h1>", unsafe_allow_html=True)
        elif tempat == 'Sulawesi, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Sulawesi</h1>", unsafe_allow_html=True)
        elif tempat == 'Sumba Region, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Sumba, Nusa Tenggara Timur</h1>", unsafe_allow_html=True)
        elif tempat == 'Sumbawa Region, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Sumbawa, Nusa Tenggara Timur</h1>", unsafe_allow_html=True)
        elif tempat == 'Sunda Strait, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Selat Sunda</h1>", unsafe_allow_html=True)
        elif tempat == 'Talaud Islands, Indonesia':
            st.markdown("<h1 style='text-align: center;' >Kepulauan Talaud</h1>", unsafe_allow_html=True)
        elif tempat == 'Timor Region':
            st.markdown("<h1 style='text-align: center;' >Pulau Timor</h1>", unsafe_allow_html=True)
    i = 0
    for Kordinat in geo_df_list:
        if geo_df.magnitudo[i] >= 5:
            type_color = "red"
        elif geo_df.magnitudo[i] <= 5 and geo_df.magnitudo[i] >= 4:
            type_color = "green"
        else:
            type_color = "black"
        m.add_child(
            folium.Marker(
                location=Kordinat,
                popup=
                    "Tanggal : " + str(geo_df.tanggal[i]) + "<br>"
                    + "Waktu : " + str(geo_df.waktu[i]) + "<br>"
                    + "Kedalaman : " + str(geo_df.kedalaman[i]) + " KM<br>"
                    + "Magnitudo : " + str(geo_df.magnitudo[i]) + " SR<br>"
                    + "Koordinat : "  + str(geo_df_list[i]),
                icon=folium.Icon(color="%s" % type_color),
            )
        )
        i = i + 1
    m.to_streamlit(height=600)

    col1, col2 = st.columns([1,30])
    with col1:
        st.image('merah.png', width=15)
        st.image('hijau.png', width=15)
        st.image('hitam.png', width=15)
    with col2:
        st.write('Magnitudo  >  5 SR')
        st.write('Magnitudo 4 - 5 SR')
        st.write('Magnitudo  <  4 SR')