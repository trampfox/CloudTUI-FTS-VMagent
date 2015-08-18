__author__ = 'trampfox'

from flask import Flask
from flask_restful import Resource, Api

import psutil

app = Flask(__name__)
api = Api(app)

class Cpu(Resource):

  def get(self):
    cpu_usage = psutil.cpu_percent(interval=1)
    return {'cpu_usage': cpu_usage}


class Memory(Resource):

  def get(self):
    memory_usage = psutil.virtual_memory()
    return {'memory_usage': memory_usage.percent}

api.add_resource(Cpu, '/cpu')
api.add_resource(Memory, '/memory')


if __name__ == '__main__':
  app.run(debug=True)
