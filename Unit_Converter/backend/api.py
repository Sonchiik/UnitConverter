from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from backend.converter import LengthConverter, WeightConverter, TemperatureConverter


app = FastAPI()
app.mount("/static", StaticFiles(directory='frontend'), name="static")

class ConvensionRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str
    
templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/convert/length")
def convert_length(request: ConvensionRequest):
    print(f"Received length conversion request: {request}")
    converter = LengthConverter()
    try: 
        result = converter.convert(request.value, request.from_unit, request.to_unit)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/convert/weight")
def convert_weight(request: ConvensionRequest):
    print(f"Received weight conversion request: {request}")
    converter = WeightConverter()
    try:
        result = converter.convert(request.value, request.from_unit, request.to_unit)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/convert/temperature")
def convert_temperature(request: ConvensionRequest):
    converter = TemperatureConverter()
    print(f"Received temperature conversion request: {request}")
    try:
        result = converter.convert(request.value, request.from_unit, request.to_unit)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        