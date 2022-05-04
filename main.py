
from flask import Flask
from configs.global_configs import *

app = Flask(__name__)
from routes.v1 import *

# main function
if __name__ == '__main__':
    app.run(host=host, port=port)
