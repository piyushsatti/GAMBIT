import cv2 as cv

class imageDataset:
    
    def __init__(self, dataset_name: str, dataset_rel_path: str, dataset_files: list):
        self.dataset_name = dataset_name
        self.dataset_rel_path = dataset_rel_path
        self.files = dataset_files
        self.image_gen = self.loadFilesFromPath(dataset_files)

        print(f"Dataset created for {dataset_name}")

    @classmethod
    def createDatasetFromTerminal(cls, dataset):
        name = dataset['root'].split('/')[-1]
        rel_path = dataset['root']
        files = dataset['files']
        return cls(name, rel_path, files)

    def loadFilesFromPath(self, dataset_files):
        '''
        Gives the generator object for 
        reading the image <ndarray>
        '''
        for file_name in dataset_files:
            yield cv.imread(self.dataset_rel_path+"/"+file_name)

    def __repr__(self):
        return f'''
        Dataset Name: {self.dataset_name}
        Path: {self.dataset_rel_path}
        Elements: {', '.join(self.files)}
        '''

    def __len__(self):
        '''
        Return the number of 
        images in the dataset
        '''
        return len(self.files)