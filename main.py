# @Author: Mustafa Osman Dilmaç
# A python code to augment the datasets

import os
import cv2
import numpy as np

# -> Fotoğrafları döndürmek için kullanılan fonksiyon
def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

# -> Fotoğrafların parlaklığını artırmak için kullanılan fonksiyon
def increase_brightness(image, value=30):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return image

# -> Fotoğrafların parlaklığını azaltmak için kullanılan fonksiyon
def decrease_brightness(image, value=30):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v[v < value] = 0
    v[v >= value] -= value
    final_hsv = cv2.merge((h, s, v))
    image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return image

# -> Fotoğraflara gürültü eklemek için kullanılan fonksiyon (salt-pepper noise)
def add_noise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    out = np.copy(image)
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    out[coords[0], coords[1], :] = 1
    num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    out[coords[0], coords[1], :] = 0
    return out

# -> Fotoğrafları 1280x720 boyutuna getirmek için kullanılan fonksiyon
def resize_image(image):
    image = cv2.resize(image, (1280, 720))
    return image

# -> Veri setinin bulunduğu klasör yolu
path = "dataset"

# -> Klasördeki sınıfların listesi -> alt klasörler
classes = os.listdir(path)

# -> Önce fotoğrafları yeniden boyutlandıracak ardından sırasıyla bütün augment işlemlerini yapacak olan fonksiyon
def augment_images():
    for c in classes:
        print("Sınıf: ", c)
        images = os.listdir(path + "/" + c)
        for img in images:
            image = cv2.imread(path + "/" + c + "/" + img)
            image = resize_image(image)
            cv2.imwrite(path + "/" + c + "/" + img, image)
            image = cv2.imread(path + "/" + c + "/" + img)
            cv2.imwrite(path + "/" + c + "/" + img.split(".")[0] + "_1.jpg", rotate_image(image, 90))
            cv2.imwrite(path + "/" + c + "/" + img.split(".")[0] + "_2.jpg", rotate_image(image, 180))
            cv2.imwrite(path + "/" + c + "/" + img.split(".")[0] + "_3.jpg", rotate_image(image, 270))
            cv2.imwrite(path + "/" + c + "/" + img.split(".")[0] + "_4.jpg", increase_brightness(image))
            cv2.imwrite(path + "/" + c + "/" + img.split(".")[0] + "_5.jpg", decrease_brightness(image))
            cv2.imwrite(path + "/" + c + "/" + img.split(".")[0] + "_6.jpg", add_noise(image))


if __name__ == "__main__":
    augment_images()
    print("İşlem tamamlandı.")