import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ocr"

st.title("OCR Text Extractor")

uploaded_file = st.file_uploader("Upload an image", type=["jpg","jpeg","png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Extract Text"):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
        try:
            response = requests.post(API_URL, files=files)
            if response.status_code == 200:
                data = response.json()
                if "text" in data:
                    st.success("Extracted Text:")
                    st.write(data["text"])
                else:
                    st.error(f"Error: {data.get('error','Unknown')}")
            else:
                st.error(f"Status Code: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
