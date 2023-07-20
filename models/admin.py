from mongoengine import Document, StringField
class Admin(Document):
    meta = {'db_alias': 'main'}
    user_name = StringField()
    email = StringField()
    organization = StringField()
