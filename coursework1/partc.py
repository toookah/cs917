import matplotlib.pyplot as plt
import csv

"""
    Part C
    Please provide definitions for the following functions
"""

# plot_company(data, code, start_date, end_date)

# plot_portfolio(data, portfolio, start_date, end_date)


# Replace the body of this main function for your testing purposes
if __name__ == "__main__":
    # Start the program
    data = []
    with open("ftse100.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]
        
    pass
