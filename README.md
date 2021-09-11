# Rice FinTech Bootcamp, Module 1 Challenge

## Notes

Code is not modularized for reuse, error-handled, or tested by design.  The
 module was an exercise to introduce people to coding who may not have had any
 prior coding experience. Thus, the deliverable was heavily templated.

## Background

You work for a lending startup engaged in microcredit loans. The company needs
help valuing these loans. In this Challenge, you'll automate a process that  
does just that.

## Objectives

- Automate basic financial calculations for loans
- Analyze loan data against a provided set of requirements
- Perform financial calculations
- Conditionally filter lists of loans
- Save the results to a CSV file

## Requirements

### Automation

- [X] Calculate the total number of loans in the list. (2 points)
- [X] Calculate the total value (sum) of all loans in the list. (2 points)
- [X] Using the sum of all loans and the total number of loans, calculate
the average loan price. (2 points)
- [X] Print all calculations, each with a descriptive message. (2 points)
- [X] Run without error and produce the required result. (2 points)

### Analysis: Analyze Loan Data

- [X] Use get to extract future value and remaining months variables, named
 accordingly. (5 points)
- [X] Calculate the fair value of the loan using the present value formula
 and a 20% discount rate. (5 points)
- [X] Use a conditional statement to determine and print the loan's fair
 value. (5 points)
- [X] Analyze the loan value with a minimum return of 20% in order to
 determine purchasability of the loan. (5 points)

### Financial Calculations: Perform Financial Calculations

- [X] Create a new function to calculate present value, parameters included
  and present_value returned. (10 points)
- [X] Use a function to calculate the present value of the new loan, using an
 annual discount rate of 0.2. (10 points)

### Filter Lists of Loans

- [X] Create an empty list, inexpensive_loans. (1 point)
- [X] Use a for loop to determine if loan_price is less than or equal to 500.
 (3 points)
- [X] Append the inexpensive_loans list with loan_price that are less than or
 equal to 500. (3 points)
- [X] Print the inexpensive_loans list. (3 points)

### Save Results

- [X] Use with open to open a new CSV file. (2 points)
- [X] Create csvwriter using the csv library. (2 points)
- [X] Use csvwriter to write the header variable in the first row. (2 points)
- [X] Use a for loop to iterate through each loan in inexpensive. (2 points)
- [X] Use csvwriter to write the loan.values() to a row in the CSV file. (2 points)

### Coding Conventions and Formatting

- [X] Move imports to the top of the file, just after any module comments, and
 before module globals and constants. (3 points)
- [X] Name functions and variables with lowercase characters, with words
 separated by underscores. (2 points)
- [X] Follow DRY (Don't Repeat Yourself) principles, creating maintainable
 and reusable code. (3 points)
- [X] Use concise logic and creative engineering where possible.

### Deployment and Submission

- [X] Be contained in a GitHub repository.
- [X] Contain appropriate commit messages.

### Comments

- [X] Be well commented with concise, relevant notes that can be understood by
 another developer. (10 points)
