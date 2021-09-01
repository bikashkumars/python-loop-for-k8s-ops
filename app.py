from flask import Flask
from threading import Thread
from datetime import datetime
import uuid
from time import time, sleep

app = Flask(__name__)

@app.route("/rest-app3")
def index():
    return "Hello index! - app3"
    
@app.route("/")
def billing():
    return "Hello default! - app3"

def printAdp():
    while (True):   
        logMessage = str(datetime.today()) + " " + "MEDIUM" + " " + str(uuid.uuid4()) + " " + "method called" + " " + " details of method called"
        print(logMessage)
        sleep(10)
        printAdp()
        
with app.app_context():
    thread1 = Thread(target = printAdp)
    thread1.start()
        
if __name__ == "__main__":
    #printNonAdp()
    app.run(host ='0.0.0.0', port = 5004, debug = True)
    #printAdp()
