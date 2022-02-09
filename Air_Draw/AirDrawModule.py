import HandTrackModule as htm
import cv2 as cv
import os
import numpy as np

class airdraw:

    def __init__(self):

        self.obj=htm.detect_hands(MIN_DETECTION_CONFIDENCE=0.75)
        self.radius=[10,20,30]
        self.color=[(22,22,255),(255,182,56),(55,128,0),(89,222,255),(255,255,255),(0,0,0)]
        self.cno=0
        self.rno=0
        self.x=0
        self.y=0
        self.xp=0
        self.yp=0
        self.sx=0
        self.sy=0
        self.sxp=0
        self.syp=0
        self.save=0
        self.isblank=0
        self.blank=np.zeros((720,1280,3),dtype='uint8')

        # using templates to make drawing experience more interactive
        path1=r'color_template'
        dirs1=sorted(os.listdir(path1))
        self.imgs1=[]
        for i in dirs1:
            self.imgs1.append(cv.imread(os.path.join(path1,i)))

        path2=r'thickness_template'
        dirs2=sorted(os.listdir(path2))
        self.imgs2=[]
        for i in dirs2:
            self.imgs2.append(cv.imread(os.path.join(path2,i)))

        path3=r'background_template'
        dirs3=sorted(os.listdir(path3))
        self.imgs3=[]
        for i in dirs3:
            self.imgs3.append(cv.imread(os.path.join(path3,i)))

        self.color_template=self.imgs1[0]
        self.thickness_template=self.imgs2[0]
        self.background_template=self.imgs3[0]

    def start_drawing(self,bgr_img):

        bgr_img,self.lms=self.obj.mark_hands(bgr_img,False,True)
        self.status=self.obj.finger_status()

        if(self.isblank==1):
            bgr_img=np.zeros((720,1280,3),dtype='uint8')

        h,w=bgr_img.shape[:2]

        bgr_img[0:125,0:1280]=self.color_template
        bgr_img[125:720,1080:1280]=self.thickness_template
        bgr_img[125:720,980:1080]=self.background_template
    
        # When drawing
        if(self.status[1]==1 and self.status[2]==0 and self.status[3]==0 and self.status[4]==0 and self.lms!=[(0,0)]*21):           
            self.x=int(self.lms[8][0]*w)
            self.y=int(self.lms[8][1]*h)

            if(self.cno==5):
                cv.circle(bgr_img,(self.x,self.y),20,(236,235,190),5)  

            else:
                cv.circle(bgr_img,(self.x,self.y),20,self.color[self.cno],5)  

            if(self.xp==0 and self.yp==0):
                self.xp=self.x
                self.yp=self.y

            cv.line(self.blank,(self.x,self.y),(self.xp,self.yp),self.color[self.cno],self.radius[self.rno]) 
            
            self.xp=self.x
            self.yp=self.y

            self.sx=self.x
            self.sy=self.y

        # When not drawing, but tweaking options
        elif(self.status[1]==1 and self.status[2]==1 and self.status[3]==0 and self.status[4]==0 and self.lms!=[(0,0)]*21):
            self.sx=int((self.lms[8][0]*w+self.lms[12][0]*w)*0.5)
            self.sy=int((self.lms[8][1]*h+self.lms[12][1]*h)*0.5)

            self.sxp=self.sx 
            self.syp=self.sy

            cv.circle(bgr_img,(self.sx,self.sy),20,(226,43,138),5)         

            self.xp=0
            self.yp=0

            if(30<=self.sx and self.sx<=70 and 30<=self.sy and self.sy<=70):
                self.cno=0
                self.color_template=self.imgs1[self.cno]
                self.thickness_template=self.imgs2[3*self.cno+self.rno]
            elif(210<=self.sx and self.sx<=250 and 30<=self.sy and self.sy<=70):
                self.cno=1
                self.color_template=self.imgs1[self.cno]
                self.thickness_template=self.imgs2[3*self.cno+self.rno]
            elif(390<=self.sx and self.sx<=430 and 30<=self.sy and self.sy<=70):
                self.cno=2
                self.color_template=self.imgs1[self.cno]
                self.thickness_template=self.imgs2[3*self.cno+self.rno]
            elif(580<=self.sx and self.sx<=620 and 30<=self.sy and self.sy<=70):
                self.cno=3
                self.color_template=self.imgs1[self.cno]
                self.thickness_template=self.imgs2[3*self.cno+self.rno]
            elif(770<=self.sx and self.sx<=810 and 30<=self.sy and self.sy<=70):
                self.cno=4
                self.color_template=self.imgs1[self.cno]
                self.thickness_template=self.imgs2[3*self.cno+self.rno]
            elif(960<=self.sx and self.sx<=1000 and 30<=self.sy and self.sy<=70):
                self.cno=5
                self.color_template=self.imgs1[self.cno]
                self.thickness_template=self.imgs2[3*self.cno+self.rno] 
            elif(1130<=self.sx and self.sx<=1210 and 50<=self.sy and self.sy<=70):  
                self.blank=np.zeros((720,1280,3),dtype='uint8')
                print("Cleared the drawing!")       
            
            elif(1150<=self.sx and self.sx<=1210 and 175<=self.sy and self.sy<=200):
                self.rno=0
                self.thickness_template=self.imgs2[3*self.cno+self.rno]                
            elif(1150<=self.sx and self.sx<=1220 and 315<=self.sy and self.sy<=340):
                self.rno=1
                self.thickness_template=self.imgs2[3*self.cno+self.rno]                
            elif(1130<=self.sx and self.sx<=1250 and 480<=self.sy and self.sy<=510):
                self.rno=2
                self.thickness_template=self.imgs2[3*self.cno+self.rno]
                
            elif(1025<=self.sx and self.sx<=1050 and 165<=self.sy and self.sy<=175):
                self.save=1
            elif(1020<=self.sx and self.sx<=1040 and 250<=self.sy and self.sy<=350):
                self.background_template=self.imgs3[0]
                self.isblank=0
            elif(1020<=self.sx and self.sx<=1040 and 420<=self.sy and self.sy<=570):
                self.background_template=self.imgs3[1]
                self.isblank=1

        else:
            self.xp=0
            self.yp=0

        gray_blank=cv.cvtColor(self.blank,cv.COLOR_BGR2GRAY)   
        thresh,inv_blank=cv.threshold(gray_blank,20,255,cv.THRESH_BINARY_INV)
        inv_blank=cv.cvtColor(inv_blank,cv.COLOR_GRAY2BGR)
        bgr_img=cv.bitwise_or(cv.bitwise_and(inv_blank,bgr_img),self.blank)                

        if(self.save==1):
            cv.imwrite('Saved.jpg',bgr_img[125:720,0:960])
            print("Saved Image")
            self.save=0
            
        return bgr_img


def main():

    newobj=airdraw()

    capture=cv.VideoCapture(0)
    capture.set(3,1280)
    capture.set(4,720)

    while(True):
        isTrue, frame=capture.read()

        if(isTrue):

            frame=newobj.start_drawing(frame)

            cv.imshow('AirDraw!',frame)

            if(cv.waitKey(1)&0xFF==ord('q')):
                break
        else:
            break

    capture.release()
    cv.destroyAllWindows()    

if __name__=='__main__':
    main()