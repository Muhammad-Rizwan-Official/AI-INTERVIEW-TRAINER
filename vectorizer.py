import os
import pickle
import re
import sys
import nltk
import itertools
import numpy as np
import pandas as pd
from sklearn import tree
from joblib import dump, load
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import requests
def dun():
    data = pd.read_csv("UpdatedResumeDataSet.csv")
    data = data[["Category", "Resume"]]
    x = np.array(data["Resume"])
    y = np.array(data["Category"])
    cv = CountVectorizer()
    X = cv.fit_transform(x)  # fit the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    yp = clf.predict(X_test)
    acc = accuracy_score(y_test, yp)
    print("accuracy is: ",acc)
    dump(clf, 'DT.joblib')

def reuse(input1):
    with open('job_detector.pkl', 'rb') as f:
        clf = pickle.load(f)
    with open('count_vectorizer.pkl', 'rb') as f:
        cv = pickle.load(f)
    sample = input1
    data = cv.transform([sample]).toarray()
    result = clf.predict(data)
    print(result[0])
    topic = str(result[0])
    url = f"https://api.stackexchange.com/2.3/search?order=desc&sort=votes&intitle={topic}&site=stackoverflow"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open("search_results.txt", "w") as f:
            for item in data["items"]:
                f.write(item["title"] + "\n")
    else:
        print(f"Error: {response.status_code}")
    return result


# replace this with the text of your resume
#my_resume = "I am a web with 5 years of experience..."

# call the dun function with the resume text
#result = reuse(my_resume)
