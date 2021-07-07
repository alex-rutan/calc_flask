from flask import Flask, request
import operations

app = Flask(__name__)

ops = {
        "add": operations.add,
        "sub": operations.sub,
        "mult": operations.mult,
        "div": operations.div,
    }


@app.route('/add')
def return_sum():
    """Takes a, b from request.args, returns sum of a, b"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(operations.add(a, b))


@app.route('/sub')
def return_difference():
    """Takes a, b from request.args, returns difference of a, b"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(operations.sub(a, b))


@app.route('/mult')
def return_product():
    """Takes a, b from request.args, returns product of a, b"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(operations.mult(a, b))


@app.route('/div')
def return_quotient():
    """Takes a, b from request.args, returns quotient of a, b"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(operations.div(a, b))


@app.route('/math/<operation>')
def return_operation_answer(operation):
    """takes in one of four different operations as a route parameter,
    returns the answer of the operation with parameters a, b"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(ops[operation](a, b))
