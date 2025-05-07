

# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/


# Load libraries
import pandas as pd
from cgi import test
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
dataset = read_csv(url, names=names)

# shape
print(dataset.shape)

# head
print(dataset.head(10))

# descriptions
print(dataset.describe())

# class distribution
print(dataset.groupby('species').size()) # dataset['species'].value_counts()

# Create a 3D scatter plot for the Iris dataset
fig = px.scatter_3d(dataset, 
                    x='sepal_width', 
                    y='sepal_length', 
                    z='petal_width', 
                    color='species')
fig.show()


# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# histograms
dataset.hist()
plt.show()

# scatter plot matrix
scatter_matrix(dataset)
plt.show()


# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1) # stratify=y


# Spot Check Algorithms - or param_grid for the same algorithms
models = [] 
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# Compare Algorithms
plt.boxplot(results, labels=names)
plt.title('Algorithm Comparison')
plt.show()


# Make predictions on validation dataset
model = SVC(gamma='auto', probability=True)
model.fit(X_train, Y_train)
predictions = model.predict(X_test)
probability_estimates = model.predict_proba(X_test)


# Evaluate predictions
print(accuracy_score(Y_test, predictions))
# print(roc_auc_score(Y_test, predictions)) #AUC, ROC - TP, FP
print(confusion_matrix(Y_test, predictions))
print(classification_report(Y_test, predictions))

# save the results
df = pd.DataFrame()
df["y_test"] = Y_test
df["y_pred"] = predictions
df["correct"]=df["y_test"] == df["y_pred"]


import seaborn as sns
import numpy as np

mat = confusion_matrix(Y_test, predictions)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=np.unique(Y_test), yticklabels=np.unique(predictions))
plt.xlabel('true label')
plt.ylabel('predicted label');
plt.show()




# import plotly.express as px
# import pandas as pd
# from sklearn.datasets import load_iris

# # Load iris dataset
# iris = load_iris()
# df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# df['species'] = iris.target

# # Plot 3D scatter plot using plotly
# fig = px.scatter_3d(df, x='sepal length (cm)', y='sepal width (cm)', z='petal length (cm)',
#                     color='species', labels={'species': 'Species'},
#                     title="3D Scatter Plot of Iris Dataset")

# # Show plot
# fig.show()
