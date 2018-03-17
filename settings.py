import os

SECRET_KEY = 'UPDATE_UPDATE_EXCLUSIVE_UPDATE'
DEBUG = True

DB_USERNAME = 'root'  # or 'ec2-user'
DB_PASSWORD = 'flask-SQL'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = os.getenv('IP', '0.0.0.0')
DB_URI = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

print('SQL Server running on:', DB_HOST)