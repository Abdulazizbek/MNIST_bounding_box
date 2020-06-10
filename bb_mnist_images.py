#!/usr/bin/env python
# coding: utf-8

# ### Draw a bounding box using MNIST dataset

# Drawing bounding box coordinates into images and save bounding box images into the new folder



import os
import cv2 as cv

im_root = "mnist_png/"
out_im_root = "bb_mnist/"

thresh = 252     # color threshold


def thresh_callback(val):
    
    x_list = []
    y_list = []
    
    threshold = val
    
    im_shape = src_gray.shape[0]
    canny_output = cv.Canny(src_gray, threshold, threshold * 2)
    contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contr in contours:
        for c in contr:
            x_list.append(c[0][0])
            y_list.append(c[0][1])
    x_min = min(x_list)
    x_max = max(x_list)
    y_min = min(y_list)
    y_max = max(y_list)
    
    '''
    # if need padding from number: 
    
    if x_min > 3 and y_min > 3:
        x_min = x_min - 2
        y_min = y_min - 2
    
    elif x_min > 2 and y_min > 2:
        x_min = x_min - 1
        y_min = y_min - 1
    
    else:
        x_min = x_min
        y_min = y_min
    
    if x_max < (im_shape - 3) and y_max < (im_shape-3):
        x_max = x_max + 2
        y_max = y_max + 2
    
    elif x_max < (im_shape - 2) and y_max < (im_shape - 2):
        x_max = x_max + 1
        y_max = y_max + 1
        
    else:
        x_max = x_max
        y_max = y_max
    '''
    return x_min, y_min, x_max, y_max



base_folders = [name for name in os.listdir(im_root)]

for base in base_folders:
    base_path = os.path.join(im_root, base)
    out_base_path = os.path.join(out_im_root, base)
    
    folders = sorted([name for name in os.listdir(base_path)])
    
    for folder in folders:
        base_folders = os.path.join(base_path, folder)
        out_base_folders = os.path.join(out_base_path, folder)
                
        if not os.path.exists(out_base_folders):
            os.makedirs(out_base_folders)
        
        images = [name for name in os.listdir(base_folders) if name.endswith(".png")]
        
        for img in images:
            img_path = os.path.join(base_folders, img)
                        
            src = cv.imread(img_path)
            src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
            
            x_min, y_min, x_max, y_max = thresh_callback(thresh)
            
            image = cv.rectangle(src, (x_min, y_min), (x_max, y_max), (0, 255, 0), 1)
            
            cv.imwrite("{}/{}".format(out_base_folders, img), image)