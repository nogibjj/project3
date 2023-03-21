from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from mylib.querydb import querydb
from mylib.querydb import queryDeathsByLocation
from mylib.querydb import queryConfirmedByLocation
from mylib.querydb import queryRecoveredByLocation
import uvicorn
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Databricks"}
    
@app.get("/location/{location}")
async def queryNumber1(location:str):
    res=queryDeathsByLocation(location)
    ans={};
    ans["Average deaths of : "+location+" is "]=res
    return ans

@app.get("/location/{location}")
async def queryNumber2(location:str):
    res=queryConfirmedByLocation(location)
    ans={};
    ans["Average deaths of : "+location+" is "]=res
    return ans

@app.get("/location/{location}")
async def queryNumber3(location:str):
    res=queryRecoveredByLocation(location)
    ans={};
    ans["Average deaths of : "+location+" is "]=res
    return ans

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")