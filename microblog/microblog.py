# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:00:10 2018

@author: Darragh
"""

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}