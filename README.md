# Semantic-Error-Correction

Authors: Yijun Qian
Email: yijunqia@andrew.cmu.edu

## Overview
This is the released code for my project in 11727 spring 2020.

## Data Sets
We used the data sets from Spider and WikiSQL.
According to their requirements, please download the data sets yourseld from their website:
- Spider (https://yale-lily.github.io/spider)
- WikiSQL (https://github.com/salesforce/WikiSQL)

## Dependency
The code relies on Fairseq and OpenNMT for training, please download them and put it under this folder.
You can find the training code in utils folder.
- [OpenNMT-py](https://github.com/OpenNMT/OpenNMT-py)
- [Fairseq](https://github.com/pytorch/fairseq)
Also, we need to thanks for the open-sourced code from microsoftopensource(https://github.com/microsoft/IRNet).
We used part of their code in our project.

## Data Preparation
If you want to reproduce our results on AI City Challenge or train the model by yourself, please download the data set from: (https://www.aicitychallenge.org/2020-data-and-evaluation/)
and put it under the folder datasets.
Make sure the data structure is like:
* ELECTRICITY-MTMC
  * datasets
    * aic_20_trac3
      * test (test folder)
      * eval 
      * validation (validation folder)
      * cam_timestamp
      * cam_loc
      * cam_framenum
      * train (train folder) 

## Performance

The validation results are listed under folder logs.

