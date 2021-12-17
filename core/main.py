import cv2 as cv, numpy as np
from class_matlab import *

#e1 = eng("./core_m/")

if __name__ == '__main__':
    
    img = cv.imread("./img_datasets/standard_256/house_256.tif")
    img = img[:,:,0]


    if img is None:
        print("Could not read img...")
    else:
        print(type(img))

    e1 = eng()
    t = matlab.uint8(img.tolist())
    i = e1.eng.medfilt2(t)

    print(type(i))

    i = np.asarray(i, dtype=np.uint8)

    cv.imshow("Display window", i)

    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("starry_night.png", i)

    del e1