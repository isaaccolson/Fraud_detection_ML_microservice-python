#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:44:56 2020

@author: isaaccolson
"""

#https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3

from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Multiply(Resource):
    def get(self, number):
         return jsonify(movieId=number,rating=(int(number) * 2))

     
api.add_resource(Multiply, "/multiply/<string:number>")

app.run(debug=True)
