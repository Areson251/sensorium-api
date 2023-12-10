import os
import cv2
import math
import numpy as np
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

from ultralytics import YOLO


class SensorReading():
    def __init__(self) -> None:
        self.dir_path = os.path.dirname(os.path.dirname(__file__))
        self.plate_label = 0
        self.model = YOLO("data/weights/best.pt")

        self.scale_percent = 25 
        self.CIRCLE_RADIUS = None
        self.CIRCLE_CENTER = None
        self.LINE_HEIGHT = None
        self.LINE_WIDTH = None

    def get_results(self, photo):
        photo_decoded = Image.open(BytesIO(photo))
        cropped_photo = self.find_sensor(photo_decoded)
        if not cropped_photo:
            return None
        return self.detect_results(cropped_photo)
            
    def find_sensor(self, photo):
        results = self.model(photo)[0] 
        boxes = results.boxes.cpu().numpy()
        predicted_classes = boxes.cls 

        if self.plate_label not in predicted_classes:
            return None
        
        plate_idx = np.where(predicted_classes == self.plate_label)[0][0] # may be not only one plate in the photo
        # plate_box = [int(coord) for coord in boxes.xyxy[plate_idx]]
        plate_box = [int(boxes.xyxy[plate_idx][0]-50), int(boxes.xyxy[plate_idx][1]-50),
                     int(boxes.xyxy[plate_idx][2]+50), int(boxes.xyxy[plate_idx][3]+50)]
        return photo.crop(plate_box)

    def detect_results(self, img):
        photo = np.array(img)
        gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
        gray_blurred = cv2.blur(gray, (3, 3)) 
        detected_circles = cv2.HoughCircles(gray_blurred, 
                        cv2.HOUGH_GRADIENT_ALT, 1, 100, param1 = 100, 
                    param2 = 0.95, minRadius = 10, maxRadius = 400) 

        if detected_circles is not None: 
            detected_circles = np.uint16(np.around(detected_circles)) 

            for pt in detected_circles[0, :]:                           
                self.CIRCLE_RADIUS = pt[2]
                self.CIRCLE_CENTER = [pt[0], pt[1]]
                self.LINE_HEIGHT = int(self.CIRCLE_RADIUS / 2) 
                self.LINE_WIDTH = int(2 * self.CIRCLE_RADIUS * math.pi)
                            
                output3 = self.create_line_image(photo)                    
                output2 = output3[:,:,::-1]
                image = cv2.cvtColor(output2, cv2.COLOR_BGR2GRAY)

                _, thresh1 = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

                width = thresh1.shape[1]            
                s, c, s1 = 0, 0, 12000
                for col in range(thresh1.shape[1]):
                    for row in range(thresh1.shape[0]):
                        s += thresh1[row, col]

                    if s < s1:
                        c, s1 = col, s
                    s = 0

                y = width*3/40
                x = c-width/8
                return x/y + 0.2
        return None            

    def create_line_image(self, img):
        line_image = np.zeros((self.LINE_HEIGHT, self.LINE_WIDTH, 3), dtype=np.uint8)
        for row in range(line_image.shape[0]):
            for col in range(line_image.shape[1]):
                theta = math.pi *2 / self.LINE_WIDTH * (col + 1) - 1.55
                rho = self.CIRCLE_RADIUS - row - 20
                
                x = int(self.CIRCLE_CENTER[0] + rho * math.cos(theta) + 3)
                y = int(self.CIRCLE_CENTER[1] - rho * math.sin(theta) + 0)
                line_image[row, col, :] = img[y, x, :]

        line_image = cv2.rotate(line_image, cv2.ROTATE_180)
        return line_image
