import cv2

def show_webcam(mirror=False):
  cam = cv2.VideoCapture(0)
  while True:
    ret_val, img = cam.read()
    if mirror:
      img = cv2.flip(img, 1)
      cv2.imshow('My Webcam', img)
      if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
show_webcam(mirror=True)