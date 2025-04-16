import cv2
import numpy as nm
from PIL import Image #pillow package
import os
import pdb
#pdb.set_trace()

path ="C:/Users/goyal/PycharmProjects/pythonProject2/sample" #path for samples already taken
recognizer = cv2.face.LBPHFaceRecognizer_create() #local binary pattern histogram
detectors = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# cascade classifer fir effective objective detectation
def Images_And_Labels(path):#function to fetch the image and labels
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    facesample = []
    ids = []

    for imagepath in imagePaths: # to iterate particular image path
        grayimg = Image.open(imagepath).convert('L') #convert it in to grayscale
        imgarr = nm.array(grayimg,'uint8') #creat an array
        id = int(os.path.split(imagepath)[-1].split(".")[1])
        faces = detectors.detectMultiScale(imgarr)

        for (x,y,w,h) in faces:
            facesample.append(imgarr[y:y+h,x:x+w])
            ids.append(id)

        return facesample,ids
print("Traning faces. it will take a few seconds . wait....")

faces, ids = Images_And_Labels(path)
recognizer.train(faces, nm.array(ids))
recognizer.write('trainer.yml')# save trainer file in yml form
print('model trained, now we can recognize your face')
