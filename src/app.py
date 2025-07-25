"""
Sistema de Gerenciamento Escolar API

Uma aplicação FastAPI super simples que permite aos estudantes visualizar e se inscrever
em atividades extracurriculares na Mergington High School.
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path
from .backend import routers, database

# Inicializar web host
app = FastAPI(
    title="API da Mergington High School",
    description="API para visualizar e se inscrever em atividades extracurriculares"
)

# Inicializar database com dados de exemplo se estiver vazio
database.init_database()

# Montar o diretório de arquivos static para servir o frontend
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(current_dir, "static")), name="static")

# Root endpoint para redirecionar para static index.html
@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")

# Incluir routers
app.include_router(routers.activities.router)
app.include_router(routers.auth.router)
