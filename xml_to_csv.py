#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 #/Users/utsav/Desktop/PizzaDetector/images/train
    #/Users/utsav/Desktop/PizzaDetector/annotations
"""
Created on Thu May 30 20:40:17 2019

@author: utsav

Usage:
    #Create train data:
    python xml_to_csv.py -i [PATH_TO_IMAGES_FOLDER]/train -o [PATH_TO_ANNOTATIONS_FOLDER]/train_label.csv
    
    #Create test data:
    python xml_to_csv.py -i [PATH_TO_IMAGES_FOLDER]/test -o [PATH_TO_ANNOTATIONS_FOLDER]/test_label.csv
"""
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob('/Users/utsav/Desktop/PizzaDetector/images/test' + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[5][0].text),
                     int(member[5][1].text),
                     int(member[5][2].text),
                     int(member[5][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    
    image_path = os.path.join(os.getcwd(),'images')
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('test_labels.csv', index=None)

    print('Successfully converted xml to csv.')


main()
