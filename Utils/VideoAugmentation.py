# Imports
import cv2
import imutils
import numpy as np
import os

######################## Horizontal Flip ########################
def horizontal_flip(path, name):
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
    # The format of the new video is created
    output = cv2.VideoWriter(name +'.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width,height))
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

######################## Rotation ########################
def video_rotation(path, name, degree):
    '''
        video_rotation(path, name)
        
        This function takes a video, given its path, and performs a random rotatio of that video of a given angle
        
        Parameters
        -------------------------------------------------------------------------------------------
        path:       Video file path
        name:       Name of the fliped video
        degree:     Degree of rotation angle
        
    '''
    # The video is captured
    cap = cv2.VideoCapture(path)
    # Width and height of the video is taken
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # The format of the new video is created
    output = cv2.VideoWriter(name +'.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width,height))
    # Read the video
    while cap.isOpened():
        # Read the frame
        ret, frame = cap.read()
        if ret == True:
            # Rotate the frame
            frame = imutils.rotate(frame, degree)
            # Add image to output
            output.write(frame)
        else:
            break

    cap.release()
    output.release()

######################## Translation ########################
def video_translation(path, name, shift_x, shift_y):
    '''
        video_rotation(path, name)
        
        This function takes a video, given its path, and performs a translation of that video.
        
        Parameters
        -------------------------------------------------------------------------------------------
        path:       Video file path
        name:       Name of the fliped video
        shift_x:    Number of pixels that the image will be shifted. Negative values will shift the image to the left, positive values to the right.
        shift_y:    Number of pixels that the image will be shifted. Negative values will shift the image down, positive values up.
    '''
    # The video is captured
    cap = cv2.VideoCapture(path)
    print(cap)
    # Width and height of the video is taken
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # The format of the new video is created
    output = cv2.VideoWriter(name +'.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width,height))
    # Translation Matrix
    M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
    # Read the video
    while cap.isOpened():
        # Read the frame
        ret, frame = cap.read()
        if ret == True:
            # Shift the image
            frame = cv2.warpAffine(frame, M, (frame.shape[1], frame.shape[0]))
            # Add image to output
            output.write(frame)

        else:
            break

    cap.release()
    output.release()

######################## Resize ########################
def video_resize(path, name, scale_percent):
    '''
        video_rotation(path, name)
        
        This function takes a video, given its path, and performs a resize of that video.
        
        Parameters
        -------------------------------------------------------------------------------------------
        path:           Video file path
        name:           Name of the fliped video
        scale_percent:  Percentage that will increase or decrease the image. Its range is from -1 to 1.
    '''
    # The video is captured
    cap = cv2.VideoCapture(path)
    # Width and height of the video is taken
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # Calculate new width and new height
    new_width  = int(width + width*scale_percent)
    new_height = int(height + height*scale_percent)   
    # The format of the new video is created
    output = cv2.VideoWriter(name +'.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (new_width, new_height)) 
    # Read the video
    while cap.isOpened():
        # Read the frame
        ret, frame = cap.read()
        if ret == True:
            # Shift the image
            frame = cv2.resize(frame, (new_width, new_height), interpolation = cv2.INTER_AREA)
            # Add image to output
            output.write(frame)
        else:
            break

    cap.release()
    output.release()

######################## Gausian Blur ########################
def video_gausian_blur(path, name, kernel_size):
    '''
        video_rotation(path, name)
        
        This function takes a video, given its path, and applies a gaussian blur filter to it from a given kernel size.
        
        Parameters
        -------------------------------------------------------------------------------------------
        path:          Video file path
        name:          Name of the fliped video
        kerner_size:   Kernel size
        
    '''
    # The video is captured
    cap = cv2.VideoCapture(path)
    # Width and height of the video is taken
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # The format of the new video is created
    output = cv2.VideoWriter(name +'.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width,height))
    # Read the video
    while cap.isOpened():
        # Read the frame
        ret, frame = cap.read()
        if ret == True:
            # Gaussian blur filter is applied
            frame = cv2.blur(frame, (kernel_size, kernel_size))
            # Add image to output
            output.write(frame)
        else:
            break

    cap.release()
    output.release()

######################## Video Augmentation ########################
def video_augmentation(path):
    '''
        video_augmentation(path)
        
        This function takes each video found on the given path and performs different techniques of video augmentation (flipping, rotating, translating, resizing and blurring).
        
        Parameters
        -------------------------------------------------------------------------------------------
        path:          Path where the videos are
        
    '''
    words = [words for words in os.listdir(path) if os.path.isdir(os.path.join(path, words))]

    for word in words:
        word_path = os.path.join(path,word)
        for video in os.listdir(os.path.join(path, word)):
            video_path = os.path.join(word_path,video)
            # Horizontal Flip
            horizontal_flip(video_path,video_path.replace(".mp4","-flip"))
            # Rotate 10 degrees
            video_rotation(video_path,video_path.replace(".mp4","-rotate"),10)
            # Translation x+100, y+200
            video_translation(video_path,video_path.replace(".mp4","-translation"), 70, 50)
            # Increase 10%
            video_resize(video_path,video_path.replace(".mp4","-resize"), 0.1)
            # Gaussian Blur 20
            video_gausian_blur(video_path,video_path.replace(".mp4","-blur"), 20)

######################## Example ########################
# path = '../1 - Dataset/Words/'
# video_augmentation(path)