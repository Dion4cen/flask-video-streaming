#!/bin/bash

# Install Python packages via apt
sudo apt-get update
sudo apt-get install -y \
    python3-flask \
    python3-picamera2 \
    python3-opencv \
    python3-numpy \
    python3-werkzeug

# Verify installations
echo "Installation completed. Checking versions:"
python3 -c "import flask; print('Flask version:', flask.__version__)"
python3 -c "import picamera2; print('Picamera2 installed')"
python3 -c "import cv2; print('OpenCV version:', cv2.__version__)"
python3 -c "import numpy; print('NumPy version:', numpy.__version__)"
python3 -c "import werkzeug; print('Werkzeug version:', werkzeug.__version__)"

