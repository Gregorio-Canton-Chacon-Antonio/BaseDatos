import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database: 
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"=basededatoslaconexion),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )