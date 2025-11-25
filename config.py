import os
from dotenv import load_dotenv

<<<<<<< HEAD
load_dotenv()  # Load environment variables from .env

# Create a database configuration dictionary
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}
=======
# Load environment variables from .env file
load_dotenv()

# MySQL config dictionary
db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DB')
}
>>>>>>> 495517cf559e9b09aa85fc886919262642289d69
