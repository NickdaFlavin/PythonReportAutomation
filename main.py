from Test_Callv1API import AppfolioAPIV1_GET
from ParseAppfolioJSON import ParseAppfolioV1JSON
import CreateV1Endpoint as v1


endpoint = v1.AgedReceivableDetail("11/30/23", [79])

print(ParseAppfolioV1JSON(AppfolioAPIV1_GET(endpoint)))