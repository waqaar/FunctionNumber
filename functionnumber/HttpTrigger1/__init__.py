import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    FuncNumber = req.params.get('FuncNumber')
    if not FuncNumber:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            FuncNumber = req_body.get('FuncNumber')

    if FuncNumber:
        return func.HttpResponse(f"Hello, {FuncNumber}.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a FuncNumber in the query string or in the request body for a personalized response.",
             status_code=200
        )
