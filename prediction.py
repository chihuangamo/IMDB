# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import os
os.chdir("C:/Users/User/Documents/Codes/IMDB")

import pandas as pd
movie = pd.read_csv("movie_good_or_bad.csv")

#%% CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer 
vec = CountVectorizer()
vec.fit(movie.crews) 
vec.get_feature_names()

#%%
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

X_train, X_test, y_train, y_test = train_test_split(X =  movie[]
                                                    y = 
                                                    test_size=0.3,                                                    )
                                                        
 