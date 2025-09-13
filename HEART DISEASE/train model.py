
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,AdaBoostClassifier,ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score,classification_report
from sklearn.impute import SimpleImputer
import joblib

df = pd.read_csv(r"C:\Users\Saloni\Downloads\Data Science\Nit\sept\10th, 11th - Ensamble Learning\9th- Ensamble learning\Machine Learning CAPSTONE PROJECT\HEART DISEASE\heart_disease_uci.csv")

#identify all col with non-numerical data
categorical_cols = df.select_dtypes(include=['object','category']).columns.tolist()

#apply one hot encoding to all identified categorical data
df = pd.get_dummies(df, columns=categorical_cols)

#define features and target
x = df.drop('num',axis = 1)  #drop target
y = df['num'] #target col

#handling o f missing values
imputer = SimpleImputer(strategy='mean')
x = imputer.fit_transform(x)

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state= 0)

#standardlixe the features
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)


#intialilze models
models = {
    'Logistic Regression':LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'KNN':KNeighborsClassifier(),
    'SVM': SVC(probability=True),
    'XGBoost' : XGBClassifier(use_label_encoder = False,eval_metric = 'logloss'),
    'Naive Bayes': GaussianNB(),
    'Gradient Boosting':GradientBoostingClassifier(),
    'AdaBoost': AdaBoostClassifier(),
    'Extra Trees': ExtraTreesClassifier() 
}

#train and evaluate each model
for model_name, model in models.items():
    model.fit(x_train_scaled,y_train)
    y_pred = model.predict(x_test_scaled)
    accuracy = accuracy_score(y_test,y_pred)
    print(f"{model_name} Accuracy:{accuracy:.2f}")
    print(classification_report(y_test,y_pred))
    
    #save the model
    joblib.dump(model,f'{model_name.replace(" ","_").lower()}.pkl')
    
    
#save scaler and imputer
joblib.dump(scaler,'scaler.pkl')
joblib.dump(model,'model.pkl')
joblib.dump(imputer,'imputer.pkl')

















