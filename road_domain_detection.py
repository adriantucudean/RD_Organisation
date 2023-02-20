import cv2
import numpy as np
from utils import Utils
from iep import IEP
class RDD:
    """this class serves as a method to detect the road"""
    def __init__(self,frame=None):
        """class constructor that initialises required variables for RRD initialisation"""
        self.segments=76
        self.x_seg=[0]*76
        self.y_seg=[10]*76
        self.frame=frame
        #self.sign=sign
        self.height=frame.shape[0]
        self.width=frame.shape[1]
        self.fsz = np.zeros([self.height,self.width,1],dtype=np.uint8)  
        self.b=[int(self.width/2),self.height]
        self.c=[self.width,self.height]
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.stanga_lim=0
        self.dreapta_lim=0
        self.mijloc=0
    def prepair_fsv(self):
        """ Searches for horisontal limits stanga_lim and dreapta_lim"""
        """Defines the Road shape"""
        mask=cv2.Canny(self.frame,100,90)
        cv2.imshow("canny",mask)
        kernel = np.ones((10,10),np.uint8)
        mask=cv2.dilate(mask,kernel)
        y_form=[10]*self.segments
        x_form=[0]*self.segments    
        stanga_lim=int(self.width/2)
        dreapta_lim=int(self.width/2)
        pic=np.array(mask)
        #------------------------------------------------
        for i in range(int(self.width/2),self.width-10):#here we calculate dreapta_lim value
            if  pic[self.height-10][i]:
                dreapta_lim=i                              
                break
        #------------------------------------------------
        for i in range(int(self.width/2)): #here we calculate stanga_lim value
            if pic[self.height-10][int(self.width/2)-i]:
                stanga_lim=int(self.width/2)-i
                break
        #-----------------------------------------------
        if(stanga_lim==int(self.width/2)): #here we treat exception of a noisy road
            stanga_lim=1
        if(dreapta_lim==int(self.width/2)):
            dreapta_lim=self.width-1
        #-----------------------------------------------
        self.stanga_lim=stanga_lim
        self.dreapta_lim=dreapta_lim
        mijloc=int((dreapta_lim+stanga_lim)/2)
        self.mijloc=mijloc
        cntsL = cv2.findContours(mask[int(self.height*0.66):self.height,stanga_lim:mijloc], cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        pic=np.array(mask)
        cv2.circle(self.frame,(stanga_lim,self.height-10),10,(255,255,255),3)
        cv2.circle(self.frame,(dreapta_lim,self.height-10),10,(255,255,255),3)
        #cv2.imshow("canny",mask)
        tensor=0
        #----------------------------------------------------------------------------------------
        for i in range(10):   #here we calculate the space between vertical segments
            if int(mijloc-i*self.segments)+2*i*self.segments<dreapta_lim and int(mijloc-i*self.segments)+2*i*self.segments> stanga_lim:
                tensor=i
       
        for i in range(self.segments):     
            y_form[i]=int(mijloc-tensor*self.segments)+2*tensor*i
        #----------------------------------------------------------------------------------------
        for i in range(40,self.height-10):# here we calculate the x values of the RDD points
            for j in range(self.segments):
                if pic[i][y_form[j]]:
                    if x_form[j]<i:
                        x_form[j]=i
        #----------------------------------------------------------------------------------------
        for i in range(self.segments):# here we calculate the y values of the RDD points
            self.x_seg[i]=x_form[i]
            self.y_seg[i]=y_form[i]
        #-----------------------------------------------------------------------------------------
    def classify_fsv(self):
        """Depending on the road shape we cand detect Intersection Entry&Exit"""
        contorR=0
        R=0
        intersection=0
        contorG=0
        GyR=0
        GxR=0
        free_space_zone = np.zeros([self.height,self.width,1],dtype=np.uint8)
        x_cil=0
        y_cil=0
        angle=0
        #----------------------------------------------------------------------------
        for j in range(self.segments):  #here we detect the intersection
            if self.x_seg[j]>(self.height/2+50):
                contorR=contorR+1
                if j<self.segments-1 :
                    GyR=GyR+self.x_seg[j]
                    GxR=GxR+self.y_seg[j]
                    R=R+1
                    cv2.line(self.frame,(self.y_seg[j+1],self.x_seg[j+1]),(self.y_seg[j],self.x_seg[j]),(255),4)
                else:
                    if R>0.80*self.segments:
                        intersection=1
                        cv2.rectangle(self.frame,(int(GxR/R-90),int(GyR/R)-100),(int(GxR/R)+190,int(GyR/R)-60),(255,255,255),-1)
                        cv2.rectangle(self.frame,(int(GxR/R-90),int(GyR/R)-100),(int(GxR/R)+190,int(GyR/R)-60),(0,0,255),2)
                        cv2.putText(self.frame,"INTERSECTION ENTRY POINT",(int(GxR/R-80),int(GyR/R)-70),self.font, 0.6,(0,0,255),2,cv2.LINE_AA)
            else:
                contorG=contorG+1
                x_cil=x_cil+self.y_seg[j]
                y_cil=y_cil+self.x_seg[j]
                if j<self.segments-1:
                    cv2.line(self.frame,(self.y_seg[j+1],self.x_seg[j+1]),(self.y_seg[j],self.x_seg[j]),(255),4)
        #----------------------------------------------------------------------------------------------
        cv2.line(self.frame,(self.y_seg[0],self.x_seg[0]),(self.y_seg[0],self.height-10),(255),4)
        cv2.line(self.frame,(self.y_seg[self.segments-1],self.x_seg[self.segments-1]),(self.y_seg[self.segments-1],self.height-10),(255),4)
        cv2.line(self.frame,(self.y_seg[0],self.height-10),(self.y_seg[self.segments-1],self.height-10),(255),4)
        c = Utils.PolyArray(self.y_seg, self.x_seg, self.dreapta_lim, self.stanga_lim)
        #cv2.drawContours(self.frame, [c], -1, (0, 255, 0), -1)
        #cv2.drawContours(self.frame, [c], -1, (0, 255, 0), 2)
        #----------------------------------------------------------------------------------------------
        if intersection == 0:
            iep = IEP(self.frame, self.x_seg, self.y_seg, self.segments,
                      contorG, contorR, self.dreapta_lim, self.stanga_lim)

            okS,okD=iep.discontinued_line()
            okR, okL = iep.intersection_exit_points()