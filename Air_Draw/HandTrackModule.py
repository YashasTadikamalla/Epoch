import cv2 as cv
import mediapipe as mp

class detect_hands:

    # some initializations to generalize the module
    def __init__(self,STATIC_IMAGE_MODE=False,MAX_NUM_HANDS=1,MODEL_COMPLEXITY=1,MIN_DETECTION_CONFIDENCE=0.5,MIN_TRACKING_CONFIDENCE=0.5):
               
        self.STATIC_IMAGE_MODE=STATIC_IMAGE_MODE
        self.MAX_NUM_HANDS=MAX_NUM_HANDS
        self.MODEL_COMPLEXITY=MODEL_COMPLEXITY
        self.MIN_DETECTION_CONFIDENCE=MIN_DETECTION_CONFIDENCE
        self.MIN_TRACKING_CONFIDENCE=MIN_TRACKING_CONFIDENCE

        self.mp_hands=mp.solutions.hands
        self.mp_draw=mp.solutions.drawing_utils
        self.hands=self.mp_hands.Hands(self.STATIC_IMAGE_MODE,self.MAX_NUM_HANDS,self.MODEL_COMPLEXITY,self.MIN_DETECTION_CONFIDENCE,self.MIN_TRACKING_CONFIDENCE)

        self.lms=[(0,0)]*21
        self.status=[0]*5

    # to show hand connections generated using mediapipe, and to get the info related to 21 hand landmarks
    def mark_hands(self, bgr_img, draw=True,get_landmarks=False):

        bgr_img=cv.flip(bgr_img,1)
        rgb_img=cv.cvtColor(bgr_img,cv.COLOR_BGR2RGB)
        positions=self.hands.process(rgb_img)

        if(positions.multi_hand_landmarks):
            for handlms in (positions.multi_hand_landmarks): # each hand is list of 21 landmarks
                if(draw):
                    self.mp_draw.draw_landmarks(bgr_img,handlms,self.mp_hands.HAND_CONNECTIONS)
                if(get_landmarks):
                    self.lms=[(0,0)]*21
                    for id,coor in enumerate(handlms.landmark):
                        self.lms[id]=(coor.x,coor.y)

        return bgr_img,self.lms

    # to tell if a finger is open or closed
    def finger_status(self):

        if(self.lms[4][1]<self.lms[2][1]):
            self.status[0]=1
        else:
            self.status[0]=0
        if(self.lms[8][1]<self.lms[6][1]):
            self.status[1]=1
        else:
            self.status[1]=0
        if(self.lms[12][1]<self.lms[10][1]):
            self.status[2]=1
        else:
            self.status[2]=0
        if(self.lms[16][1]<self.lms[14][1]):
            self.status[3]=1
        else:
            self.status[3]=0
        if(self.lms[20][1]<self.lms[18][1]):
            self.status[4]=1
        else:
            self.status[4]=0

        return self.status
        

def main():

    capture=cv.VideoCapture(0)
    capture.set(3,1280)
    capture.set(4,720)

    obj=detect_hands()

    while(True):
        isTrue, frame=capture.read()

        if(isTrue):
            frame,landmarks=obj.mark_hands(frame)
            cv.imshow('hand_track',frame)

            if(cv.waitKey(1)&0xFF==ord('q')):
                break
        else:
            break

    capture.release()
    cv.destroyAllWindows()    

if __name__=='__main__':
    main()