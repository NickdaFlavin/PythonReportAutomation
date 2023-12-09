
from datetime import datetime
import json


#Helper Functions
def ConvertDatetoYYYYMM(date:str):
    parsed_date = datetime.strptime(date,'%m/%d/%y')
    return parsed_date.strftime('%Y-%m')

#Create a Function for each Endpoint
#   CashFlow
def CashFlow(from_date:str, to_date:str, 
             property_ids:list = [], property_group_ids:list = [], portfolios_ids:list = [], owners_ids:list = [], 
             accounting_basis:str = "Cash", visibility:str = "active", level_of_detail:str = "detail_view", include_zero_balance_gl_accounts:int = 0,
             exclude_suppressed_fees:int = 0, columns:list = []
             ):
    jsonpackage = {
        "property_visibility": visibility,
        "properties": {
            "properties_ids": [','.join(str(i) for i in property_ids)],
            "property_groups_ids": [','.join(str(i) for i in property_group_ids)],
            "portfolios_ids": [','.join(str(i) for i in portfolios_ids)],
            "owners_ids": [','.join(str(i) for i in owners_ids)]
        },
        "posted_on_from": ConvertDatetoYYYYMM(from_date),
        "posted_on_to": ConvertDatetoYYYYMM(to_date),
        "accounting_basis": accounting_basis,
        "level_of_detail": level_of_detail,
        "include_zero_balance_gl_accounts": include_zero_balance_gl_accounts,
        "exclude_suppressed_fees": exclude_suppressed_fees, 
        "columns": [','.join(i for i in columns)]
    }
    return "twelve_month_cash_flow.json", jsonpackage


data['propeties'] = {}
data['propeties']['properties_ids'] = 'value'


