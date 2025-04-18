from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from get_top_stocks import get_top_stocks
from data_crawler import (
    get_top_rising,
    get_volume_spike,
    get_institution_buy,
    get_quiet_rise,
    get_steady_up,
)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return {"message": "안녕, 미정!"}

@app.get("/ranking", response_class=HTMLResponse)
def show_ranking(request: Request):
    ranking_data = get_top_stocks()
    return templates.TemplateResponse("ranking.html", {
        "request": request,
        "title": "오늘의 상승률 순위 TOP5 (네이버 실시간)",
        "data": ranking_data
    })

@app.get("/profile")
def get_profile():
    return {"message": "여긴 미정의 프로필 페이지야!"}

@app.get("/filters", response_class=HTMLResponse)
def show_filters(request: Request):
    return templates.TemplateResponse("filters.html", {"request": request})

@app.get("/condition/sprinter", response_class=HTMLResponse)
def show_sprinter(request: Request):
    data = get_top_rising()
    return templates.TemplateResponse("sprinter.html", {"request": request, "data": data})

@app.get("/condition/volume_spike", response_class=HTMLResponse)
def show_volume_spike(request: Request):
    data = get_volume_spike()
    return templates.TemplateResponse("volume_spike.html", {"request": request, "data": data})

@app.get("/condition/institution_buy", response_class=HTMLResponse)
def show_institution_buy(request: Request):
    data = get_institution_buy()
    return templates.TemplateResponse("institution_buy.html", {"request": request, "data": data})

@app.get("/condition/quiet_rise", response_class=HTMLResponse)
def show_quiet_rise(request: Request):
    data = get_quiet_rise()
    return templates.TemplateResponse("quiet_rise.html", {"request": request, "data": data})

@app.get("/condition/steady_up", response_class=HTMLResponse)
def show_steady_up(request: Request):
    data = get_steady_up()
    return templates.TemplateResponse("steady_up.html", {"request": request, "data": data})
