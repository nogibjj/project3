from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dblib.querydb import querydb
from dblib.querydb import querySalaryofLevels
from dblib.querydb import querySalaryByCurrency
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Databricks"}
    
# query 1
@app.get("/salaryofposition/{position}")
async def getSalaryofPosition(position: str):
    salarylist_Avg = querySalaryofLevels(position)
    ansdict = {}
    ansdict["Average salary of entry level position (USD)"] = salarylist_Avg[0]
    ansdict["Average salary of medium level position (USD)"] = salarylist_Avg[1]
    ansdict["Average salary of senior level position (USD)"] = salarylist_Avg[2]
    return ansdict
    
# query 2
@app.get("/currency/{currency}")
async def queryByremote_Currency(currency:str):
    res=querySalaryByCurrency(currency)
    ans={};
    ans["Average salary of the salary currency: "+currency+" is "]=res
    return ans

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")