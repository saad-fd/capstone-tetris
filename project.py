from matplotlib.style import use
import streamlit as st
import pandas as pd
import plotly.express as px

#Setting Page
st.set_page_config(layout="centered")

#Sidebar
with st.sidebar:
        st.write("**Opsi Diagram**")

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

#KONTEN 1: Seberapa Penting Gen Z
st.subheader("Seberapa Penting Gen Z bagi Indonesia?")
col1_1, col1_2 = st.columns([1,2])
with col1_1:
    #Pargaraf 1: Gen Z    
    st.write("Generasi Z atau biasa disingkat Gen Z merupakan generasi yang lahir pada rentang tahun 1997-2012.",
            "Berdasarkan sensus penduduk pada tahun 2020, Gen Z mendominasi jumlah penduduk Indonesia dengan total populasi **74,93 juta jiwa (27,93%)**.",
            "Belum semua Gen Z berada pada kelompok penduduk usia produktif. Umur Gen Z saat ini masih berada pada rentang 10-25 tahun. ",
            "Sebagian besar masih mengenyam bangku sekolah dan universitas. Namun sekitar enam tahun lagi, seluruh Gen Z akan mencapai usia produktifnya.")
with col1_2:
    #Diagram 1: Jumlah Penduduk Berdasarkan Generasi
    gen = pd.read_csv('generasi.csv')
    fig_gen=px.pie(gen, values='jumlah_penduduk', names='generasi',
        title='Jumlah Penduduk Berdasarkan Generasi (2020)', 
        labels={'jumlah_penduduk':'Jumlah Penduduk (juta jiwa)',
                    'generasi':'Generasi'})
    fig_gen.update_layout(title_x=0.5)
    st.plotly_chart(fig_gen, use_container_width=True)
    st.caption('Sumber: Badan Pusat Statistik')

#--Opsi Diagram 2
with st.sidebar:
        radio1 = st.radio(label='Proyeksi Jumlah Penduduk', options=('Persen','Jumlah'), horizontal=True)
        if radio1 == 'Persen':
                groupnorm = 'percent'
                ylabel= 'Persentase Penduduk'
        else:
                groupnorm = ''
                ylabel='Jumlah Penduduk (ribu jiwa)'

#Diagram 2: Proyeksi Jumlah Penduduk 2015-2045
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

#Paragraf 2: Bonus Demografi
st.write("Berdasarkan Analisis Profil Penduduk Indonesia yang dilakukan oleh Badan Pusat Statistik (BPS), "
            "Indonesia telah mengalami bonus demografi sejak 2012 dan puncaknya diperkirakan terjadi pada periode 2020-2030. "
            "Bonus demografi dinilai dapat meningkatkan perekonomian suatu negara, seperti yang terjadi di Tiongkok, Korea Selatan, Jepang, dll. "
            "Dengan besarnya populasi Gen Z di masa bonus demografi, peran Gen Z sangat signifikan dalam menentukan nasib bangsa Indonesia.")

#KONTEN 2: Realita
st.subheader("Realita yang Dihadapi")
#Paragraf 3: Pengangguran Usia Muda
st.write("Sebagian pemuda di *Citayam Fashion Week* merupakan anak-anak yang telah putus sekolah dan pengangguran. Begitu pulalah kenyataan pahit yang dialami Gen Z saat ini. ",
        "Memiliki persentase jumlah penduduk terbesar, ironisnya jumlah pengangguran terbesar pun didominasi oleh Gen Z. "
        "Penduduk usia muda (15-24 tahun) mendominasi tingkat pengangguran terbuka (TPT) sebesar **43,3% (3,64 juta jiwa)** pada bulan Februari 2022. " 
        "Peningkatan jumlah angkatan kerja tidak sebanding dengan kesempatan kerja yang tersedia, terlebih jika harus sesuai dengan bidang keahliannya. "
        "Selain itu, banyak perusahaan yang mensyaratkan pengalaman kerja bagi pelamar. Padahal sebagian besar penganggur muda belum memiliki pekerjaan sebelumnya.")

#Diagram 3: Angkatan Kerja Berdasarkan Umur
tpt = pd.read_csv('pengangguran_umur.csv')
tpt = tpt.sort_values('kelompok_umur')
fig_tpt = px.bar(tpt,x='kelompok_umur',y='jumlah', 
                title='Jumlah Pengangguran Berdasarkan Kelompok Umur (Februari 2022)',
                labels={'kelompok_umur':'Kelompok Umur',
                            'jumlah':'Jumlah Pengangguran'})
fig_tpt.update_layout(title_x=0.5)
st.plotly_chart(fig_tpt, use_container_width=True)
st.caption('Sumber: Badan Pusat Statistik')

#Paragraf 4: Pengangguran Tertinggi Berdasarkan Pendidikan
st.write("Berdasarkan tingkat pendidikan tertinggi yang ditamatkan, lulusan **Sekolah Menengah Kejuruan (SMK)** justru memiliki TPT yang tertinggi, yaitu **10,38%**. "
        "Padahal SMK yang merupakan sekolah vokasi seharusnya menciptakan lulusan yang siap kerja. "
        "Dikutip dari Bisnis.com, Ketua bidang Ketenagakerjaan Asosiasi Pengusaha Indonesia (Apindo) Antonius J. Supit mengatakan "
        "ada indikasi bahwa sistem SMK di Indonesia belum efektif. \"SMK ini sekolah vokasi, Kemendikbud harus mengevaluasi, "
        "apakah SMK ini sudah berjalan sesuai dengan sistem vokasi yang benar?,\" katanya.")

#--Opsi Diagram 4
with st.sidebar:
        radio2 = st.radio(label='Tingkat Pengangguran Terbuka', options=('Persen','Jumlah'), horizontal=True)
        if radio2 == 'Persen':
                column1,column2 = 'persen_bekerja','persen_pengangguran'
                hover_list=['bekerja','pengangguran']
                value = 'Persentase'
        else:
                column1,column2 = 'bekerja','pengangguran'
                hover_list=['persen_bekerja','persen_pengangguran']
                value='Jumlah'

#Diagram 4: Angkatan Kerja Berdasarkan Tingkat Pendidikan
ak = pd.read_csv("angkatan_kerja.csv")
ak['persen_pengangguran']=ak['pengangguran']/ak['jumlah_ak']*100
ak['persen_pengangguran']=ak['persen_pengangguran'].round(2)
ak.rename(columns = {column1:'Bekerja', column2:'Pengangguran'}, inplace = True)
fig_ak = px.bar(ak, x='pendidikan_tertinggi', y=['Bekerja','Pengangguran'],
            title='Angkatan Kerja Berdasarkan Tingkat Pendidikan (Februari 2022)',
            hover_data=hover_list,
            labels={'pendidikan_tertinggi':'Pendidikan Tertinggi yang Ditamatkan',
                    'value':value,
                    'variable':'Keterangan',
                    'persen_bekerja':'Persentase Bekerja',
                    'persen_pengangguran':'Persentase Pengangguran',
                    'bekerja':'Jumlah Bekerja',
                    'pengangguran':'Jumlah Pengangguran'
                    })
fig_ak.update_layout(title_x=0.5)
st.plotly_chart(fig_ak,use_container_width=True)
st.caption('Sumber: Badan Pusat Statistik')

#Paragraf 5: Pengangguran Tertinggi Berdasarkan Pendidikan 2
st.write("Setelah SMK, TPT tertinggi selanjutnya dipegang oleh lulusan **SMA (8,35%)** dan **Universitas (6,17%)**. "
        "Lulusan yang memiliki tingkat pendidikan yang lebih tinggi umumnya lebih memilih-milih dalam pekerjaan "
        "dibanding lulusan yang memiliki tingkat pendidikan yang lebih rendah. Di sisi lain, tingginya angka "
        "pengangguran menunjukkan bahwa sistem pendidikan di Indonesia belum sesuai dengan kebutuhan dunia kerja. "
        "Bahkan Menteri Pendidikan, Kebudayaan, Riset dan Teknologi Nadiem Makarim pernah menyatakan hanya ada maksimal **20%** "
        "lulusan mahasiswa yang bekerja sesuai dengan program studinya.")

#KONTEN 3: Persaingan Gen Z di Era Digital
st.subheader("Apakah Gen Z Mampu Bersaing?")
#Paragraf 6: Pekerjaan di Era Digital
st.write("Para pemuda *Citayam Fashion Week* memanfaatkan media sosial Tiktok untuk membuat konten-konten video pendek. ",
        "Harapannya tentu saja agar mereka bisa menjadi viral dan mendapatkan penghasilan dari konten tersebut. ",
        "Dengan cara yang kreatif, mereka mencoba memanfaatkan teknologi digital menjadi sesuatu yang menghasilkan keuntungan. ",
        "Gen Z lahir dan hidup di era perkembangan teknologi. "
        "Di era digital, pekerjaan-pekerjaan konvensional akan hilang seiring waktu, "
        "tergantikan oleh robot dan sistem yang terotomatisasi. "
        "Meski demikian, akan muncul pekerjaan-pekerjaan baru yang belum pernah ada sebelumnya. "
        "Pekerjaan-pekerjaan baru ini umumnya memerlukan keterampilan digital yang baik, "
        "seperti analis dan saintis data, *artificial intelligence expert*, pengembang aplikasi dan game, "
        "*digital markerter*, *content creator*, dll."
        )

#Visualisasi Diagram 5 dan 6
tab1, tab2= st.tabs(["10 Keahlian Teratas (Diagram Batang)", 
                "Penetrasi Keahlian per Tahun (Diagram Garis)"])
sp = pd.read_csv('skill_penetration.csv')

#--Opsi Diagram 5
with st.sidebar:
        st.write(" ")
        st.write("**Penetrasi Keahlian**")
        option = st.selectbox("Pilih Tahun (Diagram Batang)", 
                (2015,2016,2017,2018,2019,'Rata-Rata'))
#Diagram 5: Penetrasi Keahlian Tertinggi
with tab1:
        sp_pivot = pd.pivot_table(sp, values='skill_group_penetration_rate', 
                                index='skill_group_name', columns='year', 
                                aggfunc='mean', sort=True)
        sp_pivot['Rata-Rata']=sp_pivot.mean(axis=1)
        sp_pivot = sp_pivot.reset_index().sort_values(by=option, axis=0, ascending=False)
        sp_pivot_top10=sp_pivot.iloc[0:10,:]
        

        sp_pivot_fig = px.bar(sp_pivot_top10, x='skill_group_name', y=option,
                                title='10 Kelompok Keahlian Teratas '+str(option),
                                labels={
                                        option: 'Penetrasi Keahlian',
                                        'skill_group_name':'Kelompok Keahlian'
                                }
                                )
        st.plotly_chart(sp_pivot_fig, use_container_width=True)
        st.caption('Sumber: World Bank dan LinkedIn')

#--Opsi Diagram 6
with st.sidebar:
        keahlian = list(sp_pivot['skill_group_name'])
        options = st.multiselect("Pilih Keahlian (Diagram Garis)", 
                                keahlian, ['Digital Literacy'])
#Diagram 6:Penetrasi Keahlian Per Tahun
with tab2:
        sp_gb=sp.groupby(by=['skill_group_name','year']).mean()
        sp_gb=sp_gb.reset_index()
        sp_gb_filter=sp_gb[sp_gb.skill_group_name.isin(options)]
        sp_gb_line = px.line(sp_gb_filter, x='year', y = 'skill_group_penetration_rate',color='skill_group_name',
                                title='Penetrasi Keahlian per Tahun',
                                labels={
                                        'skill_group_name':'Kelompok Keahlian',
                                        'skill_group_penetration_rate':'Penetrasi Keahlian',
                                        'year':'Tahun'})
        st.plotly_chart(sp_gb_line, use_container_width=True)
        st.caption('Sumber: World Bank dan LinkedIn')

#Paragraf 7: Kecakapan Digital
st.write("Berdasarkan data penetrasi keahlian dari World Bank dan LinkedIn, pekerjaan-pekerjaan yang membutuhkan keahlian "
        "literasi digital selalu mendominasi sejak tahun 2015 hinga 2019. Hal ini menunjukkan bahwa kecakapan digital "
        "berperan sangat penting dalam dunia kerja saat ini. Oleh karena itu, literasi digital yang baik sangat diperlukan "
        "bagi siapapun agar mampu bersaing di dunia kerja.")

#Diagram 7: Indeks Literasi Digital
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

#Paragraf 8: Indeks Literasi Digital Gen Z
st.write("Berdasarkan riset yang dilakukan oleh Kemeneterian Komunikasi dan Informasi bersama Katadata Insight Center, "
        "proporsi Gen Z yang memiliki indeks literasi digital yang tinggi cukup besar, yaitu **59,7%**. "
        "Namun masih ada **40,3%** Gen Z yang memiliki indeks literasi digital yang rendah. "
        "Literasi digital dapat diartikan sebagai kemampuan untuk menemukan, membaca, mengevaluasi, menyintesis, "
        "menciptakan, mengadaptasi, dan menyebarkan informasi, media, dan teknologi. Dengan literasi digital yang tinggi, "
        "seharusnya Gen Z bisa mendapat kesempatan pekerjaan lebih baik di era digital saat ini.")

#KONTEN 4: Kesimpulan dan Saran
st.subheader('Apa yang Bisa Dilakukan?')
#Paragraf 9: Kesimpulan dan Saran
st.write("Generasi Z yang menjadi penentu nasib Indonesia di masa bonus demografi harus dapat memanfaatkan kesempatan ini dengan baik. "
        "Kecakapan digital yang dimiliki Gen Z sebenarnya sudah sesuai dengan kebutuhan dunia kerja yang sedang berkembang saat ini. "
        "Meski demikian, belum semua Gen Z memiliki kecakapan digital yang baik. Oleh karena itu, terdapat hal-hal yang perlu dilakukan/diperbaiki. ")
st.markdown("- Peningkatan literasi digital perlu didorong oleh pemerintah dan perlu disadari oleh Gen Z itu sendiri dengan memanfaatkan fasilitas yang ada untuk meningkatkan kemampuan digitalnya.")
st.markdown("- Pemerintah pun perlu mengupayakan peningkatan lapangan pekerjaan untuk mengurangi tingkat pengangguran terbuka yang didominasi oleh anak-anak muda. ")
st.markdown("- Pemerintah juga mengevaluasi sistem pendidikan Indonesia agar sesuai dengan kebutuhan lapangan pekerjaan yang ada.")
