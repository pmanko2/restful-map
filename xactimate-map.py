from flask import Flask
from flask_restful import Resource
import flask_restful as restful
import argparse
import logging
import pkg_resources

app = Flask(__name__)

# app config
SECRET_KEY = '03f8c292-6388-4cab-ab3c-91621cee3fda'
VERSION = '0.2.0'
SERVICE_URL = '/xactimate-map/'

logger = logging.getLogger("pirweb")

@app.route('/')
def hello_world():
    return 'Hello World!'


def create_app():
    web_app = Flask(__name__)
    web_app.config.from_object(__name__)
    api = restful.Api(web_app)
    api.add_resource(hello_world)

    return web_app

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default=24602, dest='port',
                        type=int, help='Port on which to run.')
    parser.add_argument('-l', '--logconfig', default='logging.cfg', dest='log_config',
                        help='Logging configuration file.')
    parser.add_argument('--hostconfig', default='dev', dest='hostconfig',
                        help='flag for external visibility of the standalone web service (dev|toExternal)')
    args = parser.parse_args()
    #
    # cfg_stream = pkg_resources.resource_stream('web', args.log_config)
    # logging.config.fileConfig(cfg_stream, disable_existing_loggers=False)

    hostcfg = '127.0.0.1'
    if args.hostconfig == 'toExternal':
        hostcfg = '0.0.0.0'

    app = create_app()
    logger.debug('Running app with {0}'.format(args.log_config))
    app.run(host=hostcfg, port=args.port)
