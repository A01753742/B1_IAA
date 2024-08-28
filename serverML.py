#Pyhton Libraries
from flask import Flask, request, jsonify, render_template
import numpy as np
from load import joblib
#Files Managment
import os
from werkzeug.utils import secure_filename

#Load model
dt=joblib.load('dt1_ml.joblib')
#creat Flask app
server = Flask(__name__)

#Define a route to send JSON data 
@server.route('/predictjson', methods = ['POST'])