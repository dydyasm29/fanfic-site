from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import uuid

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate/")
async def generate_fanfic(prompt: str = Form(...)):
    # Simuler une fanfiction (ici tu mettras l’appel à l’IA plus tard)
    story = f"""Titre : Fanfic générée
Consigne : {prompt}

Chapitre 1
C'était un jour sombre et orageux. Les héros se réveillaient dans un monde inversé...

Chapitre 2
[...]
Fin.
"""

    filename = f"fanfic_{uuid.uuid4().hex}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story)

    return FileResponse(path=filename, filename="fanfic.txt", media_type='text/plain')
