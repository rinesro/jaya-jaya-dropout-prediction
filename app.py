import streamlit as st
import pandas as pd
import joblib

try:
    model = joblib.load('./model/rf_model.joblib')
    scaler = joblib.load('./model/scaler.joblib')
except FileNotFoundError:
    st.error("File model atau scaler tidak ditemukan! Pastikan 'rf_model.joblib' dan 'scaler.joblib' ada di direktori yang sama.")

st.title('🎓 Jaya Jaya Institut: Dropout Prediction Prototype')
st.write('Masukkan data historis dan akademik mahasiswa untuk memprediksi potensi dropout.')

st.header('Form Data Mahasiswa')

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Data Demografi & Latar Belakang")
    marital_status = st.selectbox('Marital Status', [1, 2, 3, 4, 5, 6])
    nacionality = st.number_input('Nacionality', value=1)
    displaced = st.selectbox('Displaced', [0, 1])
    gender = st.selectbox('Gender', [0, 1])
    age_at_enrollment = st.number_input('Age at enrollment', min_value=15, max_value=100, value=20)
    international = st.selectbox('International', [0, 1])
    mothers_qualification = st.number_input('Mothers qualification', value=1)
    fathers_qualification = st.number_input('Fathers qualification', value=1)
    mothers_occupation = st.number_input('Mothers occupation', value=1)
    fathers_occupation = st.number_input('Fathers occupation', value=1)
    educational_special_needs = st.selectbox('Educational special needs', [0, 1])

with col2:
    st.subheader("Data Akademik (Pendaftaran)")
    application_mode = st.number_input('Application mode', value=1)
    application_order = st.number_input('Application order', value=1)
    course = st.number_input('Course', value=171)
    daytime_evening_attendance = st.selectbox('Daytime/evening attendance', [0, 1])
    previous_qualification = st.number_input('Previous qualification', value=1)
    previous_qualification_grade = st.number_input('Previous qualification grade', value=120.0)
    admission_grade = st.number_input('Admission grade', value=120.0)
    debtor = st.selectbox('Debtor', [0, 1])
    tuition_fees_up_to_date = st.selectbox('Tuition fees up to date', [0, 1])
    scholarship_holder = st.selectbox('Scholarship holder', [0, 1])

with col3:
    st.subheader("Data Akademik (Semester 1 & 2)")
    cu_1st_sem_credited = st.number_input('CU 1st sem credited', value=0)
    cu_1st_sem_enrolled = st.number_input('CU 1st sem enrolled', value=6)
    cu_1st_sem_evaluations = st.number_input('CU 1st sem evaluations', value=6)
    cu_1st_sem_approved = st.number_input('CU 1st sem approved', value=6)
    cu_1st_sem_grade = st.number_input('CU 1st sem grade', value=12.0)
    cu_1st_sem_without_eval = st.number_input('CU 1st sem without eval', value=0)
    
    cu_2nd_sem_credited = st.number_input('CU 2nd sem credited', value=0)
    cu_2nd_sem_enrolled = st.number_input('CU 2nd sem enrolled', value=6)
    cu_2nd_sem_evaluations = st.number_input('CU 2nd sem evaluations', value=6)
    cu_2nd_sem_approved = st.number_input('CU 2nd sem approved', value=6)
    cu_2nd_sem_grade = st.number_input('CU 2nd sem grade', value=12.0)
    cu_2nd_sem_without_eval = st.number_input('CU 2nd sem without eval', value=0)
    
    st.subheader("Faktor Makroekonomi")
    unemployment_rate = st.number_input('Unemployment rate', value=10.8)
    inflation_rate = st.number_input('Inflation rate', value=1.4)
    gdp = st.number_input('GDP', value=1.74)

if st.button('Prediksi Status Mahasiswa'):
    input_data = pd.DataFrame({
        'Marital_status': [marital_status],
        'Application_mode': [application_mode],
        'Application_order': [application_order],
        'Course': [course],
        'Daytime_evening_attendance': [daytime_evening_attendance],
        'Previous_qualification': [previous_qualification],
        'Previous_qualification_grade': [previous_qualification_grade],
        'Nacionality': [nacionality],
        'Mothers_qualification': [mothers_qualification],
        'Fathers_qualification': [fathers_qualification],
        'Mothers_occupation': [mothers_occupation],
        'Fathers_occupation': [fathers_occupation],
        'Admission_grade': [admission_grade],
        'Displaced': [displaced],
        'Educational_special_needs': [educational_special_needs],
        'Debtor': [debtor],
        'Tuition_fees_up_to_date': [tuition_fees_up_to_date],
        'Gender': [gender],
        'Scholarship_holder': [scholarship_holder],
        'Age_at_enrollment': [age_at_enrollment],
        'International': [international],
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
        
        # c. Lakukan Prediksi
        prediksi = model.predict(input_data_scaled)
        
        # d. Tampilkan Hasil
        st.markdown("---")
        st.subheader("Hasil Prediksi:")
        if prediksi[0] == 1:
            st.error('⚠️ **Status: DROPOUT**')
            st.write('Mahasiswa ini berisiko tinggi untuk tidak menyelesaikan pendidikan. Disarankan pihak akademik segera melakukan bimbingan preventif.')
        else:
            st.success('✅ **Status: GRADUATE**')
            st.write('Mahasiswa ini diprediksi akan menyelesaikan pendidikannya dengan baik.')
            
    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")