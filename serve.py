from flask import Flask, Response
import cv2
import time

app = Flask(__name__)

def generate_frames():
    # Initialize the OpenCV camera
    camera = cv2.VideoCapture(0)  # 0 is usually the default camera index
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set higher resolution
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    camera.set(cv2.CAP_PROP_FPS, 24)  # Slightly reduce FPS for better performance
    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # Use MJPEG for fast encoding

    time.sleep(2)  # Camera warm-up time
    while True:
        success, image = camera.read()  # Capture frame-by-frame
        if not success:
            break
        # Encode the frame as JPEG with optimized quality
        ret, buffer = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 60])
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/camera')
def camera_feed():
    # Check if the camera is opened successfully
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)  # Host on all interfaces
