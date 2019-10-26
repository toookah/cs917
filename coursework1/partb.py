import csv

"""
    Part B
    Please provide definitions for the following functions
"""

# create_portfolio() -> [code]

# best_investments(data, portfolio, x, start_date. end_date) -> [code]

# worst_investments(data, portfolio, x, start_date. end_date) -> [code]


# Replace the body of this main function for your testing purposes
if __name__ == "__main__":
    # Start the program
    data = []
    with open("ftse100.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]
    pass
