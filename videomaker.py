#raspberry pi code. requires device that does object detection to have ssh enabled.
import picamera
import os
import subprocess
import time
while True:
    if True:
        camera = picamera.PiCamera()
        camera.resolution = (640, 480)
        camera.capture('foo.jpg')
        #insert your own credentials and file location here
        os.system('sshpass -p "password" scp foo.jpg user@devicename:/path/to/folder')
        camera.close()

        