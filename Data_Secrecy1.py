# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:57:26 2019

@author: Ankit
"""

from Data_Secrecy import Stegno
import cv2
S = Stegno()
print("\tEnter Your Choice:")
print("\n1.) Encode\n2.) Decode")
choice = int(input())
if choice == 1:    
    image_path = input("Enter full image path:")
    image, cache = S.get_image(image_path)
    d = input("Want to preview the image!(y|n)")
    if d == "Y" or d == "y":
        img = cv2.imread(image_path, 1)
        cv2.imshow("Preview", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    binary_converted_image = S.image_to_binary(image)
    print("\tEnter Your Choice:")
    print("\n1.)Want to hide message:\n2.)Want to hide image:")
    ch = int(input())
    if ch == 1:
        message = input("Enter message which you want to hide:")
        coded_message, key = S.bit(message)
        encoded_image, distortion = S.modified_image(coded_message, binary_converted_image, cache)
        cv2.imwrite("Modified_image.png", encoded_image)
        print("Your message is successfylly encoded in your given image with name 'Modified_image.png' having distortion = ",distortion)
        d = input("Want to preview the image!(y|n)")
        if d == "Y" or d == "y":
            img = cv2.imread("Modified_image.png", 1)
            cv2.imshow("Preview", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()    
        print("Here is your Key", key, "(Make sure you remember the key for retrival of data)")
    if ch == 2:
        image2_path = input("Enter path of image which you want to hide:")
        d = input("Want to preview the image!(y|n)")
        if d == "Y" or d == "y":
            img = cv2.imread(image2_path, 1)
            img = cv2.resize(img, (400, 400))
            cv2.imshow("Preview", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()         
        image2 = S.get_image2(image2_path)
        coded_image, key = S.bit2(image2)
        encoded_image, distortion = S.modified_image(coded_image, binary_converted_image, cache)
        cv2.imwrite("Modified_image.png", encoded_image)
        print("Your message is successfylly encoded in your given image with name 'Modified_image.png' having distortion = ",distortion)
        d = input("Want to preview the image!(y|n)")
        if d == "Y" or d == "y":
            img = cv2.imread("Modified_image.png", 1)
            cv2.imshow("Preview", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()    
        print("Here is your Key", key, "(Make sure you remember the key for retrival of data)")
if choice == 2:
    print("\tEnter Your Choice:")
    print("\n1.)Want to extract message:\n2.)Want to extract image:")
    c = int(input())
    if c == 2:
        image_path = input("Enter full image path:")
        entered_key = input("Enter Key = ")
        image, cache = S.get_image(image_path)
        image1 = S.retriving_data1(image, entered_key)
        cv2.imwrite("Extracted_image.png", image1)
        print("Your image is saved in current diectory wuth name 'Extracted_image' ")
        d = input("Want to preview image!(y|n)")
        if d == "Y" or d == "y":
            img = cv2.imread("Extracted_image.png", 1)
            cv2.imshow("Preview", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows() 
    if c == 1:
        image_path = input("Enter full image path:")
        entered_key = input("Enter Key = ")
        image, cache = S.get_image(image_path)
        message = S.retriving_data(image, entered_key)
        print(message)    
if choice != 1 and choice != 2:
    print("You have entered wrong option")