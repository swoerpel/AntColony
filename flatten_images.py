import shutil
import os
from PIL import Image
import re
import numpy as np
source = 'C:\\Users\\SteveWoerpel\\Desktop\\downloads\\'
dest = 'C:\\Files\\Art\\Global Gallery\\Workspace\\'
loop = True

source_files = os.listdir(source)
dest_files = os.listdir(dest)
# will cause saving problems if ran for long period of time
bands = []
for f in range(len(source_files)):
    print(source + source_files[f])
    if not os.path.isdir(source + source_files[f]):
        with Image.open(source + source_files[f]) as image:
            print('oppacity changed.', f, 'from',
                  source, 'to\n', dest)
            image.putalpha(255)
            bands.append(image)
            # image.save(dest + source_files[f] + '_half.png', image.format)

alphas = []
masks = []
n = len(bands)
merged = bands[0]
mask_offset = 1 / (n - 1) / 4
for i in range(n):
    alpha = int((mask_offset + (i / n)) * 255)
    mask = Image.new(mode='L', size=bands[0].size, color=(alpha))
    merged = Image.composite(merged, bands[i], mask)

merged.save(dest + 'NP_BG_02.png', image.format)
# r1, g1, b1 = split = bands[0].split()
# print(bands[0].__dict__)
# mask = Image.fromarray(np.uint8(0))
# a1 = .5
# a2 = .75
# a1 = int(255 * a1)
# a2 = int(255 * a2)
# print('g_VAL', a2)
# m1 = Image.new(mode='L', size=bands[0].size, color=(a1))
# m2 = Image.new(mode='L', size=bands[0].size, color=(a2))
# merged = Image.merge("RGB", (r1, g1, b1))

# merged = Image.composite(bands[0], bands[1], m1)
# merged = Image.composite(merged, bands[2], m2)
# merged = Image.blend(bands[0], bands[1], 20)
# merged = Image.blend(merged, bands[2], 20)
# merged.save(dest + 'chet' + '_half_03.png', image.format)
# merged.save(dest + 'chet' + '_half_02.png', image.format)
