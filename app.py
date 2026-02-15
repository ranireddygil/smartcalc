from fastapi import FastAPI
from pydantic import BaseModel

from main import calculate_expression

app = FastAPI()


# Optional homepage so visiting the root URL doesn't show {"detail":"Not Found"}
@app.get("/")
def root():
    return {"message": "SmartCalc API is running"}


class CalcRequest(BaseModel):
    expression: str


@app.post("/calculate")
def calculate(payload: CalcRequest):
    result = calculate_expression(payload.expression)
    return {"expression": payload.expression, "result": result}
