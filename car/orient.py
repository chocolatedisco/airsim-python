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

print(client.simGetCameraInfo("0").pose.orientation)

w = client.simGetCameraInfo("0").pose.orientation.w_val
x = client.simGetCameraInfo("0").pose.orientation.x_val
y = client.simGetCameraInfo("0").pose.orientation.y_val
z = client.simGetCameraInfo("0").pose.orientation.z_val
q = airsim.Quaternionr(x,y,z,w)
print(q.get_length())
client.simSetCameraOrientation("1",q)

q = airsim.Quaternionr(x,y,z,w).conjugate()
client.simSetCameraOrientation("2",q)

#restore to original state
client.reset()

client.enableApiControl(False)