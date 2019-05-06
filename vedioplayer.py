import cv2

def main():
    
    windowname = "Vedio Player"
    cv2.namedWindow(windowname)

    filename = "D:\\open_cv\\open_cv_code\\data\\data.avi"

    cap = cv2.VideoCapture(filename)
    
    while cap.isOpened() == True:

        ret,frame = cap.read()
        print(ret)

        if ret:
            cv2.imshow(windowname,frame)
            if cv2.waitKey(100) == 27:
                break
        else:
            break
        
    
    cv2.destroyWindow(windowname)
    cap.release()

if __name__ == "__main__":
    main()