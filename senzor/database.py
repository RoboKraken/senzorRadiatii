import pyodbc
from azure.identity import DefaultAzureCredential

#obtine token
credential = DefaultAzureCredential()
access_token = credential.get_token("https://databasedatabase.windows.net/").token

#conectare bd
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=datesenzori.database.windows.net;DATABASE=dateSenzori',
    attrs_before={
        "AccessToken": access_token
    }
)

#functie inserare date
def insertData(timestamp, level):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO RadiationData (Timestamp, RadiationLevel) VALUES (?, ?)", (timestamp, level))
    conn.commit()
    cursor.close()