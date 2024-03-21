from flask import Blueprint, render_template, request, send_file, redirect, url_for
import subprocess

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template('index.html')

@views.route('/ats')
def ats():
	return render_template('ats.html')
