from flask import Flask, Response, render_template_string
import cv2
import time

app = Flask(__name__)

def generate_frames():
    # Initialize the OpenCV camera
    camera = cv2.VideoCapture(0)  # 0 is usually the default camera index
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    camera.set(cv2.CAP_PROP_FPS, 24)
    
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
    # Check if the camera is opened successfully
    if not camera.isOpened():
        # Display a placeholder image or error message if the camera isn't found
        error_html = '''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Camera Error</title>
        </head>
        <body>
            <h1>Camera not found</h1>
            <p>Please check your camera connection.</p>
            <img src="https://via.placeholder.com/640x480?text=No+Camera+Detected" alt="No camera available">
        </body>
        </html>
        '''
        return render_template_string(error_html)
    else:
        return Response(generate_frames(),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Host on all interfaces
