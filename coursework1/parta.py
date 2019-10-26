import csv

"""
    Part A
    Please provide definitions for the following functions
"""

# daily_movement(data, code, date) -> float
def daily_movement(data, code, date):
  for i in range(len(data)):
    if code==data[i]['code']:
      return float('%.2f' % data[i]['diff'])
  while code==data[i]['code']:
    print
ls
# daily_high(data, code, date) -> float

# daily_low(data, code, date) -> float

# daily_avg(data, code, date) -> float

# percentage_change(data, code, date) -> float

# Replace the body of this main function for your testing purposes
if __name__ == "__main__":
    # Start the program
    
    # Example variable initialization
    # data is always the ftse100.csv read in using a DictReader
    data = []
    with open("ftse100.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]
    # code is always a string value
    code = "III"
    # date is always a string imnpoformatted 'dd/mm/yyyy'
    date = "14/10/2019"
    
    # to access individual rows from data using list indices
    first_row = data[0]
    # to access row values, use the relevant column heading found in the csv file
    print(f"code = {first_row['code']}")
    print(f"price = {first_row['price']}")
    print(f"date = {first_row['date']}")
    pass
