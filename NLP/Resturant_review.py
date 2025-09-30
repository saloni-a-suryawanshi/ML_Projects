
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"C:\Users\Saloni\Downloads\Data Science\Nit\sept\Restaurant_Reviews.tsv",delimiter= '\t',quoting= 3)


#cleaning the texts
import re #regular expression
import nltk    #library
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []

for i in range (0,1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

#creating the bag of words
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,1].values


#splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
x_train , x_test , y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=0)


from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(x_train,y_train)

#predicting the test set results
y_pred = classifier.predict(x_test)

#making the confusion tree
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test,y_pred)
print(ac)

bias = classifier.score(x_train,y_train)
bias

variance = classifier.score(x_test,y_test)
variance














