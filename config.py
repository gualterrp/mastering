class Config(object):
    pass

class ProdConfig(Config):
    pass


class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Hardcore_1964@localhost/mastering"
    SQLALCHEMY_TRACK_MODIFICATIONS = False