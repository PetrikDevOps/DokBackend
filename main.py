from flask import Flask, jsonify, request

app = Flask(__name__)

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
        'errormsg': ''
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=2506, debug=True)
