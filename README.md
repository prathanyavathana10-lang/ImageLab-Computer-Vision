# ImageLab — Image Processing & Enhancement Studio

A beginner-friendly Computer Vision web app built with Python, Streamlit, OpenCV, NumPy and Pillow.

## Features
- Upload JPG, JPEG, PNG, BMP or WEBP images
- Grayscale conversion
- Median-filter noise reduction
- Image sharpening
- Canny edge detection
- Binary thresholding
- Brightness adjustment
- Side-by-side comparison and processed-image download

## Run on Windows
1. Install Python 3.10 or newer from https://www.python.org/downloads/ . During installation, enable **Add Python to PATH** if offered.
2. Open this folder in Visual Studio Code.
3. Open **Terminal → New Terminal**.
4. Create a virtual environment (recommended):
   ```powershell
   python -m venv .venv
   ```
5. Activate it:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, you can skip activation and use `python -m pip` directly.
6. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
7. Start the app:
   ```powershell
   python -m streamlit run app.py
   ```
8. Streamlit prints a local URL, usually `http://localhost:8501`. Open it in your browser.

If `python` is not recognised, try `py` in place of `python`.

## Computer Vision concepts demonstrated
- Image representation and RGB colour images
- RGB/BGR colour-space conversion and HSV brightness adjustment
- Median filtering and Gaussian blur
- Canny edge detection
- Binary thresholding
- Pixel dimensions and downloadable image output

## Limitations
- This is a classical image-processing tool, not a trained AI classifier or object detector.
- Edge detection highlights intensity changes; it does not understand object meaning.
- A fixed threshold may not work well for every lighting condition.
- Sharpening can amplify noise.
- The app is a learning prototype and has not been clinically or industrially validated.

## Project documentation
See `PROJECT_DOCUMENTATION.md`.
