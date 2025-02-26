import cv2
import numpy as np
import streamlit as st
from PIL import Image
from io import BytesIO

# Streamlit Web App UI
st.title("HDR Image Fusion")
st.write("Upload two images with different exposures.")

# Create file uploader widget.
img_file_buffer_1 = st.file_uploader("Upload the bright image", type=['jpg', 'jpeg', 'png'])
img_file_buffer_2 = st.file_uploader("Upload the dark image", type=['jpg', 'jpeg', 'png'])

# Initialize session state variables
if 'file_uploaded_name' not in st.session_state:
    st.session_state.file_uploaded_name = None
    
# Function to generate a download link for output file.
def get_image_download_link(img, filename, text):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href

if img_file_buffer_1 and img_file_buffer_2:
    # Convert uploaded files to OpenCV images
    image1 = np.array(Image.open(img_file_buffer_1).convert("RGB"))
    image2 = np.array(Image.open(img_file_buffer_2).convert("RGB"))

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
    out_image = Image.fromarray(fused_hdr[:, :, ::-1])
    # Create a link for downloading the output file.
    st.markdown(get_image_download_link(out_image, "HDR_output.jpg", 'Download Output Image'), unsafe_allow_html=True)
