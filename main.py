# starts the computer webcam, detects movement and captures a picture
import cv2
import os
import time
import glob
from emailing import send_email
from threading import Thread


def delete_images():
    print("delete_images function started")
    images_to_delete = glob.glob("images/*.png")
    for image in images_to_delete:
        os.remove(image)
    print("delete_images function ended")


video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
status_list = []
count = 0

while True:
    status = 0
    check, frame = video.read()
    # remove unnecessary information (color)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # put the first frame in a variable
    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count = count + 1
            all_images = glob.glob("images/*.png")
            email_image = all_images[int(len(all_images)/2)]

    status_list.append(status)
    status_list = status_list[-2:]
    print(status_list)

    clean_thread = Thread(target=delete_images)

    if status_list[0] == 1 and status_list[1] == 0:
        # here I use threading so the video doesn't stop while
        # waiting for the email to be sent
        email_thread = Thread(target=send_email, args=(email_image,))
        # this will be executed in the background
        email_thread.daemon = True
        email_thread.start()

    cv2.imshow("Video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
clean_thread.start()

