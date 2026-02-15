from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from main import calculate_expression

app = FastAPI()

class CalcRequest(BaseModel):
    expression: str

@app.post("/calculate")
def calculate(req: CalcRequest):
    try:
        result = calculate_expression(req.expression)
        return {
            "expression": req.expression,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
