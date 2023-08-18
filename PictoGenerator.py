import cv2
import numpy as np
from rembg import remove
from PIL import Image
import os
from pathlib import Path
from math import *  
import subprocess

#Use image processing techniqes (mainly the rembg library) to extract the contour from the background
image_array = []
def clean_pictures(folder):
    image_array = []
    for file in sorted(os.listdir(folder)):
        if file.endswith('.jpg'):
          print(file)
          img = cv2.imread((folder + file), cv2.COLOR_BGR2GRAY)
          isolated_img = remove(img)
          image = Image.fromarray(isolated_img)
          new_image = Image.new("RGBA", image.size, "GREEN")
          new_image.paste(image, (0, 0), image)
          new_image = np.array(new_image)
          #take the rembg output and process it correctly to output a matte photo of the input
          mask = cv2.inRange(new_image, (0,126,0,220), (5,130,5,280))
          imask = mask>0
          green = np.zeros_like(new_image, np.uint8)
          green[imask] = new_image[imask]
          gray = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)
          _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
          image_array.append(threshold)
    return image_array

#Use the dimensions of the images to resize them all to fit a standardized size 
def resize_images(image_array):
    ret, thresh1 = cv2.threshold(cv2.bitwise_not(image_array[0]), 127, 255, 0)
    ret, thresh2 = cv2.threshold(cv2.bitwise_not(image_array[1]), 127, 255, 0)
    ret, thresh3 = cv2.threshold(cv2.bitwise_not(image_array[2]), 127, 255, 0)
    contours1, hierarchy1 = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours2, hierarchy2 = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours3, hierarchy3 = cv2.findContours(thresh3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    largest_contour1 = max(contours1, key=cv2.contourArea)
    largest_contour2 = max(contours2, key=cv2.contourArea)
    largest_contour3 = max(contours3, key=cv2.contourArea)
    _, _, w1, h1 = cv2.boundingRect(largest_contour1)
    _, _, w2, h2 = cv2.boundingRect(largest_contour2)
    _, _, w3, h3 = cv2.boundingRect(largest_contour3)
    #This is the specific logic, it compares different dimensions together
    up_points = (image_array[0].shape[1], image_array[0].shape[0])
    resized_1 = cv2.resize(image_array[0], up_points, interpolation= cv2.INTER_LINEAR)
    up_points = (int(image_array[1].shape[1] * w1 / w2), (int(image_array[1].shape[0] * w1 / w2)))
    resized_2 = cv2.resize(image_array[1], up_points, interpolation= cv2.INTER_LINEAR)
    up_points = (int(image_array[2].shape[1] * h1 / w3), int(image_array[2].shape[0] * h1 / w3))
    resized_3 = cv2.resize(image_array[2], up_points, interpolation= cv2.INTER_LINEAR)
    resized_array = [resized_1, resized_2, resized_3]
    return resized_array

#This code simply converts the largest contour to an svg file for blender and resizes it correctly
def image_to_svg(resized_array):
    svg_array = []
    x = 0
    for image in resized_array:
        x += 1
        inverted = cv2.bitwise_not(image)
        ret, thresh = cv2.threshold(inverted, 127, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        largest_contour = max(contours, key=cv2.contourArea)
        kernel = np.ones((5, 5), np.uint8)
        eroded = cv2.erode(inverted, kernel, iterations=2)
        dilated = cv2.dilate(eroded, kernel, iterations=2)
        inverted = dilated
        #This code ensures that there's exactly 10 pixels on all sides of image
        x, y, w, h = cv2.boundingRect(largest_contour)
        w = min((w + 20), inverted.shape[1] - max(0, (x - 10)))
        h = min((h + 20), inverted.shape[0] - max(0, (y - 10)))
        cropped = inverted[max(0, (y - 10)):max(0, (y - 10))+h, max(0, (x - 10)):max(0, (x - 10))+w]
        contours, hierarchy = cv2.findContours(cropped, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        largest_contour = max(contours, key=cv2.contourArea)
        kernel = np.ones((5, 5), np.uint8)
        height, width = cropped.shape[:2]
        blank_image = np.zeros((height, width, 3), np.uint8)
        cv2.drawContours(blank_image, [largest_contour], 0, (255, 255, 255), -1)
        cv2.imwrite("/Users/NBSchwa/Desktop/s/test.png", cv2.bitwise_not(blank_image))
        with Image.open('/Users/NBSchwa/Desktop/s/test.png') as img:
            img = img.convert('L')
            img_arr = np.array(img)
        #img_arr = np.array(cv2.bitwise_not(image1))
        with open('input.pgm', 'wb') as f:
            f.write(bytes(f'P5\n{img_arr.shape[1]} {img_arr.shape[0]}\n255\n', 'ascii'))
            img_arr.tofile(f)
        svg = subprocess.check_output(['potrace', '-s', '-o', '-', 'input.pgm'])
        svg_array.append(svg)
    return svg_array


if __name__=='__main__':
  image_array = clean_pictures("/Users/NBSchwa/Desktop/Picto/")
  resized_array = resize_images(image_array)
  x = 10
  for image in resized_array:
    x += 1
    cv2.imwrite("/Users/NBSchwa/Desktop/s/" + str(x) + ".png", image)
  svg_array = image_to_svg(resized_array)
  x = 0
  for svg in svg_array:
    x += 1
    with open("/Users/NBSchwa/Desktop/Script/" + str(x) + ".svg", 'wb') as f:
        f.write(svg)