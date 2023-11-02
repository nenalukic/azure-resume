import logging

import azure.functions as func

from azure.cosmos import exceptions, CosmosClient, PartitionKey


def main(req: func.HttpRequest, inputDocument: func.DocumentList,
         outputDocument: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    counter = getNewCounterValue(inputDocument[0]['count'])
    inputDocument[0]['count'] = counter
    outputDocument.set(func.Document.from_json(inputDocument[0].to_json()))
    if counter:
        return func.HttpResponse(f"{counter}", status_code=200)
    else:
        return func.HttpResponse(
            "Error",
            status_code=500)


def getNewCounterValue(value: int):
    return value + 1


# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )
