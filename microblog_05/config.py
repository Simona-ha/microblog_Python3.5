CSRF_ENABLED = True# CSRF_ENABLED 配置是为了激活 跨站点请求伪造 保护。在大多数情况下，你需要激活该配置使得你的应用程序更安全些。
SECRET_KEY = 'you-will-never-guess'#SECRET_KEY 配置仅仅当 CSRF 激活的时候才需要，它是用来建立一个加密的令牌，用于验证一个表单。当你编写自己的应用程序的时候，请务必设置很难被猜测到密钥。
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
import os
#针对我们小型的应用，我们将采用 sqlite 数据库。sqlite 数据库是小型应用的最方便的选择，
# 每一个数据库都是存储在单个文件里。
basedir=os.path.abspath(os.path.dirname(__file__))
#dirname Return the directory name of pathname path,返回文件路径所在文件夹的名字
#再返回绝对路径作为basedir
SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'app.db')#数据库文件的路径
SQLALCHEMY_MIGRATE_REPO=os.path.join(basedir,'db_repository')#SQLALCHEMY_MIGRATE_REPO 是文件夹
SQLALCHEMY_TRACK_MODIFICATIONS=True
#仓库也存储在basedir中
#  我们将会把 SQLAlchemy-migrate 数据文件存储在这里。
# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['you@example.com']
