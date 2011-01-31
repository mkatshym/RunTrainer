'''
Created on Jan 30, 2011

@author: mike
'''

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users

from RTModules.RTUser import RTUser

class RTNewUser(webapp.RequestHandler):
    '''
    classdocs
    '''
    def get(self):
        
        if users.get_current_user():
            
            url = users.create_logout_url('/')
            url_linktext = 'Cancel'
            
            template_values = {
                               'url': url,
                               'url_linktext': url_linktext
                               }
            
            path = os.path.join(os.path.dirname(__file__),'../html_templates/RTNewUser.html')
            self.response.out.write(template.render(path,template_values)) 
            
        else:
            
            self.redirect('/')