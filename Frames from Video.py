#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import os


# ### one video

# In[71]:


def convert_video_to_frames(outputdir, video_path):
    outputdir = outputdir
    vidcap = cv2.VideoCapture(video_path)
    success,image = vidcap.read()
    count = 0
    while success:
        if count%2==0:   
            cv2.imwrite(f"{outputdir}\\video%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
    #print('Read a new frame: ', success)
        count += 1
    return


# In[72]:


def rename_images(path):
    path=path+"/"
    os.getcwd()
    collection = path
    for i, filename in enumerate(os.listdir(collection)):
        os.rename(collection + filename, collection + str(i) + ".jpg")
    return 


# In[73]:


def convert_videos_to_frames_rename_them(outputdir, vid_path):
    convert_video_to_frames(outputdir, vid_path)
    rename_images(outputdir)
    return


# In[74]:


outputdir = r"E:\Egyptian Car Plate Detection\car_plate\Egyptian-Licence-Plate-Detector-master\frames"
video_path = r'E:\Egyptian Car Plate Detection\car_plate\Egyptian-Licence-Plate-Detector-master\1.mp4'


# In[75]:


convert_videos_to_frames_rename_them(outputdir, video_path)


# ### one folder

# In[42]:


videos = r"C:\Users\Ahmed\Downloads\Videos\sign\folder1"
outputdir=r"C:\Users\Ahmed\Downloads\Videos\output\folder1"
for video in os.listdir(videos):
    vidcap = cv2.VideoCapture(r'C:\Users\Ahmed\Downloads\Videos\sign\folder1' + f"\{video}")
    success,image = vidcap.read()
    count = int(f"{video}".split(".mp4")[0][-1])*100
    while success:
          if count%1==0:   
                  cv2.imwrite(f"{outputdir}\\video%d.jpg" % count, image)     # save frame as JPEG file      
  
          success,image = vidcap.read()
#print('Read a new frame: ', success)
          count += 1


# ### many folders

# In[99]:


videos_folder = r"C:\Users\Ahmed\Downloads\Videos\sign"
images_folder = r"C:\Users\Ahmed\Downloads\Videos\output"
for folder in os.listdir(videos_folder):
    for video in os.listdir(f"{videos_folder}\\{folder}"):
        vidcap = cv2.VideoCapture(f"{videos_folder}\\{folder}\\{video}")
        success,image = vidcap.read()
        count = int(f"{video}".split(".mp4")[0][-1])*100
        while success:
              if count%1==0:   
                      cv2.imwrite(f"{images_folder}\\{folder}\\video%d.jpg" % count, image)     # save frame as JPEG file      
  
              success,image = vidcap.read()
#print('Read a new frame: ', success)
              count += 1

