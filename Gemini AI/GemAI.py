import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# 🔐 Hardcode your API key (⚠️ keep this secret!)
os.environ["GEMINI_API_KEY"] = "AIzaSyDmqSorG6iMHKaLFQNEIM-08LgkLbGneHo"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# UI Setup
st.set_page_config(page_title="Gemini AI Assistant", layout="centered")
st.title("🧠 Gemini AI Assistant")
st.caption("Text and Image Input | Powered by Gemini")

# # Sidebar settings
# with st.sidebar:
#     st.header("\U0001F9E0 AI Settings")
#     model_name = st.selectbox("Choose Model", ["gemini-2.5-pro-exp-03-25"])

# Mode Selection
mode = st.radio("Choose Mode:", ["Text ➡️ Text", "Image ➡️ Text"])

if mode == "Text ➡️ Text":
    st.subheader("✍️ Enter your prompt")
    prompt = st.text_area("Prompt", "What is the future of Generative AI?")
    if st.button("🚀 Generate Response"):
        if prompt.strip():
            try:
                model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")
                response = model.generate_content(prompt)
                st.subheader("💬 Gemini Response")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a prompt.")

elif mode == "Image ➡️ Text":
    st.subheader("🖼️ Upload an image for analysis")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    image_prompt = st.text_input("Optional prompt (e.g., 'Describe this image')", "")

    if uploaded_file and st.button("🔍 Analyze Image"):
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)

            model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")
            response = model.generate_content([image_prompt, image] if image_prompt else [image])

            st.subheader("🧠 Gemini's Interpretation")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
