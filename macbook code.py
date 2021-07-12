# import the necessary packages
from collections import OrderedDict
import numpy as np
import cv2
import dlib
import imutils
from pynput.mouse import Button, Controller
import array as arr
webcam = cv2.VideoCapture("./foo.jpg")

facial_features_cordinates = {}
classes = None

with open("yolov3.txt", 'r') as f:
    classes = [line.strip() for line in f.readlines()]
mouse=Controller()

change = 0;
prevch = 0;
changed = False
def get_output_layers(net):
    
    layer_names = net.getLayerNames()
    
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    return output_layers


def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    global changed
    if class_id==0:
        Width = img.shape[1]
        Height = img.shape[0]
        label = str(classes[class_id])
        
        color = COLORS[class_id]

        cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)
        cv2.circle(image, (int(Width/2),int(Height/2)), 5, (0,255,255))
        midx = int(Width/2)
        midy = int(Height/2)
        avx = int((x+x_plus_w)/2)
        avy = int((y+y_plus_h)/2)
        cv2.line(img,(avx,avy),(midx+5,midy),(0,0,255))
        cv2.line(img,(avx,avy),(midx-5,midy),(0,0,255))
        print("Distance from centre to general location:{0}".format(midx-avx))
        change = abs(midx-avx)
        #true = spin, false = stop
        if change<150:
            if (changed):
                print("stop rotate")
                mouse.click(Button.left, 1)
                changed = False
        else:
            if not changed:
                print("rotate")
                mouse.click(Button.left, 1)
                changed = True
        cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
while True:
    webcam = cv2.VideoCapture("./foo.jpg")
    res, frame = webcam.read()
    if res:
        
        image = frame
        #print('Original Dimensions : ',image.shape)
        #image = imutils.resize(image, width=500)
        Width = image.shape[1]
        Height = image.shape[0]
        scale = 0.00392
        blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(get_output_layers(net))
        class_ids = []
        confidences = []
        boxes = []
        conf_threshold = 0.5
        nms_threshold = 0.4
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                cv2.circle(image, (int(Width/2),int(Height/2)), 5, (0,255,255))
                if confidence > 0.5:
                    center_x = int(detection[0] * Width)
                    center_y = int(detection[1] * Height)
                    w = int(detection[2] * Width)
                    h = int(detection[3] * Height)
                    #print(Width/2)
                    
                    x = center_x - w / 2
                    y = center_y - h / 2
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])


        indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
        if not len(indices):
            if not changed:
                print("rotate")
                mouse.click(Button.left, 1)
                changed = True
        for i in indices:
            i = i[0]
            box = boxes[i]
            x = box[0]
            y = box[1]
            w = box[2]
            h = box[3]
            draw_prediction(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))

#image = cv2.imread("images/image_1.jpg")

webcam.release()
cv2.destroyAllWindows()


# detect faces in the grayscale image


# loop over the face detections

