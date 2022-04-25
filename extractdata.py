#import the necessary library that are required


from itertools import count
from unittest import result
from google_play_scraper import app, Sort, reviews, reviews_all , permissions
import pandas as pd
import numpy as np
import json 


#Extracting the application details
appdata = app('com.android.chrome',
             lang='en',
             country = 'us')

appdetails = pd.DataFrame(list(appdata.items()),columns = ['app detail','value'])

appdetails.to_csv('Appdetails.csv',index=True)

#print(appdetails)
#print(type(appdetails))


#Extracting the application Permissions Details
permissiondata = permissions('com.android.chrome',
                             lang='en',
                             country='us')

permissionsdetails=pd.DataFrame(list(permissiondata.items()), columns= ['PermissionType','Value'])

permissionsdetails.to_csv('Permission.csv',index=True)
#print(permissionsdetails)
#print(type(permissionsdetails))



#Extracting the reviews of the apps
review, continuation_token = reviews('com.android.chrome',
    lang = 'en',
    country = 'us',
    sort = Sort.MOST_RELEVANT,
    count = 200000,
    filter_score_with=None
    )

app_reviews = pd.DataFrame(review)
app_reviews.to_csv('Appreviews.csv',index=True)
#print(app_reviews)
#print(type(app_reviews))