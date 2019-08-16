import shutil
import os
import re
source = 'C:\\Users\\SteveWoerpel\\Desktop\\downloads\\'
dest = 'C:\\Files\\Art\\Global Gallery\\Workspace\\'
filename_re = ''
loop = True

# will cause saving problems if ran for long period of time

while(loop):
    if os.listdir(source):  # downloads has images to move
        print('moving image')
        dest_files = os.listdir(dest)
        source_files = os.listdir(source)
        # code = re.search("^.*[0-9]_", f)

        for f in source_files:
            save_code = re.search("^(.*_.*)_", f).group(0)
            dest_path = dest  # + '_' + save_code + '.png'
            # print(f, save_code)
            # if not os.path.exists(dest_path):
            # os.makedirs(dest_path)
            # else:
            print('file moved.', f, 'from',
                  source, 'to\n', dest_path)
            shutil.move(source + f, dest_path)
    else:
        loop = False
