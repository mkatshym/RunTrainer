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

class RTCreateUser(webapp.RequestHandler):
    '''
    classdocs
    '''
    def post(self):
        
        student = RTUser()
        
        student.RT_user_id = users.get_current_user().user_id()
        student.RT_first_name = self.request.get('first_name')
        
        if self.request.get('role') == 'trainer':
            
            student.RT_role = 'trainer'
        
        else:
        
            student.RT_role = 'student'
        
        student.put()
        self.redirect('/')
        