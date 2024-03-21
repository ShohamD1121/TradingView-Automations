# import pip_system_certs
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.insert_stocks_script import read_stocks_from_excel, add_stocks_to_watchlist
from services.delete_stocks_script import remove_stocks_from_watchlist

app = FastAPI()

# Set the directory for the templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # Render the index.html template
    # Note: The `request` parameter is required by Jinja2Templates to render the template
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/add_to_watchlist")
def add_to_watchlist():
    stocks = read_stocks_from_excel("stocks.xlsx")
    add_stocks_to_watchlist(stocks)
    return {"message": "Item has been added to the watchlist!"}


@app.post("/remove_from_watchlist")
def add_to_watchlist():
    stocks = read_stocks_from_excel("stocks.xlsx")
    remove_stocks_from_watchlist(stocks)
    return {"message": "Item has been Removed to the watchlist!"}

# run app local : ./start_up.sh
