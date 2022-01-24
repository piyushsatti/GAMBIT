import matlab.engine
import os

class engMATLAB:
    '''
    eng class is used for creation
    and control of a MATLAB engine 
    instance, use del to close
    '''
    def __init__(self,  path: str="./"):
        self.eng = matlab.engine.start_matlab()
        self.eng.addpath(path)
        print(f"Created MATLAB engine instance w/t path {path}")
    
    def add2path(self, path: str):
        if not os.path.exists(path):
            print("Invalid pathname")
            return
        self.eng.addpath(path)

    def test(self):
        print(self.eng.triarea(1.0,2.0))

    def __del__(self):
        print(f"Closed MATLAB engine instance")
        self.eng.close()

if __name__ == '__main__':
    # used to write quick tests of the class
    e1 = engMATLAB("./core_m/")
    print(e1.__doc__)
    e1.test()
    del e1