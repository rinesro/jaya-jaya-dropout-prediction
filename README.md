# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institut

* **Nama**: Sandhika Hamzah  
* **Email**: sanvinzah@gmail.com  
* **Id Dicoding**: sandhika\_hamzah\_jvzn

## Business Understanding

Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Meskipun memiliki reputasi yang sangat baik dan telah meluluskan banyak mahasiswa, institusi ini menghadapi tantangan besar berupa tingginya tingkat mahasiswa yang putus kuliah (dropout), yang saat ini mencapai angka 32,1% dari total populasi historis.


### Permasalahan Bisnis

Tingginya angka *dropout* ini bukan sekadar metrik akademik yang buruk, melainkan **ancaman serius terhadap stabilitas finansial dan reputasi institusi**. Jika permasalahan ini tidak segera diselesaikan, Jaya Jaya Institut akan menghadapi risiko jangka panjang berupa:
1. **Kehilangan Pendapatan Berkelanjutan:** Setiap mahasiswa yang *dropout* berarti berhentinya arus kas dari pembayaran uang kuliah (*tuition fees*) di semester-semester berikutnya, yang berdampak langsung pada ketahanan operasional dan *cash flow* kampus.
2. **Penurunan Reputasi dan Daya Saing:** Rasio kelulusan yang rendah akan menjadi catatan buruk bagi institusi. Hal ini akan membuat calon mahasiswa baru ragu untuk mendaftar, sehingga kampus kalah saing di industri Edutech.
3. **Inefisiensi Alokasi Sumber Daya:** Fasilitas, laboratorium, dan tenaga pengajar yang sudah dialokasikan dari awal menjadi tidak optimal karena kapasitas kelas perlahan kosong di pertengahan masa studi.


### Cakupan Proyek

1.**Data Preparation & Exploratory Data Analysis (EDA):** Membersihkan dataset dan mengeksplorasi wawasan (*insight*) mendalam terkait faktor yang paling mempengaruhi *dropout* melalui analisis *univariate* dan *bivariate*.
2. **Business Dashboard:** Membangun *dashboard* interaktif menggunakan Metabase untuk memonitor profil siswa secara *real-time* dengan label data yang sudah dikategorikan.
3. **Machine Learning Modeling:** Membangun, melatih, dan mengevaluasi performa model klasifikasi (*Random Forest*) untuk memprediksi status mahasiswa berdasarkan pola historis.
4. **Deployment:** Membangun prototipe antarmuka prediksi (*Machine Learning*) yang ramah pengguna (*user-friendly*) menggunakan Streamlit.

### Persiapan

Sumber data: Dataset Jaya Jaya Institut  yang mencakup informasi pendaftaran, latar belakang keluarga, kondisi finansial makro dan mikro, serta performa akademik di semester 1 dan 2.
[data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
Untuk menjalankan proyek ini, pastikan Anda menggunakan lingkungan virtual (*Virtual Environment*) agar dependensi proyek tetap terisolasi, stabil, dan tidak konflik dengan proyek lain di komputer Anda. Berikut adalah instruksinya:

**Opsi 1: Setup Environment - Anaconda (Direkomendasikan)**
```bash
# Membuat virtual environment baru bernama 'main-ds' dengan Python 3.9
conda create --name main-ds python=3.9

# Mengaktifkan virtual environment
conda activate main-ds

# Menginstal semua dependensi yang dibutuhkan secara otomatis melalui requirements.txt
pip install -r requirements.txt
```
**Opsi 2: Setup Environment - Shell/Terminal**
```bash
# Membuat virtual environment bernama 'env'
python -m venv env

# Mengaktifkan virtual environment (Untuk Windows)
env\Scripts\activate
# ATAU Mengaktifkan virtual environment (Untuk Mac/Linux)
source env/bin/activate

# Menginstal semua dependensi yang dibutuhkan secara otomatis melalui requirements.txt
pip install -r requirements.txt
```
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


*Catatan:* Perintah di atas akan mengeksekusi file utama app.py. Server lokal akan berjalan dan aplikasi antarmuka web akan otomatis terbuka di browser pada alamat http://localhost:8501.

## Conclusion
Berdasarkan analisis Metabase dan permodelan Machine Learning, dapat ditarik kesimpulan bahwa:
1. **Insight Utama (Mengapa Siswa Dropout?):** Faktor paling dominan penyebab dropout adalah masalah finansial. Data menunjukkan bahwa kelompok siswa yang menunggak biaya kuliah (*Tuition fees not up to date*) hampir seluruhnya berakhir dengan *dropout*. Hal ini memberikan insight bahwa kegagalan melanjutkan kuliah seringkali bukan karena kurangnya kemampuan akademik, melainkan faktor ekonomi keluarga yang memaksa siswa harus berhenti.
Selain itu, kegagalan meluluskan SKS yang parah sejak Semester 1 dan 2 menunjukkan adanya culture shock atau kegagalan adaptasi akademik di tahun pertama kuliah yang tidak terdeteksi sejak awal oleh dosen pembimbing.
2. **Performa Model & Fitur Terpenting:** Model **Random Forest** yang digunakan telah dievaluasi dan menunjukkan performa klasifikasi yang sangat baik. Model ini sangat tangguh dalam metrik *Recall*, yang artinya model berhasil meminimalisir angka *False Negative* (meminimalisir kasus berbahaya di mana siswa yang aslinya *dropout*, tetapi diprediksi aman/lulus oleh sistem).
Berdasarkan hasil analisis *Feature Importance*, tiga (3) fitur yang paling berpengaruh bagi model dalam menentukan prediksi *dropout* adalah:
* Curricular_units_2nd_sem_approved (Jumlah SKS yang diluluskan di semester 2)

* Curricular_units_1st_sem_approved (Jumlah SKS yang diluluskan di semester 1)

* Tuition_fees_up_to_date (Status pelunasan biaya kuliah)


### Rekomendasi Action Items
Untuk menyelesaikan urgensi bisnis di atas, manajemen Jaya Jaya Institut direkomendasikan melakukan tindakan berikut:
- **Sistem Peringatan Dini Finansial:** Mengimplementasikan sistem *alert* bagi staf keuangan ketika ada mahasiswa yang belum melunasi tagihan di pertengahan semester. Kampus dapat proaktif memanggil mahasiswa tersebut untuk menawarkan opsi restrukturisasi cicilan atau beasiswa bantuan agar mereka tidak perlu *dropout*.
- **Intervensi Akademik Tahun Pertama:** Mewajibkan Dosen Pembimbing Akademik (DPA) untuk melakukan pemanggilan khusus kepada mahasiswa yang gagal meluluskan lebih dari 2 SKS pada Semester 1, guna memberikan bimbingan belajar intensif sebelum masuk ke Semester 2.
- **Pemanfaatan Prototipe:** Mengintegrasikan prototipe Streamlit yang ada ke portal registrasi, sehingga staf kemahasiswaan bisa mengecek "Skor Risiko" mahasiswa secara mandiri dan cepat setiap awal semester baru.

