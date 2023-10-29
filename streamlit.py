import streamlit as st
import requests

st.markdown(
    """
    <style>
        .reportview-container {
            background-color: #000000;
            padding-top: 70px;  /* Adjust the padding to match the height of the header */
        }
        .big-font {
            font-size:30px !important;
        }
        .blue-bg {
            background-color: #fff;
            padding: 40px 30px;
            color: black;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;  /* This ensures the header is on top of other elements */
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #000000;
            color: white;
            text-align: center;
            padding: 10px 30px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# Marquee Moving Title
st.markdown("<marquee class='blue-bg big-font'>Breast Cancer Machine Learning Diagnosis</marquee>", unsafe_allow_html=True)

# Welcome markdown
st.markdown(
    """
    ## Welcome to the Breast Cancer Diagnosis Tool!
    
    This tool helps in predicting the malignancy of a breast tumor based on certain input features. It utilizes machine learning algorithms and trained datasets to offer a possible diagnosis.
    
    ### Disclaimer:
    The prediction provided by this tool is purely based on the input data and the model it was trained on. It should not be used as a definitive diagnosis. Please consult with a healthcare professional for an accurate diagnosis.
    """
)

# Input fields in main content
st.header('Input Features')

radius_mean = st.number_input('Input radius_mean', value=0.0)
texture_mean = st.number_input('Input texture_mean', value=0.0)
perimeter_mean = st.number_input('Input perimeter_mean', value=0.0)
area_mean = st.number_input('Input area_mean', value=0.0)
smoothness_mean = st.number_input('Input smoothness_mean', value=0.0)
compactness_mean = st.number_input('Input compactness_mean', value=0.0)
concavity_mean = st.number_input('Input concavity_mean', value=0.0)
concave_points_mean = st.number_input('Input concave points_mean', value=0.0)
symmetry_mean = st.number_input('Input symmetry_mean', value=0.0)
fractal_dimension_mean = st.number_input('Input fractal_dimension_mean', value=0.0)
radius_se = st.number_input('Input radius_se', value=0.0)
texture_se = st.number_input('Input texture_se', value=0.0)
# ... continued ...
perimeter_se = st.number_input('Input perimeter_se', value=0.0)
area_se = st.number_input('Input area_se', value=0.0)
smoothness_se = st.number_input('Input smoothness_se', value=0.0)
compactness_se = st.number_input('Input compactness_se', value=0.0)
concavity_se = st.number_input('Input concavity_se', value=0.0)
concave_points_se = st.number_input('Input concave points_se', value=0.0)
symmetry_se = st.number_input('Input symmetry_se', value=0.0)
fractal_dimension_se = st.number_input('Input fractal_dimension_se', value=0.0)
radius_worst = st.number_input('Input radius_worst', value=0.0)
texture_worst = st.number_input('Input texture_worst', value=0.0)
perimeter_worst = st.number_input('Input perimeter_worst', value=0.0)
area_worst = st.number_input('Input area_worst', value=0.0)
smoothness_worst = st.number_input('Input smoothness_worst', value=0.0)
compactness_worst = st.number_input('Input compactness_worst', value=0.0)
concavity_worst = st.number_input('Input concavity_worst', value=0.0)
concave_points_worst = st.number_input('Input concave points_worst', value=0.0)
symmetry_worst = st.number_input('Input symmetry_worst', value=0.0)
fractal_dimension_worst = st.number_input('Input fractal_dimension_worst', value=0.0)

# Predict button
if st.button('Predict'):
    with st.spinner('Predicting...'):
        data = {
        'radius_mean': radius_mean,
        'texture_mean': texture_mean,
        'perimeter_mean': perimeter_mean,
        'area_mean': area_mean,
        'smoothness_mean': smoothness_mean,
        'compactness_mean': compactness_mean,
        'concavity_mean': concavity_mean,
        'concave_points_mean': concave_points_mean,
        'symmetry_mean': symmetry_mean,
        'fractal_dimension_mean': fractal_dimension_mean,
        'radius_se': radius_se,
        'texture_se': texture_se,
        'perimeter_se': perimeter_se,
        'area_se': area_se,
        'smoothness_se': smoothness_se,
        'compactness_se': compactness_se,
        'concavity_se': concavity_se,
        'concave_points_se': concave_points_se,
        'symmetry_se': symmetry_se,
        'fractal_dimension_se': fractal_dimension_se,
        'radius_worst': radius_worst,
        'texture_worst': texture_worst,
        'perimeter_worst': perimeter_worst,
        'area_worst': area_worst,
        'smoothness_worst': smoothness_worst,
        'compactness_worst': compactness_worst,
        'concavity_worst': concavity_worst,
        'concave_points_worst': concave_points_worst,
        'symmetry_worst': symmetry_worst,
        'fractal_dimension_worst': fractal_dimension_worst
    }
    
    
        try:
            response = requests.post('https://cancer-project-68fadaecc9a0.herokuapp.com/predict/', json=data, timeout=10)

            
            if response.status_code == 200:
                diagnosis = response.json()['diagnosis']
                st.write(f'The prediction is {diagnosis}')
            else:
                st.error(f"Error occurred: {response.text}")

        except requests.ConnectionError:
            st.error("Error connecting to the server. Please ensure the server is running and try again.")
        except requests.Timeout:
            st.error("Server took too long to respond. Please try again later.")
        except Exception as e:
            st.error(f"An error occurred: {e}")



# Copyright footer
st.markdown("<div class='footer'> &copy; Nyanda Jr @2023</div>", unsafe_allow_html=True)

