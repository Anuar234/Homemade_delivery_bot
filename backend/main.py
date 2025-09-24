from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# API роуты
@app.get("/api/user/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "name": "Test User"}

# Serve Vue app
if os.path.exists("../frontend/dist"):
    app.mount("/static", StaticFiles(directory="../frontend/dist/assets"), name="static")
    
    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        return FileResponse("../frontend/dist/index.html")