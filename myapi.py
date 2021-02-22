from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)




languages = [{'id' : 'python','name' : 'python lang'}, {'id' : 'java','name' : 'java lang'}, {'id' : 'C', 'name' : 'C lang'}]




@app.route('/myapi',methods=['GET','POST'])
def myapigp():
    if request.method == 'GET':
        return jsonify(languages)


    if request.method == 'POST':
        languages.append(request.json)
        return jsonify(languages)







if __name__ == '__main__':
    app.run(debug=True,port=8081)
    


