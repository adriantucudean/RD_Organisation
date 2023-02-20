import cv2
import numpy
import math
import imutils
import numpy as np
def poly_array(X, Y, dreapta_lim, stanga_lim):
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
def distance(p1,p2):
  dist = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
  return dist
class IEP:
  def __init__(self,frame,X,Y,SEGMENTS,G,R,DreaptaLim,StangaLim):
    self.frame=frame
    self.segments=SEGMENTS
    self.x_seg=X
    self.y_seg=Y
    
    self.height=frame.shape[0]
    self.width=frame.shape[1]
    self.font = cv2.FONT_HERSHEY_SIMPLEX
    self.contorG=G
    self.contorR=R
    self.DreaptaLim=DreaptaLim
    self.StangaLim=StangaLim
    self.mij=int(self.width/2)
  def discontinued_line(self):
    contorD,contorS,okS,okR,XR,XL,YR,YL,ok0,ok1=0,0,0,0,0,0,0,0,0,0
    
    for i in range(1,15):
      
      if distance((self.x_seg[i],self.y_seg[i]),(self.x_seg[i+1],self.y_seg[i+1]))>20 and self.x_seg[i]>self.height/2 :
        contorS+=1
        if ok0==0:
          XL=self.y_seg[i]-10
          YL=self.x_seg[i]-10
          ok0=1
        if contorS>1:
          cv2.rectangle(self.frame, (100, 152),(100+132, 150-10), (0, 0, 0), 2)
          cv2.rectangle(self.frame, (100, 152),(100+132, 150-10), (0, 255, 255), -1)
          cv2.putText(self.frame, "OVERTAKE ENTRY", (100, 150),self.font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        #print(distance((self.x_seg[i],self.y_seg[i]),(self.x_seg[i+1],self.y_seg[i+1])))
          okS=1
          cv2.line(self.frame,(self.y_seg[i]-10,self.x_seg[i]),(self.y_seg[i+1]-10,self.x_seg[i+1]),(0,0,255),3)
      if contorS>1:
        
      
     
      
    # if XR>1:
        cv2.arrowedLine(self.frame,(self.mij,self.height),(XL,YL),(255,0,0),2)
    for i in range(35,49):
      
      if distance((self.x_seg[i],self.y_seg[i]),(self.x_seg[i+1],self.y_seg[i+1]))>20 and self.x_seg[i]>self.height/2:
        #print(distance((self.x_seg[i],self.y_seg[i]),(self.x_seg[i+1],self.y_seg[i+1])))
        contorD+=1
        if ok1==0:
          XR=self.y_seg[i]-10
          YR=self.x_seg[i]-10
          ok1=1
        if contorD>3:
          cv2.rectangle(self.frame, (300, 152),(300+132, 150-12), (0, 0, 0), 2)
          cv2.rectangle(self.frame, (300, 152),(300+132, 150-12), (0, 255, 255), -1)
          cv2.putText(self.frame, "RETAKE ENTRY", (300, 150),self.font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
          
          
          cv2.line(self.frame,(self.y_seg[i]-10,self.x_seg[i]),(self.y_seg[i+1]-10,self.x_seg[i+1]),(0,0,255),3)
          okR=1
    if contorD>3:
      
     
      
    # if XR>1:
      cv2.arrowedLine(self.frame,(self.mij,self.height),(XR,YR),(255,0,0),2)
    return okS,okR
  def intersection_exit_points(self):
    XR=0
    YR=0
    XL=0
    YL=0
    XT=0
    YT=0
    okR=0
    okL=0
    edge=cv2.Canny(self.frame,100,80)
    cnts = cv2.findContours(edge, cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
   # extBot = tuple(c[c[:, :, 1].argmax()][0])
    if  self.DreaptaLim-self.StangaLim>500 :
        if self.x_seg[self.segments-1]<self.height-100 and self.x_seg[self.segments-2]<self.height-100   and self.DreaptaLim!= self.height:
          XR=extRight[0]#self.y_seg[self.segments-1]
          YR=extRight[1]#self.x_seg[self.segments-1]
          okR=1
          #cv2.line(self.frame,(XR-10,YR-33),(int(self.width/2),0),(0,0,0),3)
          #cv2.line(self.frame,(XR-10,YR-33),(int(self.width/2),0),(255,255,0),1)
          cv2.rectangle(self.frame,(XR-10,YR-15),(XR+90,YR-33),(255,255,255),-1)
          cv2.rectangle(self.frame,(XR-10,YR-15),(XR+90,YR-33),(0,0,255),2)
          cv2.putText(self.frame,"RIGHT ENTRY",(XR-5,YR-20),self.font, 0.4,(0,0,255),1,cv2.LINE_AA)
          
        if self.x_seg[0]<self.height-100 or self.x_seg[1]<self.height-100 or self.x_seg[2] <self.height-100 and self.StangaLim!= 0 :
        
          #if self.x_seg[0]<self.height-100 and self.x_seg[1]<self.height-100 and self.x_seg[2] <self.height-100 :
          okL=1
          XL=extLeft[0]
          YL=extRight[1]
          #cv2.line(self.frame,(XL+90,YL-33),(int(self.width/2),0),(20,0,0),3)
          #cv2.line(self.frame,(XL+90,YL-33),(int(self.width/2),0),(255,255,0),1)
          cv2.rectangle(self.frame,(XL-10,YL-15),(XL+90,YL-33),(255,255,255),-1)
          cv2.rectangle(self.frame,(XL-10,YL-15),(XL+90,YL-33),(0,0,255),2)
          cv2.putText(self.frame,"LEFT ENTRY",(XL-5,YL-20),self.font, 0.4,(0,0,255),1,cv2.LINE_AA)
        if self.x_seg[25]<self.height-100 :
          okT=1
          XT=extTop[0]
          YT=extTop[1]
         # cv2.line(self.frame,(XT+45,YT-33),(int(self.width/2),0),(20,0,0),3)
         # cv2.line(self.frame,(XT+45,YT-33),(int(self.width/2),0),(255,255,0),1)
          cv2.rectangle(self.frame,(XT-10,YT-15),(XT+90,YT-33),(255,255,255),-1)
          cv2.rectangle(self.frame,(XT-10,YT-15),(XT+90,YT-33),(0,0,255),2)
          cv2.putText(self.frame,"TOP ENTRY",(XT-5,YT-20),self.font, 0.4,(0,0,255),1,cv2.LINE_AA)
    return okR,okL
       
          
         
