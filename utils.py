import tkinter as tk
import cv2
from PIL import ImageTk, Image
import math
import numpy as np
class Utils:
    """this class is designed to store functions for general purpose"""
    
    cap = cv2.VideoCapture("data/1.avi")
   # def __init__(self):
    root = tk.Tk()
    lmain = tk.Label(root)
    
    lmain.pack()
    
    root.bind('<Escape>', lambda e: Utils.close_win(e))
    def close_win(e):
        Utils.root.destroy()
    def tk_image_converter(source_image,destination_image):
        """This function is used for a conversion of data"""
        cv2image = cv2.cvtColor(source_image, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        return imgtk
    def get_angle(a, b, c):
        """This function calculates the angle between 2 vectors"""
        ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
        return ang + 360 if ang < 0 else ang
    def distance(p1,p2):
        """ This function calculates the distance between 2 points"""
        dist = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
        return dist
    def PolyArray(X, Y, dreapta_lim, stanga_lim):
        """This function converts a poly array into an opencv contour"""
        h = 470
        c = np.zeros((len(X)+2, 2), np.int32)
        c[0][0] = stanga_lim
        c[0][1] = h
        c[len(X)+1][0] = dreapta_lim
        c[len(X)+1][1] = h
        for i in range(len(X)):
            c[i+1][0] = X[i]
            c[i+1][1] = Y[i]
        c = np.array(c, np.int32)
        c = c.reshape((-1, 1, 2))
        return c
