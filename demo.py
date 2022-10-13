from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
import streamlit as st 
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
st.title("Classifiers")
st.write(""" # This are differnet classifers""")
dataset_name=st.sidebar.selectbox("Select Dataset",("Iris","Breast Cancer","Wine"))
classifier_name=st.sidebar.selectbox("Select Classifier",("KNN","SVM","Random Forest"))
def get_dataset(dataset_name):
        if dataset_name=="Iris":
            data=datasets.load_iris()
        elif dataset_name=="Breast Cancer":
            data=datasets.load_breast_cancer()
        else:
            data=datasets.load_wine()
        X=data.data
        y=data.target
        return X,y
X,y=get_dataset(dataset_name)
st.write("shape of data",X.shape)
st.write("Number of classes",len(np.unique(y)))
def add_parameter_ui(clf_name):
    params=dict()
    if clf_name == "KNN":
        params["K"]= st.sidebar.slider("K",1,15)
        
    elif clf_name == "SVM":
        params["C"]=st.sidebar.slider("C",0.01,10.0)
        
    else:
        params["max_depth"]=st.sidebar.slider("max_depth",2,15)
        params["n_estimators"]=st.sidebar.slider("n_estimtors",1,100)
        
    return params

params= add_parameter_ui(classifier_name)
def get_classifier(clf_name,params):
    if clf_name == "KNN":
        clf=KNeighborsClassifier(n_neighbors=params["K"])
    elif clf_name == "SVM":
        clf=SVC(C=params["C"])
    else:
        clf=RandomForestClassifier(n_estimators=params["n_estimators"],max_depth=["max_depth"],random_state=1600)
    return clf
clf=get_classifier(classifier_name, params)
X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2,random_state=1600)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
acc =accuracy_score(y_test,y_pred)
st.write(f"Classifier = {classifier_name}")
st.write(f"Accuracy={acc}")
pca=PCA(2)
X_projected=pca.fit_transform(X)
x1=X_projected[:,0]
x2=X_projected[:,1]
fig=plt.figure()
plt.scatter(x1,x2,c=y,alpha=0.8,cmap="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar()
st.pyplot(fig)

    

