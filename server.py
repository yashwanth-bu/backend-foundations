# server file

from fastapi import FastAPI

server = FastAPI(
    title="Backend-Server-Entry",
    version="0.1.0"
)

@server.get("/health")
def check_health():
    return {
        "Status": "OK"
    }