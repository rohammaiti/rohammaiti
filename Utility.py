import cv2
import time
import mediapipe as mp
import numpy as np
import pyautogui


def control_volume():
    print("Voice Control for Volume Selected")

    x1 = y1 = x2 = y2 = 0
    webcam = cv2.VideoCapture(0)
    my_hands = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils

    if not webcam.isOpened():
        print("Error: Could not open webcam.")
    
    while True:
        _, image = webcam.read()
        image = cv2.flip(image, 1)
        frame_height, frame_width, _ = image.shape
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        output = my_hands.process(rgb_image)
        hands = output.multi_hand_landmarks

        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(image, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:
                        cv2.circle(img=image, center=(x, y), radius=10, color=(0, 200, 200), thickness=3)
                        x1 = x
                        y1 = y
                    if id == 4:
                        cv2.circle(img=image, center=(x, y), radius=10, color=(0, 200, 200), thickness=3)
                        x2 = x
                        y2 = y

            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 // 4
            cv2.line(image, (x1, y1), (x2, y2), (250, 0, 0), 6)
            if dist > 50:
                pyautogui.press("volumeup")
            else:
                pyautogui.press("volumedown")

        cv2.imshow("Hand volume control", image)

        key = cv2.waitKey(1)
        if key == 27:
            break

    webcam.release()
    cv2.destroyAllWindows()

def virtual_mouse_control():
    webcam = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    index_y = 0

    while True:
        _, frame = webcam.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks

        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        index_x = screen_width / frame_width * x
                        index_y = screen_height / frame_height * y

                    if id == 4:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        thumb_x = screen_width / frame_width * x
                        thumb_y = screen_height / frame_height * y
                        print('outside', abs(index_y - thumb_y))
                        if abs(index_y - thumb_y) < 100:
                            pyautogui.click()
                            pyautogui.sleep(1)
                        elif abs(index_y - thumb_y) < 180:
                            pyautogui.moveTo(index_x, index_y)
        
        cv2.imshow('Virtual Mouse', frame)
        key=cv2.waitKey(1)
        if key == 27:
            break

    webcam.release()
    cv2.destroyAllWindows()

# Main menu for user selection
while True:
    print("Choose an option:")
    print("1. AI Volume Control")
    print("2. AI Mouse Control")
    print("3. Exit")

    choice = input("Enter the option number: ")

    if choice == "1":
        control_volume()
    elif choice == "2":
        virtual_mouse_control()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select a valid option.")
