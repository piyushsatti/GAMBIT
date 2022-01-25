###### The GUI Tool for Image Denoising Research (dubbed GAMBIT) hopes to reduce evaluation, testing, and verification time of new research into the domain of Image Denoising. This is a collection of tools that should drastically speed up the rate of innovation by reducing the time spent on testing so that researchers spend time on ideation instead. If OpenCV is not getting installed use  ```pip install --upgrade wheel```

### List of Features: 
- Generating denoised images for a selected set of images and a range of noise densities (Default: standard image dataset and 10->90% noise range with 10% step size)
- Performance calculation using the generated images for PSNR, SSIM, IEF (Let us know if there are other metrics that are useful)
- Qualitative performance comparison
- Quantitative performance comparison (will include a new method for comparing two images in a qualitative manner) 

> Initial lifecycle of the tool will be like so: pre-apha -> alpha -> beta -> v1.x -> ...   
> Different features will be added at different stages of the project with the most critical aspects added first

The tool is current in pre-alpha as a collection of loose scripts. In the coming weeks, a CLI tool will be developed with a variety of features as listed. We will start with a basic implementation with more complex offerings part of the beta.

#### Installing MATLAB API for Python
To make sure your MATLAB functions can run using the Python script you will need to install the MATLAB API for python. It can be a complicated and irritating process if you are doing so the first time around. Because of this we have created a simple script that takes care of all this nonsense for you.
 
In the current release, a virtual env is used to ensure that GAMBIT is independent of your other installations. For this, the MATLAB python API has been installed directly to the virtual env - [official documentation](https://in.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html) or [stackoverflow](https://stackoverflow.com/questions/31550622/call-matlab-from-a-python-virtual-environment).

> matlab is stored here ../../Applications/MATLAB_R2020b.app/bin/matlab
>
>matlab -nodisplay -nosplash -nodesktop -r "run('path/to/your/script.m');exit;"
>
> We assume that the correct python version (corresponding to the appropriate MATLAB version) is installed and added to the system path. You can [refer here](https://stackoverflow.com/questions/4583367/how-to-run-multiple-python-versions-on-windows) to learn more about this. Please do let us know if you face any difficulties or would like this section expanded in the future, you may contact us directly - piyushsatti@gmail.com
>
> In case you wish to install this on your own, please refer to the [version compatibility sheet.](https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/support/sysreq/files/python-compatibility.pdf)

#### Work to be done
>Currently, no system design structure has been used for this project and all the modules and functionalities are loosely tied together. Down the line, it would be preferable to have all the individual components much neately reqritten in a pythonic way with effective use of classes.

To Do:
- [ ] Denoising Operation
    - [ ] addNoiseToImage(img, noise_type, noise_density) => Adding noise to images given as input
    - [ ] denoiseImage(path_to_algo, n_img) => Should internally handle calling the appropriate resolution engine (matlab, python, c/c++, js etc.)
    - [ ] denoiseDataset(dataset: class attribute img_dataset from ./core/utils/classes/class_img_dataset/) => Output should be written to the predefined folder structure
- [ ] Quantitative Metrics
    - [ ] evalQuantMetric(img, n_img, d_img, metric_type) => internally calls eval{MetricName} that deals with specific metric types; should generate a common json file for named 
    - [ ] showQuantEval(data: the json data generated, method: should take in the form of representation) => options such as sort/group/show by {attribute} with finer selection methods must be made available. Indirect use of a SQL database may be considered to allow the user to query and search the data themselves.
    - [ ] graphQualEval(data: same as showQualEval) => should generate the common/most-used graphs used in research papers

## Why this project?
>This project has been a personal favorite due to several reasons. Firstly, it eases the implementation and testing time of algorithms in my domain significantly. Secondly, it helps me and my team improve our rate of development of the NERD repository. Lastly, it can be shipped as a free-to-use product for fellow researchers! having someone use something you create is one of the best accomplishments one can get.
