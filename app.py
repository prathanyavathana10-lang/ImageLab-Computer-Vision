import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="ImageLab | Computer Vision", page_icon="🖼️", layout="wide")

st.title("🖼️ ImageLab — Image Processing & Enhancement Studio")
st.write("Upload an image, choose a Computer Vision operation, and compare the original with the processed result.")
st.caption("Educational prototype using classical image processing. It does not diagnose objects or train an AI model.")

uploaded = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg", "bmp", "webp"])

def to_rgb(pil_image):
    return np.array(pil_image.convert("RGB"))

def process_image(image_rgb, operation, strength):
    # OpenCV commonly processes colour images in BGR order.
    bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    if operation == "Original":
        result = bgr
    elif operation == "Grayscale":
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        result = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    elif operation == "Noise reduction":
        # Median filtering can reduce salt-and-pepper noise.
        k = int(strength)
        if k % 2 == 0:
            k += 1
        result = cv2.medianBlur(bgr, k)
    elif operation == "Sharpen":
        blur = cv2.GaussianBlur(bgr, (0, 0), 3)
        result = cv2.addWeighted(bgr, 1.0 + strength / 10.0, blur, -strength / 10.0, 0)
    elif operation == "Edge detection":
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        result = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    elif operation == "Threshold (black and white)":
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        result = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    elif operation == "Brightness":
        hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        v = np.clip(v.astype(np.int16) + int(strength) * 5, 0, 255).astype(np.uint8)
        result = cv2.cvtColor(cv2.merge((h, s, v)), cv2.COLOR_HSV2BGR)
    else:
        result = bgr

    return cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

if uploaded is None:
    st.info("Start by uploading a photo. You can use a photo from your computer.")
    st.subheader("Available operations")
    st.markdown("- **Grayscale:** converts colour to shades of grey.\n"
                "- **Noise reduction:** uses a median filter to smooth small noise.\n"
                "- **Sharpen:** enhances visible edges and details.\n"
                "- **Edge detection:** highlights strong intensity changes using Canny.\n"
                "- **Threshold:** converts the image into black and white based on intensity.\n"
                "- **Brightness:** adjusts image brightness.")
else:
    try:
        pil_image = Image.open(uploaded).convert("RGB")
        original = to_rgb(pil_image)

        if original.shape[0] * original.shape[1] > 16_000_000:
            st.warning("This image is very large. Consider using a smaller image for faster processing.")

        st.sidebar.header("Processing controls")
        operation = st.sidebar.selectbox(
            "Choose an operation",
            ["Grayscale", "Noise reduction", "Sharpen", "Edge detection",
             "Threshold (black and white)", "Brightness"]
        )

        if operation == "Noise reduction":
            strength = st.sidebar.slider("Filter size", min_value=3, max_value=9, value=5, step=2)
        elif operation == "Sharpen":
            strength = st.sidebar.slider("Sharpen strength", min_value=1, max_value=10, value=5)
        elif operation == "Brightness":
            strength = st.sidebar.slider("Brightness", min_value=-10, max_value=10, value=2)
        else:
            strength = 5

        processed = process_image(original, operation, strength)

        left, right = st.columns(2)
        with left:
            st.subheader("Original image")
            st.image(original, use_container_width=True)
        with right:
            st.subheader("Processed image")
            st.image(processed, use_container_width=True)

        st.success(f"Operation applied: {operation}")
        st.write(f"**Image dimensions:** {original.shape[1]} × {original.shape[0]} pixels")
        st.write(f"**Selected operation:** {operation}")

        output = BytesIO()
        Image.fromarray(processed).save(output, format="PNG")
        st.download_button(
            "⬇️ Download processed image",
            data=output.getvalue(),
            file_name="imagelab_processed.png",
            mime="image/png"
        )

        with st.expander("How does this operation work?"):
            explanations = {
                "Grayscale": "Each pixel is represented by an intensity value instead of three colour channels.",
                "Noise reduction": "A median filter replaces each pixel using the median of nearby pixel values. It can reduce certain types of noise.",
                "Sharpen": "The app combines the original image with a blurred version to make local details more pronounced.",
                "Edge detection": "Canny edge detection finds strong intensity changes that may correspond to object boundaries.",
                "Threshold (black and white)": "Pixels above the intensity threshold become white; the rest become black.",
                "Brightness": "Brightness is adjusted in the Value channel of HSV colour space."
            }
            st.write(explanations[operation])
    except Exception as exc:
        st.error("The image could not be processed. Try a different JPG or PNG image.")
        st.caption(f"Technical detail: {exc}")

st.divider()
st.caption("ImageLab is an educational demonstration. Results depend on image quality and parameter settings.")
