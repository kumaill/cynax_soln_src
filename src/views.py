import json
from flask import request, jsonify
from connection import Stationery, Session
from utils import json_response_with_err_obj

def get_products_by_name():
    try:
        results ={}
        req_name = request.args.get('name', default = "null", type = str)
        sess = Session()
        db_query = sess.query(Stationery.id, Stationery.name, Stationery.price, Stationery.currency).filter(
                            Stationery.name == req_name).all()
        if req_name == "null":
            return json_response_with_err_obj(400, "No name found kindly use a correct name" .format(req_name))
        elif len(db_query) == 0:
            return json_response_with_err_obj(204, "No content found kindly use a correct name" .format(req_name))
        else:
            for n,ech_db_query in enumerate(db_query):
                results["Result-" + str(n+1)] = {"ID":ech_db_query[0], "Name": ech_db_query[1],\
                        "PRICE": ech_db_query[2], "CURRENCY" : ech_db_query[3]}
            response = {"meta": {"code": 200}, "data": results}
            return jsonify(response)
    except Exception as e:
        print("Error is: ", str(e))
        return jsonify({})

def get_all_products():
    try:
        results ={}
        sess = Session()
        db_query = sess.query(Stationery.id, Stationery.name, Stationery.price, Stationery.currency).all()
        if len(db_query) == 0:
            return json_response_with_err_obj(200, "No content found")
        else:
            for n,ech_db_query in enumerate(db_query):
                results["Result-" + str(n+1)] = {"ID":ech_db_query[0], "Name": ech_db_query[1],\
                        "PRICE": ech_db_query[2], "CURRENCY" : ech_db_query[3]}
            response = {"meta": {"code": 200}, "data": results}
            return jsonify(response)
    except Exception as e:
        print("Error is: ", str(e))
        return jsonify({})

def create_products():
    try:
        content = json.loads(request.data.decode('utf-8'))
        if "currency" in content.keys():
            sestn = Session()
            sestn.add(Stationery(**content))
            sestn.commit()
            sestn.close()
            return "Stationery Entry Made in DB"
        else:
            return json_response_with_err_obj(206, "Data for Currency is not available in Body. Kindly provide data updated format using the following example:   {'name': 'xyz', 'price': 345, 'currrency':'euro'}")
    except Exception as e:
        print("Error is: ", str(e))
        return jsonify({})

def delete_products(ID):
    try:
        sesn= Session()
        if sesn.query(Stationery.id).filter(Stationery.id == ID).first():
            sesn.query(Stationery).filter_by(id=ID).delete()
            sesn.commit()
            sesn.close()
            return "Entry for ID: {} is deleted" .format(ID)
        else:
            return json_response_with_err_obj(200, "Provided ID: {} not found in DB kindly use a correct ID" .format(ID))
    except Exception as e:
        print("Error is: ", str(e))
        return jsonify({})

def update_products():
    try:
        req_id = request.args.get('id', default = None, type = int)
        if req_id == None:
            return json_response_with_err_obj(200, "Stationery ID is not provided. Kindly provide Stationery ID in URL as follows, example URL: http://127.0.0.1:5000/v1/updateProductById?id=233 ")
        else: 
            sestn= Session()
            if sestn.query(Stationery.id).filter(Stationery.id == req_id).first():
                content = json.loads(request.data.decode('utf-8'))
                sestn.query(Stationery).filter_by(id = req_id).update({"name" : content["name"] ,"price" : content["price"] ,"currency" : content["currency"]})
                sestn.commit()
                sestn.close()
                return "Entry for ID: {} is updated" .format(req_id)
            else:
                return json_response_with_err_obj(200, "Provided ID: {} not found in DB kindly use a correct Stationery ID" .format(req_id))
    except Exception as e:
        print("Error is: ", str(e))
        return jsonify({})