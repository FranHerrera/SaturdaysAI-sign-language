# Imports
import cv2
import imutils
import numpy as np
from pathlib import Path
import shutil
import os




######################## Horizontal Flip ########################
def horizontal_flip(path, new_path):
    '''
        horizontal_flip(path, name)
        
        This function takes a video, given its path, and performs a horizontal flip of that video.
        
        Parameters
        -------------------------------------------------------------------------------------------
        path:  Video file path
        name:  Name of the fliped video
        
    '''
    # The video is captured
    cap = cv2.VideoCapture(path)
    # Width and height of the video is taken
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # Generate new name
    name = extract_name(path, "flip")
    # The format of the new video is created
    output = cv2.VideoWriter(name,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width,height))
    # Read the video
    while cap.isOpened():
        # Read the frame
        ret, frame = cap.read()
        if ret == True:
            # Flip the frame
            frame = cv2.flip(frame, 1)
            # Add frame to outputiv
            output.write(frame)
        else:
            break

    cap.release()
    output.release()
    return name

path = "../1 - Dataset/Words/Abajo\word-abajo-001.mp4"
extract_name(path, "flip")
new_path = "../Tran_Dataset/Abajo"
#horizontal_flip(path, new_path)