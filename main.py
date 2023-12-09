from v1.Test_Callv1API import AppfolioAPIv1_GET
from Test_Callv2API import AppfolioAPIv2_POST
from ParseAppfolioJSON import ParseAppfoliov1JSON
import v1.Createv1Endpoint as v1
import Createv2Endpoint as v2


endpoint = v1.AgedReceivableDetail("11/30/23", [79])

endpoint, json_data = v2.CashFlow("01/01/23", "12/31/23", property_ids=[79])

print(AppfolioAPIv2_POST(endpoint, json_data))
