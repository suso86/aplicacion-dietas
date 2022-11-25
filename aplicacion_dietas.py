from flask import Flask, render_template, request, redirect, url_for, make_response,jsonify
from werkzeug.utils import secure_filename
from os import remove

from datetime import timedelta

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

if __name__ == '__main__':
    app.run(debug=True)