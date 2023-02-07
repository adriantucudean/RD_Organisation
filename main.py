
import tkinter as tk
import cv2
from PIL import Image, ImageTk
from utils import Utils
from road_domain_detection import RDD


def show_frame():
    """shows camera image"""
    _, frame = Utils.cap.read()
    #frame = cv2.flip(frame, 1)
    frame=cv2.resize(frame,(640,480),cv2.INTER_AREA)
    rdd=RDD(frame)
    rdd.prepair_fsv()
    rdd.classify_fsv()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    #cv2.imshow("Frame",frame)
    imgtk = ImageTk.PhotoImage(image=img)
    Utils.lmain.imgtk = imgtk
    Utils.lmain.configure(image=imgtk)
    Utils.lmain.after(10, show_frame)

show_frame()
Utils.root.mainloop()