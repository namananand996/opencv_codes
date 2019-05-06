import cv2

def main():

    windowname = "Vedio Save"
    cv2.namedWindow(windowname,cv2.WINDOW_AUTOSIZE)

    cap = cv2.VideoCapture(0)

    # parameter of vedio save
    filename = "D:\\open_cv\\open_cv_code\\data\\data.avi"
    codec = cv2.VideoWriter_fourcc('X','V','I','D')
    framerate = 10
    resolution = (640,480)

    fileOutput = cv2.VideoWriter(filename,codec,framerate,resolution)

    if cap.isOpened() == True:
        ret,frame = cap.read()
    else:
        ret = False
    
    while ret:

        ret,frame = cap.read()

        fileOutput.write(frame)

        # output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("vedio",frame)

        if cv2.waitKey(1) == 27:
            break
    
    cv2.destroyAllWindows()
    fileOutput.release()
    cap.release()


if __name__ == "__main__":
    main()