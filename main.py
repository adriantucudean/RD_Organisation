
import tkinter as tk
import cv2
from PIL import Image, ImageTk
from utils import Utils
from road_domain_detection import RDD
from gui import Control_Panel
import numpy as np


def show_frame():
    """shows camera image"""
    _, frame = Utils.cap.read()
    pts = np.array([(250, 400), (100, 100), (540, 100), (390, 400)], dtype = "float32")
    frame=cv2.resize(frame,(640,480),cv2.INTER_AREA)
    rdd=RDD(frame)
    rdd.prepair_fsv()
    rdd.classify_fsv()
  

    
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    
    img = Image.fromarray(cv2image)
    
    imgtk = ImageTk.PhotoImage(image=img)
    Utils.lmain.imgtk = imgtk
    Utils.lmain.configure(image=imgtk)
    Utils.lmain.after(10, show_frame)
# import the necessary packages
cp=Control_Panel()
cp.populate_control_panel()
show_frame()
Utils.root.mainloop()