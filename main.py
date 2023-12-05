from Callv1API import AppfolioAPIV1_GET
from ParseAppfolioJSON import ParseAppfolioV1JSON
print(AppfolioAPIV1_GET("tweleve_month_cash_flow.json"))

print(ParseAppfolioV1JSON(AppfolioAPIV1_GET("twelve_month_cash_flow.json")))