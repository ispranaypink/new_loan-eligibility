import pandas as pd
import random

# Set a random seed for reproducibility
random.seed(42)

# Create an empty DataFrame
data = pd.DataFrame(columns=[
    'Age', 'Income', 'Credit_Score', 'Employment_Status', 'Previous_Loan_Default', 'Loan_Eligibility'
])

# Generate synthetic data
for _ in range(10000):  # Generating data for 10,000 individuals
    age = random.randint(18, 35)
    income = random.randint(20000, 90000)
    credit_score = random.randint(500, 850)
    employment_status = random.choice(['Unemployed', 'Student', 'Employed'])
    previous_loan_default = random.choice([0, 1])

    # Define loan eligibility criteria (you can adjust these as needed)
    if 18 <= age <= 30 and income > 30000 and credit_score > 600 and employment_status == 'Employed' and previous_loan_default == 0:
        loan_eligibility = 'Yes'
    else:
        loan_eligibility = 'No'

    data = pd.concat([data, pd.DataFrame({

        'Age': [age],
        'Income': [income],
        'Credit_Score': [credit_score],
        'Employment_Status': [employment_status],
        'Previous_Loan_Default': [previous_loan_default],
        'Loan_Eligibility': [loan_eligibility]
    })], ignore_index=True)

# Save the synthetic dataset to a CSV file
data.to_csv('C:/Users/prana/Working directory/Projects repository/Loan eligibility/student_loan_eligibility_dataset.csv', index=False)
