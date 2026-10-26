from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hola desde mi API Docker optimizada",
        "student": "André Espinoza",
        "version": "2.0"
    }


@app.get("/health")
def health():
    return {"status": "ok"}