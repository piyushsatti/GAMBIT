class img_dataset:
    def __init__(self, name: str, rel_path: str, color_type: str, file_type: str, files: list):
        self.name = name
        self.rel_path = rel_path
        self.color_type = color_type
        self.file_type = file_type
        self.files = files

        print(f"Dataset created for {name}")

    @classmethod
    def from_terminal(cls, dataset):
        name = dataset['root'].split('/')[-1]
        rel_path = dataset['root']
        color_type = 'Default'
        file_type = dataset['files'][0].split('.')[-1]
        files = dataset['files']
        return cls(name, rel_path, color_type, file_type, files)

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