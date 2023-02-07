import tkinter as tk
import cv2
from PIL import ImageTk, Image
import math
class Utils:
    """this class is designed to store functions for general purpose"""
    width, height = 1024, 720
    cap = cv2.VideoCapture("data/1.avi")
   # def __init__(self):
    root = tk.Tk()
    lmain = tk.Label(root)
    lmain.pack()
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
 
