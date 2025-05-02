import os
import pyodbc, struct
from azure.identity import DefaultAzureCredential

#connection string

connection_string = os.environ["AZURE_SQL_CONNECTIONSTRING"]

#conectare bd
credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
token_bytes = credential.get_token("https://database.windows.net/.default").token.encode("UTF-16-LE")
token_struct = struct.pack(f'<I{len(token_bytes)}s', len(token_bytes), token_bytes)
SQL_COPT_SS_ACCESS_TOKEN = 1256  # This connection option is defined by microsoft in msodbcsql.h
conn = pyodbc.connect(connection_string, attrs_before={SQL_COPT_SS_ACCESS_TOKEN: token_struct})
    

#functie inserare date
def insertData(timestamp, level):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO RadiationData (Timestamp, RadiationLevel) VALUES (?, ?)", (timestamp, level))
    conn.commit()
    cursor.close()