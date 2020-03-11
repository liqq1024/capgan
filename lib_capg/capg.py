import os
import torch
import numpy as np
from os.path import dirname, join as pjoin
import scipy.io as sio
import re

class CAPG:
    sblist = [1,2]

    def __init__(self, *arg, **kwargs):
        self.data = []
        self.targets = []
        
        if len(arg) != 0:
            self._myinit(arg[0])
    
    def _myinit(self, root: str):
        for sbdir in os.listdir(root):
            path = pjoin(root, sbdir)
            data_, targets_ = self._readdata(path)
            self.data.append(data_)
            self.targets.append(targets_)
        self.data = np.vstack(self.data)
        self.targets = np.vstack(self.targets)
    
    def _readdata(self, dir: str):
        data = []
        targets = []
        sblabel = []
        gslabel = []
        tllabel =[]
        file: str
        for file in os.listdir(dir):
            if file.endswith(".mat"):
                labels = re.split('-|\.',file)[0:3]
                matname = pjoin(dir, file)
                file_data = sio.loadmat(matname)['data']
                file_data = file_data.reshape(1000,16,8)
                #file_data = np.expand_dims(file_data, axis=2)
                file_data = np.expand_dims(file_data, axis=1)
                sblabel.extend([int(labels[0]) for i in range(file_data.shape[0])])
                gslabel.extend([int(labels[1]) for i in range(file_data.shape[0])])
                tllabel.extend([int(labels[2]) for i in range(file_data.shape[0])])
                data.append(file_data)
        data = np.vstack(data)
        targets = np.column_stack((sblabel,gslabel,tllabel))
        return data, targets    

    def __getitem__(self, index):
        """
        Args:
            index (int): Index
        Returns:
            tuple: (image, target) where target is index of the target class.
        
        if label =='sb':
            img, target = self.data[index], self.targets[index][0]
        elif label =='gs':
            img, target = self.data[index], self.targets[index][1]
        else:
            img, target = self.data[index], self.targets[index][2]
        """
        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        #img = Image.fromarray(img)
        img, target = self.data[index], self.targets[index]
        return img, target

    def __len__(self):
        return len(self.data)
