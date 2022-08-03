from matplotlib.style import use
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

#Setting Page
st.set_page_config(layout="centered")

#Judul
st.title("Ramai di *Citayam Fashion Week*, Bagaimana Nasib Gen Z?")
st.caption("Oleh: Sa'ad Fadlulloh, Agustus 2022")

#Pendahuluan
st.header("*Citayam Fashion Week* dan Generasi Z")
st.write("Beberapa waktu lalu, kita dihebohkan oleh sekumpulan remaja dari daerah pinggiran Jakarta "
        "yang berkumpul di kawasan Sudirman. Remaja-remaja SCBD (Sudirman, Citayam, Bojonggede, Depok) "
        "ini beradu model pakaian menyebrang zebra cross dalam kegiatan yang mereka sebut *Citayam Fashion Week*. "
        "Memanfaatkan media sosial Tiktok, mereka membuat konten-konten video pendek agar menjadi viral. "
        "Pemuda-pemuda tersebut umumnya merupakan anak-anak berusia 15-24 tahun yang termasuk ke dalam golongan Generasi Z. "
        "Konon generasi ini akan menentukan masa depan Indonesia karena jumlahnya yang sangat banyak. " 
        "Di tengah euforia Gen Z di media sosial, ada tantangan dan realita yang harus dihadapi oleh mereka.")

#Konten 1
st.subheader("Seberapa Penting Gen Z bagi Indonesia?")
col1_1, col1_2 = st.columns([1,2])
with col1_1:
    st.write("Generasi Z atau biasa disingkat Gen Z merupakan generasi yang lahir pada rentang tahun 1997-2012.",
            "Berdasarkan sensus penduduk pada tahun 2020, Gen Z mendominasi jumlah penduduk Indonesia dengan total populasi **74,93 juta jiwa (27,93%)**.",
            "Belum semua Gen Z berada pada kelompok penduduk usia produktif. Umur Gen Z saat ini masih berada pada rentang 10-25 tahun. ",
            "Sebagian besar masih mengenyam bangku sekolah dan universitas. Namun sekitar enam tahun lagi, seluruh Gen Z akan mencapai usia produktifnya.")
with col1_2:
    #Jumlah Penduduk Berdasarkan Generasi
    gen = pd.read_csv('generasi.csv')
    fig_gen=px.pie(gen, values='jumlah_penduduk', names='generasi',
        title='Jumlah Penduduk Berdasarkan Generasi (2020)', 
        labels={'jumlah_penduduk':'Jumlah Penduduk (juta jiwa)',
                    'generasi':'Generasi'})
    fig_gen.update_layout(title_x=0.5)
    st.plotly_chart(fig_gen, use_container_width=True)
    st.caption('Sumber: Badan Pusat Statistik')

radio2 = st.radio(label='Opsi Diagram:', options=('Persen','Total'), horizontal=True)
if radio2 == 'Persen':
    groupnorm = 'percent'
    ylabel= 'Persentase Penduduk'
else:
    groupnorm = ''
    ylabel='Jumlah Penduduk (ribu jiwa)'

col2_1, col2_2 = st.columns([2,1])
with col2_1:
    #Proyeksi Jumlah Penduduk 2015-2045
    proyeksi = pd.read_csv('proyeksi_2015_2045.csv')
    proyeksi_pivot = proyeksi.groupby(by='kelompok_umur').sum()
    proyeksi_pivot = proyeksi_pivot.transpose()
    fig_proyeksi= px.area(proyeksi_pivot, groupnorm=groupnorm,
                title = 'Proyeksi Jumlah Penduduk Tahun 2015-2045',
                labels={'index':'Tahun',
                        'value':ylabel,
                        'kelompok_umur':'Kelompok Umur'})
    fig_proyeksi.update_layout(title_x=0.5)
    st.plotly_chart(fig_proyeksi, use_container_width=True)
    st.caption('Sumber: Badan Pusat Statistik')
with col2_2:
    st.subheader('')
    st.write("Berdasarkan Analisis Profil Penduduk Indonesia yang dilakukan oleh Badan Pusat Statistik (BPS), "
            "Indonesia telah mengalami bonus demografi sejak 2012 dan puncaknya diperkirakan terjadi pada periode 2020-2030. "
            "Bonus demografi dinilai dapat meningkatkan perekomonian suatu negara, seperti yang terjadi di Tiongkok, Korea Selatan, Jepang, dll. "
            "Dengan besarnya populasi Gen Z di masa bonus demografi, peran Gen Z sangat signifikan dalam menentukan nasib bangsa Indonesia.")

#Konten 2
st.subheader("Realita yang Dihadapi")
st.write("Memiliki persentase jumlah penduduk terbesar, ironisnya jumlah pengangguran terbesar pun didominasi oleh Gen Z. "
        "Penduduk usia muda (15-24 tahun) mendominasi tingkat pengangguran terbuka (TPT) sebesar **43,3% (3,64 juta jiwa)** pada bulan Februari 2022. " 
        "Peningkatan jumlah angkatan kerja tidak sebanding dengan kesempatan kerja yang tersedia, terlebih jika harus sesuai dengan bidang keahliannya. "
        "Selain itu, banyak perusahaan yang mensyaratkan pengalaman kerja bagi pelamar. Padahal sebagian besar penganggur muda belum memiliki pekerjaan sebelumnya.")

tpt = pd.read_csv('pengangguran_umur.csv')
fig_tpt = px.pie(tpt,values='jumlah',names='kelompok_umur',
                title='Jumlah Pengangguran Berdasarkan Kelompok Umur (Februari 2022)',
                labels={'kelompok_umur':'Kelompok Umur',
                            'jumlah':'Jumlah Pengangguran'})
fig_tpt.update_layout(title_x=0.5)
st.plotly_chart(fig_tpt, use_container_width=True)
st.caption('Sumber: Badan Pusat Statistik')

st.write("Berdasarkan tingkat pendidikan tertinggi yang ditamatkan, lulusan **Sekolah Menengah Kejuruan (SMK)** justru memiliki TPT yang tertinggi, yaitu **10,38%**. "
        "Padahal SMK yang merupakan sekolah vokasi seharusnya menciptakan lulusan yang siap kerja. "
        "Dikutip dari Bisnis.com, Ketua bidang Ketenagakerjaan Asosiasi Pengusaha Indonesia (Apindo) Antonius J. Supit mengatakan "
        "ada indikasi bahwa sistem SMK di Indonesia belum efektif. \"SMK ini sekolah vokasi, Kemendikbud harus mengevaluasi, "
        "apakah SMK ini sudah berjalan sesuai dengan sistem vokasi yang benar?,\" katanya.")

#Angkatan Kerja Berdasarkan Tingkat Pendidikan
ak = pd.read_csv("angkatan_kerja.csv")
ak['persen_pengangguran']=ak['pengangguran']/ak['jumlah_ak']*100
ak['persen_pengangguran']=ak['persen_pengangguran'].round(2)
ak. rename(columns = {'pengangguran':'Pengangguran', 'bekerja':'Bekerja'}, inplace = True)
fig_ak = px.bar(ak, x='pendidikan_tertinggi', y=['Bekerja','Pengangguran'], 
            title='Jumlah Angkatan Kerja Berdasarkan Tingkat Pendidikan (Februari 2022)',
            hover_data=['persen_bekerja','persen_pengangguran'],
            labels={'pendidikan_tertinggi':'Pendidikan Tertinggi yang Ditamatkan',
                    'value':'Jumlah Penduduk',
                    'variable':'Keterangan',
                    'persen_bekerja':'Persentase Bekerja',
                    'persen_pengangguran':'Persentase Pengangguran'})
fig_ak.update_layout(title_x=0.5)
st.plotly_chart(fig_ak,use_container_width=True)
st.caption('Sumber: Badan Pusat Statistik')

st.write("Setelah SMK, TPT tertinggi selanjutnya dipegang oleh lulusan **SMA (8,35%)** dan **Universitas (6,17%)**. "
        "Lulusan yang memiliki tingkat pendidikan yang lebih tinggi umumnya lebih memilih-milih dalam pekerjaan "
        "dibanding lulusan yang memiliki tingkat pendidikan yang lebih rendah. Di sisi lain, tingginya angka "
        "pengangguran menunjukkan bahwa sistem pendidikan di Indonesia belum sesuai dengan kebutuhan dunia kerja. "
        "Bahkan Menteri Pendidikan, Kebudayaan, Riset dan Teknologi Nadiem Makarim pernah menyatakan hanya ada maksimal **20%** "
        "lulusan mahasiswa yang bekerja sesuai dengan program studinya.")

#Konten 3
st.subheader("Gen Z Raja Era Digital")
st.write("Gen Z lahir dan hidup di era perkembangan teknologi. "
        "Di era digital, pekerjaan-pekerjaan konvensional akan hilang seiring waktu, "
        "tergantikan oleh robot dan sistem yang terotomatisasi. "
        "Meski demikian, akan muncul pekerjaan-pekerjaan baru yang belum pernah ada sebelumnya. "
        "Pekerjaan-pekerjaan baru ini umumnya memerlukan keterampilan digital yang baik, "
        "seperti analis dan saintis data, *artificial intelligence expert*, pengembang aplikasi dan game, "
        "*digital markerter*, *content creator*, dll."
        )

#Indeks Literasi Digital
ild = pd.read_csv('indeks_literasi_digital.csv')
ild.rename(columns={'rendah':'Rendah','tinggi':'Tinggi'}, inplace=True)
ild_fig=px.bar(ild, x=['Tinggi','Rendah'], y='generasi',
                title='Indeks Literasi Digital Berdasarkan Generasi (2021)',
                labels={'generasi':'Generasi',
                        'value':'Persentase',
                        'variable':'Indeks Literasi Digital'})
ild_fig.update_layout(title_x=0.5)
st.plotly_chart(ild_fig, use_container_width=True)
st.caption("Sumber: Kominfo dan Katadata Insight Center")

st.write("Berdasarkan riset yang dilakukan oleh Kemeneterian Komunikasi dan Informasi bersama Katadata Insight Center, "
        "proporsi Gen Z yang memiliki indeks literasi digital yang tinggi cukup besar, yaitu **59,7%**. "
        "Namun masih ada **40,3%** Gen Z yang memiliki indeks literasi digital yang rendah. "
        "Literasi digital dapat diartikan sebagai kemampuan untuk menemukan, membaca, mengevaluasi, menyintesis, "
        "menciptakan, mengadaptasi, dan menyebarkan informasi, media, dan teknologi. Dengan literasi digital yang tinggi, "
        "seharusnya Gen Z bisa mendapat kesempatan pekerjaan lebih baik di era digital saat ini.")

#Konten 4
st.subheader('Apa yang Bisa Dilakukan?')
st.write("Generasi Z yang menjadi penentu nasib Indonesia di masa bonus demografi harus dapat memanfaatkan kesempatan ini dengan baik. "
        "Kecakapan digital yang dimiliki Gen Z sebenarnya sudah sesuai dengan kebutuhan dunia kerja yang sedang berkembang saat ini. "
        "Meski demikian, belum semua Gen Z memiliki kecakapan digital yang baik. Peningkatan literasi digital perlu didorong oleh pemerintah "
        "dan perlu disadari oleh Gen Z itu sendiri dengan memanfaatkan fasilitas yang ada untuk meningkatkan kemampuan digitalnya. "
        "Pemerintah pun perlu mengupayakan peningkatan lapangan pekerjaan untuk mengurangi tingkat pengangguran terbuka yang didominasi oleh anak-anak muda. "
        "Selain itu, pemerintah juga mengevaluasi sistem pendidikan Indonesia agar sesuai dengan kebutuhan lapangan pekerjaan yang ada."
        )
