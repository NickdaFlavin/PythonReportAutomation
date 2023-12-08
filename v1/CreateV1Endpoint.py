from datetime import datetime


#Create a function for each common endpoint
#   Aged Receivable Detail
def AgedReceivableDetail(to_date:str, property:list = [], columns:list = [], owners:list = [], paginate:bool = False):
    return f"aged_receivables_detail.json?{ToDate(to_date)}&{Properties(property)}&{Columns(columns)}&{Owners(owners)}&{PaginateResults(paginate)}"
#   Annual Budget Comparative
def AnnualBudgetComparative():
    return
#   Balance Sheet

#   Balance Sheet Comparison
#   Budget Detail
#   Cashflow 1-month/12 month
#   Chart of Accounts
#   Delinquency/Aged Receivables
#   GPR
#   GL
#   Lease Expiration
#   Property Directory
#   Rent Roll
#   Tenant Tickler
#   Trial Balance
#
#Create a Function for each argument
#   Properties
def Properties(propertylist:list):
    return f"properties={','.join(str(i) for i in propertylist)}"
#   GL Accounts
def GLCodes(accountlist:list):
    return f"gl_accounts={','.join(str(i) for i in accountlist)}"
#   Columns
def Columns(columnlist:list):
    return f"columns={','.join(i for i in columnlist)}"
#   Owners
def Owners(ownerlist:list):
    return f"owners={','.join(str(i) for i in ownerlist)}"
#   Tags
def Tags(taglist:list):
    return f"tags={','.join(i for i in taglist)}"
#   Accounting Basis
def AccountingBasis(accounting:str):
    return f"accounting_basis={accounting}"
#   From Date
def FromDate(date:str):#Let's Assume that the date is in the format "mm/dd/yy" already
    return f"from_date={ConvertDatetoAppfolioFormat(date)}"
#   To Date
def ToDate(date:str):
    return f"to_date={ConvertDatetoAppfolioFormat(date)}"
#   Reversed Transactions
def ReversedTransactions(rv:bool):
    return f"show_reversed_transactions={str(rv)}"
#   Property Visibility
def PropertyVisibility(visibility:str):
    return f"property_visibility={visibility}"
#   Paginate Results
def PaginateResults(paged:bool):
    return f"paginate_results={str(paged)}"


#Helper Functions
def ConvertDatetoAppfolioFormat(date:str):
    parsed_date = datetime.strptime(date,'%m/%d/%y')
    return parsed_date.strftime('%Y-%m-%d')

