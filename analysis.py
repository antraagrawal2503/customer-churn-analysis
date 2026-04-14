import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customer_churn.csv")

# Basic info
print(df.head())
print(df.info())

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Drop missing values
df = df.dropna()

# Churn distribution
churn_counts = df['Churn'].value_counts()
print(churn_counts)

# Plot churn distribution
churn_counts.plot(kind='bar')
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Count")
plt.show()

# Monthly charges vs churn
df.boxplot(column='MonthlyCharges', by='Churn')
plt.title("Monthly Charges vs Churn")
plt.suptitle("")
plt.show()

# Contract type vs churn
contract_churn = pd.crosstab(df['Contract'], df['Churn'])
contract_churn.plot(kind='bar', stacked=True)
plt.title("Contract Type vs Churn")
plt.xlabel("Contract Type")
plt.ylabel("Count")
plt.show()