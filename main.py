from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dblib.querydb import querydb
import uvicorn
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Databricks"}
    
@app.get("/location/{location}")
async def queryNumber(location:str):
    res=queryByLocation(location)
    ans={};
    ans["Average salary of the salary currency: "+location+" is "]=res
    return ans
    

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")