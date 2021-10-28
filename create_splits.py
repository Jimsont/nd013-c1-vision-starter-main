import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger

import shutil

def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /mnt/data
    """
    # TODO: Implement function
    
    # define source directory
    src_file_dir = '/data/waymo/'

    # retrieve file name from source directory and only keeps file starts with name 'segment'
    file_names_raw = os.listdir(src_file_dir)
    file_names = [];
    for file_name in file_names_raw:
        if file_name[0:7] == 'segment':
            file_names.append(file_name)
    
    # random shuffle file names
    random.shuffle(file_names)

    # split data into train, val and test set
    # define split percentage for train, val, test set
    split_percentage = [0.75, 0.15, 0.10]

    # retrieve data length
    n_data = len(file_names)

    # create train, val and test directory
    path = ['train/', 'val/', 'test/']
    for i in range(len(path)):
        path_dir = data_dir + path[i]
        if os.path.exists(path_dir) == False:
            os.makedirs(path_dir)
        else:
            shutil.rmtree(path_dir)
            os.makedirs(path_dir)

    # if data length is long enough, split data into train, val, and test set
    # else, print error message and stop
    if n_data > 25:
        ids_train = int(n_data*split_percentage[0])
        ids_val = int(n_data*(split_percentage[0] + split_percentage[1]))

        # loop through data and assign train, val, and test destination
        for i in range(n_data):
            # declare source_path and destination path
            src_path = src_file_dir + file_names[i]

            if i >=0 and i<ids_train:
                dst_path = data_dir + path[0] + file_names[i]

            elif i>=ids_train and i<ids_val:
                dst_path = data_dir + path[1] + file_names[i]

            else:
                dst_path = data_dir + path[2] + file_names[i]

            # check if file is already exist, if not, move data to the folder
            if os.path.exists(dst_path) == False:
                os.symlink(src_path, dst_path)   
                
    else:
        print("not enough data to split")
    
    
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)