from fastapi import FastAPI
from pydantic import BaseModel
from .math_ops import add

app = FastAPI(title="Mini FastAPI App")


class SumRequest(BaseModel):
    numbers: list[float]


@app.get("/ping")
def ping() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/sum")
def sum_numbers(payload: SumRequest) -> dict[str, float]:
    return {"sum": add(payload.numbers)}
