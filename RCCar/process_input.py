
#!/usr/bin/env python

import cv2

def process_simplify_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3)
    return thresh

def process_video_file(path):
    cap = cv2.VideoCapture(path)
    print(cap)
    print(cap.isOpened())
    while (cap.isOpened()):
        ret, frame = cap.read()
        simplified = process_simplify_image(frame)
        cv2.imshow('input', simplified)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # image = cv2.imread('test.jpg', 0)
    # blurred = cv2.GaussianBlur(image, (5, 5), 0)
    # thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3) 
    # matplotlib.pyplot.imshow(tresh, 'output')
    process_video_file("C:/Users/toshiba/Videos/cash.mp4")
