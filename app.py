import cv2
import numpy as np
import streamlit as st
from PIL import Image

# Streamlit Web App UI
st.title("HDR Image Fusion")
st.write("Upload two images with different exposures.")

# Upload images
uploaded_file1 = st.file_uploader("Upload the first image (bright window, dark room)", type=["jpg", "png", "jpeg"])
uploaded_file2 = st.file_uploader("Upload the second image (bright room, overexposed window)", type=["jpg", "png", "jpeg"])

if uploaded_file1 and uploaded_file2:
    # Convert uploaded files to OpenCV images
    image1 = np.array(Image.open(uploaded_file1).convert("RGB"))
    image2 = np.array(Image.open(uploaded_file2).convert("RGB"))

    # Convert to OpenCV BGR format
    img1 = cv2.cvtColor(image1, cv2.COLOR_RGB2BGR)
    img2 = cv2.cvtColor(image2, cv2.COLOR_RGB2BGR)

    # Resize images to be the same shape (if needed)
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Align images (feature-based alignment could be added)
    # Using OpenCV's Exposure Fusion
    merge_mertens = cv2.createMergeMertens()
    fused_hdr = merge_mertens.process([img1.astype(np.float32) / 255, img2.astype(np.float32) / 255])

    # Convert back to 8-bit format
    fused_hdr = (fused_hdr * 255).astype(np.uint8)
    fused_hdr = cv2.cvtColor(fused_hdr, cv2.COLOR_BGR2RGB)  # Convert to RGB for displaying

    # Display images
    st.image([image1, image2, fused_hdr], caption=["Bright Window Image", "Bright Room Image", "HDR Fused Result"], width=300)

    # Download result
    result_pil = Image.fromarray(fused_hdr)
    st.download_button("Download HDR Image", data=result_pil.tobytes(), file_name="hdr_result.jpg", mime="image/jpeg")
