import os
import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db


from RTModules.RTCreateUser import RTCreateUser

from RTPages.RTMainPage import RTMainPage
from RTPages.RTDashBoard import RTDashBoard
from RTPages.RTNewUser import RTNewUser


application = webapp.WSGIApplication([('/',RTMainPage),
                                      ('/newuser',RTNewUser),
                                      ('/dashboard',RTDashBoard),
                                      ('/createuser',RTCreateUser)],
                                      debug=True)

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()
    


