import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
df = pd.read_csv("../data/financial_loan.csv")

# Target
df['target'] = df['loan_status'].apply(lambda x: 1 if x == 'Charged Off' else 0)

# Features
X = df[['loan_amount', 'int_rate', 'dti']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))


print("Confusion Matrix:")
print(confusion_matrix(y_test, pred))