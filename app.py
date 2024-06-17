# Python In-built packages
from pathlib import Path
import PIL

# External packages
import streamlit as st

# Local Modules
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="Preview Tooth Detection System by MahaseenLab",
    page_icon="🦷",
    layout="wide",
    initial_sidebar_state="expanded"
)
 
# Main page heading
st.title("Tooth Detection and Numbering")
st.write("**This system is a preview version, not for commercial use. For the full version, please contact mmasadar@gmail.com.**")
st.write("____________________________________________________________________________________________________________________")

# Sidebar
st.sidebar.header("Preview ML Model for Tooth Detection")

# Model Options
model_type = st.sidebar.radio(
    "Select Task", ['Tooth Detection', 'Implant (future)', 'Cavity (future)'])

confidence = float(st.sidebar.slider(
    "Select Model Confidence", 1, 100, 30)) / 100

# Selecting Detection Or Segmentation
if model_type == 'Tooth Detection':
    model_path = Path(settings.DETECTION_MODEL)
    model = helper.load_model(model_path)
    helper.image_config(model, confidence)
elif model_type == 'Implant (future)':
    helper.future_development("## 🔍 Future Development: Implant Detection", 
                              "images/implant_detection.png")
elif model_type == 'Cavity (future)':
    helper.future_development("## 🔍 Future Development: Cavity Detection",
                              "images/cavity_detection.png")
