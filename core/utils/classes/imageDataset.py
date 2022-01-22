import cv2 as cv

class imageDataset:
    
    def __init__(self, dataset_name: str, dataset_rel_path: str, dataset_files: list):
        self.name = dataset_name
        self.rel_path = dataset_rel_path
        self.files = self.loadFilesFromPath(dataset_files)

        print(f"Dataset created for {dataset_name}")

    @classmethod
    def createDatasetFromTerminal(cls, dataset):
        name = dataset['root'].split('/')[-1]
        rel_path = dataset['root']
        files = dataset['files']
        return cls(name, rel_path, files)

    def loadFilesFromPath(self, dataset_files):
        for file in dataset_files:
            pass

    def __repr__(self):
        return f'''
        Dataset Name: {self.name}
        Path: {self.rel_path}
        Type: {self.color_type}
        File Type: {self.file_type}
        Elements: {', '.join(self.files)}
        '''

    def __len__(self):
        '''
        Return the number of 
        images in the dataset
        '''
        return len(self.files)