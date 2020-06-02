from flask import (Flask, render_template, url_for, flash, redirect, request, Blueprint, abort)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title="Ads For BLM")
