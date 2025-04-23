import streamlit as st
import google.generativeai as genai

# Configuration
st.set_page_config(page_title="Gemini AI Tutor", layout="centered")
st.title("\U0001F4D8 Gemini AI Tutor")

# Sidebar settings
with st.sidebar:
    st.header("\U0001F9E0 AI Settings")
    model_name = st.selectbox("Choose Model", ["gemini-2.5-flash-preview-04-17", "gemini-2.0-flash"])
    api_key = st.text_input("Enter your Gemini API Key", type="password")

# Configure Gemini
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)

    st.markdown("### ✍️ Ask me anything")
    user_prompt = st.text_area("Your question for the AI", height=100, placeholder="e.g. Explain photosynthesis like I'm 12")

    if st.button("Generate Answer"):
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(user_prompt)
                st.success("Here's what I came up with:")
                st.markdown("""<div style='background-color:#f1f3f6; padding: 1em; border-radius: 10px; overflow-x: auto; white-space: pre-wrap; font-family: monospace;' id='response-box'>
<pre id='response-text'>{}</pre>
</div>
<button onclick=\"navigator.clipboard.writeText(document.getElementById('response-text').innerText);\" style='margin-top: 10px; padding: 0.5em 1em; border: none; background-color: #4CAF50; color: white; border-radius: 5px; cursor: pointer;'>
📋 Copy to Clipboard
</button>
""".format(response.text), unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
else:
    st.warning("Please enter your Gemini API key to get started.")