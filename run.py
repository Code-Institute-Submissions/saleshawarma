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


def get_sales_data():
    
    print("Please enter sales data from last market.")
    print("Data should be six number, separated by commas.")
    print("Comma separation: 1,2,3,4,5,6\n")

    data_str = input("Enter your data:")

    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    # Inside the try, converst all string valuees into integers
   
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f" 6 values are necessary, you enterd {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, enter again. \n")


get_sales_data()