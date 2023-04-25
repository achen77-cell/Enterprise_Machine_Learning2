#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:14:31 2023

@author: alicia
"""
import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port) #define 0.0.0.0 for Docker
    

#Fast API
#from typing import Union

#from fastapi import FastAPI

#app = FastAPI()
#@app.get("/")
#def hello():
#    return "Hello World!"

#if __name__ == "__main__":
#    port = int(os.environ.get('PORT', 8000))
#    app.run(host='0.0.0.0', port=port) #define 0.0.0.0 for Docker