#Imports
import pandas as pd
import string
import re
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib
import os
import hashlib
import requests

#Define model path
MODEL_PATH = "saved_pipeline.joblib"

'''
#Import training data
data_fake=pd.read_csv('Fake-News-Detection\Fake.csv')
data_true=pd.read_csv('Fake-News-Detection\True.csv')

#Add labels
data_fake["class"]=0
data_true['class']=1

#Concatenate and clean data
data_merge=pd.concat([data_fake, data_true], axis = 0)
data=data_merge.drop(['title','subject','date'], axis = 1)
data = data.sample(frac = 1)
data.reset_index(inplace = True)
data.drop(['index'], axis = 1, inplace = True)



#Applying the function to the dataset
data['text'] = data['text'].apply(wordopt)

#Defining features and labels
x = data['text']
y = data['class']

#Splitting the dataset
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25)
'''

#Vectorization and pipeline creation
if os.path.exists(MODEL_PATH) :
    pipeline = joblib.load(MODEL_PATH)
    print("Model loaded from disk.")

#Normalising the text using some regex operations
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]','',text)
    text = re.sub("\\W"," ",text)
    text = re.sub('https?://\S+|www\.\S+','',text)
    text = re.sub('<.*?>+',b'',text)
    text = re.sub('[%s]' % re.escape(string.punctuation),'',text)
    text = re.sub('\w*\d\w*','',text)
    return text

#Prediction and evaluation
#print(classification_report(y_test, pred_lr))


#Model Tester
def output_label(n):
    if n==0:
        return "Fake News"
    elif n==1:
        return "Real News"
    
def manual_testing(news):
    testing_news = {"text":[news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test['text'] = new_def_test["text"].apply(wordopt)
    pred_LR = pipeline.predict(new_def_test['text'])
    prob_LR = pipeline.predict_proba(new_def_test['text'])
    confidence_LR = prob_LR.max()   
    #return print("\nLR Predicition: {} (Confidence: {:.2f})".format(output_label(int(pred_LR[0])), confidence_LR))
    return {
        "Input": hashlib.sha256(news.encode()).hexdigest(),
        "Prediction": output_label(int(pred_LR[0])),
        "Confidence": float(confidence_LR)   
    }

news = input("Enter a news article:\n")
requests.post("http://localhost:5000/predict", json={"files": manual_testing(news)})