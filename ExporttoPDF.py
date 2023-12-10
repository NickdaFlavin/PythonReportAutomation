from v1.Test_Callv1API import AppfolioAPIv1_GET
from v2.Test_Callv2API import AppfolioAPIv2_POST
from ParseAppfolioJSON import ParseAppfoliov1JSON
import v1.Createv1Endpoint as v1
import v2.Createv2Endpoint as v2

import pandas as pd


endpoint, json_data = v2.CashFlow("01/01/23", "12/31/23", property_ids=[79])

print(AppfolioAPIv2_POST(endpoint, json_data))


pd.DataFrame