import numpy as np
from scipy.optimize import minimize
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data file from URL address
#df = pd.read_csv("5.csv")
#dataset = dataframe.values
#print(dataset)

# split into input (X) and output (Y) variables
#X = dataset[:,0:2]
#print(X.shape)
#Y = dataset[:,3]
#Y=pd.DataFrame(dataframe,columns=['dis'])
#X=dataframe.drop('dis',axis=1)
#start=1
#index=45
#print(test[:32]))
'''
xm1 = np.array(df["angle/vx"][:index],dtype="float64")  # WTI Oil Price
xm2 = np.array(df["yaw/vx2"][:index],dtype="float64")   # Henry Hub Gas Price
xm3 = np.array(df["front/vx"][:index],dtype="float64")  # MB Propane Spot Price
ym=np.array(df["dangle_yaw"][:index],dtype="float64")  

######################
xm1 = np.array(df[" slip angle"][:index],dtype="float64")  # WTI Oil Price
xm2 = np.array(df[" yaw"][:index],dtype="float64")   # Henry Hub Gas Price
xm3 = np.array(df[" front wheel"][:index],dtype="float64")  # MB Propane Spot Price
ym=np.array(df[" dyaw"][:index],dtype="float64")  
#ym = np.array(df["dis"])  # oil sales price received (outcome)
'''
from sklearn.datasets import make_regression
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from pickle import load
import joblib
file1 = open("test.txt","r") 
file2 = open("test2.txt","r+")
sc_X = joblib.load('sc_X.sav')
sc_y =joblib.load('sc_y.sav')
regressor = joblib.load('finalized_model.sav')
while(1):
 
 d=file1.readline()
 if(d):
  input_svn=d.split(",")

  X=np.array(input_svn,dtype='float64')
  X=X.reshape(-1,5)
  print(X)
  Xs =sc_X.transform(X)
  k=regressor.predict(Xs)
  ks=sc_y.inverse_transform(k)
  print(ks)
  file2.write(str(ks[0]))
  file2 .close()
  file2 = open("test2.txt","r+") 
  file1.close()
  file1 = open("test.txt","r+") 
  file1.truncate(0)
  file1.close()
  file1 = open("test.txt","r")
'''
X = np.array(df[[' dyaw','yaw/vx', ' front wheel', 'yaw/vx2',' front/vx']][start:index],dtype='float64')#
#X = np.array(df[[' dyaw', 'yaw/vx2','front/vx']][start:index])#,' speed motor'

y = np.array(df[' slip angle'][start:index],dtype='float64')
#y = np.array(df[' slip angle'][start:index])
#print(y.shape)
y=y.reshape(-1,1)

sc_X = joblib.load('sc_X.sav')

sc_y =joblib.load('sc_y.sav')
#print(X)
X =sc_X.transform(X)
y = sc_y.transform(y)


#print("x is {}".format(X))
#print("y is {}".format(y))
#print(y.shape)
# define model

regressor = joblib.load('finalized_model.sav')
k=regressor.predict(X)
ks=sc_y.inverse_transform(k)
ks=ks.reshape(-1,1)
print(regressor.score(X,y))
print(ks)
#from here 
#df = pd.read_csv("cars.csv")
'''
'''
X = df[['angle/vx', 'yaw/vx2','front/vx']][start:index]

y = df['dangle_yaw'][start:index]
'''


'''
X = df[['y_hat-y','est_angle']][start:index]
#print(X)
y = df[' slip angle'][start:index]
'''
