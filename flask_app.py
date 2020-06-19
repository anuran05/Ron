# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:44:24 2020

@author: Anuran Aich
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("anuran.html")

if __name__ == '__main__':
    app.run()