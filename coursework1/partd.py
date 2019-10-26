import matplotlib.pyplot as plt
import csv

"""
    Part D
    Please provide definitions for the following clas and functions
"""

class Company:
    pass


# predict_next_average(company) -> float

# classify_trend(company) -> str


# Replace the body of this main function for your testing purposes
if __name__ == "__main__":
    # Start the program
    data = []
    with open("ftse100.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]
    pass
