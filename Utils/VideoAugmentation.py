# Imports
import cv2
import imutils
import numpy as np
from pathlib import Path
import shutil
import os
import time

######################## Horizontal Flip ########################
def horizontal_flip(path, new_path):
    '''
        horizontal_flip(path, new_path)
        
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

def generate_flipped_video(original_video_path, new_directory_path):
    '''
        generate_fliped_video(original_video_path, new_directory_path)
        
        This function takes the path to a video and the directory where to save the new video and generates a new video by flipping the original.
        It returns the path to this video.
        
        Parameters
        -------------------------------------------------------------------------------------------
        original_video_path:    Path to the original video
        new_directory_path:     Path of the directory whre the new video will save

        Returns
        -------------------------------------------------------------------------------------------
        new_video_path:         Path to the new video
        
    '''
     # Generates the name of the fliped video
    new_name = extract_name(original_video_path,"flip")
    # Generates the path of the fliped video
    flipped_video_path = os.path.join(new_directory_path, new_name)
    # Generates the fliped video
    horizontal_flip(original_video_path, flipped_video_path)
    # Return the path to the new video
    return flipped_video_path


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

def generate_rotated_video(original_video_path, new_directory_path, degrees):
    '''
        generate_fliped_video(original_video_path, new_directory_path, degrees)
        
        This function takes the path to a video and the directory where to save the new video, and generates a new video by rotating XX degrees the original one. 
        It returns the path to this video.
        
        Parameters
        -------------------------------------------------------------------------------------------
        original_video_path:    Path to the original video
        new_directory_path:     Path of the directory whre the new video will save

        Returns
        -------------------------------------------------------------------------------------------
        new_video_path:         Path to the new video
        
    '''
    # Generates the name of the rotated video
    new_name = extract_name(original_video_path,"rotated"+str(degrees))
    # Generates the path of the rotated video
    rotated_video_path = os.path.join(new_directory_path, new_name)
    # Generates the rotated video
    video_rotation(original_video_path, rotated_video_path, degrees)
    # Return the path to the new video
    return rotated_video_path


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
def extract_name(path, transformation):
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
    video_path_split = path.split("\\") # ['../1 - Dataset/Words/Sentir', 'word-sentir-001.mp4']
    name = video_path_split[1]
    # Add the transformation and the extension
    transformation = "-" + transformation + ".avi"
    name = name.replace(".mp4",transformation)
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
    Path(new_path).mkdir(parents=True,exist_ok=True)
    words = [words for words in os.listdir(path) if os.path.isdir(os.path.join(path, words))]

    for word in words:
        word_path = os.path.join(path,word)
        # If it does not exist, a new directory is created for each word
        new_word_path = os.path.join(new_path,word)
        Path(new_word_path).mkdir(parents=True,exist_ok=True)
        for video in os.listdir(os.path.join(path, word)):
            ## Original video ##
            original_video_path = os.path.join(word_path,video)
            # Generates an array with two positions, one for the path and the other for the video name.
            video_path_split = original_video_path.split("\\") # ['../1 - Dataset/Words/Sentir', 'word-sentir-001.mp4']
            # Copy the orignal video in the new folder
            shutil.copyfile(original_video_path, os.path.join(new_word_path,video_path_split[1]))
            ## Flip video ##
            flipped_video_path = generate_flipped_video(original_video_path, new_word_path)
            # ### Rotation +10 degrees. From the original ###
            # rotated10_video_path = generate_rotated_video(original_video_path, new_word_path, 10)
            # ### Rotation +10 degrees. From the flipped ###
            # flipped_rotated10_video_path = generate_rotated_video(flipped_video_path, new_word_path, 10)
            # ### Rotation -15 degrees. From the original ###
            # rotated15_video_path = generate_rotated_video(original_video_path, new_word_path, -15)
            # # ### Rotation -15 degrees. From the flipped ###
            # # flipped_rotated15_video_path = generate_rotated_video(flipped_video_path, new_word_path, -15)
            break


        

######################## Example ########################
path = "../1 - Dataset/Words/"
video_augmentation(path)