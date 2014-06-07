
# system imports
import json, os

# flask imports
from flask import Flask, redirect, url_for, session, render_template, g, request, flash, jsonify


# setup flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def main():

    app.debug = True
    app.run()

if __name__ == '__main__':
    main()
