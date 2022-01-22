from email.mime import image
import os
from simple_term_menu import TerminalMenu
from utils.classes.imageDataset import imageDataset

def checkDatasetTree(tree):
    '''
    checks the dataset tree for standard
    pathing as defined in the documentation
    '''
    state = (True, None)
    for i in range(len(tree)):
        if i != 0 and len(tree[i]['dirs']):
            state = (False, tree[i]['root'])

    if not state[0]:
        print("Error in directory or sub-dir structure ->")
        print(state[1])
        print("Make sure to follow directory guidelines")
        return (0, None)

    return (1, tree)

def walkDir(path):
    if not os.path.exists(path):
        print("Invalid pathname")
        return (0,None)

    tree = []
    for (root,dirs,files) in os.walk(path, topdown=True):
        tree.append(
            {
            'root':root,
            'dirs':dirs,
            'files':files
            }
        )

    return (1,tree)

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

    return createClassObjectFromDatasets(selected_datasets)
    

def createClassObjectFromDatasets(selected_datasets):
    '''
    filetype conversion for easier access
    class allows more flexibility down the line
    '''
    datasets_obj = [imageDataset.createDatasetFromTerminal(dataset) for dataset in selected_datasets]
    return datasets_obj

if __name__ == "__main__":
    # quick test
    path = './image-datasets'
    tmp = createImageDatasetObjectFromPath(path)
    [print(e) for e in tmp]