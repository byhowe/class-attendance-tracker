import networking

import data

address = (data.config['server']['host'], data.config['server']['port'],
           data.config['server']['username'], data.config['server']['password'])

is_connected_server = False

client: networking.client.Client


def connect_to_server():
    global is_connected_server
    global client
    print("[Client] Attempting to connect to the server.")
    client = networking.client.Client(networking.create_tcp_socket())
    status = client.connect(address[0], address[1])
    if status == networking.client.ConnectionStatus.CONNECTION_FAILED:
        is_connected_server = False
        print("[Client] Server connection is failed. Connection failure.")
        return
    client.send(address[2])
    client.send(address[3])
    res = client.recv()
    if res != "OK":
        is_connected_server = False
        print("[Client] Server connection is failed. Unmet credentials.")
        return
    client.send("CLIENT")
    is_connected_server = True
    print("[Client] Server connection is successful.")


connect_to_server()
