import random
import datetime
import json

import azure.functions as func

from senzor.model import radiationData
from senzor.view import formatRadiationData
from senzor.database import insertData

def main(req: func.HttpRequest) -> func.HttpResponse:
    #Simuleaza date
    radiationLevel = random.uniform(0.1, 5.0)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    #Creeaza obiect de date
    data = radiationData(level=radiationLevel, timestamp=timestamp)
    
    #Formateaza
    formattedData = formatRadiationData(data)

    #Scrie in baza de date
    insertData(timestamp, radiationLevel)

    #Returneaza
    return func.HttpResponse(
        body=json.dumps(formattedData),
        status_code=200,
        mimetype="application/json"
    )