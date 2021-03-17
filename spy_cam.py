import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity
import logging
from datetime import datetime
import time

if __name__ == '__main__':
    cv2.namedWindow("last")
    cv2.namedWindow("curr")
    cv2.namedWindow("diff")
    vc = cv2.VideoCapture(0)
    r,v = vc.read() # throw away first frame
    
    logging.basicConfig(filename='LOG.log', filemode='w', level=logging.DEBUG)

    print("Press ESC with Preview window active to end.")

    while vc:
        
        suffix = datetime.now().strftime('%Y%B%d_%H-%M-%S.%f')
        
        rval1, frame1 = vc.read()
        time.sleep(1) # compare captures 1 second apart
        rval2, frame2 = vc.read()
        
        #cv2.imwrite(name,frame)
        
        last_capture = frame1
        curr_capture = frame2
        
        last_capture = cv2.cvtColor(last_capture, cv2.COLOR_BGR2GRAY)
        curr_capture = cv2.cvtColor(curr_capture, cv2.COLOR_BGR2GRAY)
        (score, diff) = structural_similarity(last_capture, curr_capture, full=True)
        print('score: %f' % score)
        
        th = 0.9
        if score <= th:
            filename = "cap%s.jpg" % suffix
            cv2.imwrite(filename,frame2)
            logging.debug("Detected anomaly in %s" % filename)
        
        cv2.imshow("last",last_capture)
        cv2.imshow("curr",curr_capture)
        cv2.imshow("diff",diff)

        
        # check if user wants to end using ESC
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
    
    # cv2.destroyWindow("last")
    # cv2.destroyWindow("curr")
    # cv2.destroyWindow("diff")
    vc.release()
    cv2.destroyAllWindows()