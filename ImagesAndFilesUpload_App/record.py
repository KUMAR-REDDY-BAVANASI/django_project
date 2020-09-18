

import cv2
import numpy as np
import pyautogui

screen_size = (1920,1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi",fourcc,20.0,(screen_size))

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    # cv2.imshow("show",frame)
    if cv2.waitKey(1) == ord("q"):
        break


# import cv2
# import numpy as np
# from PIL import ImageGrab
# import time
#
# screen_size = (1920,1080)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# filename = "output"+str(time.time())+".avi"
# out = cv2.VideoWriter("output.avi",fourcc,20.0,(screen_size))
# time.sleep(3)
#
# while True:
#     img = ImageGrab.grab()
#     img_np = np.array(img)
#     frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
#     out.write(frame)
#
#     if cv2.waitKey(1) == ord("q"):
#         break
# out.release()
# cv2.destroyAllWindows()