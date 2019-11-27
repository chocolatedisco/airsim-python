import airsim
import cv2
import numpy as np
import os
import setup_path 
import time

# connect to the AirSim simulator
client = airsim.CarClient()
client.confirmConnection()
client.enableApiControl(True)

if not os.path.exists('c:/temp/'):
    os.makedirs('c:/temp/')

for i in range(0,5):
    print(i)
    filename = 'c:/temp/py' + str(i)
    png_image = client.simGetImage(str(i), airsim.ImageType.Scene)
    airsim.write_file(os.path.normpath(filename+".png"),png_image)

#restore to original state
client.reset()
client.enableApiControl(False)

