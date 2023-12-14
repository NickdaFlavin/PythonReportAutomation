from v1.Test_Callv1API import AppfolioAPIv1_GET
from v2.Test_Callv2API import AppfolioAPIv2_POST
from ParseAppfolioJSON import ParseAppfoliov1JSON
import v1.Createv1Endpoint as v1
import v2.Createv2Endpoint as v2
import CashFlow as cash_flow

import pandas as pd
import json
from fpdf import FPDF


endpoint, json_data = v2.CashFlow("01/01/23", "12/31/23", property_ids=[79])

api_data = json.loads(AppfolioAPIv2_POST(endpoint, json_data))

df = pd.json_normalize(api_data, record_path=['months'], meta=['account_code'])

df['value'] = df['value'].astype(float)

df_agg = df.groupby(by=['account_code', 'id']).sum().round(2).reset_index()

pivot_df = df_agg.pivot(index='account_code', columns='id', values='value')

cahflowdict_strkeys = {str(key): value for key, value in cash_flow.cashflowdict.items()}
custom_cashflow_order = ['rental income', 'subsidized rental income', 'other op income', 'payroll', 'utilities', 'turnove costs', 'maintenance expense', 'advertising', 'other expenditures', 'taxes and licenses']

pivot_df['cash_flow_cat'] = pivot_df.index.map(cahflowdict_strkeys)

df_agg = pivot_df.groupby(by=['cash_flow_cat']).sum().round(2).reset_index()
df_agg.set_index('cash_flow_cat', inplace=True)


pdf = FPDF('L')

pdf.add_page()

pdf.set_font('Times', '', 10)


for index, row in pivot_df.iterrows():
    pdf.cell(20, 10, txt=str(index).encode().decode('latin-1', 'strict'), ln=False)
    for i, col in enumerate(row):
        if i == len(row)-1:
            pdf.ln()
        else:
            pdf.cell(20, 10, txt=str(col).encode().decode('latin-1', 'strict'), ln=False)
            

pdf.output('ouput.pdf', 'F')
