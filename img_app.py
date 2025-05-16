import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- Configure Gemini API ---
genai.configure(api_key="AIzaSyDB2RcnDWOlOVn4cHY1hbwpyZpwVTqE2A4")
model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Gemini Image-to-Text", layout="centered")
st.title(" Gemini Image-to-Text Generator")
st.markdown("Upload an image, and Gemini will automatically describe it.")

# --- Upload Section ---
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Analyzing image..."):
        try:
            # Auto-generate description
            response = model.generate_content([image])
            st.success("Gemini's Description:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
