# Run this and then run labelImg on training-images

import cv2
import os
import time
import uuid

IMAGES_PATH = '../training-images'
labels = ['✋', '✋-left', '🤟', '🤟-left', '👈', '👈-left', '👌']
number_imgs = 15

if __name__ == "__main__":
    for label in labels:
        directory_path = os.path.join(IMAGES_PATH, label)
        os.makedirs(directory_path, exist_ok=True)

        video = cv2.VideoCapture(0)
        print(f"Capture images for: {label}")
        time.sleep(5)

        for i in range(number_imgs):
            ret, frame = video.read()
            image_name = os.path.join(directory_path, f"{label}_{str(uuid.uuid1())}.jpg")
            cv2.imwrite(image_name, frame)
            cv2.imshow('Capturing Images', frame)
            time.sleep(1)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video.release()

    cv2.destroyAllWindows()
