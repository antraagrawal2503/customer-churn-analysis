# Customer Churn Analysis

This project analyzes customer churn data to uncover patterns and generate business insights that can help improve customer retention strategies.

## Objective
Understand why customers leave and identify insights that can help improve retention strategies.

## Tools & Technologies
- Python (pandas, matplotlib)
- Data cleaning and preprocessing
- Data visualization

## Key Analysis
- Distribution of churned vs retained customers
- Impact of monthly charges on churn
- Contract type vs churn
- Data cleaning (handling missing values)

## Key Insights
- Customers with higher monthly charges show a higher likelihood of churning, suggesting pricing sensitivity.
- Customers with long-term contracts are less likely to churn compared to month-to-month users.
- Churn is significantly higher among customers without add-on services like streaming or tech support.

## Project Structure
- analysis.py → data cleaning and analysis
- customer_churn.csv → dataset
- requirements.txt → dependencies

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt