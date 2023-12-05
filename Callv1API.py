import requests
import os


def AppfolioAPIV1_GET(endpoint: str):

    appfolio_client_ID = os.environ.get('APPFOLIO_CLIENT_ID')
    appfolio_client_Secret = os.environ.get('APPFOLIO_CLIENT_SECRET')
    appfolio_database = os.environ.get('APPFOLIO_DATABASE_NAME')

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
