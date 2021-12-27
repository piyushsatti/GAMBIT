import os
from simple_term_menu import TerminalMenu
from utils.classes.class_img_dataset import img_dataset

def checkTree(tree):
    '''
    checks the tree for standard pathing
    pathing is defined in the documentation
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

def getDatasets(path: str):
    '''
    scans the default directory for datasets 
    checks they are in the correct format
    creates a class instance for each dataset
    '''
    ret = walkDir(path)
    if not ret[0]:
        print('encountered an issue... quitting')
        quit()
    else:
        dataset_tree = ret[1]
    
    ret = checkTree(dataset_tree)
    if not ret[0]:
        print('encountered an issue... quitting')
        quit()
    else:
        dataset_tree = ret[1]

    return dataset_tree

def createClass(selected_datasets):
    '''
    filetype conversion for easier access
    class allows more flexibility down the line
    '''
    dataset_obj = []
    for dataset in selected_datasets:
        tmp = img_dataset(dataset)
        dataset_obj.append(tmp)

    return dataset_obj

def loadImages(path='./img_datasets'):

    datasets = getDatasets(path)

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

    # create selected dataset class instace
    datasets_obj = [img_dataset.from_terminal(dataset) for dataset in selected_datasets]
    return datasets_obj

if __name__ == "__main__":
    path = './img_datasets'
    tmp = loadImages()
    [print(e) for e in tmp]