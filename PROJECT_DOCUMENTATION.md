# ImageLab — Image Processing & Enhancement Studio
## Computer Vision Project Documentation

### 1. Abstract
ImageLab is a small interactive web application that demonstrates fundamental Computer Vision operations. A user uploads an image, chooses an operation, views the result beside the original, and downloads the processed image. The prototype focuses on explainable classical image processing rather than claiming to use a trained AI model.

### 2. Problem statement
Basic image inspection and preparation can be difficult for new learners when they have to use separate command-line scripts for each operation. The project provides one simple interface to demonstrate common image-processing methods and compare their effects.

### 3. Proposed solution
ImageLab combines several operations in one browser-based interface: grayscale conversion, median-filter noise reduction, sharpening, Canny edge detection, binary thresholding and brightness adjustment. Users can inspect the output immediately and download it.

### 4. Objectives
- Demonstrate foundational Computer Vision operations.
- Make image processing accessible through a simple web interface.
- Allow comparison between original and processed images.
- Explain the purpose of each operation.
- Provide a downloadable processed image.

### 5. Technologies used
- **Python:** application logic.
- **Streamlit:** browser-based user interface.
- **OpenCV:** image transformations and filters.
- **NumPy:** pixel-array handling and numeric operations.
- **Pillow:** reading and saving image files.

### 6. Technical approach / workflow
1. The user uploads a supported image.
2. Pillow reads the image and converts it to RGB.
3. The app converts the image to OpenCV's BGR representation when required.
4. The selected image-processing operation is applied.
5. The result is converted back to RGB for display.
6. The original and processed images are shown side by side.
7. The user can download the processed result as a PNG file.

### 7. Algorithms and methods
- **Grayscale conversion:** converts a colour image into intensity values.
- **Median filtering:** replaces a pixel using the median value in a neighbourhood; useful for reducing salt-and-pepper noise.
- **Sharpening:** combines the original image with a blurred version to make details more pronounced.
- **Canny edge detection:** detects strong intensity transitions using gradient and edge-linking stages.
- **Binary thresholding:** separates pixels into black or white based on a chosen intensity threshold.
- **HSV brightness adjustment:** changes the Value channel while retaining the Hue and Saturation channels as much as possible.

### 8. Implementation
The project is implemented in `app.py`. Streamlit manages image upload, selection controls, image display and download. OpenCV performs the image transformations. The dependency list is provided in `requirements.txt`.

### 9. Results
After running the application, test each operation with at least two images. Insert screenshots of the actual application and outputs here before final submission:
- Screenshot 1: application before image upload.
- Screenshot 2: original image compared with grayscale output.
- Screenshot 3: edge detection or threshold output.
- Screenshot 4: download control and a second test image.

Do not claim quantitative accuracy or performance results because this project does not train a predictive model and no benchmark evaluation is included.

### 10. Novelty / contribution
The individual algorithms are established Computer Vision techniques. The project's contribution is educational integration: several common image-processing operations, adjustable controls, explanations and downloadable results are combined in one lightweight interface. The project should not claim that the algorithms themselves are newly invented.

### 11. Limitations
- No deep-learning model or semantic object recognition is included.
- Fixed thresholding may perform poorly when lighting varies.
- Sharpening can amplify image noise.
- Edge maps can include unwanted edges or miss low-contrast boundaries.
- Results depend on image quality and selected settings.
- This prototype has not been validated for safety-critical use.

### 12. Future improvements
- Add adaptive thresholding and histogram equalisation.
- Add a noise simulation option to compare denoising methods.
- Add batch processing and an operation history.
- Add objective image-quality metrics where appropriate.
- Add automated tests and accessibility improvements.

### 13. Conclusion
ImageLab provides a practical introduction to Computer Vision by letting users experiment with image transformations in a browser. It demonstrates image representation, colour conversion, filtering, thresholding and edge detection in a compact, explainable application.

### 14. References
- OpenCV documentation: https://docs.opencv.org/
- Streamlit documentation: https://docs.streamlit.io/
- NumPy documentation: https://numpy.org/doc/
- Pillow documentation: https://pillow.readthedocs.io/

### Team details
Add the participant names and team details required by the event before submission.
