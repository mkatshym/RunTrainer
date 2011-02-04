'''
Created on Jan 30, 2011

@author: mike
'''

from google.appengine.ext import db

class RTUser(db.Model):
    RT_user_id = db.StringProperty()
    RT_role = db.StringProperty()
    RT_first_name = db.StringProperty()
    RT_last_name = db.StringProperty()
    RT_email = db.EmailProperty()
    RT_postal_address = db.PostalAddressProperty()
    RT_phonenumber = db.PhoneNumberProperty()
    RT_birthdate = db.DateProperty()
    RT_shirt_size = db.StringProperty()

    def to_dict(self):
        return dict([(p, unicode(getattr(self, p))) for p in self.properties()])
        
   
   