from flask import Flask
from app.routes import bp
from app.utils import hash_index  
from dotenv import load_dotenv
import os

load_dotenv()
gcs_credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")


app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
