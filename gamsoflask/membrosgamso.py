from dotenv import load_dotenv
from os import getenv
import pandas as pd

load_dotenv()
sheet_id = getenv('SHEET_ID')
sheet_name = getenv('SHEET_NAME')

url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

df = pd.read_csv(url)

#print(df.head(20))
#print(url)

#for index, row in df.iterrows():
#    print(row['Nome'], row['Ocupação'], row['Tag discord'])
#    print(str(row['Nome']).split())