###### The GUI Tool for Image Denoising Research (dubbed GAMBIT) hopes to reduce evaluation, testing, and verification time of new research into the domain of Image Denoising. This is a collection of tools that should drastically speed up the rate of innovation by reducing the time spent on testing so that researchers spend time on ideation instead.

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

> In case you wish to install this on your own, please refer to the [version compatibility sheet.](https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/support/sysreq/files/python-compatibility.pdf)