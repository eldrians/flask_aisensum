from dotenv import load_dotenv
import os

load_dotenv()

dbconfig = {
    "hostname": os.environ.get("DB_HOSTNAME"),
    "username":os.environ.get("DB_USERNAME"),
    "password":os.environ.get("DB_PASSWORD"),
    "database":os.environ.get("DB_DATABASE"),
    "port": os.environ.get("DB_PORT")
}