from mongoengine import Document, StringField
class User(Document):
    user_name = StringField()
    email = StringField()
    
