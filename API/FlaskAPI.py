from flask import Flask
from flask import request
import logging
from logging.handlers import RotatingFileHandler
import datetime as s
from flask import Response

app = Flask(__name__)

@app.route('/report/<user>')
def emailReporting(user):
    subject = request.args['subject']
    app.logger.error(s.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+', user: '+user+' ,Subject : '+subject)
    print user, subject
    return Response(status=200)
    
    
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
    
if __name__ == '__main__':
    handler = RotatingFileHandler('/home/ubuntu/FlaskAPI/email.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    app.run()
