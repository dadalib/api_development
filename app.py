from flask import Flask,Request, request

# Create a webservice using FLask
app = Flask(__name__)

# Implement a RESTful endpoint for a Get request
@app.route('/',methods=['GET'])
def index():
    name = request.args.get('name',type =str)
    last_name = request.args.get('last_name',type =str)

    if name is None and last_name is None:
        name = 'World'
        last_name = 'Babe'

    return 'Hello , %s %s'%(name,last_name) 