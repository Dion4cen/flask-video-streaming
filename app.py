from flask import Flask, render_template, Response, jsonify
from picamera2 import Picamera2
from libcamera import Transform, controls
import cv2
import time

app = Flask(__name__)
picam2 = None

def init_camera():
    global picam2
    if picam2 is not None:
        picam2.stop()
        picam2.close()
    
    picam2 = Picamera2()
    
    # IMX708 autofocus settings
    picam2.options["AfMode"] = 2  # Continuous autofocus mode
    picam2.options["AfSpeed"] = 1  # Normal focus speed
    
    config = picam2.create_preview_configuration(
        main={"size": (1920, 1080)},
        lores={"size": (640, 480)},
        transform=Transform(hflip=False, vflip=False)
    )
    picam2.configure(config)
    picam2.start()
    return picam2

def gen_frames():
    global picam2
    try:
        if picam2 is None:
            picam2 = init_camera()
            
        while True:
            frame = picam2.capture_array()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.1)
            
    except Exception as e:
        print(f"Error: {e}")
        if picam2:
            picam2.stop()
            picam2.close()
            picam2 = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/trigger_autofocus')
def trigger_autofocus():
    if picam2:
        try:
            picam2.set_controls({"AfMode": 2})  # Retrigger continuous autofocus
            return jsonify({"status": "success", "message": "Focus mode updated"})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)})
    return jsonify({"status": "error", "message": "Camera not initialized"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

