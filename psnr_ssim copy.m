clc; close all;clear all;
dir_name = "512_images";

image_list = dir(dir_name+"/*.tif");
code_list = dir("test_codes/*.m");
addpath("test_codes");
addpath(dir_name);

for i = 1:length(code_list)
    for j = 1:length(image_list)
        for k = 1:1:9
            Img = imread(image_list(j).name);
            Img = Img(:,:,1);
            ac = split(image_list(j).name,'.');
            nd = int2str(k*10);
            code_name = split(code_list(i).name,'.');
            try
                oImg = imread(dir_name +"_result/"+ac(1)+"/"+nd+"/"+code_name(1)+"_"+nd+"_"+image_list(j).name);
                tmp_psnr(j,k,i) = psnr(Img,oImg);
                tmp_ssim(j,k,i) = ssim(Img,oImg);
            catch e
                disp(e)
                disp(dir_name +"_result/"+ac(1)+"/"+nd+"/"+code_name(1)+"_"+nd+"_"+image_list(j).name)
            end
        end
    end
end