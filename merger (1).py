import cv2,os
from PIL import Image,ImageOps
def merge_image(img1, img2, vertically):
    filename = img1.split('/')[-1]
    images = list(map(Image.open, [img1, img2])) 
    widths, heights = zip(*(i.size for i in images))
    if vertically:
        max_width = max(widths)
        total_height = sum(heights)
        new_im = Image.new('RGB', (max_width, total_height))

        y_offset = 0
        for im in images:
            new_im.paste(im, (0, y_offset))
            y_offset += im.size[1]
    else:
        total_width = sum(widths)
        max_height = max(heights)
        new_im = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset, 0))
            x_offset += im.size[0]

    # new_im.save(f'./inter/{filename}')
    new_im.save(f'./final_image/{filename}')
    # return filename
filelist= [file for file in os.listdir('.') if file.endswith('.png')]
for file_name in filelist:
    # #add border 
    # ImageOps.expand(Image.open(f'./pink_flower/{file_name}'),border=2,fill='red').save(f'./red_border/{file_name}')

    # merge_image(f'./red_border/{file_name}',f'./blue_border/{file_name}',0)
    img = Image.open(f'./inter/{file_name}')
    img = img.resize((768,300))
    img.save(f'./inter2/{file_name}')
    final = merge_image(f'./blue_square/{file_name}',f'./inter2/{file_name}' ,1)