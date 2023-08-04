import cv2
import mediapipe as mp
dispW  =500
dispH= 500
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
mp_hands = mp.solutions.hands

# Initialize MediaPipe Hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Open video stream

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Convert the BGR frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe
    results = hands.process(rgb_frame)

    # Check for hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Iterate through all the landmarks
            for landmark in hand_landmarks.landmark:
                # Extract the X, Y, Z coordinates of the landmark
                x, y, z = landmark.x, landmark.y, landmark.z
                
                # Display the X, Y, Z coordinates on the frame
                cv2.putText(frame, f'X: {x:.2f}, Y: {y:.2f}, Z: {z:.2f}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Draw landmarks on the frame
            mp_hands.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the frame
    cv2.imshow('Hand Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

