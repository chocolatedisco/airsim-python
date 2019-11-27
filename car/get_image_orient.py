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

filename = 'c:/temp/py' + str(0)
png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
airsim.write_file(os.path.normpath(filename+".png"),png_image)

w = client.simGetCameraInfo("0").pose.orientation.w_val
x = client.simGetCameraInfo("0").pose.orientation.x_val
y = client.simGetCameraInfo("0").pose.orientation.y_val
z = client.simGetCameraInfo("0").pose.orientation.z_val
q = airsim.Quaternionr(x,y,z,w).conjugate()
client.simSetCameraOrientation("0",q)
filename = 'c:/temp/py' + str(1)
png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
airsim.write_file(os.path.normpath(filename+".png"),png_image)

w = client.simGetCameraInfo("0").pose.orientation.w_val
x = client.simGetCameraInfo("0").pose.orientation.x_val
y = client.simGetCameraInfo("0").pose.orientation.y_val
z = client.simGetCameraInfo("0").pose.orientation.z_val
q = airsim.Quaternionr(x,y,z,w).inverse()
client.simSetCameraOrientation("0",q)
filename = 'c:/temp/py' + str(2)
png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
airsim.write_file(os.path.normpath(filename+".png"),png_image)

w = client.simGetCameraInfo("0").pose.orientation.w_val
x = client.simGetCameraInfo("0").pose.orientation.x_val
y = client.simGetCameraInfo("0").pose.orientation.y_val
z = client.simGetCameraInfo("0").pose.orientation.z_val
q = airsim.Quaternionr(x,y,z,w).conjugate()
client.simSetCameraOrientation("0",q)
filename = 'c:/temp/py' + str(3)
png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
airsim.write_file(os.path.normpath(filename+".png"),png_image)

w = client.simGetCameraInfo("0").pose.orientation.w_val
x = client.simGetCameraInfo("0").pose.orientation.x_val
y = client.simGetCameraInfo("0").pose.orientation.y_val
z = client.simGetCameraInfo("0").pose.orientation.z_val
q = airsim.Quaternionr(x,y,z,w).conjugate()
client.simSetCameraOrientation("0",q)
filename = 'c:/temp/py' + str(4)
png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
airsim.write_file(os.path.normpath(filename+".png"),png_image)

filename = 'c:/temp/py' + str(5)
png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
airsim.write_file(os.path.normpath(filename+".png"),png_image)

#restore to original state
client.reset()
client.enableApiControl(False)

