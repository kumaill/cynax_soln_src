from flask import Flask
from views import get_products_by_name, get_all_products, create_products, delete_products, update_products

app = Flask(__name__)

@app.route("/v1/getProductsByName", methods=['GET'])
def getProductsByName():
    return get_products_by_name()

@app.route("/v1/getAllProducts", methods=['GET'])
def getAllProducts():
    return get_all_products()

@app.route("/v1/createProduct", methods=['POST'])
def createProducts():
    return create_products()


@app.route("/v1/deleteProductById/<ID>", methods=["DELETE"])
def deleteProducts(ID):
    return delete_products(ID)

@app.route("/v1/updateProductById", methods=["PUT"])
def updateProducts():
    return update_products()

if __name__ == '__main__':
    app.run(debug=True)