from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)

languages = [{'id' : 'python','name' : 'python lang'}, {'id' : 'java','name' : 'java lang'}, {'id' : 'C', 'name' : 'C lang'}]

#API Basic Authorisation - Users
users = {
            "admin": generate_password_hash("admin"),
            "user": generate_password_hash("user")
        }

auth = HTTPBasicAuth()

#API Basic Authorisation - Password Verification
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
    


@app.route('/myapi',methods=['GET','POST'])
@auth.login_required    #API Basic Authorisation - Add authorisation
def myapigp():
    #print(request.authorization.username)
    #print(request.authorization.password)
    if request.method == 'GET':
        return jsonify(languages)

    if request.method == 'POST':
        newlang = request.json
        languages.append(newlang)
        print(languages)
        return jsonify(languages)

@app.route('/myapi/<string:lid>',methods=['PUT'])
@auth.login_required 
def myapi(lid):
    newlang = []
    for lang in languages:
        if lang['id'] == lid:
           lang['name'] = request.json['name']
        newlang.append(lang)
    return jsonify(newlang)


if __name__ == '__main__':
    app.run(debug=True,port=8081)
    


