import cv2
import numpy as np
import types



def messageToBinary(message):
  if(type(message)==str):
    return ''.join([format(ord(i),"08b") for i in message])
  elif(type(message)==bytes or type(message)==np.ndarray):
    return [format(i,"08b") for i in message]
  elif(type(message)==int or type(message)==np.uint8):
    return format(message,"08b")
  else:
    raise TypeError("Unsupported Input Type")


def binary_to_gray(n):
    n = int(n, 2)
    n ^= (n >> 1)
    return bin(n)[2:]


def hideData(image,secret_message):
  n_bytes=image.shape[0]*image.shape[1]*3//8
  print("Maximum Bytes To Encode:",n_bytes)
  if(len(secret_message)>n_bytes):
    raise ValueError("Small size image,need bigger image")
  secret_message+="#####"
  data_index=0
  binary_secret_message1=messageToBinary(secret_message)
  a=len(binary_secret_message1)
  #print(binary_secret_message1)
  binary_secret_message=binary_to_gray(binary_secret_message1)
  binary_secret_message=binary_secret_message.zfill(a)
  #print(binary_secret_message)
  data_length=len(binary_secret_message)
  for values in image:
    for pixel in values:
      r,g,b=messageToBinary(pixel)
      '''if(data_index<data_length):
        pixel[0]=int(r[:-1]+binary_secret_message[data_index],2)
        data_index+=1
      if(data_index<data_length):
        pixel[1]=int(g[:-1]+binary_secret_message[data_index],2)
        data_index+=1'''
      if(data_index<data_length):
        pixel[2]=int(b[:-1]+binary_secret_message[data_index],2)
        data_index+=1
      if(data_index>=data_length):
        break
  return image


def encode_text():
  image_name=input("Enter image name with extension: ")
  image=cv2.imread(image_name)
  print("Shape of Image:",image.shape)
  print("Original image")
  resized_image=cv2.resize(image,(500,500))
  cv2.imshow('image',resized_image)
  data=input("Enter data to be Encoded: ")
  if(len(data)==0):
    raise ValueError('Data is empty')
  filename=input("Enter the name of new Encoded image with extension: ")
  encoded_image=hideData(image,data)
  cv2.imwrite(filename,encoded_image)



print("\nSteganography Encoding:-")
encode_text()



