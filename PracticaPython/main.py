from db import getDB, deleteDB, postDB_1, putDB, postDB_2
from flask import Flask, request
from flask_restful import Api, Resource
from time import sleep, time
import simple_websocket


app = Flask(__name__)
api = Api()

class Main(Resource):

    def get(self):
        return getDB()

    def post(self):
        return postDB_1()


class MainID(Resource):

    def put(self, id):
        return putDB(id)

    def delete(self, id):
        return deleteDB(id)


class MainIDSend(Resource):

    def post(self, id):
        return postDB_2(id)


api.add_resource(Main, "/api/notifications")

api.add_resource(MainID, "/api/notifications/<int:id>")


api.add_resource(MainIDSend, "/api/notifications/<int:id>/send")
api.init_app(app)


@app.route('/echo', websocket=True)
def echo():
    ws = simple_websocket.Server(request.environ, ping_interval=5)
    try:
        while True:
            start = time()
            data = ws.receive()
            ws.send( { 'id': '2', 'message': 'pong'})
            print(f'< {data}')
            sleep(2)
            a = time() - start
            print(a)
            if int(float(a)) > 5:
                ws.close(message="time out!")
    except simple_websocket.ConnectionClosed:
        pass
    return ''



if __name__ == "__main__":
    app.run(debug=True, port=3001)
