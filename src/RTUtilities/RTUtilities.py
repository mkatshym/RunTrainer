'''
Created on Jan 30, 2011

@author: mike
'''

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users

from google.appengine.ext import db

from RTModules.RTUser import RTUser

def checkuser():
    current_user = users.get_current_user()
    if current_user == None:
        return False
    else:
        q = RTUser.all()
        q.filter("RT_user_id =",current_user.user_id())
        current_user = q.get()
        if current_user == None:
            return False
        else:
            return current_user