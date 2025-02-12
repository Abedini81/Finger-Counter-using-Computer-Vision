# Finger Counter using Computer Vision

![Screenshot 2025-01-13 215240](FingerCounter.png)

This project is a Python-based application that uses computer vision to detect hand gestures, count raised fingers, and display corresponding images based on the detected gesture. It utilizes the **cvzone** library for hand tracking and **OpenCV** for real-time video processing.

## Features
- **Real-Time Detection**: Detects hand gestures live through your webcam.
- **Finger Counting**: Counts the number of fingers raised and maps them to corresponding images.

## How It Works
1. Captures a live video feed from your webcam.
2. Detects a hand and the number of fingers raised using the **cvzone HandTrackingModule**.
3. Overlays an image corresponding to the detected finger count onto the video feed.

## Installation
To run this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Abedini81/Finger-Counter-using-Computer-Vision.git
