import shutil
import glob
import random
import os
vids = glob.glob('/home/ubuntu/dataset/indoor/GT/pair*')
random.shuffle(vids)

for v in vids[:12]:
    des = v.replace('indoor', 'indoor_test')
    shutil.move(v, des)
    shutil.move(v.replace('GT', 'input'), des.replace('GT', 'input'))
        