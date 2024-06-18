# -> Function to convert jpeg(can be changed according to need) files to jpg

import os
import cv2

path = "dataset"
classes = os.listdir(path)

def convert_jpeg_to_jpg():
    for c in classes:
        print("Sınıf: ", c)
        class_path = os.path.join(path, c)
        images = os.listdir(class_path)
        for img in images:
            if img.endswith(".jpeg"): # -> can be modified as .png etc.
                img_path = os.path.join(class_path, img)
                image = cv2.imread(img_path)
                new_img_path = os.path.join(class_path, img.replace(".jpeg", ".jpg"))
                cv2.imwrite(new_img_path, image)
                os.remove(img_path)

convert_jpeg_to_jpg()
