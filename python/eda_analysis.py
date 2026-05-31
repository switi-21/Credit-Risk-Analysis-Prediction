import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/financial_loan.csv")

print(df.info())
print(df.describe())

# Missing values
print(df.isnull().sum())

# Distribution
sns.histplot(df['loan_amount'])
plt.show()