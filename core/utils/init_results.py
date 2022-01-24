'''
saves the noisy images
using the image generator
from the load dataset class
'''
import warnings, os, cv2 as cv

from helpers.add_noise import addNoiseToImageByNoiseType
warnings.filterwarnings("ignore")

def initResultsDirWithOrigAndNoisyImage(selectedImageDatasets):
    for dataset in selectedImageDatasets:
        img_gen = dataset.image_gen
        # havnt used the gen object
        for file_name in dataset.files:
            img_name = file_name.rsplit(".",1)[0]
            path = f'./results/{dataset.dataset_name}/{img_name}'

            # makes the dirs
            os.makedirs(path, exist_ok=True)

            # writes the orig and noisy image
            img = next(img_gen)
            nImg = addNoiseToImageByNoiseType('s&p', img)
            cv.imwrite(path+'/orig.jpg', img)
            cv.imwrite(path+'/noisy.jpg', nImg)