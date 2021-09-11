"""Module 1 Challenge
    Part 1: Automate calculation example
    Part 2: Analyze loan data example
    Part 3: Perform financial calculations
    Part 4: Conditionally filter lists of loans
    Part 5: Save results to CSV 
"""
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the
       list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the
       average loan price.
    4. Print all calculations with descriptive messages.
"""

print("\n")
print("PART 1: AUTOMATE THE CALCULATIONS".center(70,"="))

loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!

loan_count = len(loan_costs)
print("Loan count: ".ljust(30, "."), loan_count)

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!

total_loan_cost = sum(loan_costs)
print("Total loan costs: ".ljust(30, "."), total_loan_cost)

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!

average_loan_cost = round(total_loan_cost / loan_count, 2)
print("Average loan cost: ".ljust(30, "."), average_loan_cost)


##############################################################################
"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to 
calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the 
   **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and 
       `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon 
    maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan
    needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan.
   Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the
   present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost,
       then print a message that says the loan is worth at least the cost to 
       buy it.
    b. Else, the present value of the loan is less than the loan cost, then
       print a message that says that the loan is too expensive and not worth 
       the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required
    minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
print("\n")
print("PART 2: ANALYZE LOAN DATA".center(70,"="))

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the
# Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!

future_value = loan.get("future_value", 0)
remaining_months = loan.get("remaining_months", 0)

print("Future value: ".ljust(30,"."), future_value)
print("Remaining months: ".ljust(30, "."), remaining_months)

# @TODO: Use the formula for Present Value to calculate a "fair value" of the
# loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: 
#   Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# YOUR CODE HERE!

present_value = round(future_value / (1 + .20 / 12) ** 9, 2)
print("Present value: ".ljust(30,"."), present_value)
print("Loan price: ".ljust(30,"."), loan.get("loan_price",0))

# If Present Value represents what the loan is really worth, does it make 
# sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if
# the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost,
#    then print a message that says the loan is worth at least the cost to
#    buy it.
#    Else, the present value of the loan is less than the loan cost, then 
#    print a message that says that the loan is too expensive and not worth
#    the price.
# YOUR CODE HERE!

if present_value >= loan.get("loan_price", 0):
    buy_loan = "Yes"
else:
    buy_loan = "No"

print("Buy loan?".ljust(30,"."), buy_loan)


##############################################################################
"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, 
       `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given 
   below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""
print("\n")
print("PART 3: PERFORM FINANCIAL CALCULATIONS".center(70,"="))

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, 
#    `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!

def calculate_present_value(future_value:int, annual_discount_rate:float,
        periods:int):
    """
        Calculates present value.

        :param future_value: [Required] Value of the asset at some point in
            the future.
        :param annual_discount_rate: [Required] Amount of interest paid or 
            earned as a percentage of the balance at the end of the annual
            period.
        :param periods: [Required] Number of remaining periods in which 
            interest is earned or paid.
    """
    present_value = future_value / (1 + annual_discount_rate / 12) ** periods
    return round(present_value, 2)

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!

future_value = new_loan.get("future_value", 0)
remaining_months = new_loan.get("remaining_months", 0)
present_value = calculate_present_value(future_value, .20, remaining_months)
print("Present value: ".ljust(30,"."), present_value)


##############################################################################
"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and 
select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the 
       loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the 
       `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

print("\n")
print("PART 4: CONDITIONALLY FILTER LISTS OF LOANS".center(70,"="))

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

inexpensive_loans=  []

# @TODO: Loop through all the loans and append any that cost $500 or less to
# the `inexpensive_loans` list
# YOUR CODE HERE!

for loan in loans:
    if loan.get("loan_price", 0) <= 500:
        inexpensive_loans.append(loan)


# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!

header = ["Loan Price", "Remaining Months", "Repayment Interval",
            "Future Value"]

print("{:<15} {:<20} {:<20} {:<15}".format("Loan Price", "Remaining Months", 
    "Repayment Interval", "Future Value"))

for loan in inexpensive_loans:
    print("{:<15} {:<20} {:<20} {:<15}".format(loan.get("loan_price",0), 
        loan.get("remaining_months", 0), loan.get("repayment_interval", 0),
        loan.get("future_value",0)))


##############################################################################
"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first 
           row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the 
               CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""
print("\n")
print("PART 5: SAVE THE RESULTS".center(70,"="))

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!

with open(output_path,"w",newline='') as csvfile:
    csv.writer(csvfile).writerow(header)
    for loan in inexpensive_loans:
        csv.writer(csvfile).writerow(loan.values())

print("Inexpensive loans exported to: ", output_path.absolute())