from dotenv import load_dotenv
import os


load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')

basedir = os.path.abspath(os.path.dirname(__file__))
BASEDIR_DB = os.path.join(basedir, 'db.sqlite3')