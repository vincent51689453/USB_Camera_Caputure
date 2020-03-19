import numpy as np
import cv2

index = 0
cap = cv2.VideoCapture(1)
print("[INFO] Press <<x>> to capture")
print("[INFO] Press <<q>> to quit") 

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Flip image horizontally
    frame_H = cv2.flip(frame,0)
    

    # Display the resulting frame
    cv2.imshow('USB_Camera',frame_H)

    key = cv2.waitKey(1)
    if key == ord('x'):
        print("[INFO]Frame is captured!")
        index+=1
        output_name = 'capture_'+str(index)+'.jpg'
        output_path = './output_frames/'+output_name
        print("[INFO] Here is the saving path:")
        print("-----> "+output_path)
        cv2.imwrite(output_path,frame_H)
    if key & 0xFF == ord('q'):
        print("[INFO] System Closed!")
        break
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
