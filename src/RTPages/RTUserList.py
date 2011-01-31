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
from RTUtilities.RTUtilities import *

class RTUserList(webapp.RequestHandler):
    '''
    classdocs
    '''
    def get(self):
        
        current_user = checkuser()
        
        if not current_user:
            self.redirect('/')
            
        if current_user.RT_role == "student":
            self.redirect('/dashbaord')
        
        url = users.create_logout_url('/')
        url_linktext = 'Logout'
        template_values = {
                           'current_user': current_user,
                           'url': url,
                           'url_linktext': url_linktext
                           }
                
        path = os.path.join(os.path.dirname(__file__),'../html_templates/RTUserList.html')
        self.response.out.write(template.render(path, template_values))
            