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

# -> Veri setinin bulunduğu klasör yolu
path = "dataset"

# -> Klasördeki sınıfların listesi -> alt klasörler
classes = os.listdir(path)

# -> Alt klasörlerdeki resimlerin döndürülmesi

for class_name in classes:
    # -> Sınıfın klasör yolu
    class_path = os.path.join(path, class_name)
    # -> Klasördeki resimlerin listesi
    images = os.listdir(class_path)
    # -> Her bir resmi döndür
    for image_name in images:
        # -> Resmin yolu
        image_path = os.path.join(class_path, image_name)
        # -> Resmi oku
        image = cv2.imread(image_path)
        # -> Resmi 90 derece döndür
        rotated_image = rotate_image(image, 90)
        # -> Döndürülmüş resmin yolu
        rotated_image_path = os.path.join(class_path, image_name
                                             .replace(".png", "_rotated_90.png")) # UZANTI ÖNEMLİ!!

        cv2.imwrite(rotated_image_path, rotated_image)

        rotated_image = rotate_image(image, 180)

        rotated_image_path = os.path.join(class_path, image_name
                                             .replace(".png", "_rotated_180.png"))

        cv2.imwrite(rotated_image_path, rotated_image)

        rotated_image = rotate_image(image, 270)

        rotated_image_path = os.path.join(class_path, image_name
                                                .replace(".png", "_rotated_270.png"))

        cv2.imwrite(rotated_image_path, rotated_image)

        
print("Resimler üzerinde döndürme işlemi tamamlandı.")