from Test_Callv1API import AppfolioAPIV1_GET
from ParseAppfolioJSON import ParseAppfolioV1JSON


endpoint = "twelve_month_cash_flow.json"

print(AppfolioAPIV1_GET(endpoint))

print(ParseAppfolioV1JSON(AppfolioAPIV1_GET(endpoint)))