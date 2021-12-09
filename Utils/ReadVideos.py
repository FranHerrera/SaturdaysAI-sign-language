# Imports
import cv2
import numpy as np
import pandas as pd
import mediapipe as mp
from mediapipe.python.solutions.face_mesh_connections import FACEMESH_CONTOURS

######################## Draw Landmarks ########################
def draw_landmarks(path, character_to_stop = 'q'):
    '''
        draw_landmarks(path)
        
        This function draws landmarks on the video from the path provided using mediapipe

        Parameters
        -------------------------------------------------------------------------------------------
        path:               Path where the video is
        character_to_stop:  Character to stop the video capture. The default is 'q'
    '''
    # Drawing helpers
    mp_drawing = mp.solutions.drawing_utils 
    # Mediapipe Solutions
    mp_holistic = mp.solutions.holistic 
    # Capture the video
    cap = cv2.VideoCapture(path)

    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
        while cap.isOpened():
            ret, frame = cap.read()
            if ret == True:
                # Change color from BGR to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame.flags.writeable = False        
                # Detections
                results = holistic.process(frame)
                # If the flag "show_video" is True, the renderizate image will be show
                
                # Change the order of the colors to display the image using cv2
                frame.flags.writeable = True   
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                # Face Landmarks
                mp_drawing.draw_landmarks(frame, results.face_landmarks,FACEMESH_CONTOURS, 
                                        mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                                        mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                                        )
                # Right Hand Landmarks
                mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                                        )
                # Left Hand Landmarks
                mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                                        )
                # Body Landmarks
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                        )
                cv2.imshow('Frame with Landmarks', frame)

                
                if cv2.waitKey(10) & 0xFF == ord(character_to_stop):
                    break
            else:
                break
    
    cap.release()
    cv2.destroyAllWindows()



draw_landmarks(1,'m')