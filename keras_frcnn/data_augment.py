import cv2
import numpy as np
import copy

def augment(img_data, config):
    assert 'filepath' in img_data
    assert 'bboxes' in img_data
    assert 'width' in img_data
    assert 'height' in img_data

    try:
        img_data_aug = copy.deepcopy(img_data)
        img = cv2.imread(img_data_aug['filepath'])
        return img_data_aug, img
    except Exception as e:
        print(e)
        return img_data_aug, None
