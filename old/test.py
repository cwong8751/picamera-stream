import cv2

camera = cv2.VideoCapture(1)  # Adjust the index if necessary

if camera.isOpened():
    print("Camera is accessible!")
else:
    print("Camera not accessible.")

camera.release()

