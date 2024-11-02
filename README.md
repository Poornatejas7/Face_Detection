# Real-Time Face Detection with OpenCV

This repository contains a Python script that performs real-time face detection using OpenCV. The script captures video from the webcam, detects faces in each frame, and displays the video with rectangles drawn around detected faces.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Explanation](#explanation)
- [Contributing](#contributing)


## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/facedetection.git
    cd facedetection
    ```

2. **Install Dependencies**:
    Ensure you have Python and OpenCV installed. You can install OpenCV using pip:
    ```sh
    pip install opencv-python
    ```

3. **Download Haar Cascade File**:
    Download the `haarcascade_frontalface_default.xml` file from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place it in the project directory.

## Usage

1. **Run the Script**:
    ```sh
    python face_detection.py
    ```

2. **Exit**:
    - Press the `Escape` key to exit the video capture and close the display window.

## Explanation

### Code Overview

The script includes the following key components:
- **Loading the Haar Cascade**: Uses `cv2.CascadeClassifier` to load the pre-trained Haar Cascade for face detection.
- **Video Capture**: Initiates video capture from the default webcam using `cv2.VideoCapture(0)`.
- **Frame Processing**: Converts each frame to grayscale and applies the face detection algorithm.
- **Face Detection**: Detects faces using `detectMultiScale` and draws rectangles around them.
- **Display and Exit**: Displays the processed frames and exits the loop when the 'Escape' key is pressed.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add YourFeature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

