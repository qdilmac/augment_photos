# @Author: Mustafa Osman Dilmaç
# A python code to augment the dataset by rotating the images

import os
import cv2
import numpy as np

# -> Fotoğrafları döndürmek için kullanılan fonksiyon
def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

# -> Fotoğrafları 640x640 boyutuna getirmek için kullanılan fonksiyon
def resize_image(image):
    image = cv2.resize(image, (640, 640))
    return image

# -> Veri setinin bulunduğu klasör yolu
path = "dataset"

# -> Klasördeki sınıfların listesi -> alt klasörler
classes = os.listdir(path)

# -> Alt klasörlerdeki resimlerin yeniden boyutlandırılması, dikeyde ve yatayda döndürülmesi

for i in classes:
    print(f"{i} sınıfı için işlem yapılıyor.")
    images = os.listdir(os.path.join(path, i))
    for j in images:
        image = cv2.imread(os.path.join(path, i, j))
        image = resize_image(image)
        cv2.imwrite(os.path.join(path, i, "resized_" + j), image)
        for angle in [90, 180, 270]:
            rotated_image = rotate_image(image, angle)
            cv2.imwrite(os.path.join(path, i, "rotated_" + str(angle) + "_" + j), rotated_image)
    print(f"{i} sınıfı için işlem tamamlandı.")





        
print("Resimler üzerinde döndürme işlemi tamamlandı.")