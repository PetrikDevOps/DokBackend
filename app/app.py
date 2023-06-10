## Imports
from flask import Flask, redirect, request, session, url_for, jsonify, render_template
from dotenv import load_dotenv
from flask_session import Session
import identity.web
import logging as l
import os

## Load config
load_dotenv()


## Basic configuration
l.basicConfig(level=l.INFO)

app_config = {
    "CLIENT_ID": os.getenv("MS_CLIENT_ID"),
    "CLIENT_SECRET": os.getenv("MS_CLIENT_SECRET"),
    "AUTHORITY": os.getenv("MS_AUTHORITY", "https://login.microsoftonline.com/common"),
    "REDIRECT_PATH": os.getenv("MS_REDIRECT_PATH"),
    "ENDPOINT": os.getenv("MS_ENDPOINT"),
    "SCOPE": os.getenv("MS_SCOPE"),
    "SESSION_TYPE": os.getenv("MS_SESSION_TYPE")
}

## Check config validity
required_env_vars = app_config.keys()
missing_vars = [var for var in required_env_vars if app_config[var] is None]
if missing_vars:
    l.error(f"Missing required environment variables: {', '.join(missing_vars)}")
    exit()
else:
    l.info(f"Env vars are valid!")

## Do fucky with the app
app = Flask(__name__)
app.config.from_mapping(app_config)
Session(app)
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

## Auth config
auth = identity.web.Auth(
    session=session,
    authority=app.config["AUTHORITY"],
    client_id=app.config["CLIENT_ID"],
    client_credential=app.config["CLIENT_SECRET"],
)

## Microsoft auth routes
@app.route("/mslogin")
def mslogin():
    l.info(app_config['REDIRECT_PATH'])
    scopes = app.config["SCOPE"]
    if not isinstance(scopes, (list, tuple, set)):
        scopes = [scopes]
    return redirect(auth.log_in(scopes=scopes, redirect_uri="http://localhost:5000/msauth_response")["auth_uri"])
    #return jsonify(auth.log_in(scopes=scopes, redirect_uri=url_for("msauth_response", _external=True)))

@app.route("/msauth_response")
def msauth_response():
    result = auth.complete_log_in(request.args)
    if "error" in result:
        return jsonify({"result": result})
    return redirect(url_for("msindex"))

@app.route("/mslogout")
def mslogout():
    return redirect(auth.log_out(url_for("msindex", _external=True)))

@app.route("/msindex")
def msindex():
    if not auth.get_user():
        return redirect(url_for("mslogin"))
    return jsonify({"user": auth.get_user()})

# - innentol szar a kod mert presiler irta - #

# Login (POST)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    name = data['name']
    pw = data['pw']

    # Ellenőrizd a felhasználónevet és jelszót
    # ...

    # Válasz küldése
    response = {
        'status': True,
        'user_id': 123,
        'errormsg': '',
        'key': 'secret_key'
    }
    return jsonify(response)

# Reg (POST)
@app.route('/reg', methods=['POST'])
def register():
    data = request.get_json()
    name = data['name']
    pw = data['pw']
    email = data['email']

    # Felhasználó regisztrálása
    # ...

    # Válasz küldése
    response = {
        'status': True,
        'user_id': 456,
        'errormsg': '',
        'key': 'secret_key'
    }
    return jsonify(response)

# Hírek (GET)
@app.route('/news', methods=['GET'])
def get_news():
    # Hírek lekérdezése
    # ...

    # Válasz küldése
    response = {
        'post': [
            {'title': 'name', 'disc': 'lldalsdlasdas da s das d asdasdasd asdas dasd asdas'},
            {'title': 'name', 'disc': 'dsa dsa das d as das das das as da'}
        ]
    }
    return jsonify(response)

# Chat (GET)
@app.route('/chat', methods=['GET'])
def get_chat():
    # Chat üzenetek lekérdezése
    # ...

    # Válasz küldése
    response = {
        'comment': [
            {'name': 'name', 'msg': 'dasda'},
            {'name': 'name', 'msg': 'dads ddas'}
        ]
    }
    return jsonify(response)

# Chat (POST)
@app.route('/newmsg', methods=['POST'])
def post_message():
    data = request.get_json()
    user_id = data['user_id']
    msg = data['msg']

    # Új üzenet hozzáadása a chathez
    # ...

    # Válasz küldése
    response = {
        'status': True,
        'errormsg': ''
    }
    return jsonify(response)

# Live Chat
# Implementáció: Live Socket IO server (PORT 2506)

# Tipp (POST)
@app.route('/sendtipp', methods=['POST'])
def send_tipp():
    data = request.get_json()
    user_id = data['user_id']
    tipp = data['tipp']

    # Tipp küldése feldolgozásra
    # ...

    # Válasz küldése
    response = {
        'status': True,
        'errormsg': ''
    }
    return jsonify(response)

# Feladat (GET)
@app.route('/job', methods=['GET'])
def get_jobs():
    # Feladatok lekérdezése
    # ...

    # Válasz küldése
    response = {
        'jobs': [
            {'id': 1, 'job': 'name of job', 'desc': 'dsaddsa'},
            {'id': 2, 'job': 'sec job', 'desc': 'dsany'}
        ]
    }
    return jsonify(response)

# FeladatHelp (POST)
@app.route('/jobHelp', methods=['POST'])
def job_help():
    data = request.get_json()
    user_id = data['user_id']
    job_id = data['job_id']
    msg = data['msg']

    # Segítségkérés küldése a feladathoz
    # ...

    # Válasz küldése
    response = {
        'status': True,
        'errormsg': ''
    }
    return jsonify(response)

# SzavazásLekérés(GET)
@app.route('/vote', methods=['GET'])
def get_votes():
    # Szavazások lekérdezése
    # ...

    # Válasz küldése
    response = {
        'votes': [
            {
                'vote_name': 'Vote name',
                'vote_id': 1,
                'list_of_ch': [
                    {'op_name': 'string', 'op_id': 1},
                    {'op_name': 'string', 'op_id': 2},
                    {'op_name': 'string', 'op_id': 3}
                ]
            }
        ]
    }
    return jsonify(response)

# SzavazásLeadás(POST)
@app.route('/voteTo', methods=['POST'])
def vote_to():
    data = request.get_json()
    user_id = data['user_id']
    vote_id = data['vote_id']
    op_id = data['op_id']

    # Szavazat leadása
    # ...

    # Válasz küldése
    response = {
        'status': True,
        'errormsg': ''
    }
    return jsonify(response)

# GenVote (Post)
@app.route('/genVote', methods=['POST'])
def generate_vote():
    data = request.get_json()
    user_id = data['user_id']
    key = data['key']
    vote_name = data['vote_name']
    list_of_ch = data['list_of_ch']

    # Szavazás generálása
    # ...

    # Válasz küldése
    response = {
        'status': True,
        'errormsg': None
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)