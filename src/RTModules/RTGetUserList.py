'''
Created on Jan 31, 2011

@author: mike
'''

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db

from RTUtilities.RTUtilities import *

from RTModules.RTUser import RTUser

from django.utils import simplejson

class RTGetUserList(webapp.RequestHandler):
    '''
    classdocs
    '''
    def get(self):
        
        if not isuser():
            self.redirect('/')
            
        if not istrainer():
            self.redirect('/dashboard')
            
        
        if (self.request.get('_search') == "false"):    
            users_list_query = db.GqlQuery("SELECT * FROM RTUser ORDER BY " + self.request.get('sidx') + " " + self.request.get('sord'))
            users_list = users_list_query.fetch(int(self.request.get('rows')))
            rows = [u.to_dict() for u in users_list]
            user_dict = {'total':1,'page':1,'records': len(rows), 'rows':rows}
            self.response.out.write(simplejson.dumps(user_dict))
        else:
            oper = {'eq':'=',
                    'ne':'!=',
                    'lt':'<',
                    'le':'<=',
                    'gt':'>',
                    'ge':'>='}
            qu = "SELECT * FROM RTUser WHERE " + self.request.get('searchField') + " " + oper[self.request.get('searchOper')] + " \'" + self.request.get('searchString')  + "\' ORDER BY " + self.request.get('sidx') + " " + self.request.get('sord')
            users_list_query = db.GqlQuery(qu)
            users_list = users_list_query.fetch(int(self.request.get('rows')))
            rows = [u.to_dict() for u in users_list]
            user_dict = {'total':1,'page':1,'records': len(rows), 'rows':rows}
            self.response.out.write(simplejson.dumps(user_dict))
