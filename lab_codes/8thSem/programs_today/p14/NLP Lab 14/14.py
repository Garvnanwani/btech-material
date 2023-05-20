#For a given dataset, Implement logistic regression, SVM, Random Forest, Adaboost classifier, using bigram language modelling for feature vector generation, with some train and test set. Use sklearn library for implementation
#For each classification method, display
#confusion matrix
#Classification report
#Accuracy precision, recall and F1 score
#Display the graph showing the comparisons of measures in 3) 


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import matplotlib.pyplot as plt
import re

def preprocess_and_split_data(file_path):
    # Read the dataset from the Excel file
    data = pd.read_excel(file_path)

    # Preprocess the text column
    data['text'] = data['text'].apply(preprocess_text)

    # Split the dataset into text and class columns
    X = data['text'].values
    y = data['class'].values

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def preprocess_text(text):
    # Apply text preprocessing steps (to be done)
    # lowercasing
    # removing punctutation
    # emoji replace with text

    return text

def parse_classification_report(report):
    lines = report.split('\n')
    data = [re.sub(r'\s+', ' ', line).strip().split(' ') for line in lines[2:-3]]
    metrics = ['precision', 'recall', 'f1-score', 'support']
    results = {}
    for metric in metrics:
        values = [float(row[i]) for row in data for i in range(1, len(row)-1) if row[i] != 'avg']
        results[metric] = sum(values) / len(values)
    return results

def main():
    # Preprocess and Split the Data
    file_path = '/Users/yashvinayvanshi/Desktop/NLP Lab/NLP Lab 14/dataset14.xlsx'
    X_train, X_test, y_train, y_test = preprocess_and_split_data(file_path)

    # Generate Bigram Language Model
    vectorizer = CountVectorizer(ngram_range=(2, 2))
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)

    # Implement Logistic Regression
    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)
    y_pred_logreg = logreg.predict(X_test)
    confusion_logreg = confusion_matrix(y_test, y_pred_logreg)
    report_logreg = classification_report(y_test, y_pred_logreg)
    accuracy_logreg = accuracy_score(y_test, y_pred_logreg)
    metrics_logreg = parse_classification_report(report_logreg)

    # Implement SVM
    svm = SVC()
    svm.fit(X_train, y_train)
    y_pred_svm = svm.predict(X_test)
    confusion_svm = confusion_matrix(y_test, y_pred_svm)
    report_svm = classification_report(y_test, y_pred_svm)
    accuracy_svm = accuracy_score(y_test, y_pred_svm)
    metrics_svm = parse_classification_report(report_svm)

    # Implement Random Forest
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    confusion_rf = confusion_matrix(y_test, y_pred_rf)
    report_rf = classification_report(y_test, y_pred_rf)
    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    metrics_rf = parse_classification_report(report_rf)

    # Implement AdaBoost
    adaboost = AdaBoostClassifier()
    adaboost.fit(X_train, y_train)
    y_pred_adaboost = adaboost.predict(X_test)
    confusion_adaboost = confusion_matrix(y_test, y_pred_adaboost)
    report_adaboost = classification_report(y_test, y_pred_adaboost)
    accuracy_adaboost = accuracy_score(y_test, y_pred_adaboost)
    metrics_adaboost = parse_classification_report(report_adaboost)

    # Display Evaluation Metrics and Comparison
    labels = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
    values_logreg = [accuracy_logreg, metrics_logreg['precision'], metrics_logreg['recall'], metrics_logreg['f1-score']]
    values_svm = [accuracy_svm, metrics_svm['precision'], metrics_svm['recall'], metrics_svm['f1-score']]
    values_rf = [accuracy_rf, metrics_rf['precision'], metrics_rf['recall'], metrics_rf['f1-score']]
    values_adaboost = [accuracy_adaboost, metrics_adaboost['precision'], metrics_adaboost['recall'], metrics_adaboost['f1-score']]

    print("Logistic Regression:")
    print("Confusion Matrix:")
    print(confusion_logreg)
    print("Classification Report:")
    print(report_logreg)

    print("\nSVM:")
    print("Confusion Matrix:")
    print(confusion_svm)
    print("Classification Report:")
    print(report_svm)

    print("\nRandom Forest:")
    print("Confusion Matrix:")
    print(confusion_rf)
    print("Classification Report:")
    print(report_rf)

    print("\nAdaBoost:")
    print("Confusion Matrix:")
    print(confusion_adaboost)
    print("Classification Report:")
    print(report_adaboost)

    # Plotting Comparison Graph
    values = [values_logreg, values_svm, values_rf, values_adaboost]
    classifiers = ['Logistic Regression', 'SVM', 'Random Forest', 'AdaBoost']

    plt.figure(figsize=(10, 6))
    for i in range(len(classifiers)):
        plt.plot(labels, values[i], label=classifiers[i], marker='o')
    plt.xlabel('Measures')
    plt.ylabel('Values')
    plt.title('Classifier Performance Comparison')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
