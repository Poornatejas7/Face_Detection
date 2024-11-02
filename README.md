# Face Detection with OpenCV

This repository contains a Python script for real-time face detection using OpenCV. The script captures video from the webcam, detects faces in each frame, and displays the video with rectangles drawn around detected faces.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Explanation](#explanation)
- [Contributing](#contributing)
- [License](#license)

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
```python
import cv2

# Load the face cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Start video capture
cap = cv2.VideoCapture(0)

# Check if video capture or cascade loaded correctly
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
if face_cascade.empty():
    print("Error: Could not load cascade classifier.")
    exit()

# Continuously read frames
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to read frame.")
        break
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 6)
    
    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
    
    # Display the frame with detected faces
    cv2.imshow('img', frame)
    
    # Break if 'Escape' key (ASCII 27) is pressed
    if cv2.waitKey(40) & 0xff == 27:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()


Key Components
Loading the Haar Cascade: Uses cv2.CascadeClassifier to load the pre-trained Haar Cascade for face detection.

Video Capture: Initiates video capture from the default webcam using cv2.VideoCapture(0).

Frame Processing: Converts each frame to grayscale and applies the face detection algorithm.

Face Detection: Detects faces using detectMultiScale and draws rectangles around them.

Display and Exit: Displays the processed frames and exits the loop when the 'Escape' key is pressed.

Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.

Create your feature branch: git checkout -b feature/YourFeature.

Commit your changes: git commit -m 'Add YourFeature'.

Push to the branch: git push origin feature/YourFeature.

Open a pull request.
