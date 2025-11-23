from fastapi import FastAPI

app = FastAPI(title="API TDD VGMG")

@app.get("/")
def ler_root():
    return {"message": "API TDD VGMG funcionando!"}