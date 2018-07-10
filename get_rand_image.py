import os
import sys
import random
import shutil


'''
随机分割数据集为query 和lib，
copy到各自目录queryimg 和 libimg中存储。
其中10%作为lib 剩下的作为query
'''

imgdir = '../data/missfresh_goods'		
savedir = '../data'
dirlist = os.listdir(imgdir)

libratio = 0.1


for n,m in enumerate(dirlist):
    print n,m
    imgd = os.path.join(imgdir,m,'images')
    if not os.path.exists(imgd):
        print '%s not exist'%imgd
        continue
    print imgd
    imglist = os.listdir(imgd)
    imgnum = len(imglist)
    use_len = imgnum/10
    real_len = 0

    search_p_dir = os.path.join(savedir,'libimg',m,'images')
    if not os.path.exists(search_p_dir):
        os.makedirs(search_p_dir)
    query_p_dir = os.path.join(savedir,'queryimg',m,'images')
    if not os.path.exists(query_p_dir):
        os.makedirs(query_p_dir)

    for imgname in imglist:
        rval = random.random()
        if rval < libratio:
            real_len += 1
            shutil.copyfile(os.path.join(imgd,imgname),os.path.join(search_p_dir,imgname))
        else:
            shutil.copyfile(os.path.join(imgd,imgname),os.path.join(query_p_dir,imgname))
    print 'search len %d , %d'%(real_len,use_len)


        
