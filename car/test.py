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

print(client.simGetCameraInfo("0"))
print(client.simGetCameraInfo("0").pose.orientation)
print(client.simGetCameraInfo("1").pose.orientation)
print(client.simGetCameraInfo("2").pose.orientation)
print(client.simGetCameraInfo("3").pose.orientation)
print(client.simGetCameraInfo("4").pose.orientation)

#restore to original state
client.reset()

client.enableApiControl(False)