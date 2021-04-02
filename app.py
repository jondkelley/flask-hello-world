from flask import Flask
import logging
app = Flask(__name__)

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

log.debug('Startup Info message')
log.info('Startup Info message')
log.warning('Startup Warning message')
log.error('Startup Error message')
@app.route('/')
def hello_world():
    log.info('Info message')
    log.warning('Warning message')
    log.error('Error message')
    return 'Hello, World!'
