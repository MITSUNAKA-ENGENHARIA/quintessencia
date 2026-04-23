import pandas as pd
from dotenv import load_dotenv
import os

def get_sheets_data() -> str:
     load_dotenv()
     sheet_id = os.getenv("SHEET_ID")
     sheet_name = "data"
     url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

     df = pd.read_csv(url)
     return df.to_csv(index=False)