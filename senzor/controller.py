import random
import datetime
import json

import azure.functions as func

from senzor.model import RadiationData
from senzor.view import format_radiation_data

def main(req: func.HttpRequest) -> func.HttpResponse:
    #Simuleaza date
    radiation_level = random.uniform(0.1, 5.0)
    timestamp = datetime.datetime.now().isoformat()
    #Creeaza obiect de date
    data = RadiationData(level=radiation_level, timestamp=timestamp)
    #Formateaza
    formatted_data = format_radiation_data(data)
    #Returneaza
    return func.HttpResponse(
        body=json.dumps(formatted_data),
        status_code=200,
        mimetype="application/json"
    )