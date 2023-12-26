import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

heart_model = pickle.load(open('heart_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson\'s Prediction'],
                           icons=['activity','heart','person'],
                           default_index=0)
    
# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # Page Title
    st.title("Diabetes Prediction using ML")
    
    # Getting the input data from the user
    # Columns for input fields
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies',value=None,format="%.5f")
    with col2:
        Glucose = st.number_input('Glucose Level (0 - 199)',value=None,format="%.5f")
    with col3:
        BloodPressure = st.number_input('Blood Pressure Value (0 - 122)',value=None,format="%.5f")
    with col1:
        SkinThickness = st.number_input('Skin Thickness Value (0 - 99)',value=None,format="%.5f")
    with col2:
        Insulin = st.number_input('Insulin Level (0 - 846)',value=None,format="%.5f")
    with col3:
        BMI = st.number_input('BMI Value (0 - 67.1)',value=None,format="%.5f")
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function (0.078 - 2.42)',value=None,format="%.5f")
    with col2:
        Age = st.number_input('Age of the Person',value=None,format="%.5f")
    
    # Code for Prediction
    diab_diagnosis = ''
    
    # Creating a button for prediction
    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if(diab_prediction[0]==1):
            diab_diagnosis="The person has Diabetes."
        else:
            diab_diagnosis="The person does not have Diabetes."
    st.success(diab_diagnosis)
    
if selected == 'Heart Disease Prediction':
    # Page Title
    st.title("Heart Disease Prediction using ML")
    
    # Getting the input data from the user
    # Columns for input fields
    col1,col2,col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age of the Person',value=None,format="%.5f")
    with col2:
        sex = st.number_input('Sex of the Person (1-Male , 0-Female)',value=None,format="%.5f")
    with col3:
        cp = st.number_input('Chest Pain Types (0, 1, 2, 3)',value=None,format="%.5f")
    with col1:
        trestbps = st.number_input('Resting Blood Pressure (94 - 200)',value=None,format="%.5f")
    with col2:
        chol = st.number_input('Serum Cholestrol in mg/dl (126 - 564)',value=None,format="%.5f")
    with col3:
        fbs = st.number_input('Dasting Blood Sugar >120mg/dl (1-True , 0-False)',value=None,format="%.5f")
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results (0, 1, 2)',value=None,format="%.5f")
    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved (71 - 202)',value=None,format="%.5f")
    with col3:
        exang = st.number_input('Exercise Induced Angina (1-Yes , 0-No)',value=None,format="%.5f")
    with col1:
        oldpeak = st.number_input('ST Depression induced by exercise (0 - 6.2)',value=None,format="%.5f")
    with col2:
        slope = st.number_input('The slope of the peak exercise ST segment (0, 1, 2)',value=None,format="%.5f")
    with col3:
        ca = st.number_input('Number of major vessels colored by flourosopy (0, 1, 2, 3, 4)',value=None,format="%.5f")
    with col1:
        thal = st.number_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',value=None,format="%.5f")
    
    # Code for Prediction
    heart_diagnosis = ''
    
    # Creating a button for prediction
    if st.button("Heart Disease Test Result"):
        heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if(heart_prediction[0]==1):
            heart_diagnosis = "The person have Heart Disease."
        else:
            heart_diagnosis = "The person does not have Heart Disease."
    st.success(heart_diagnosis)
    
    
if selected == 'Parkinson\'s Prediction':
    # Page Title
    st.title("Parkinson\'s Prediction using ML")
    
    # Getting the input data from the user
    # Columns for input fields
    col1,col2,col3,col4 = st.columns(4)
    
    with col1:
        Fo  = st.number_input('MDVP: Fo(Hz) (88.333 - 260.105)',value=None,format="%.6f")
    with col2:
        Fhi = st.number_input('MDVP: Fhi(Hz) (102.145 - 592.030)',value=None,format="%.6f")
    with col3:
        Flo = st.number_input('MDVP: Flo(Hz) (65.476 - 239.170)',value=None,format="%.6f")
    with col4:
        JitterPercent = st.number_input('MDVP: Jitter(%) (0.00168 - 0.03316)',value=None,format="%.6f")
    with col1:
        JitterABs = st.number_input('MDVP: Jitter(Abs) (0.000007 - 0.000260)',value=None,format="%.6f")
    with col2:
        RAP = st.number_input('MDVP: RAP (0.00068 - 0.02144)',value=None,format="%.6f")
    with col3:
        PPQ = st.number_input('MDVP: PPQ (0.00092 - 0.01958)',value=None,format="%.6f")
    with col4:
        DDP = st.number_input('Jitter: DDP (0.00204 - 0.06433)',value=None,format="%.6f")
    with col1:
        Shimmer = st.number_input('MDVP: Shimmer (0.00954 - 0.11908)',value=None,format="%.6f")
    with col2:
        ShimmerDB = st.number_input('MDVP: Shimmer(dB) (0.0850 - 1.3020)',value=None,format="%.6f")
    with col3:
        APQ3 = st.number_input('Shimmer: APQ3 (0.00455 - 0.05647)',value=None,format="%.6f")
    with col4:
        APQ5 = st.number_input('Shimmer: APQ5 (0.00570 - 0.07940)',value=None,format="%.6f")
    with col1:
        APQ = st.number_input('MDVP: APQ (0.00719 - 0.13778)',value=None,format="%.6f")
    with col2:
        DDA = st.number_input('Shimmer: DDA (0.00719 - 0.16942)',value=None,format="%.6f")
    with col3:
        NHR = st.number_input('NHR (0.00065 - 0.31482)',value=None,format="%.6f")
    with col4:
        HNR = st.number_input('HNR (8.441 - 33.047)',value=None,format="%.6f")
    with col1:
        RPDE = st.number_input('RPDE (0.256570 - 0.685151)',value=None,format="%.6f")
    with col2:
        DFA = st.number_input('DFA (0.574282 - 0.825288)',value=None,format="%.6f")
    with col3:
        spread1 = st.number_input('spread1 (-7.964984 - -2.434031)',value=None,format="%.6f")
    with col4:
        spread2 = st.number_input('spread2 (0.006274 - 0.450493)',value=None,format="%.6f")
    with col1:
        D2 = st.number_input('D2 (1.423287 - 3.671155)',value=None,format="%.6f")
    with col2:
        PPE = st.number_input('PPE (0.044539 - 0.527367)',value=None,format="%.6f")
    
    # Code for Prediction
    parkinsons_diagnosis = ''
    
    # Creating a button for prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[Fo,Fhi,Flo,JitterPercent,JitterABs,RAP,PPQ,DDP,Shimmer,ShimmerDB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if(parkinsons_prediction[0]==1):
            parkinsons_diagnosis = "The person have parkinson\'s Disease."
        else:
            parkinsons_diagnosis = "The person does not have Parkinson\'s Disease."
    st.success(parkinsons_diagnosis)
