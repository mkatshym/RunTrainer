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

class RTMainPage(webapp.RequestHandler):
   def get(self):
       
       current_user = users.get_current_user()
       
       if current_user:

           student_query = db.GqlQuery("SELECT * FROM RTUser WHERE RT_user_id=:1",current_user.user_id())
           
           current_student = student_query.get()
           
           if current_student:
               
               self.redirect('/dashboard')
           
           else:
               
               self.redirect('/newuser')
           
       else:
           
           url = users.create_login_url(self.request.uri)
           url_linktext = 'Login'
           
           template_values = {
                          'url' : url,
                          'url_linktext': url_linktext
                          }
           path = os.path.join(os.path.dirname(__file__), '../html_templates/RTMainPage.html')
           self.response.out.write(template.render(path,template_values))
