import cv2 

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # draw circle where mouse is clicked
        cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
        
        # add text with coordinates next to circle
        text = str(x) + ", " + str(y)
        cv2.putText(frame, text, (x + 5, y + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow("frame", frame)
        print(x, y)
        


# get first frame of video
cap = cv2.VideoCapture("./data/redcar.mp4")
ret, frame = cap.read()

# get dimensions of frame
height, width, channels = frame.shape
print(height, width)

# show image
cv2.namedWindow("frame")
cv2.setMouseCallback("frame", mouse_callback)

cv2.imshow("frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()