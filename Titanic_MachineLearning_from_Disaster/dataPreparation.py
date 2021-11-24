# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 13:30:16 2021

     This is a .py file for data preparation in order to train a 
     machine learning model properly.
     
     To check the data and information: https://www.kaggle.com/c/titanic/data
     
@authors: Jorge Ivan Avalos Lopez & Jose Alberto Moreno Guerra

python: 3.8.3
pytorch: 1.6.0
sklearn: 0.23.1
numpy: 1.18.5
panadas: 1.0.5
"""

import pandas as pd

# data folder  path
dataPath = "./data/"


if __name__ == "__main__":
    data_train = pd.read_csv(dataPath+"train.csv",encoding="latin-1",low_memory=False)
    
    # Tasks
        # data description. (dtypes,missing values,unique values, etc) --> deto
        # transform object to categorical.  --> beto
        # set levels of some categorical variable that be important or make sense. --> ivan
        # handling missing values. --> beto
        # handling categorical values (convert categorical values to its respective code). --> ivan
        # Transform the data if required for the models.
        # feature engineering to create new features. --> beto e ivan
        
        
# Some links:
    """
    	-- 1) How to Handle Missing Data in Machine Learning: 5 Techniques (soruce: https://dev.acquia.com/blog/how-to-handle-missing-data-in-machine-learning-5-techniques/09/07/2018/19651)
    	-- 2) Hitchhiker's guide to Exploratory Data Analysis (soruce: https://towardsdatascience.com/hitchhikers-guide-to-exploratory-data-analysis-6e8d896d3f7e)
    	-- 3) Pythonic Data Cleaning With Pandas and NumPy (soruce: https://realpython.com/python-data-cleaning-numpy-pandas/)
    	-- 4) Data Cleaning Using Pandas (soruce: https://www.analyticsvidhya.com/blog/2021/06/data-cleaning-using-pandas/)
    	-- 5) Data Cleaning with Python and Pandas: Detecting Missing Values (soruce https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b)   
    """
    
    
    
