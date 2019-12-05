# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
# code starts here
bank = pd.read_csv(path) 
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var.head())
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var.head())
# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'], axis=1)
print(type(banks))
print(banks.isnull().sum())
bank_mode = banks.mode()
#print(type(bank_mode))
#print(bank_mode.head())
banks.fillna(value=bank_mode.T.squeeze(), inplace=True)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
#avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'], values=['LoanAmount'], aggfunc='mean')
avg_loan_amount = pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'], values=['LoanAmount'], aggfunc=np.mean)
print(avg_loan_amount)
# code ends here


# --------------
# code starts here
loan_approved_se = len(banks[(banks['Self_Employed'] == "Yes") & (banks['Loan_Status'] == "Y")])
loan_approved_nse = len(banks[(banks['Self_Employed'] == "No") & (banks['Loan_Status'] == "Y")])
print(loan_approved_se)
print(loan_approved_nse)
Loan_Status = 614
percentage_se = (loan_approved_se/Loan_Status) * 100
percentage_nse = (loan_approved_nse/Loan_Status) * 100
# code ends here


# --------------
# code starts here
loan_term = banks["Loan_Amount_Term"].apply(lambda x: x/12)
#print(loan_term.head())
big_loan_term = len(banks[loan_term >= 25])
print(big_loan_term)
# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
print(loan_groupby.first())
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
print(loan_groupby.head())
mean_values = loan_groupby.agg([np.mean])
print(mean_values.head())
# code ends here


