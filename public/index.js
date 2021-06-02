const sio=io();

sio.on('connect',()=>{
    alert('Connected')
    sio.emit('sum',{numbers:[1,2]})
})


sio.on('disconnect',()=>{
    alert('Disconnected')
})