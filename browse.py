import numpy as np
import matplotlib.pyplot as plt
import json
import os
import cv2

GQA_Path = "/GQA/"
filenames = os.listdir(GQA_Path)
filenames.sort()
for filename in filenames[0:1000]:
    path = GQA_Path + filename
    img = cv2.imread(path, 0)
    cv2.imshow(filename, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

