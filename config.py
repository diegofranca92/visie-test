import databases
import sqlalchemy
import os


# from sqlalchemy import create_engine, MetaData
# engine = create_engine('mysql+pymysql://root@localhost:3306/py_crud')
# meta = MetaData()
# con = engine.connect()

# DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
DATABASE_URL = os.getenv('DATABASE_URL', 'mysql+pymysql://diegofranca:ZGllZ29mcmFu@jobs.visie.com.br:3306/diegofranca')
TEST_DATABASE = os.getenv('TEST_DATABASE', 'false') in ('true', 'yes')
database = databases.Database(DATABASE_URL, force_rollback=TEST_DATABASE)
metadata = sqlalchemy.MetaData()