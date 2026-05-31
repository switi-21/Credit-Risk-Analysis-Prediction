import pandas as pd

df = pd.read_csv("../data/financial_loan.csv")

# Convert target variable
df['target'] = df['loan_status'].apply(lambda x: 1 if x == 'Charged Off' else 0)

# Bucket income
df['income_group'] = pd.cut(df['annual_income'],
                           bins=[0,50000,100000,200000,1000000],
                           labels=['Low','Medium','High','Very High'])

print(df.head())
