import pandas as pd
import numpy as np

readData = pd.read_csv('Appreviews.csv')

required = readData.head(100000)

review = required['content']

review.to_csv('Reviews.csv',index=True)

print(review.head())