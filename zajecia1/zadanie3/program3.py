#!/usr/bin/python3


import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model


os.chdir('/home/students/s442188/konsultacje/umz-template/zajecia1/zadanie3/train')
report=pd.read_csv('train.tsv', sep='\t', names=['price', 'isNew', 'rooms', 'floor', 'location', 'sqrMeters'])
reg=linear_model.LinearRegression()
reg.fit(pd.DataFrame(report, columns=['rooms', 'sqrMeters']), report['price'])
print(reg.coef_)
print(reg.intercept_)

os.chdir('/home/students/s442188/konsultacje/umz-template/zajecia1/zadanie3/dev-0')
report2=pd.read_csv('in.tsv', sep='\t', names=['isNew', 'rooms', 'floor', 'location', 'sqrMeters'])
x_dev=pd.DataFrame(report2, columns=['rooms', 'sqrMeters'])
y_dev_predict=reg.predict(x_dev)
pd.DataFrame(y_dev_predict).to_csv('out.tsv', sep='\t', index=False, header=False)

os.chdir('/home/students/s442188/konsultacje/umz-template/zajecia1/zadanie3/test-A')
report3=pd.read_csv('in.tsv', sep='\t', names=['isNew', 'rooms', 'floor', 'location','sqrMeters']) 
x_test=pd.DataFrame(report3, columns=['rooms', 'sqrMeters'])
y_test_predict=reg.predict(x_test)
pd.DataFrame(y_test_predict).to_csv('out.tsv', sep='\t', index=False, header=False)

sns.regplot(y=report["price"], x=report["rooms"]); plt.show()
