#  -*- coding: UTF-8 -*-
# unihiker.com

import numpy as np 
import cv2 
from PIL import Image 
import time

print("Sticker Face Tracking")
print("Start...")
time.sleep(2)

def languageIsZh():
    import locale
    current_locale, encoding = locale.getdefaultlocale()
    if 'zh' in current_locale.lower():
        return True



if languageIsZh():
    print("人脸识别之魔法贴图")
    print("在USB口插入一个摄像头")
    print("按A键退出程序，按B键切换贴图")
print("augmented reality sticker-tracking.")
print("Insert a camera into the USB port")
print("Press the A button-A to exit the program, press the button-B to switch textures")
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)

# Open usb camera 
cap = cv2.VideoCapture(-1) 

while not cap.isOpened():
    if languageIsZh():
        print("无法打开摄像头，请将摄像头插入USB口")
    print("Unable to open the camera, please plug the camera into the USB port")
    time.sleep(1)
    cap = cv2.VideoCapture(-1) 

# Set the camera buffer to 1, to decrease the latency. 
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1) 
# Set the windows to be full screen. 
cv2.namedWindow('winname',cv2.WND_PROP_FULLSCREEN) 
# Set the windows to be full screen. 
cv2.setWindowProperty('winname', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) 

# Load face recognition model. 
faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') 
# Name of the png file like 1.png 2.png ...
ImageID = 1 
# Read the mark image file from disk. 
markOrigin = Image.fromarray(cv2.imread(str(ImageID) + ".png" , cv2.IMREAD_UNCHANGED))  

# get and render face with mark.
def getAndRenderFace(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,  
        scaleFactor=1.1, 
        minNeighbors=5,  
        minSize=(30, 30) 
    )
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)  
        img = drawMark(img, x, y, w, h) 
    return img


# draw Mask
def drawMark(img, x, y, w, h):
    # Get the size of the mark image. 
    wm, hm = markOrigin.size  
    # Keep the ratio and resize the image to fit the width of face. 
    h1 = w*hm//wm  
    # Resize. 
    mark = markOrigin.resize((w, h1)) 
    # Convert from opencv Mat to Pillow Image. 
    img = Image.fromarray(img) 
    img.paste(mark, (x, y-h1), mark)  
    # Convert from Pillow Image to opencv Mat. 
    img = np.array(img) 
    return img


while(cap.isOpened()):  
    # Read one frame from usbcam. 
    ret, img = cap.read() 
    # If frame available. 
    if ret: 
        '''crop the center of the frame and resize to (240, 320) while keeping image ratio. '''
        h, w, c = img.shape  
        w1 = h*240//320
        x1 = (w-w1)//2
        img = img[:, x1:x1+w1] 
        img = cv2.resize(img, (240, 320)) 
        img = getAndRenderFace(img)
        cv2.imshow('winname',img) 
        key = cv2.waitKey(1) 

        if key & 0xFF == ord('a'): # Press the "a" key on Unihiker will stop the program.
            print("exit")
            break
        elif key & 0xFF == ord('b'): # Press the "b" key on Unihiker will change the mark.
            ImageID += 1  # Change the ImageID on every A click.
            if ImageID > 2: # Two marks are available in this program.
                ImageID = 1
            # Reload the mark from disk. 
            markOrigin = Image.fromarray(cv2.imread(str(ImageID) + ".png" , cv2.IMREAD_UNCHANGED))  
    else:
        break

cap.release() # Release usb camera. 
cv2.destroyAllWindows() # Destory all windows created by opencv.
