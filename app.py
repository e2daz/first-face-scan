import streamlit as st

st.set_page_config(page_title="First Face Scan", page_icon="📷")
st.title("First Face Scan")
st.write("Choose an input source to provide an image for face detection.")

source = st.radio("Input source", ("Drag & drop image", "Webcam"))

image_file = None
if source == "Drag & drop image":
    image_file = st.file_uploader("Drop an image here or click to browse", type=["png", "jpg", "jpeg", "webp"])
else:
    image_file = st.camera_input("Take a picture")

if image_file is not None:
    st.image(image_file, caption="Selected input", use_container_width=True)
    st.info("Image captured. Add your face-detection logic here.")
else:
    st.warning("No image provided yet.")
