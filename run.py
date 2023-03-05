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
    
    while True:
        print("Enter the data from the last sales")
        print("Exactly 6 numbers must be entered, with commas separating them.")
        print("The number as to be as: 1,2,3,4,5,6")

        data_str = input("Enter your data:")

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
    print("The update was sucessfull\n")


data = get_sales_data()
sales_data = [int(num)for num in data]
update_sales_sheet(sales_data)