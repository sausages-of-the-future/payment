from flask import Flask, request, redirect, render_template, url_for, session, flash, abort, current_app
from payment import app, forms

#views
@app.route("/")
def index():
    return render_template('index.html')

