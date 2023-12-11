from v1.Test_Callv1API import AppfolioAPIv1_GET
from v2.Test_Callv2API import AppfolioAPIv2_POST
from ParseAppfolioJSON import ParseAppfoliov1JSON
import v1.Createv1Endpoint as v1
import v2.Createv2Endpoint as v2
import json

endpoint = v1.AgedReceivableDetail("11/30/23", [79])

endpoint, json_data = v2.CashFlow("01/01/23", "12/31/23", property_ids=[79])

response, used_package = AppfolioAPIv2_POST(endpoint, json_data)

print(used_package)
print(json.loads(response))