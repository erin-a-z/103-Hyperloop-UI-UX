from flask import Flask, request, Response, render_template
import cv2
from ml import analyze_frame

app = Flask(__name__)

# This route accepts the image file and displays it on the webpage
@app.route('/')
def index():
    return render_template('index.html')

# This route accepts the image file and returns it to the client in real-time
@app.route('/video_feed')
def video_feed():
    return Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# This function reads the frames from the video capture, analyzes them using the ml.analyze_frame function, and returns them as JPEG images
def get_frames():
    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()
        if not ret:
            break

        # analyze the frame using the ml.analyze_frame function
        analyzed_frame = analyze_frame(frame)

        # encode the frame in JPEG format
        jpeg = cv2.imencode('.jpg', analyzed_frame)[1].tobytes()

        # yield the result to the client
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg + b'\r\n')

    capture.release()

if __name__ == '__main__':
    app.run(debug=True)
