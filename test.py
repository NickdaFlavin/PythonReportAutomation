import json
import requests
import Ignore.api_details as api_details

json_package = {
   "property_visibility": "active", 
   "properties": {"properties_ids": ["79"]}, 
   "posted_on_from": "2023-01", 
   "posted_on_to": "2023-12", 
   "accounting_basis": "Cash", 
   "level_of_detail": "detail_view", 
   "include_zero_balance_gl_accounts": 0, 
   "exclude_suppressed_fees": 0
}

appfolio_client_ID = api_details.appfolio_client_id
appfolio_client_Secret = api_details.appfolio_client_secret
appfolio_database = api_details.appfolio_database_name

api_url = f"https://{appfolio_database}.appfolio.com/api/v2/reports/twelve_month_cash_flow.json"

headers = {
   'Content-Type': 'application/json'
}

try:
   response = requests.post(api_url, json=json_package, headers=headers, auth=(appfolio_client_ID, appfolio_client_Secret))
   
except requests.RequestException as e:
   response = f"ERROR: Request Failed - {e}"

json_response = response.json()

print(json_response)