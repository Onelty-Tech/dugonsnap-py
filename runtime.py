from websockets.legacy.server import WebSocketServerProtocol
import websockets


class Runtime:
    def __init__(self, address: str, port: int):
        self.address = address
        self.port = port
        self.client: WebSocketServerProtocol = None
    
    async def Establish(self) -> None:
        try:
            server = await websockets.serve(
                self.handler,
                self.address,
                self.port,
                ping_interval=20,
                ping_timeout=20
            )
            print(f"Servidor WebSocket establecido en ws://{self.address}:{self.port}")
            print("Esperando conexiones...")
            await server.wait_closed()
        except OSError as e:
            print(f"error Runtime.Establish: {e}")
    async def handler(self, ws: WebSocketServerProtocol) -> None:
        try:
            if self.client != None:
                self.client = ws
                print("Runtime orrectly connected.")
                return
            # Como ya tiene conectado al runtime entonces cierra la conexion.
            ws.close()
        except websockets.exceptions.ConnectionClosed:
            self.client = None
            print(f"Runtime disconnected")
    async def SendPacket(self,parameters: list[bytes],data: list[bytes]):
        #testing
        await self.client.send(f"{len(parameters)}\n{data}\n")
