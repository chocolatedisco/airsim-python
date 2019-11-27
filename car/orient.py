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
print(client.simGetCameraInfo("1").pose.orientation)
print(client.simGetCameraInfo("2").pose.orientation)
print(client.simGetCameraInfo("3").pose.orientation)
print(client.simGetCameraInfo("4").pose.orientation)

from pyquaternion import Quaternion
w = client.simGetCameraInfo("0").pose.orientation.w_val
x = client.simGetCameraInfo("0").pose.orientation.x_val
y = client.simGetCameraInfo("0").pose.orientation.y_val
z = client.simGetCameraInfo("0").pose.orientation.z_val
q_f = Quaternion(w,x,y,z)
q_1 = Quaternion(axis=[1, 0, 0], angle=3.14159265)
q_2 = Quaternion(axis=[0, 1, 0], angle=3.14159265)
q_3 = Quaternion(axis=[1, 1, 0], angle=3.14159265)
q_tmp = q_f*q_3
q = airsim.Quaternionr(q_tmp[0],q_tmp[1],q_tmp[2],q_tmp[3])
client.simSetCameraOrientation("1",q)
q_tmp = q_f*q_3
q = airsim.Quaternionr(q_tmp[0],q_tmp[1],q_tmp[2],q_tmp[3])
client.simSetCameraOrientation("2",q)
q_tmp = q_f*q_3
q = airsim.Quaternionr(q_tmp[0],q_tmp[1],q_tmp[2],q_tmp[3])
client.simSetCameraOrientation("3",q)

#restore to original state
client.reset()

client.enableApiControl(False)