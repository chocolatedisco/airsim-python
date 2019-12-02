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

print(client.getGpsData())
print(client.getGpsLocation())
print(client.getLandedState())


#restore to original state
client.reset()

client.enableApiControl(False)