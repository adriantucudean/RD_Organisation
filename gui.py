from utils import Utils
import tkinter as tk
from tkinter import *

class GUI:
    def __init__(self):
        self.root=Utils.root
        self.image=Utils.lmain
        #self.root.attributes("-fullscreen",True)
        self.root.bind('<Escape>', lambda e: GUI.close_win(e,self.root))
    def close_win(e,root):
        root.destroy()


class Control_Panel(GUI):
    def __init__(self):
        super().__init__()
        self.image.grid(column=0,row=0)
        self.control_panel_zone=tk.Frame(self.root)
        self.control_panel_zone.grid(column=1,row=0)
        self.control_panel_zone.config(height=480,width=300,background="red")
    def populate_control_panel(self):
        play_vid = Button(self.control_panel_zone, text="play")
        play_vid.grid(column=0,row=0)
        pause_vid = Button(self.control_panel_zone, text="pause")
        pause_vid.grid(column=1,row=0)
        zoom_in = Button(self.control_panel_zone, text="zoom +")
        zoom_in.grid(column=2,row=0)
        zoom_out = Button(self.control_panel_zone, text="zoom -")
        zoom_out.grid(column=3,row=0)
        pass
        
        