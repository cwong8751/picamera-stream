from flask import Flask, Response
from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import time

app = Flask(__name__)

# Initialize the Pi Camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24
raw_capture = PiRGBArray(camera, size=(640, 480))


def generate_frames():
    time.sleep(2)  # Camera warm-up time
    for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
        # Convert the image to a JPEG format
        image = frame.array
        ret, buffer = cv2.imencode('.jpg', image)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        raw_capture.truncate(0)  # Clear the stream for the next frame


@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/camera')
def camera_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Host on all interfaces
