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
car_controls = airsim.CarControls()

q = airsim.Quaternionr()
print(client.simGetCameraInfo("0").pose)
print(client.simGetCameraInfo("4").pose)
print(client.simGetCameraInfo("0").pose["orientation"])
print(client.simGetCameraInfo("4").pose["orientation"].Quaternionr)


#restore to original state
client.reset()

client.enableApiControl(False)