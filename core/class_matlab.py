import matlab.engine

class eng:
    def __init__(self,  path: str="./"):
        self.eng = matlab.engine.start_matlab()
        self.eng.addpath(path)
        print(f"Created MATLAB engine instance w/t path {path}")
    
    def add2path(self, path: str):
        self.eng.addpath(path)

    def test(self):
        print(self.eng.triarea(1.0,2.0))

    def __del__(self):
        print(f"Closed MATLAB engine instance")
        self.eng.close()

if __name__ == '__main__':
    # used to write quick tests of the class
    e1 = eng("./core_m/")
    e1.test()
    del e1