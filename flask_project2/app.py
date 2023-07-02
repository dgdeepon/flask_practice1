from flask import Flask,request, jsonify


app=Flask(__name__)

products=[
    {
        "id":1,
        "title":"T-shirts",
        "price":250
    },
    {
        "id":2,
        "title":"Jeans",
        "price":600
    },
    {
        "id":3,
        "title":"Shirts",
        "price":450
    }
]


class createProduct:
    def __init__(self,title,price):
        self.title=title
        self.price=price
        self.id=len(products)+1
        

@app.route('/', methods=['GET'])
def getNow():
    return jsonify(products),200

@app.route('/create',methods=["POST"])
def createNow():
    # product=createProduct(request.json["title"],request.json["price"])
    product={
        "title":request.json["title"],
        "price":request.json["price"],
        "id":len(products)+1
    }
    products.append(product)
    return jsonify({"message":"product is added"})


@app.route('/update/<int:id>',methods=['PUT'])
def updateNow(id):
    for product in products:
        if product["id"] == id:
            product["price"]=request.json.get("price",product["price"])
            return jsonify(product)
    return jsonify({"message":"product not found"}),404

@app.route('/delete/<int:id>',methods=["DELETE"])
def deleteNow(id):
    for product in products:
        if product["id"]==id:
            products.remove(product)
            return jsonify({"message":"successfully removed"}),200
    return jsonify({"message":"product not found"}),404


if __name__=="__main__":
    app.run()