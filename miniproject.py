import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
import pickle
df=pd.read_csv('/content/miniproject.csv')

df.head(5)

df.info()

df.isnull().sum()

df['Class'].unique()

df.dropna(inplace=True)

amount_scaler = StandardScaler()
time_scaler = StandardScaler()

df['Amount'] = amount_scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
df['Time'] = time_scaler.fit_transform(df['Time'].values.reshape(-1, 1))

df['Class'].value_counts()

"""this dataset is highly unbalanced
"""

x = df.drop(columns='Class', axis=1)
y = df['Class']

x_train, x_test, y_train, y_test= train_test_split(x, y, test_size=0.2, stratify=y, random_state=42)

print(f"Original shape: {df.shape}")
print(f"Training set shape: {x_train.shape}")
print(f"Realistic test set shape: {x_test.shape}")

train_df = pd.concat([x_train, y_train], axis=1)

legit= df[df.Class==0]
fraud= df[df.Class==1]

print(f"Legit transactions in training set: {legit.shape[0]}")
print(f"Fraud transactions in training set: {fraud.shape[0]}")

"""Building a sample dataset containing similar distribution of normal and fraudulent transactions
"""

legit_sample= legit.sample(n=500)

new_df=pd.concat([legit_sample,fraud],axis=0)

"""shuffling new dataset
"""

new_df = new_df.sample(frac=1, random_state=42)

new_df.groupby('Class').mean()

"""Splitting features and target
"""

x_train_new = new_df.drop(columns='Class', axis=1)
y_train_new = new_df['Class']

model = LogisticRegression()
model.fit(x_train_new, y_train_new)

x_train_prediction=model.predict(x_train_new)
training_data_accuracy= accuracy_score(x_train_prediction, y_train_new)

print(training_data_accuracy)

x_test_prediction= model.predict(x_test)
test_data_accuracy= accuracy_score(x_test_prediction, y_test)

print(test_data_accuracy)

print(confusion_matrix(y_test, x_test_prediction))

print(classification_report(y_test, x_test_prediction))

pickle.dump(model, open('model.pkl','wb'))
pickle.dump(time_scaler, open('time.pkl','wb'))
pickle.dump(amount_scaler, open('amount.pkl','wb'))
