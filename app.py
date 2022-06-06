from flask import Flask, make_response, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/<int:quan>/<int:start>/<int:end>', methods=['GET'])
def home(quan,start,end):  
  numList = []
  for i in range (quan):
    numList.append(random.randint(start,end))
  response = make_response({"answer":numList})
  # response.headers['Access-Control-Allow-Origin'] = '*'
  return response

if __name__ == '__main__':
  app.run(debug=True)