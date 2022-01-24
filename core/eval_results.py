import cv2 as cv, sys
# imported for pathing of sub-module imports
sys.path.append('./core/utils/')
from utils.load_datasets import createImageDatasetObjectFromPath
from utils.init_results import initResultsDirWithOrigAndNoisyImage 

def evaluateTestCodes():
    pass

if __name__ == "__main__":

    # quick test
    path = './image-datasets'
    selectedImageDatasets = createImageDatasetObjectFromPath(path)
    initResultsDirWithOrigAndNoisyImage(selectedImageDatasets)

    # prints all the datasets
    [print(e) for e in selectedImageDatasets]

    # loops over and shows all the images
    for dataset in selectedImageDatasets:
        for img in dataset.image_gen:
            print(type(img))
            cv.imshow("img", img)
            cv.waitKey(0)