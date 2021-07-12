# dysonfanautoturn
Code from ShizumeruMaking's YouTube Video about turning fans but without hands


the weights for the object detection can be downloaded here: https://pjreddie.com/media/files/yolov3.weights


download them and just drop them in that folder and you should be good. (sorry to the people who actually know what they're doing)

# setup
after extracting, do pip install -r requirements.txt. this should install all the necessary libraries to run the code.

then, go through the instructions to set up homebridge:https://github.com/homebridge/homebridge

after setting it up, search for the dyson pure cool link plugin and go through the setup process.  you can find your fan's ip address by using arp -a. the fan's device name should be the serial number of the fan.

for the raspberry pi, just put in your ssh credentials into videomaker.py so that it can send the images it'll take to the device that you're accessing the home app on, then run videomaker.py. it should start sending the image(foo.jpg) to that device. 

finally, just run macbook code.py and then hover your cursor over the oscillate button. Feel free to reach out if there are any issues or if you have any ways to improve upon this design.
