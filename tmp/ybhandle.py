import csv
import numpy as np
import pandas as pd


filename='./output/jb18.csv'

df=pd.DataFrame(pd.read_csv(filename))
print(df.info())
print(df.head())