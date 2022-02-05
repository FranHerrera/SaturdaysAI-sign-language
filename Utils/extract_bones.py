import cv2
import numpy as np
import mediapipe as mp
from mediapipe.python.solutions.face_mesh_connections import FACEMESH_CONTOURS

mp_drawing = mp.solutions.drawing_utils 
mp_holistic = mp.solutions.holistic 



cap = cv2.VideoCapture(0)
# Initialize holistic model
with mp_holistic.Holistic(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as holistic:
    while cap.isOpened():
        # Read frame
        ret, frame = cap.read()
        img = np.zeros((frame.shape[0], frame.shape[1], frame.shape[2]))
        if ret == True:
            # Resize frame
            #frame = cv2.resize(frame, (WIDTH, HEIGHT), interpolation = cv2.INTER_AREA)
            # Change color from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame.flags.writeable = False
            # Detect landmarks
            results = holistic.process(frame)
            # Mano izquieda (azul)
            mp_drawing.draw_landmarks(
                img, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2, circle_radius=1),
                mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2))

            # Mano derecha (verde)
            mp_drawing.draw_landmarks(
                img, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=1),
                mp_drawing.DrawingSpec(color=(57, 143, 0), thickness=2))

            # Postura
            mp_drawing.draw_landmarks(
                img, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(128, 0, 255), thickness=2, circle_radius=1),
                mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))
    
            
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            cv2.imshow("Imagen a detectar", frame)
            cv2.imshow("Imagen Negra", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        else:
            break
cap.release()