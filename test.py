import cv2
import os
from cvzone.HandTrackingModule import HandDetector

# Initialize HandDetector
detector = HandDetector(maxHands=1, detectionCon=0.8)

# Default image path
default_image_path = r"C:\Users\abedi\OneDrive\Desktop\OOP Prj\pic\zero.jpeg"
if not os.path.exists(default_image_path):
    print(f"Error: Default image not found at {default_image_path}. Exiting.")
    exit()

# Start video capture with the default camera (0)
video = cv2.VideoCapture(0)

while True:
    success, img = video.read()
    if not success:
        print("Error: Unable to access the camera.")
        break

    img = cv2.flip(img, 1)  # Mirror the camera feed for natural interaction

    # Detect hands in the image
    hands, img = detector.findHands(img, draw=True)

    # Load default image
    fing = cv2.imread(default_image_path)

    if hands:
        hand = hands[0]
        lmList = hand['lmList']  # List of landmarks
        label = "Right" if hand['type'] == "Right" else "Left"  # Fix mirrored logic

        # Detect the fingers that are up
        fingerup = detector.fingersUp(hand)
        print(f"Fingers detected: {fingerup}")

        # Image paths for finger count
        image_paths = {
            "[0, 1, 0, 0, 0]": r"C:\Users\abedi\OneDrive\Desktop\OOP Prj\pic\one.jpg",
            "[0, 1, 1, 0, 0]": r"C:\Users\abedi\OneDrive\Desktop\OOP Prj\pic\two.jpg",
            "[0, 1, 1, 1, 0]": r"C:\Users\abedi\OneDrive\Desktop\OOP Prj\pic\three.jpg",
            "[0, 1, 1, 1, 1]": r"C:\Users\abedi\OneDrive\Desktop\OOP Prj\pic\four.jpg",
            "[1, 1, 1, 1, 1]": r"C:\Users\abedi\OneDrive\Desktop\OOP Prj\pic\five.jpg",
        }

        fing_path = image_paths.get(str(fingerup), default_image_path)
        fing = cv2.imread(fing_path)

        if fing is None:
            print(f"Error: Image not found at {fing_path}")
            continue

        fing = cv2.resize(fing, (220, 280))

    # Overlay the finger image on the video feed
    if fing is not None and img.shape[0] > 330 and img.shape[1] > 240:
        img[50:330, 20:240] = fing
    else:
        print("Warning: Image or video feed size mismatch.")

    # Display the video feed with the overlay
    cv2.imshow("Finger Counter", img)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video.release()
cv2.destroyAllWindows()
