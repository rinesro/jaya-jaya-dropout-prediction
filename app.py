import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Jaya Jaya Institut - Dropout Prediction", layout="wide")

try:
    model = joblib.load('rf_model.joblib')
    scaler = joblib.load('scaler.joblib')
except FileNotFoundError:
    st.error("File model atau scaler tidak ditemukan! Pastikan file berada di folder yang sama.")

marital_status_mapping = {
    "Belum Menikah": 1,
    "Menikah": 2,
    "Duda / Janda": 3,
    "Bercerai": 4,
    "Tinggal Bersama (Facto Union)": 5,
    "Berpisah Secara Sah": 6
}

gender_mapping = {
    "Perempuan": 0,
    "Laki-laki": 1
}

tuition_mapping = {
    "Menunggak": 0,
    "Lunas": 1
}

mapping_yes_no = {'Tidak': 0, 'Ya': 1}
mapping_daytime = {'Siang (Daytime)': 1, 'Malam (Evening)': 0}

education_mapping = {
    "Pendidikan Menengah Atas (SMA/SMK/Sederajat)": 1,
    "Pendidikan Tinggi (Sarjana/S1)": 2,
    "Pendidikan Tinggi (Magister/Doktor/S2/S3)": 3,
    "Pendidikan Dasar (SD/Sederajat)": 37,
    "Pendidikan Menengah Pertama (SMP/Sederajat)": 38,
    "Lainnya": 19
}

st.title('🎓 Jaya Jaya Institut: Dropout Prediction Prototype')
st.markdown("Aplikasi ini membantu staf akademik mendeteksi dini mahasiswa yang berisiko putus kuliah berdasarkan data historis.")
st.header('Form Data Mahasiswa')

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Data Demografi")
    marital_status_label = st.selectbox('Status Pernikahan', list(marital_status_mapping.keys()))
    gender_label = st.selectbox('Jenis Kelamin', list(gender_mapping.keys()))
    displaced_label = st.selectbox('Orang Terlantar (Displaced)', list(mapping_yes_no.keys()))
    international_label = st.selectbox('Mahasiswa Internasional', list(mapping_yes_no.keys()))
    educational_special_needs_label = st.selectbox('Kebutuhan Khusus Pendidikan', list(mapping_yes_no.keys()))
    age_at_enrollment = st.number_input('Usia saat Mendaftar', min_value=15, max_value=100, value=20)
    
    nacionality = st.number_input('Kode Kewarganegaraan', value=1)
    
    mothers_qualification_label = st.selectbox('Pendidikan Terakhir Ibu', list(education_mapping.keys()))
    fathers_qualification_label = st.selectbox('Pendidikan Terakhir Ayah', list(education_mapping.keys()))
    
    mothers_occupation = st.number_input('Pekerjaan Ibu (Kode)', value=1)
    fathers_occupation = st.number_input('Pekerjaan Ayah (Kode)', value=1)

with col2:
    st.subheader("Data Pendaftaran & Keuangan")
    daytime_evening_label = st.selectbox('Waktu Kuliah', list(mapping_daytime.keys()))
    debtor_label = st.selectbox('Memiliki Hutang Kuliah (Debtor)?', list(mapping_yes_no.keys()))
    tuition_fees_label = st.selectbox('Biaya Kuliah Lunas?', list(tuition_mapping.keys()))
    scholarship_label = st.selectbox('Penerima Beasiswa?', list(mapping_yes_no.keys()))
    
    application_mode = st.number_input('Mode Aplikasi (Kode)', value=1)
    application_order = st.number_input('Urutan Aplikasi', value=1)
    course = st.number_input('Program Studi (Kode)', value=171)
    previous_qualification = st.number_input('Kualifikasi Sebelumnya (Kode)', value=1)
    previous_qualification_grade = st.number_input('Nilai Kualifikasi Sebelumnya', value=120.0)
    admission_grade = st.number_input('Nilai Masuk (Admission Grade)', value=120.0)

with col3:
    st.subheader("Performa Akademik & Makroekonomi")
    cu_1st_sem_credited = st.number_input('SKS Sem 1 - Diakui', value=0)
    cu_1st_sem_enrolled = st.number_input('SKS Sem 1 - Diambil', value=6)
    cu_1st_sem_evaluations = st.number_input('SKS Sem 1 - Dievaluasi', value=6)
    cu_1st_sem_approved = st.number_input('SKS Sem 1 - Lulus', value=6)
    cu_1st_sem_grade = st.number_input('Nilai Rata-rata Sem 1', value=12.0)
    cu_1st_sem_without_eval = st.number_input('SKS Sem 1 - Tanpa Evaluasi', value=0)
    
    cu_2nd_sem_credited = st.number_input('SKS Sem 2 - Diakui', value=0)
    cu_2nd_sem_enrolled = st.number_input('SKS Sem 2 - Diambil', value=6)
    cu_2nd_sem_evaluations = st.number_input('SKS Sem 2 - Dievaluasi', value=6)
    cu_2nd_sem_approved = st.number_input('SKS Sem 2 - Lulus', value=6)
    cu_2nd_sem_grade = st.number_input('Nilai Rata-rata Sem 2', value=12.0)
    cu_2nd_sem_without_eval = st.number_input('SKS Sem 2 - Tanpa Evaluasi', value=0)
    
    unemployment_rate = st.number_input('Tingkat Pengangguran (%)', value=10.8)
    inflation_rate = st.number_input('Tingkat Inflasi (%)', value=1.4)
    gdp = st.number_input('GDP', value=1.74)

if st.button('Prediksi Status Mahasiswa', type='primary'):
    
    input_data = pd.DataFrame({
        'Marital_status': [marital_status_mapping[marital_status_label]],
        'Application_mode': [application_mode],
        'Application_order': [application_order],
        'Course': [course],
        'Daytime_evening_attendance': [mapping_daytime[daytime_evening_label]],
        'Previous_qualification': [previous_qualification],
        'Previous_qualification_grade': [previous_qualification_grade],
        'Nacionality': [nacionality],
        'Mothers_qualification': [education_mapping[mothers_qualification_label]],
        'Fathers_qualification': [education_mapping[fathers_qualification_label]],
        'Mothers_occupation': [mothers_occupation],
        'Fathers_occupation': [fathers_occupation],
        'Admission_grade': [admission_grade],
        'Displaced': [mapping_yes_no[displaced_label]],
        'Educational_special_needs': [mapping_yes_no[educational_special_needs_label]],
        'Debtor': [mapping_yes_no[debtor_label]],
        'Tuition_fees_up_to_date': [tuition_mapping[tuition_fees_label]],
        'Gender': [gender_mapping[gender_label]],
        'Scholarship_holder': [mapping_yes_no[scholarship_label]],
        'Age_at_enrollment': [age_at_enrollment],
        'International': [mapping_yes_no[international_label]],
        'Curricular_units_1st_sem_credited': [cu_1st_sem_credited],
        'Curricular_units_1st_sem_enrolled': [cu_1st_sem_enrolled],
        'Curricular_units_1st_sem_evaluations': [cu_1st_sem_evaluations],
        'Curricular_units_1st_sem_approved': [cu_1st_sem_approved],
        'Curricular_units_1st_sem_grade': [cu_1st_sem_grade],
        'Curricular_units_1st_sem_without_evaluations': [cu_1st_sem_without_eval],
        'Curricular_units_2nd_sem_credited': [cu_2nd_sem_credited],
        'Curricular_units_2nd_sem_enrolled': [cu_2nd_sem_enrolled],
        'Curricular_units_2nd_sem_evaluations': [cu_2nd_sem_evaluations],
        'Curricular_units_2nd_sem_approved': [cu_2nd_sem_approved],
        'Curricular_units_2nd_sem_grade': [cu_2nd_sem_grade],
        'Curricular_units_2nd_sem_without_evaluations': [cu_2nd_sem_without_eval],
        'Unemployment_rate': [unemployment_rate],
        'Inflation_rate': [inflation_rate],
        'GDP': [gdp]
    })

    try:
        input_data_scaled = scaler.transform(input_data)
        prediksi = model.predict(input_data_scaled)
        
        st.markdown("---")
        if prediksi[0] == 1:
            st.error('⚠️ **PREDIKSI: MAHASISWA BERISIKO TINGGI DROPOUT**')
            st.write('Tindakan Disarankan: Segera lakukan pemanggilan untuk bimbingan akademik/finansial.')
        else:
            st.success('✅ **PREDIKSI: MAHASISWA AKAN LULUS (GRADUATE)**')
            st.write('Tindakan Disarankan: Tidak ada tindakan khusus, mahasiswa dalam jalur yang aman.')
            
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses data: {e}")
