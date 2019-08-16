from PIL import Image
import os

from resizeimage import resizeimage

input_size = {

}

source = 'C:\\Files\\Art\\WebsiteImages\\Workspace\\'
dest = 'C:\\Files\\Art\\WebsiteImages\\Workspace\\Showcase\\'
source_files = os.listdir(source)
dest_files = os.listdir(dest)
print(source_files)
# with open('16.png', 'r+b') as f:

image_index = 29
for f in range(len(source_files)):
    print(source + source_files[f])
    if not os.path.isdir(source + source_files[f]):
        with Image.open(source + source_files[f]) as image:
            width, height = image.size

            adjusted_height = 1000  # adjusted_width * height / width
            adjusted_width = width * adjusted_height / height
            print(adjusted_width, adjusted_height)
            cover = resizeimage.resize_cover(
                image, [adjusted_width, adjusted_height]
            )
            cover.save(dest + str(image_index) + '.png', image.format)
            print('image saved', dest + str(image_index) + '_tri.png')
            image_index += 1
