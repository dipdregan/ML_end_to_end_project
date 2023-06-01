from flask import Flask 
import sys
from housing.logger import logging
from housing.exception import HousingException as ex

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom Exception")
    except Exception as e:
        housing = ex(e,sys)
        logging.info(housing.error_message)
        logging.info('Here we are testing logging modules')
    return 'Ci-Cd pipeline has been established'

if __name__ =="__main__":
    app.run(debug=True)