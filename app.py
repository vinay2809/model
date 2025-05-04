
import streamlit as st
import torch
from PIL import Image
from model import BusterNet  # Placeholder for the BusterNet model

# Load the pretrained model (replace with actual path when ready)
model = BusterNet()
model.load_state_dict(torch.load('model/BusterNet_pretrained.pth'))
model.eval()

st.title('Image Forgery Detection using BusterNet')

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Analyzing...")

    # Perform forgery detection (dummy code for now)
    result = "Forgery Detected"  # Placeholder result
    st.write(result)
