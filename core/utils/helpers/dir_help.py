import os

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