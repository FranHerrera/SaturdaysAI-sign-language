# Imports
import cv2
import imutils
import numpy as np
from pathlib import Path
import shutil
import os
from random import randrange
import time
from distutils.dir_util import copy_tree

######################## Horizontal Flip ########################
def video_flip(path, new_path):
    '''
        video_flip(path, new_path)
        
        This function takes a video, given its path, and performs a horizontal flip of that video.
        
        Parameters
        -------------------------------------------------------------------------------------------
        path:       Video file path
        new_path:   Path of the new video
        
    '''
    # The video is captured
    cap = cv2.VideoCapture(path)
    # Width and height of the video is taken
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # The format of the new video is created
    output = cv2.VideoWriter(new_path,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width,height))
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
def video_rotation(path, new_path, degree):
    '''
        video_rotation(path, new_path)
        
        This function takes a video, given its path, and performs a random rotatio of that video of a given angle
        
        Parameters
        -------------------------------------------------------------------------------------------
        path:       Video file path
        new_path:   Path of the new video
        degree:     Degree of rotation angle
        
    '''
    # The video is captured
    cap = cv2.VideoCapture(path)
    # Width and height of the video is taken
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # The format of the new video is created
    output = cv2.VideoWriter(new_path,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width,height))
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
def video_translation(path, new_path, shift_x, shift_y):
    '''
        video_rotation(path, new_path)
        
        This function takes a video, given its path, and performs a translation of that video.
        
        Parameters
        -------------------------------------------------------------------------------------------
        path:       Video file path
        new_path:   Path of the new video
        shift_x:    Number of pixels that the image will be shifted. Negative values will shift the image to the left, positive values to the right.
        shift_y:    Number of pixels that the image will be shifted. Negative values will shift the image down, positive values up.
    '''
    # The video is captured
    cap = cv2.VideoCapture(path)
    # Width and height of the video is taken
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # The format of the new video is created
    output = cv2.VideoWriter(new_path,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width,height))
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
def video_resize(path, new_path, scale_percent):
    '''
        video_rotation(path, new_path)
        
        This function takes a video, given its path, and performs a resize of that video.
        
        Parameters
        -------------------------------------------------------------------------------------------
        path:           Video file path
        new_path:       Path of the new video
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
    output = cv2.VideoWriter(new_path,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (new_width, new_height)) 
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
def video_gausian_blur(path, new_path, kernel_size):
    '''
        video_rotation(path, new_path)
        
        This function takes a video, given its path, and applies a gaussian blur filter to it from a given kernel size.
        
        Parameters
        -------------------------------------------------------------------------------------------
        path:          Video file path
        new_path:      Path of the new video
        kerner_size:   Kernel size
        
    '''
    # The video is captured
    cap = cv2.VideoCapture(path)
    # Width and height of the video is taken
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # The format of the new video is created
    output = cv2.VideoWriter(new_path,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width,height))
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


####################### Rename #######################
def extract_name(word, count, transformation):
    '''
        extract_name(path, transformation)
        
        This function takes a path and extracts the file name, adds the transformation being done and the extension ".avi".
        
        Parameters
        -------------------------------------------------------------------------------------------
        path:            Path string
        transformation:  String with the transformation to be performed "flip", "rotationXX", "tranlation", "resizeXX" and "blur" (XX is the angle in the case of rotation or 
        the percentege of size change)
        Return
        -------------------------------------------------------------------------------------------
        name:            The new name that the video has.
    '''
    # Generates an array with two positions, one for the path and the other for the video name.
    # video_path_split = path.split("\\") # ['../1 - Dataset/Words/Sentir', 'word-sentir-001.mp4']
    # name = video_path_split[1]
    # name_array = name.split("-")
    # # Add the transformation and the extension
    # transformation = "-" + transformation + ".avi"
    # name = name.replace(".mp4",transformation)
    name = word + transformation + str(count) + str(randrange(9999)) + ".avi"
    return name

def new_name(word, count):
    name = word + "_" + str(count) + "_" + str(time.time_ns()) + ".avi"
    return name

######################## Video Augmentation ########################
def video_augmentation(path):
    '''
        video_augmentation(path)
        
        This function takes each video found on the given path and performs different techniques of video augmentation (flipping, rotating, translating, resizing and blurring).
        
        Parameters
        -------------------------------------------------------------------------------------------
        path:          Path where the videos are
        
    '''
    # If it does not exist, a new path is created where the videos will be saved.
    new_path = "../Train_Dataset/"
    copy_tree(path, new_path)
    words = [words for words in os.listdir(new_path) if os.path.isdir(os.path.join(new_path, words))]

    # Flip
    for word in words:
        for video in os.listdir(os.path.join(new_path, word)):
            video_path = os.path.join(os.path.join(new_path, word), video)
            if video_path.endswith(".mp4"):
                new_video_path = video_path.replace(".mp4","-f" + ".avi")
            else:
                new_video_path = video_path.replace(".avi","-f" + ".avi")
            video_flip(video_path, new_video_path)
    # Rotation
    for word in words:
        for video in os.listdir(os.path.join(new_path, word)):
            video_path = os.path.join(os.path.join(new_path, word), video)
            if video_path.endswith(".mp4"):
                new_video_path_1 = video_path.replace(".mp4","-r10" + ".avi")
                new_video_path_2 = video_path.replace(".mp4","-r13" + ".avi")
            else:
                new_video_path_1 = video_path.replace(".avi","-r10" + ".avi")
                new_video_path_2 = video_path.replace(".avi","-r13" + ".avi")
            video_rotation(video_path, new_video_path_1, 10)
            video_rotation(video_path, new_video_path_2, -13)
    # Translation
    for word in words:
        for video in os.listdir(os.path.join(new_path, word)):
            video_path = os.path.join(os.path.join(new_path, word), video)
            if video_path.endswith(".mp4"):
                new_video_path_1 = video_path.replace(".mp4","-t25" + ".avi")
                new_video_path_2 = video_path.replace(".mp4","-t30" + ".avi")
            else:
                new_video_path_1 = video_path.replace(".avi","-t25" + ".avi")
                new_video_path_2 = video_path.replace(".avi","-t30" + ".avi")
            video_translation(video_path, new_video_path_1, 25, 25)
            video_translation(video_path, new_video_path_2, -30, -30)
    # Resize
    for word in words:
        for video in os.listdir(os.path.join(new_path, word)):
            video_path = os.path.join(os.path.join(new_path, word), video)
            if video_path.endswith(".mp4"):
                new_video_path_1 = video_path.replace(".mp4","-rs10" + ".avi")
                new_video_path_2 = video_path.replace(".mp4","-rs13" + ".avi")
            else:
                new_video_path_1 = video_path.replace(".avi","-rs10" + ".avi")
                new_video_path_2 = video_path.replace(".avi","-rs13" + ".avi")
            video_resize(video_path, new_video_path_1, 0.1)
            video_resize(video_path, new_video_path_2, -0.13)
    # Blur
    for word in words:
        for video in os.listdir(os.path.join(new_path, word)):
            video_path = os.path.join(os.path.join(new_path, word), video)
            if video_path.endswith(".mp4"):
                new_video_path = video_path.replace(".mp4","-b" + ".avi")
            else:
                new_video_path = video_path.replace(".avi","-b" + ".avi")
            video_gausian_blur(video_path, new_video_path, 35)
            
                

######################## Example ########################
path = "../1 - Dataset/Words/"
video_augmentation(path)