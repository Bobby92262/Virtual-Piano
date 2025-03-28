import cv2
from cvzone.HandTrackingModule import HandDetector
import os

# Function to map finger gestures to image paths
def get_image_path(fingerup):
    gesture_to_path = {
        (0, 1, 0, 0, 0): r"C:\Users\bobby\OneDrive - South East Technological University (Waterford Campus)\IOT\IOT Raspberry\Hands images\Finger_One.jpg",
        (0, 1, 1, 0, 0): r"C:\Users\bobby\OneDrive - South East Technological University (Waterford Campus)\IOT\IOT Raspberry\Hands images\Finger_Two.jpg",
        (0, 1, 1, 1, 0): r"C:\Users\bobby\OneDrive - South East Technological University (Waterford Campus)\IOT\IOT Raspberry\Hands images\Finger_Three.jpg",
        (0, 1, 1, 1, 1): r"C:\Users\bobby\OneDrive - South East Technological University (Waterford Campus)\IOT\IOT Raspberry\Hands images\Finger_Four.jpg",
        (1, 1, 1, 1, 1): r"C:\Users\bobby\OneDrive - South East Technological University (Waterford Campus)\IOT\IOT Raspberry\Hands images\Finger_Five.jpg"
    }
    return gesture_to_path.get(tuple(fingerup), None)

# Initialize the camera and hand detector
camera = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.8)

if not camera.isOpened():
    print("Cannot open camera")
    exit()

haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = camera.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # Perform hand detection
    fing = None  # Default to None
    hand = detector.findHands(frame, draw=False)
    print("Hand detected:", hand)  # Debugging output

    if hand and len(hand[0]) > 0:
        if isinstance(hand[0], dict) and "lmList" in hand[0]:
            lmlist = hand[0]["lmList"]  # Correctly access the landmark list
            fingerup = detector.fingersUp(lmlist)
            print("Finger up:", fingerup)

            # Check if the gesture corresponds to a specific image
            image_path = get_image_path(fingerup)  # Get the image path
            print("Image path:", image_path)  # Debugging output

            if image_path and os.path.exists(image_path):
                fing = cv2.imread(image_path)
                fing = cv2.resize(fing, (220, 280))  # Resize the image
                frame[50:330, 20:240] = fing  # Overlay the image
            else:
                print("No valid image found for the gesture or file is missing.")
        else:
            print("No landmarks found in detected hand.")
    else:
        print("No hand detected.")

    # Perform face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the frame with detections
    cv2.imshow('Face Detection', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()