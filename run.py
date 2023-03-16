import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json') 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('saleshawarma')

sales = SHEET.worksheet('sales')
data = sales.get_all_values()

print(data)

"""vdef get_sales_data():

while True:
        print("Enter the data from the last sales")
        print("Exactly 6 numbers must be entered, with commas separating them.")
        print("The number as to be as: 1,2,3,4,5,6")

        data_str = input("Enter your data:\n")

        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("The entered data is valid!")
            break

    return sales_data    


def validate_data(values):

    # Inside the try, converst all string valuees into integers
   
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f" 6 values are necessary, you enterd {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, enter again.\n")
        return False
    
    return True


def update_sales_sheet(data):
    # sales_sheets updater
    print("updating sales values")
    sales_sheet = SHEET.worksheet("sales")
    sales_sheet.append_row(data)
    print(" The sale update was sucessfull.\n")


def update_surplus_sheet(data):
    # surplus_sheets updater
    print("updating surplus values")
    surplus_sheet = SHEET.worksheet("surplus")
    surplus_sheet.append_row(data)
    print("The surplus update was sucessfull.\n")



def update_worksheet(data, worksheet):

    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet update was successful\n")


def calculate_surplus(sales_row):

    # suplus calculation

    print("Calculating surplus\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
        # if (surplus != 0 and -surplus):
        # print("Keep the surplus for the Doggs ")

    return surplus_data    


def get_last_5_entries_sales():

    sales = SHEET.worksheet("sales")
    # column = sales.col_values(3)
    # print(column)

    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column)
    print(columns)   


def main():

    # run all the functions

    data = get_sales_data()
    sales_data = [int(num)for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus = calculate_surplus(sales_data)
    update_worksheet(new_surplus, "surplus")
  

print("welcome Sale Sawhawarma")

# main()
get_last_5_entries_sales()
"""
