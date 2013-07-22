'''
Created on Jul 22, 2013

@author: Milos
'''

import os, imghdr

index = 1
for filename in os.listdir(os.getcwd()):
    try:
        imageType = imghdr.what(filename)
        if imageType:
            os.rename(filename, "image_" + str(index) + "." + imageType)
            index += 1
    except:
        pass