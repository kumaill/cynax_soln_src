from flask import Flask
from views import get_products_by_name, get_all_products, create_products, delete_products, update_products

app = Flask(__name__)

#List entries from the stationery using the name provided as a query parameter. e.g: http://127.0.0.1:5000/v1/getProductsByName?name=pen
@app.route("/v1/getProductsByName", methods=['GET'])
def getProductsByName():
    return get_products_by_name()

#Read all entries in stationery table
@app.route("/v1/getAllProducts", methods=['GET'])
def getAllProducts():
    return get_all_products()

# provide (name, price & currency) in body to make a new entry in the Stationery table inside products DB.
@app.route("/v1/createProduct", methods=['POST'])
def createProducts():
    return create_products()

#Delete entry in the stationery DB based on the ID recieved as argument. e.g: http://127.0.0.1:5000/v1/deleteProductById/5
@app.route("/v1/deleteProductById/<ID>", methods=["DELETE"])
def deleteProducts(ID):
    return delete_products(ID)

#Update the entry in the stationery DB based on the ID provided in the query param: e.g: http://127.0.0.1:5000/v1/updateProductById?id=5
@app.route("/v1/updateProductById", methods=["PUT"])
def updateProducts():
    return update_products()

if __name__ == '__main__':
    app.run(debug=True)