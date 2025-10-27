
import pandas as pd
import numpy as np
 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
 
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import urllib.request
import pickle
import os
os.chdir(os.path.dirname(__file__))


C = 1.0
n_splits = 5
output_file = f'model_C={C}.bin'

 
df = pd.read_csv('data/data-week-3.csv')