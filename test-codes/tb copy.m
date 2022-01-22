clc; close all; clear all;
image_dir  = "kodak";
code_dir = "test_codes";
image_list = dir(image_dir);
code_list = dir(code_dir);
addpath(code_dir);
addpath(image_dir);

parfor j = 4:length(image_list)

    disp(image_list(j).name)
    Img = imread(image_list(j).name);
    ac = split(image_list(j).name,'.');
%     Img = Img(:,:,1);

    for k = 0.1:0.1:0.9
        % adding noise
        nImg = imnoise(Img,'salt & pepper',k);

        nd = int2str(k*100);
        name = image_dir+"_result/"+ac(1)+"/"+nd;

        if not(exist(name,'dir'))
            mkdir(name);
        end

        imwrite(nImg,"C:\Users\piyus\MATLAB Drive/testing/"+name+"/"+nd+"_"+image_list(j).name,'png');

        for i = 4:length(code_list)
            code_name = split(code_list(i).name,'.');
            disp(code_name(1))
            test_code = str2func(string(code_name(1)));
            oImg = reshape([test_code(nImg(:,:,1)),test_code(nImg(:,:,2)),test_code(nImg(:,:,3))],size(Img));
%             oImg = test_code(nImg);
            imwrite(oImg,"C:\Users\piyus\MATLAB Drive/testing/"+name+"/"+code_name(1)+"_"+nd+"_"+image_list(j).name,'png');
        end

    end

end

save("proposed")