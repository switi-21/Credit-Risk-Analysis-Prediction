import sqlite3
import pandas as pd

conn = sqlite3.connect("loan.db")

df = pd.read_csv("../data/financial_loan.csv")
df.to_sql("loans", conn, if_exists="replace", index=False)

query = """
SELECT grade, AVG(int_rate) as avg_interest
FROM loans
GROUP BY grade
"""

result = pd.read_sql(query, conn)
print(result)