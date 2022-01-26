import AirDrawModule as adm
import cv2 as cv

ob=adm.airdraw()

capture=cv.VideoCapture(0)
capture.set(3,1280)
capture.set(4,720)

while(True):
    isTrue,frame=capture.read()

    if(isTrue):
        frame=ob.start_drawing(frame)

        cv.imshow('AirDraw!',frame)

        if(cv.waitKey(1)&0xFF==ord('q')):
            break

    else:
        break

capture.release()
cv.destroyAllWindows()