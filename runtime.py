import websockets
import errno
from collections import deque


class Runtime:
    def __init__(self,address,port):
        self.address = address
        self.port = port
        # solo puede haber uno escuchando el puerto del websockets que ese es el runtime, ya vere si se necesita mas conexiones.
        self.clients = set()
    async def Establish(self):
        # iniciamos el servidor websockets
        try:
            server = await websockets.serve(
                self.handlingRuntime,
                self.address,
                self.port,
                ping_interval=20,
                ping_timeout=20
            )
            # manejamos los respectivos errores.
        except OSError as e:
            if e.errno == errno.EADDRINUSE:
                pass
            elif e.errno == errno.EADDRNOTAVAIL:
                pass
            elif e.errno == errno.EACCES:
                pass
            elif e.errno == errno.EAFNOSUPPORT:
                pass
        # indicamos que esta funcionando
        print(f"Servidor WebSocket establecido en ws://{self.ip}:{self.port}")
        print("Esperando conexiones...")
        # mantenemos el servidor corriendo con await
        await server.wait_closed()
    async def handlingRuntime(self,ws):
        self.clients.add(ws)
        clientId = id(ws)
        try:
            print(f"Client {clientId}correctly connected.")
        except websockets.exceptions.ConnectionClosed:
            print(f"Customer {clientId} disconnected")
        finally:
            # removemos el cliente al final de la conexion por cualquier error imprevisto
            self.clients.remove(ws)
