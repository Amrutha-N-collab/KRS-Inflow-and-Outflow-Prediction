import streamlit as st
import pickle

# Function to load models
def load_model(model_name):
    if model_name == 'Gradient Boosting':
        with open('gbr_inflow_model.pkl', 'rb') as inflow_file:
            inflow_model = pickle.load(inflow_file)
        with open('gbr_outflow_model.pkl', 'rb') as outflow_file:
            outflow_model = pickle.load(outflow_file)
    elif model_name == 'Support Vector Regression':
        with open('svr_inflow_model.pkl', 'rb') as inflow_file:
            inflow_model = pickle.load(inflow_file)
        with open('svr_outflow_model.pkl', 'rb') as outflow_file:
            outflow_model = pickle.load(outflow_file)
    elif model_name == 'Random Forest':
        with open('rf_inflow_model.pkl', 'rb') as inflow_file:
            inflow_model = pickle.load(inflow_file)
        with open('rf_outflow_model.pkl', 'rb') as outflow_file:
            outflow_model = pickle.load(outflow_file)
    
    return inflow_model, outflow_model

# Mapping season to numeric values
season_mapping = {'Winter': 4, 'Summer': 3, 'Monsoon': 2, 'Post-monsoon': 1}

# Prediction function
def predict_inflow_outflow(present_storage, reservoir_level, season_numeric, inflow_model, outflow_model):
    features = [[present_storage, reservoir_level, season_numeric]]
    inflow = inflow_model.predict(features)[0]
    outflow = outflow_model.predict(features)[0]
    return inflow, outflow
def add_bg(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_url});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    
    )
def style_sidebar():
    st.markdown(
        """
        <style>
        /* Background color for the sidebar */
        .css-1e5imcs {  /* This is the new class name for the sidebar */
            background-color: #FFD700;
        }
        </style>
        """,
        unsafe_allow_html=True
    
    )
# Home Page
def home():
    add_bg("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/d8/31/79/krs-dam-view-from-the.jpg?w=2000&h=-1&s=1")
    style_sidebar()
    st.title("KRS Reservoir Inflow and Outflow Prediction")
    st.markdown("""
        BY Amrutha N
    """)
    # Set background color
    st.markdown("<style>body {background-color: #fffacd;}</style>", unsafe_allow_html=True)  # Lemon Chiffon

# Introduction Page
def introduction():
    add_bg("https://www.trawell.in/admin/images/upload/398398115KRSDam_Main.jpg")
    style_sidebar()
    st.title("Introduction")
    st.markdown("""
        The KRS reservoir inflow and outflow prediction project utilizes advanced machine learning techniques to forecast water levels. 
        By considering various parameters, we aim to enhance decision-making regarding water management and resource allocation.
    """)
    # Set background color
    st.markdown("<style>body {background-color: #ffe4e1;}</style>", unsafe_allow_html=True)  # Misty Rose

# Prediction Page
def prediction():
    add_bg("https://www.trawell.in/admin/images/upload/398398115KRSDam_Main.jpg")
    style_sidebar()
    st.title("Prediction of Inflow and Outflow ")
    
    # Add custom CSS for background image
    page_bg_img = '''
    <style>
    body {
        background-image: url("images/background.jpg");  /* Update with your image path */
        background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    present_storage = st.number_input("PRESENT_STORAGE_TMC", min_value=10.0, max_value=60.0, step=0.1)
    reservoir_level = st.number_input("RESERVOIR_LEVEL_FT", min_value=50.0, max_value=200.0, step=0.1)

    season = st.selectbox('Select Season', ['Winter', 'Summer', 'Monsoon', 'Post-monsoon'])
    season_numeric = season_mapping[season]
    
    model_choice = st.selectbox("Select Model", ['Gradient Boosting', 'Support Vector Regression', 'Random Forest'])
    
    inflow_model, outflow_model = load_model(model_choice)
    
    if st.button("Predict"):
        inflow, outflow = predict_inflow_outflow(present_storage, reservoir_level, season_numeric, inflow_model, outflow_model)
        st.success(f"Predicted Inflow using {model_choice}: {inflow:.2f}")
        st.success(f"Predicted Outflow using {model_choice}: {outflow:.2f}")

    # Set a different background color
    st.markdown("<style>body {background-color: #ffffff;}</style>", unsafe_allow_html=True)  # White

# Sidebar navigation
st.sidebar.title("Navigation")
pages = {
    "Home": home,
    "Introduction": introduction,
    "Prediction": prediction
}

# Call the selected page
selection = st.sidebar.radio("Go to", list(pages.keys()))
pages[selection]()
