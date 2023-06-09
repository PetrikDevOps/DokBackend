import identity.web
from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session
import os

app_config = {
    "CLIENT_ID": os.getenv("MS_CLIENT_ID"),
    "CLIENT_SECRET": os.getenv("MS_CLIENT_SECRET"),
    "AUTHORITY": os.getenv("MS_AUTHORITY", "https://login.microsoftonline.com/common"),
    "REDIRECT_PATH": os.getenv("MS_REDIRECT_PATH"),
    "ENDPOINT": os.getenv("MS_ENDPOINT"),
    "SCOPE": os.getenv("MS_SCOPE"),
    "SESSION_TYPE": os.getenv("MS_SESSION_TYPE")
}

required_env_vars = ["CLIENT_ID", "CLIENT_SECRET", "REDIRECT_PATH", "SCOPE"]
missing_vars = [var for var in required_env_vars if app_config[var] is None]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

app = Flask(__name__)
app.config.from_mapping(app_config)
Session(app)
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

auth = identity.web.Auth(
    session=session,
    authority=app.config["AUTHORITY"],
    client_id=app.config["CLIENT_ID"],
    client_credential=app.config["CLIENT_SECRET"],
)

@app.route("/mslogin")
def login():
    return render_template("login.html", **auth.log_in(
        scopes=app.config["SCOPE"],
        redirect_uri=url_for("auth_response", _external=True),
        ))

@app.route(app_config["REDIRECT_PATH"])
def auth_response():
    result = auth.complete_log_in(request.args)
    if "error" in result:
        return render_template("auth_error.html", result=result)
    return redirect(url_for("index"))

@app.route("/mslogout")
def logout():
    return redirect(auth.log_out(url_for("index", _external=True)))

@app.route("/msindex")
def msindex():
    if not auth.get_user():
        return redirect(url_for("login"))
    return render_template('index.html', user=auth.get_user())
