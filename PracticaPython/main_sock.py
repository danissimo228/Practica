from time import sleep
import simple_websocket


def main():
    ws = simple_websocket.Client('ws://localhost:3001/echo', ping_interval=5)
    try:
        while True:
            data =  { 'id': '1', 'message': 'ping'}
            ws.send(data)
            data = ws.receive()
            print(f'< {data}')
            sleep(2)
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()

main()