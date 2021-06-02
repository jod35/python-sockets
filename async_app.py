import socketio

sio=socketio.AsyncServer(async_mode='asgi')

app=socketio.ASGIApp(sio,static_files={
    '/':'./public/'
})


@sio.event
async def connect(sid,environ):
    print(sid,"Connected")



@sio.event
async def disconnect(sid):
    print(sid,"Disconnected")





