import os
from simple_term_menu import TerminalMenu

class img_dataset:
    def __init__(self, name: str, rel_path: str, color_type: str, filetype: str, files: list):
        self.name = name
        self.rel_path = rel_path
        self.colortype = colortype
        self.filetype = filetype
        self.files = files

    @classmethod
    def from_terminal(cls, dataset):
        name = dataset['root'].split('/')[-1]
        rel_path = dataset['root']
        color_type = 'Default'
        filetype = dataset['files'][0].split('.')[-1]
        files = dataset['files']

    def __repr__(self):
        pass

    def __str__(self):
        pass

    # return # of files
    def __len__(self):
        pass
    
    # used to load all the images associated with a dataset
    def load_images(self):
        pass
    
    # converts all images to a single uniform type
    # checks if the conversion type is valid
    # throws an error of the image not compatible
    # e.g. .png -> .tif
    def convert_extn(self, from_type, to_type):
        pass
    
    # converts to matlab readable format
    def matlab_readable(self):
        pass

    # converts to default
    def convert_default(self):
        pass

# checks the tree for standard pathing
# as per the documentation
def checkTree(tree):
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

# scans the default directory for datasets 
# checks they are in the correct format
# creates a class instance for each dataset
def getDatasets(path: str):
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

    # filetype conversion for easier access
    # class allows more flexibility down the line
    dataset_obj = []
    for dataset in selected_datasets:
        tmp = img_dataset(dataset)
        dataset_obj.append(tmp)

    return dataset_obj

def main(path='./img_DAtasets'):

    # gets the datasets
    datasets = getDatasets(path)

    # choosing datasets
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

    print(selected_datasets)
    quit()
    # create selected dataset class instace
    datasets_obj = [img_dataset.from_terminal(dataset) for dataset in selected_datasets]
    return datasets_obj

if __name__ == "__main__":
    path = './img_datasets'
    tmp = main()
    print(tmp)