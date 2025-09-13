
from flask import Flask, render_template,request

app = Flask(__name__)

#results of model
results = {
    'Logistic Regression':{
        'accuracy': 0.53,
        'report':'''\
              precision    recall  f1-score   support

           0       0.71      0.78      0.74        80
           1       0.52      0.50      0.51        52
           2       0.20      0.07      0.10        29
           3       0.21      0.41      0.27        17
           4       0.00      0.00      0.00         6

    accuracy                           0.53       184
   macro avg       0.33      0.35      0.33       184
weighted avg       0.51      0.53      0.51       184
'''
    },
    'Decision Tree':{
        'accuracy':0.58,
        'report':'''\
              precision    recall  f1-score   support

           0       0.83      0.80      0.82        80
           1       0.65      0.62      0.63        52
           2       0.22      0.14      0.17        29
           3       0.17      0.29      0.22        17
           4       0.09      0.17      0.12         6

    accuracy                           0.58       184
   macro avg       0.39      0.40      0.39       184
weighted avg       0.60      0.58      0.58       184
'''
    },
    
    'Random Forest':{
        'accuracy':0.60,
        'report':'''\
              precision    recall  f1-score   support

           0       0.79      0.86      0.83        80
           1       0.60      0.60      0.60        52
           2       0.36      0.17      0.23        29
           3       0.17      0.29      0.22        17
           4       0.00      0.00      0.00         6

    accuracy                           0.60       184
   macro avg       0.38      0.39      0.37       184
weighted avg       0.59      0.60      0.58       184
'''
    },
    'KNN':{
        'accuracy': 0.57,
        'report':'''\
              precision    recall  f1-score   support

           0       0.78      0.78      0.78        80
           1       0.46      0.60      0.52        52
           2       0.43      0.21      0.28        29
           3       0.25      0.24      0.24        17
           4       0.17      0.17      0.17         6

    accuracy                           0.57       184
   macro avg       0.42      0.40      0.40       184
weighted avg       0.56      0.57      0.55       184
'''
    },
    'SVM': {
    'accuracy':0.52,
    'report':'''\
       precision    recall  f1-score   support

           0       0.75      0.79      0.77        80
           1       0.44      0.56      0.49        52
           2       0.20      0.03      0.06        29
           3       0.10      0.18      0.13        17
           4       0.00      0.00      0.00         6

    accuracy                           0.52       184
   macro avg       0.30      0.31      0.29       184
weighted avg       0.49      0.52      0.49       184
'''
    },
    'XGBoost':{
        'accuracy':0.60,
        'report':'''\
              precision    recall  f1-score   support

           0       0.84      0.81      0.83        80
           1       0.58      0.65      0.61        52
           2       0.36      0.31      0.33        29
           3       0.11      0.12      0.11        17
           4       0.00      0.00      0.00         6

    accuracy                           0.60       184
   macro avg       0.38      0.38      0.38       184
weighted avg       0.60      0.60      0.60       184
'''
    },
    
    'Naive Bayes':{
        'accuracy':0.38,
        'report':'''\
              precision    recall  f1-score   support

           0       0.86      0.62      0.72        80
           1       0.70      0.27      0.39        52
           2       0.25      0.07      0.11        29
           3       0.00      0.00      0.00        17
           4       0.04      0.67      0.08         6

    accuracy                           0.38       184
   macro avg       0.37      0.33      0.26       184
weighted avg       0.61      0.38      0.44       184
'''
    },
    
    'Gradient Boosting':{
        'accuracy':0.58,
        'report':'''\
              precision    recall  f1-score   support

           0       0.80      0.81      0.81        80
           1       0.58      0.63      0.61        52
           2       0.38      0.28      0.32        29
           3       0.05      0.06      0.05        17
           4       0.00      0.00      0.00         6

    accuracy                           0.58       184
   macro avg       0.36      0.36      0.36       184
weighted avg       0.58      0.58      0.58       184
'''
    },
    

    'AdaBoost':{ 
    'accuracy':0.57,
    'report':'''\
              precision    recall  f1-score   support

           0       0.81      0.79      0.80        80
           1       0.49      0.69      0.57        52
           2       0.43      0.10      0.17        29
           3       0.12      0.18      0.15        17
           4       0.00      0.00      0.00         6

    accuracy                           0.57       184
   macro avg       0.37      0.35      0.34       184
weighted avg       0.57      0.57      0.55       184
'''
    },
    
    'Extra Trees':{
        'accuracy':0.54,
        'report':'''\
              precision    recall  f1-score   support

           0       0.75      0.80      0.78        80
           1       0.51      0.50      0.50        52
           2       0.27      0.14      0.18        29
           3       0.14      0.24      0.18        17
           4       0.20      0.17      0.18         6

    accuracy                           0.54       184
   macro avg       0.37      0.37      0.36       184
weighted avg       0.53      0.54      0.53       184
'''
    }
}


# Find the best model
best_model = max(results,key=lambda x: results[x]['accuracy'])

@app.route('/')
def home():
    return render_template('index.html',best_model=best_model, best_accuracy=results[best_model]['accuracy'])

@app.route('/results')
def get_results():
    return render_template('results.html',results=results)

@app.route('/model/<model_name>')
def get_model_details(model_name):
    if model_name in results:
        return render_template('model.html',model_name=model_name,report=results[model_name]['report'],accuracy=results[model_name]['accuracy'])
    else:
        return f"Model {model_name} not found",404
    
     
    if __name__ == '__main__':
        app.run(debug=True)
        