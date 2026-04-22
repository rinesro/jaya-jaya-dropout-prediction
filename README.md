# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institut

* **Nama**: Sandhika Hamzah  
* **Email**: sanvinzah@gmail.com  
* **Id Dicoding**: sandhika\_hamzah\_jvzn

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Meskipun memiliki reputasi yang sangat baik dan telah meluluskan banyak mahasiswa, institusi ini menghadapi tantangan besar berupa tingginya tingkat mahasiswa yang putus kuliah (dropout), yang saat ini mencapai angka 32,1% dari total populasi historis. Tingginya angka dropout ini berdampak negatif pada performa akademik institusi dan keberlanjutan operasional. Oleh karena itu, manajemen membutuhkan solusi berbasis data untuk mendeteksi dini mahasiswa yang berisiko dropout.


### Permasalahan Bisnis
1. Apa saja faktor-faktor utama (akademik, finansial, demografi) yang paling berkontribusi terhadap keputusan mahasiswa untuk dropout?
2. Bagaimana cara memprediksi kemungkinan seorang mahasiswa baru atau mahasiswa aktif akan dropout sedini mungkin agar pihak kampus dapat memberikan intervensi yang tepat?


### Cakupan Proyek
1. **Data Preparation & Exploratory Data Analysis (EDA):** Membersihkan dataset, menangani pemformatan tabel, dan mengeksplorasi wawasan (insight) awal.
2. **Business Dashboard:** Membangun dashboard interaktif menggunakan Metabase untuk memonitor profil siswa dan memvisualisasikan faktor penyebab dropout.
3. **Machine Learning Modeling:** Membangun, melatih, dan mengevaluasi model klasifikasi Random Forest untuk memprediksi status mahasiswa berdasarkan data historis.
4. **Deployment:** Mengembangkan prototipe aplikasi prediksi berbasis antarmuka web menggunakan Streamlit.

### Persiapan

Sumber data: Dataset Jaya Jaya Institut  yang mencakup informasi pendaftaran, latar belakang keluarga, kondisi finansial makro dan mikro, serta performa akademik di semester 1 dan 2.
[data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
# Clone repository proyek
git clone https://github.com/rinesro/jaya-jaya-dropout-prediction.git

# Masuk ke direktori proyek
cd hasil_akhir

# Instal semua library yang dibutuhkan
pip install -r requirements.txt


## Business Dashboard

Business Dashboard telah dibangun menggunakan **Metabase**. Berkas database Metabase untuk proyek ini dilampirkan dengan nama metabase.db.mv.db.
 
Dashboard ini menyoroti beberapa temuan kritis:

1. **Proporsi Status Siswa:** Menampilkan rasio keseluruhan siswa di mana 49.9% Graduate, 32.1% Dropout, dan 17.9% Enrolled.
2. **Faktor Demografi:** Mengidentifikasi bahwa lonjakan dropout sering terjadi pada rentang usia masuk (Age at Enrollment) sekitar 18-21 tahun.
3. **Faktor Akademik:** Melalui analisis histogram Curricular Units 1st & 2nd Sem Approved, terlihat jelas bahwa mahasiswa yang dropout rata-rata memiliki tingkat kelulusan mata kuliah yang sangat rendah (berkisar antara 0-5 unit) sejak semester pertama.
4. **Faktor Finansial (Paling Kritis):** Terdapat korelasi yang sangat kuat antara mahasiswa yang menunggak biaya kuliah (Tuition fees up to date = 0) dengan status dropout.

## Cara Menjalankan Dashboard Metabase secara Lokal


1. Tarik image Metabase versi 0.46.4:
   `docker pull metabase/metabase:v0.46.4`


2. Jalankan container Metabase:
   `docker run -d -p 3000:3000 --name metabase metabase/metabase:v0.46.4`


3. Copy file database Metabase yang sudah saya lampirkan (`metabase.db.mv.db`) ke dalam container:
   `docker cp metabase.db.mv.db metabase:/metabase.db/`


4. Buka browser dan akses `http://localhost:3000`

## Menjalankan Sistem Machine Learning

Prototipe sistem machine learning untuk mendeteksi risiko dropout telah dibuat menggunakan **Streamlit** dan dapat diakses secara publik lewat Streamlit Community Cloud.

**Link Prototype Streamlit:** https://jaya-jaya-dropout-prediction-pcnvle44o7pykccsdapptvp.streamlit.app/

Jika ingin menjalankan prototype secara lokal, gunakan perintah berikut di terminal:
streamlit run app.py


Aplikasi akan secara otomatis terbuka di browser pada alamat http://localhost:8501.


## Conclusion
Berdasarkan analisis Metabase dan permodelan Machine Learning, dapat ditarik kesimpulan bahwa:
1. **Masalah Finansial adalah Pemicu Utama:** Ketidakmampuan membayar biaya kuliah tepat waktu (Tuition fees not up to date) adalah indikator non-akademik terkuat yang menyebabkan mahasiswa berhenti kuliah di Jaya Jaya Institut.
2. **Sinyal Peringatan Akademik Sejak Semester 1:** Performa mahasiswa yang buruk pada semester pertama (gagal lulus di sebagian besar unit mata kuliah) hampir selalu berujung pada dropout di semester berikutnya.
3. **Model Machine Learning yang Efektif:** Model Random Forest yang dibangun telah terbukti mampu memprediksi status dropout mahasiswa berdasarkan kombinasi 37 fitur demografi, akademik, dan finansial, sehingga sangat layak dijadikan alat deteksi dini oleh manajemen.


### Rekomendasi Action Items
Untuk menekan angka dropout, Jaya Jaya Institut direkomendasikan untuk melakukan tindakan preventif berikut:
- **Program Bantuan/Restrukturisasi Finansial:** Membangun sistem peringatan (alert) otomatis bagi mahasiswa yang mulai menunggak biaya kuliah di pertengahan semester, lalu menawarkan opsi cicilan atau beasiswa bantuan sebelum mereka memutuskan dropout.
- **Intervensi Akademik Dini:** Mengaktifkan peran Dosen Pembimbing Akademik untuk wajib memanggil dan membimbing mahasiswa yang gagal meluluskan lebih dari 2 SKS/Unit pada **Semester 1**, tanpa harus menunggu evaluasi di akhir tahun ajaran.
- **Implementasi Prototipe AI:** Mengintegrasikan dashboard dan prototipe prediksi Streamlit yang telah dibuat ke dalam alur kerja staf kemahasiswaan agar deteksi mahasiswa berisiko tinggi (high-risk) dapat dilakukan sejak awal masa pendaftaran.

