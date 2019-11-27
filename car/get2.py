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

filename = 'c:/temp/' + "none"
png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
airsim.write_file(os.path.normpath(filename+".png"),png_image)

w = client.simGetCameraInfo("0").pose.orientation.w_val
x = client.simGetCameraInfo("0").pose.orientation.x_val
y = client.simGetCameraInfo("0").pose.orientation.y_val
z = client.simGetCameraInfo("0").pose.orientation.z_val
q = airsim.Quaternionr(x,y,z,w)
client.simSetCameraOrientation("0",q)

w = client.simGetCameraInfo("0").pose.orientation.w_val
x = client.simGetCameraInfo("0").pose.orientation.x_val
y = client.simGetCameraInfo("0").pose.orientation.y_val
z = client.simGetCameraInfo("0").pose.orientation.z_val
xr = airsim.Quaternionr(1,0,0,0)
yr = airsim.Quaternionr(0,1,0,0)
zr = airsim.Quaternionr(0,0,1,0)

q = airsim.Quaternionr(x,y,z,w).inverse()
client.simSetCameraOrientation("0",q)
filename = 'c:/temp/' + "inverse"
png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
airsim.write_file(os.path.normpath(filename+".png"),png_image)

q = airsim.Quaternionr(x,y,z,w).conjugate()
client.simSetCameraOrientation("0",q)
filename = 'c:/temp/' + "conjugate"
png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
airsim.write_file(os.path.normpath(filename+".png"),png_image)

q = airsim.Quaternionr(x,y,z,w).inverse().conjugate()
client.simSetCameraOrientation("0",q)
filename = 'c:/temp/' + "inverse_conjugate"
png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
airsim.write_file(os.path.normpath(filename+".png"),png_image)

q = airsim.Quaternionr(x,y,z,w).rotate(xr)
client.simSetCameraOrientation("0",q)
filename = 'c:/temp/' + "xr"
png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
airsim.write_file(os.path.normpath(filename+".png"),png_image)

# q = airsim.Quaternionr(x,y,z,w).conjugate().conjugate()
# client.simSetCameraOrientation("0",q)
# filename = 'c:/temp/' + "conjugate_conjugate"
# png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
# airsim.write_file(os.path.normpath(filename+".png"),png_image)

# q = airsim.Quaternionr(x,y,z,w).inverse().inverse()
# client.simSetCameraOrientation("0",q)
# filename = 'c:/temp/' + "inverse_inverse"
# png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
# airsim.write_file(os.path.normpath(filename+".png"),png_image)

# q = airsim.Quaternionr(x,y,z,w).conjugate().conjugate().conjugate()
# client.simSetCameraOrientation("0",q)
# filename = 'c:/temp/' + "conjugate_conjugate_conjugate"
# png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
# airsim.write_file(os.path.normpath(filename+".png"),png_image)

# q = airsim.Quaternionr(x,y,z,w).inverse().inverse().inverse()
# client.simSetCameraOrientation("0",q)
# filename = 'c:/temp/' + "inverse_inverse_inverse"
# png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
# airsim.write_file(os.path.normpath(filename+".png"),png_image)

# q = airsim.Quaternionr(x,y,z,w).conjugate().conjugate().conjugate().conjugate()
# client.simSetCameraOrientation("0",q)
# filename = 'c:/temp/' + "conjugate_conjugate_conjugate_conjugate"
# png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
# airsim.write_file(os.path.normpath(filename+".png"),png_image)

# q = airsim.Quaternionr(x,y,z,w).inverse().inverse().inverse().inverse()
# client.simSetCameraOrientation("0",q)
# filename = 'c:/temp/' + "inverse_inverse_inverse_inverse"
# png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
# airsim.write_file(os.path.normpath(filename+".png"),png_image)

# w = client.simGetCameraInfo("0").pose.orientation.w_val
# x = client.simGetCameraInfo("0").pose.orientation.x_val
# y = client.simGetCameraInfo("0").pose.orientation.y_val
# z = client.simGetCameraInfo("0").pose.orientation.z_val
# q = airsim.Quaternionr(x,y,z,w).conjugate().conjugate().inverse()
# client.simSetCameraOrientation("0",q)
# filename = 'c:/temp/py' + str(3)
# png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
# airsim.write_file(os.path.normpath(filename+".png"),png_image)

# w = client.simGetCameraInfo("0").pose.orientation.w_val
# x = client.simGetCameraInfo("0").pose.orientation.x_val
# y = client.simGetCameraInfo("0").pose.orientation.y_val
# z = client.simGetCameraInfo("0").pose.orientation.z_val
# q = airsim.Quaternionr(x,y,z,w).conjugate().conjugate().conjugate()
# client.simSetCameraOrientation("0",q)
# filename = 'c:/temp/py' + str(4)
# png_image = client.simGetImage(str(0), airsim.ImageType.Scene)
# airsim.write_file(os.path.normpath(filename+".png"),png_image)

# filename = 'c:/temp/py' + str(5)
# png_image = client.simGetImage(str(4), airsim.ImageType.Scene)
# airsim.write_file(os.path.normpath(filename+".png"),png_image)

#restore to original state
client.reset()
client.enableApiControl(False)

