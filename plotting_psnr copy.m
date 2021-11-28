close all;
x = 10:10:90;
y = ['+', 'o' , 'pentagram' , "square" , '^' ,"diamond",'>' , 'hexagram' , '|' , '_' , '*' , 'x'];

code_list = code_list(1:end);

for var = 1:2
    switch var
        case 1
            tmp_plot  = mean(tmp_psnr);
        case 2
            tmp_plot = mean(tmp_ssim);
        otherwise
            continue
            tmp_plot = tmp_ief;
    end
        
    plot(x,matr,'Marker',y(i),'LineWidth',1.5);
    hold on;
    
    legend(code_list.name);
    %ylim([15,43])    %legend('ASWMF',  'BPDM','DAMF' , 'FSBMMF' ,'Proposed','MDBUTM','RSIF', 'SMF','SWMF','TVWA');
    %legend('FSBMMF' ,'IBLF','MMAPF');
    %legend('IBLF',  'IBLF_old', 'MMAPF_1_1');
end

