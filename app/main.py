from pathlib import Path
from typing import Union
from fastapi import FastAPI, Form
from pydantic import BaseModel
from app.API_rotes.Api_Rotes import router, read_user
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI()


app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



class Item(BaseModel):
    name: str
    price: float 
    is_offer: Union[bool, None] = None


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/", response_class=HTMLResponse)
async def calcular(request: Request, numero: int = Form(...) ):
    resultado = read_user(numero)
    return templates.TemplateResponse("index.html", {"request": request, "resultado": resultado})
