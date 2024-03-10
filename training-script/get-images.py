import cv2
import os
import time
import uuid

IMAGES_PATH = 'training-images/collected-images'
labels = ['✋', '✋-left', '🤟', '🤟-left', '👈', '👈-left', '👌']
number_imgs = 15

for label in labels:
    os.makedirs(IMAGES_PATH, exist_ok=True)

    video = cv2.VideoCapture(0)
    print(f"Capture images for: {label}")
    time.sleep(5)

    for i in range(number_imgs):
        ret, frame = video.read()
        image_name = os.path.join(IMAGES_PATH, f"{label}_{str(uuid.uuid1())}.jpg")
        cv2.imwrite(image_name, frame)
        cv2.imshow('Capturing Images', frame)
        time.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()

cv2.destroyAllWindows()
