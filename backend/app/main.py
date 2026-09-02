from fastapi import FastAPI

app = FastAPI(
    title="CAMRA API",
    description="Context-Aware Medical Report Analyzer",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "name": "CAMRA",
        "status": "online",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }