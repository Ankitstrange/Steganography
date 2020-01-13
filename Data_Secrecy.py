# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:56:51 2019

@author: Ankit
"""
import cv2
import numpy as np
import random
class Stegno():
    
    def get_image(self, image_path):
        img = cv2.imread(image_path, 1)
        ri1 = np.array(img)
        cache = [ri1.shape[0], ri1.shape[1], ri1.shape[2]]
        ri1 = ri1.reshape(cache[0] * cache[1] * cache[2], 1)
        ri1 = ri1.astype(int)
        return ri1, cache
    
    def get_image2(self, image_path):
        img = cv2.imread(image_path, 0)
        ri1 = np.array(img)
        ri1 = cv2.resize(ri1, (400, 400))
        ri1 = ri1.reshape(400 * 400, 1)
        ri1 = ri1.astype(int)
        return ri1
    
    def image_to_binary(self, ri1):
        ri2 = []
        for i in range(ri1.shape[0]):
            a = int(ri1[i])
            ri2.append(format(a, "b"))
        return ri2
    
    def bit(self, message):
        m = []
        seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&abcdefghijklmnopqrstuvwxyz"
        key = ""
        for i in range(10):
            key = key + random.choice(seq)
        message = key+message
        for i in message:
            m.append(ord(i))
        m.append('1023')
        m = np.array(m)
        m = m.reshape(m.shape[0], 1)
        m1 = []
        for i in range(len(m)):
            a = int(m[i])
            m1.append(format(a, "b"))
        m2 = []
        for i in range(len(m1)):
            a = list(m1[i])
            c = len(a)
            while c != 10:
                a.insert(0, 0)
                c += 1
            for j in range(c):
                m2.append(int(a[j]))    
        return m2, key    
  
    def bit2(self, image2):
        ri1 = []
        for i in range(len(image2)):
            a = int(image2[i])
            ri1.append(a)
        seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&abcdefghijklmnopqrstuvwxyz"
        key = ""
        for i in range(10):
            key = key + random.choice(seq)
        for i in range(len(key)):
            ri1.insert(i, ord(key[i]))
        ri1.append('1023')
        ri1 = np.array(ri1)
        ri1 = ri1.reshape(ri1.shape[0], 1)
        m1 = []
        for i in range(len(ri1)):
            a = int(ri1[i])
            m1.append(format(a, "b"))
        m2 = []
        for i in range(len(m1)):
            a = list(m1[i])
            c = len(a)
            while c != 10:
                a.insert(0, 0)
                c += 1
            for j in range(c):
                m2.append(int(a[j]))    
        return m2, key
    
    def modified_image(self, m2, ri2, cache):
        l = len(m2)
        ri3 = []
        for i in range(len(ri2)):
            a = ri2[i]
            if l == 0:
                ri3.append(a)
            if l != 0:
                a = list(a)
                a[-1] = m2[i]
                b = ''
                for j in range(len(a)):
                    b = b + str(a[j])            
                ri3.append(b)
                l -= 1
        ri4 = []    
        for i in range(len(ri3)):
            a = int(ri3[i], 2)
            ri4.append(a)
        ri1 = []
        for i in range(len(ri2)):
            a = int(ri2[i], 2)
            ri1.append(a)
        ri1 = np.array(ri1)
        ri4 = np.array(ri4)
        distortion = np.sum(np.abs(ri4-ri1))
        img1 = np.array(ri4)
        img1 = img1.reshape(cache[0], cache[1], cache[2])
        img1 = img1.astype("uint8")
        ri5 = cv2.resize(img1, (cache[1], cache[0]))
        return ri5, distortion
    
    def retriving_data(self, ri5, entered_key):
        ri6 = []
        for i in range(len(ri5)):
            a = int(ri5[i])
            a = format(a, "b")
            a = a[-1]
            ri6.append(a)
        ri6 = [ri6[n:n+10] for n in range(0, len(ri5), 10)]
        ri7 = []
        for i in range(len(ri6)):
            a = ri6[i]
            b = ''
            for j in range(len(a)):
                b = b + str(a[j])
            if int(b, 2) == 1023:
                break
            ri7.append(b)
        ri8 = []
        for i in range(len(ri7)):
            a = ri7[i]
            ri8.append(chr(int(a, 2)))
        d = ''
        for i in range(len(ri8)):
            d = d + str(ri8[i])
        if d[0:10] != entered_key:
            d = "You have entered wrong key!"
        else:
            d = d[10:]
        return d    
    
    def retriving_data1(self, ri5, entered_key):
        ri6 = []
        for i in range(len(ri5)):
            a = int(ri5[i])
            a = format(a, "b")
            a = a[-1]
            ri6.append(a)
        ri6 = [ri6[n:n+10] for n in range(0, len(ri5), 10)]
        ri7 = []
        for i in range(len(ri6)):
            a = ri6[i]
            b = ''
            for j in range(len(a)):
                b = b + str(a[j])
            if int(b, 2) == 1023:
                break
            ri7.append(b)
        ri8 = []
        for i in range(len(ri7)):
            a = ri7[i]
            ri8.append(int(a, 2))
        d = ''
        for i in range(10):
            d = d + chr(ri8[i])
        if d != entered_key:
            d = "You have entered wrong key!"
            return d
        else:
            ri9 = []
            for i in range(10, len(ri8)):
                ri9.append(ri8[i])
            ri9 = np.array(ri9)
            img1 = ri9.reshape(400, 400)
            img1 = img1.astype("uint8")
            img1 = cv2.resize(img1, (400, 400))
            return img1
