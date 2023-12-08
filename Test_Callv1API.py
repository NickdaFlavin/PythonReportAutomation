import requests
import os
import Ignore.api_details as api_details


def AppfolioAPIV1_GET(endpoint: str):

    appfolio_client_ID = api_details.appfolio_client_id
    appfolio_client_Secret = api_details.appfolio_client_secret
    appfolio_database = api_details.appfolio_database_name

    if appfolio_client_ID and appfolio_client_Secret and appfolio_database:
        api_url = f"https://{appfolio_database}.appfolio.com/api/v1/reports/{endpoint}"
    else:
        return "ERROR: Retrieving Secrets"
    
    try:
        response = requests.get(api_url, auth=(appfolio_client_ID, appfolio_client_Secret))
        if response.status_code == 200:
            return response.text
        else:
            return f"ERROR: Invaild Response: {response.status_code}"

    except requests.RequestException as e:
        return f"ERROR: Request Failed - {e}"
