import socketio

sio=socketio.Server()

app=socketio.WSGIApp(sio,static_files={
    '/':'./public/'
})


@sio.event
def connect(sid,environ):
    print(sid,"Connected")

@sio.event
def sum(sid,data):
    print(f"result: {data['numbers'][0]+data['numbers'][1]}")

@sio.event
def disconnect(sid):
    print(sid,"Disconnected")





