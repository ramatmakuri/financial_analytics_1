# coding: utf-8
import csv
from os import path
from pathlib import Path
from typing import DefaultDict

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!
number_loans = len(loan_costs)
print(f"The total number of loans in the list are {number_loans}")
# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!
total_loans = sum(loan_costs)
print(f"The sum of loans in the list are {total_loans}")

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!
average_loans = total_loans / number_loans
print(f"The average of the loans in the list is {average_loans}")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.
    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!
future_value = loan.get('future_value',0)
remaining_months = loan.get('remaining_months')
print(f"The future valiue of the loan is {future_value}")
print (f"The remaining period in months for the laon is {remaining_months}")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# YOUR CODE HERE!
discount_rate = (20/100)
print(f"The discount rate used is {discount_rate}")
present_value = future_value / ((1+(discount_rate/12))**remaining_months)
print (f"The present value of the loan is {present_value}")
# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!
for item in loan_costs:
    if present_value>= item:
        print(f"The loan amounting to {item} is worth ateleast the cost to buy it")
    else:
        print(f"The loan amounting to {item} is too expensive and not worth the price") 

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value_new = new_loan.get('future_value')
print (f"The future value for the new loan is {future_value_new}")
remaining_months_new = new_loan.get('remaining_months')
print (f"The remaining period in  months for the new loan is {remaining_months_new}")
discount_rate_new = 0.2
print (f"The annual discount rate for the new loan is {discount_rate_new}")
present_value_new = future_value_new / ((1+(discount_rate_new/12)) ** remaining_months_new)
#present_value_new = future_value_new / ((1+(discount_rate_new/12))**remaining_months_new)
print (f"The present value for the  new loan is {present_value_new}")

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!

def pv_calculate():
    present_value_new_1 = 0
    future_value_new1 = input("Please provide the future value of the loan: ")
    remaining_months_new1 = input("Please provide the remaining months of the loan: ")
    discount_rate_new1 = input("Please provide the annual discount rate of the loan: ")
    return float(future_value_new1) / float((1+(float(discount_rate_new1)/12))**float(remaining_months_new1))
# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!
print(f"The present value of the loan is:{pv_calculate()}")

"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]
# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!
inexpensive_loans = []
# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!
for i in loans:
    for (key, value)  in i.items():
        if key == "loan_price":
            if value <= 500:
                inexpensive_loans.append(value)        
# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!
print (inexpensive_loans)
 
"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""
# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!
# Iterate over all the items in dictionary and filter items which has values in inexpensive_loans list
newDict =  loans.copy()
for i in newDict:
    for key, value in list(i.items()):
        if key == 'loan_price' and value not in inexpensive_loans:
            i.clear()            
import csv
from pathlib import Path 
output_path = Path('taste.csv')
file_keys = newDict[0].keys()
field_names = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
with open (output_path, 'w', newline = '') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=field_names,delimiter = ';')
    csv_writer.writeheader()
    csv_writer.writerows(newDict)
print(newDict) 