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


def gray_to_binary(n):
  n = int(n, 2)
  mask = n
  while mask != 0:
      mask >>= 1
      n ^= mask
  return bin(n)[2:]


def showData(image):
  binary_data1=""
  for values in image:
    for pixel in values:
      r,g,b=messageToBinary(pixel)
      #binary_data1+=r[-1]
      #binary_data1+=g[-1]
      binary_data1+=b[-1]
  a=len(binary_data1)
  binary_data=gray_to_binary(binary_data1)
  binary_data=binary_data.zfill(a)
  all_bytes=[binary_data[i:i+8] for i in range(0,len(binary_data),8)]
  decoded_data=""
  for byte in all_bytes:
    decoded_data+=chr(int(byte,2))
    if(decoded_data[-5:]=="#####"):
      break
  return decoded_data[:-5]




def decode_text():
  image_name=input("Enter the name of the stegnographed image which is needed to be decoded with extension: ")
  image=cv2.imread(image_name)
  print("stegnographed imgage: ")
  resized_image=cv2.resize(image,(500,500))
  cv2.imshow('image',resized_image)
  text=showData(image)
  return text



print("\nSteganography Decoding:-")
print("Decoded Data is: "+ decode_text())

