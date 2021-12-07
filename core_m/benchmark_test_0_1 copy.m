clc; close all; clear;

image_list = dir("kodak_images");
code_list = dir("test_codes");
addpath("test_codes");

tmp_ssim = zeros([24,24,24]);
tmp_psnr = zeros([24,24,24]);

for i = 4:length(code_list)
    
    code_name = split(code_list(i).name,'.');
    disp(code_name(1))
    test_code = str2func(string(code_name(1)));
    
    parfor j = 4:length(image_list)
        disp(image_list(j).name)
        Img = imread("kodak_images/"+image_list(j).name);
        try
            Img = rgb2gray();
        catch
            Img = Img(:,:,1);
        end
        
        for k = 1:1:9
            
            nImg = imnoise(Img,'salt & pepper',k/10);
            oImg = test_code(nImg);
            tmp_psnr(j,k,i) = psnr(Img,oImg);
            tmp_ssim(j,k,i) = ssim(Img,oImg);
            
        end
    end
end
save('euclid_test');
