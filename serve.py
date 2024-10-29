from flask import Flask, Response
import cv2
import time

app = Flask(__name__)

# Initialize the OpenCV camera
camera = cv2.VideoCapture(0)  # 0 is usually the default camera index
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
camera.set(cv2.CAP_PROP_FPS, 24)


def generate_frames():
    time.sleep(2)  # Camera warm-up time
    while True:
        success, image = camera.read()  # Capture frame-by-frame
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', image)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/camera')
def camera_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Host on all interfaces
