import random
import datetime
import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Simulating sensor data.')

    #Simularea datelor de la senzor
    radiation_level = random.uniform(0.1, 5.0) 
    timestamp = datetime.datetime.now().isoformat()

    #Crearea raspunsului
    data = {
        "timestamp": timestamp,
        "radiation_level": radiation_level
    }

    logging.info(f'Sensor data: {data}')

    #Trimite rasp.
    return func.HttpResponse(
        body=str(data),
        status_code=200,
        mimetype="application/json"
    )