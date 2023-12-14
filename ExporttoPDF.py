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
pivot_df['total'] = pivot_df.sum(axis=1).round(2)

cahflowdict_strkeys = {str(key): value for key, value in cash_flow.cashflowdict.items()}
custom_cashflow_order = ['rental income', 'subsidized rental income', 'other op income', 'payroll', 'utilities', 
                         'turnover costs', 'maintenance expense', 'advertising', 'other expenditures', 'taxes and licenses', 'other op expense', 
                         'other income', 'capital expenditure', 'other expense', 'other item']

pivot_df['cash_flow_cat'] = pivot_df.index.map(cahflowdict_strkeys)
pivot_df['cash_flow_cat'] = pd.Categorical(pivot_df['cash_flow_cat'], categories=custom_cashflow_order, ordered=True)
pivot_df = pivot_df.sort_values(by='cash_flow_cat')

df_agg = pivot_df.groupby(by=['cash_flow_cat'], observed=True).sum().round(2).reset_index()
df_agg.set_index('cash_flow_cat', inplace=True)


pdf = FPDF('L')

pdf.add_page()

pdf.set_font('Times', '', 10)

previous_cat = ''

for index, row in pivot_df.iterrows():
    current_cat = row.iloc[-1]
    if previous_cat != current_cat and previous_cat != '' and pd.notnull(previous_cat):
        pdf.cell(20, 10, txt=str('Total '+previous_cat).encode().decode('latin-1', 'strict'), ln=False)
        for i, col in enumerate(df_agg.loc[previous_cat]):
            pdf.cell(20, 10, txt=str(col).encode().decode('latin-1', 'strict'), ln=False)
        pdf.ln()
        pdf.cell(20, 10, txt=str(current_cat).encode().decode('latin-1', 'strict'), ln=True)
    
    #Add all the extra Lines here - lines that are not a subtotal, but a total of two other subtotals


    pdf.cell(20, 10, txt=str(index).encode().decode('latin-1', 'strict'), ln=False)
    for i, col in enumerate(row):
        
        if i == len(row)-1:
            previous_cat = col
            pdf.ln()
        else:
            pdf.cell(20, 10, txt=str(col).encode().decode('latin-1', 'strict'), ln=False)

        #Need to add the line total
        #need to ignore lines that have a zero total
        
            

pdf.output('ouput.pdf', 'F')
