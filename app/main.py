from fastapi import FastAPI
app = FastAPI(title="电网灵活负荷编排器")
@app.get("/healthz")
def healthz() -> dict[str, str]: return {"status": "ok"}
