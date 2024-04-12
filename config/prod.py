import os
DEBUG=True

SECRET_KEY='Aashay%40123'
# SQLALCHEMY_DATABASE_URI='postgresql://postgres:Aashay%40123@localhost/New'
SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS=False
# 'postgresql://postgres:Aashay%40123@localhost/New'