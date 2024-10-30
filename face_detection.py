import cv2

# Load the face cascade
a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Start video capture
b = cv2.VideoCapture(0)

# Check if video capture or cascade loaded correctly
if not b.isOpened():
    print("Error: Could not open video.")
    exit()
if a.empty():
    print("Error: Could not load cascade classifier.")
    exit()

# Continuously read frames
while True:
    c_rec, d_image = b.read()
    if not c_rec:
        print("Error: Failed to read frame.")
        break
    
    # Convert frame to grayscale
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    f = a.detectMultiScale(e, 1.3, 6)
    
    # Draw rectangles around faces
    for (x1, y1, w1, h1) in f:
        cv2.rectangle(d_image, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 5)
    
    # Display the frame with detected faces
    cv2.imshow('img', d_image)
    
    # Break if 'Escape' key (ASCII 27) is pressed
    h = cv2.waitKey(40) & 0xff
    if h == 27:
        break

# Release the video capture object and close all windows
b.release()
cv2.destroyAllWindows()
