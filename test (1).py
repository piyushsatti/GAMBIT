import cv2,os
from PIL import Image
filelist= [file for file in os.listdir('.') if file.endswith('.png')]
for file_name in filelist:
    x,y = [70 , 70]
    print(file_name)
    im = Image.open(file_name)
    width, height = im.size
    print(width, ' ', height)
    img = cv2.imread(file_name)
    center = [100 , 490]
    crop_img = img[center[0] - 100 : center[0] + 100 , center[1] - 100 : center[1] + 100  ]
    cv2.imwrite(f'./pink_flower/{file_name}',crop_img)
    start_point = (center[1] - x,center[0] - y)
    end_point = (center[1]+ x,center[0] + y)
    color = (0,0,255)
    thickness = 2
    sq = cv2.rectangle(img, start_point, end_point, color, thickness)
    center = [103,267]
    crop_img2 = img[center[0] - 100 : center[0] + 100 , center[1] - 100 : center[1] + 100  ]
    cv2.imwrite(f'./wind/{file_name}',crop_img2)
    start_point = (center[1] - x,center[0] - y)
    end_point = (center[1]+ x,center[0] + y)
    color = (255,0,0)
    thickness = 2
    rsq = cv2.rectangle(sq, start_point, end_point, color, thickness)
    cv2.imwrite(f'./blue_square/{file_name}',rsq)
    new_im = Image.new('RGB', (width+100, height+100))
    # new_im.save('test.png')
    # im = Image.open('test.png')
    # width, height = im.size
    # print(width, ' ', height)
    # cv2.imshow('rsq',new_im)
    # cv2.waitKey(0)