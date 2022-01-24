import cv2 as cv
from simple_term_menu import TerminalMenu
from classes.imageDataset import imageDataset
from helpers.dir_help import walkDir, checkDatasetTree

def getDatasetsFromPath(path: str):
    '''
    scans the default directory for datasets 
    checks they are in the correct format
    creates a class instance for each dataset
    '''
    ret = walkDir(path)
    if not ret[0]:
        print('encountered an issue with walking on the path... quitting')
        quit()
    else:
        dataset_tree = ret[1]
    
    ret = checkDatasetTree(dataset_tree)
    if not ret[0]:
        print('encountered an issue while checking the dataset tree... quitting')
        quit()
    else:
        dataset_tree = ret[1]

    return dataset_tree

def createDatasetClassObjectFromDatasets(selected_datasets):
    '''
    class allows more flexibility down the line
    '''
    datasets_obj = [imageDataset.createDatasetFromTerminal(dataset) for dataset in selected_datasets]
    return datasets_obj

def createImageDatasetObjectFromPath(path):

    datasets = getDatasetsFromPath(path)

    terminal_menu = TerminalMenu(
        datasets[0]['dirs'],
        multi_select=True,
        show_multi_select_hint=True,
    )
    menu_entry_indices = terminal_menu.show()
    
    selected_datasets = []
    for dataset in datasets[1:]:
        if dataset['root'].split('/')[-1] in terminal_menu.chosen_menu_entries:
            selected_datasets.append(dataset)

    return createDatasetClassObjectFromDatasets(selected_datasets)

if __name__ == "__main__":
    # quick test
    path = './image-datasets'
    selectedImageDatasets = createImageDatasetObjectFromPath(path)
    
    # prints all the datasets
    [print(e) for e in selectedImageDatasets]

    # loops over and shows all the images
    for dataset in selectedImageDatasets:
        for img in dataset.image_gen:
            print(type(img))
            cv.imshow("img", img)
            cv.waitKey(0)