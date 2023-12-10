from v1.Test_Callv1API import AppfolioAPIv1_GET
from v2.Test_Callv2API import AppfolioAPIv2_POST
from ParseAppfolioJSON import ParseAppfoliov1JSON
import v1.Createv1Endpoint as v1
import v2.Createv2Endpoint as v2

import pandas as pd
import json
from fpdf import FPDF


endpoint, json_data = v2.CashFlow("01/01/23", "12/31/23", property_ids=[79])


api_data = json.loads(AppfolioAPIv2_POST(endpoint, json_data))


df = pd.DataFrame(api_data)
columns = ['AccountCode'] + [col for col in df.columns if 'Slice' in col]
new_df = df[columns]

pdf = FPDF('L')

pdf.add_page()

pdf.set_font('Times', '', 12)

for index, row in new_df.iterrows():
    for i, col in enumerate(row):
        pdf.cell(20, 10, txt=str(col).encode().decode('latin-1', 'strict'), ln=True if i == len(row)-1 else 0)

pdf.output('ouput.pdf', 'F')
