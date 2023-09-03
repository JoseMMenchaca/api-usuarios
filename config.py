import os
from dotenv import load_dotenv

path=os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(path)

FLASK_DEBUG=os.environ.get("FLASK_DEBUG", False)
TESTING=os.environ.get("TESTING", False)
SECRET_KEY=os.environ.get("SECRET_KEY", "")

SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO", False)
SQLALCHEMY_TRACK_MODIFICATION = os.environ.get("SQLALCHEMY_TRACK_MODIFICATION", False)
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "")


