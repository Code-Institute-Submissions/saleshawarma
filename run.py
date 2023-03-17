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

    print("Enter the data from the last sales")
    print("Exactly 6 numbers must be entered, with commas separating them.")
    print("The number as to be as: 10,20,30,40,50,60")

    data_str = input("Enter your data: \n")
    
    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):

    try:
        if len(values) == 6:
            
            print(f"Exatly 6 values are entered as shown: {len(values)}")
            
        else:
            raise ValueError(
                f"The entered element is shorter {len(values)}"
             )
    except ValueError as e:
        print(f"Invalid date: {e}, please try again.\n")        


get_sales_data()



 
 