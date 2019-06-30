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

#%%
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, SelectPercentile
from sklearn.feature_selection import chi2
from sklearn.metrics import f1_score, confusion_matrix, accuracy_score

X_train, X_test, y_train, y_test = train_test_split(movie.crews,
                                                    movie.good_or_bad,
                                                    test_size = 0.2)                                                    )
accuracy_list = []
f1_list = []
for p in range(10, 101, 10):
    pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('chi_2', SelectPercentile(chi2, percentile=p)),
        ('clf', SGDClassifier())
        ])
    
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    accuracy_list.append(accuracy)
    f1_list.append(f1)
    
print(accuracy_list)
print(f1_list)

#%%
import numpy as np
skf =  StratifiedKFold(n_splits = 4)
all_accuracy_list = []
all_f1_list = []
for train, test in skf.split(movie.crews, movie.good_or_bad):
    accuracy_list = []
    f1_list = []
    for p in range(10, 101, 10):
        pipeline = Pipeline([
            ('vect', CountVectorizer()),
            ('chi_2', SelectPercentile(chi2, percentile=p)),
            ('clf', SGDClassifier())
            ])
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        accuracy_list.append(accuracy)
        f1_list.append(f1)
    all_accuracy_list.append(accuracy_list)
    all_f1_list.append(f1_list)

acc_array = np.array(all_accuracy_list)
np.mean(acc_array, axis = 0)    
#%%
chi_2 = SelectPercentile(chi2)
param_grid = [{'chi_2__percentile': list(range(10, 101, 10))}]

pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('chi_2', chi_2),
        ('clf', SGDClassifier())
        ])

gscv = GridSearchCV(pipeline, cv=5, param_grid=param_grid)
gscv.fit(movie.crews, movie.good_or_bad)

results = pd.DataFrame(gscv.cv_results_)
gscv.best_estimator_ 
