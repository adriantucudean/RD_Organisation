from utils import Utils
import tkinter as tk

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
        pass
        
        