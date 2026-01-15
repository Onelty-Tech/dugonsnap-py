import runtime
import asyncio



myRuntime = runtime.Runtime("localhost",8092)

print("estableciendo conexion.")
asyncio.run(myRuntime.Establish())


print("enviando datos.")

