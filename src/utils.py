import json
from flask import Response

def json_response_with_err_obj(code, error_string):
    error_obj = {
        "meta": {
            "code": code,
            "errors": error_string
        },
        "body": {
            "status": None
        }
    }
    return Response(json.dumps(error_obj), code, mimetype='application/json')