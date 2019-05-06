import cv2

def main():
    windowname = "Live Video Feed"
    cv2.namedWindow(windowname)
    cap = cv2.VideoCapture(0)

    print(cap.get(3))
    print(cap.get(4))

    # cap.set(3,1080)
    # cap.set(4,786)
    window_width = int(cap.shape[1] * scale)
    window_height = int(cap.shape[0] * scale)

    print(cap.get(3))
    print(cap.get(4))
    cv2.resizeWindow('Resized Window', window_width, window_height)


    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    
    while ret:
        ret,frame = cap.read()

        output = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.imshow(windowname,frame)
        # cv2.imshow('Gray',output)
        # cv2.imshow('Blue',output)
        if cv2.waitKey(1) == 27:
            break
    

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()