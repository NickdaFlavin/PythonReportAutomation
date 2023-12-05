from Callv1API import AppfolioAPIV1_GET
from ParseAppfolioJSON import ParseAppfolioV1JSON


print(ParseAppfolioV1JSON(AppfolioAPIV1_GET("tweleve_month_cash_flow.json")))