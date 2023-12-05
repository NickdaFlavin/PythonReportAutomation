from Callv1API import AppfolioAPIV1_GET
from ParseAppfolioJSON import ParseAppfolioV1JSON

print(type(ParseAppfolioV1JSON(AppfolioAPIV1_GET("balance_sheet.json"))))
print(ParseAppfolioV1JSON(AppfolioAPIV1_GET("balance_sheet.json")))