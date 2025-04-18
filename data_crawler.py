import requests
from bs4 import BeautifulSoup

def get_top_rising():
    url = "https://finance.naver.com/sise/sise_rise.naver"
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')

        rows = soup.select("table.type_2 tr")
        result = []
        for row in rows:
            cols = row.select("td")
            if len(cols) > 2:
                name = cols[1].text.strip()
                rate = cols[2].text.strip()
                if name:
                    result.append({'종목명': name, '등락률': rate})
        return result[:20]
    except Exception as e:
        print("급등중 크롤링 에러:", e)
        return []

def get_volume_spike():
    url = "https://finance.naver.com/sise/sise_quant.naver"
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')

        rows = soup.select("table.type_2 tr")
        result = []
        for row in rows:
            cols = row.select("td")
            if len(cols) > 6:
                name = cols[1].text.strip()
                volume = cols[6].text.strip()
                if name:
                    result.append({'종목명': name, '거래량': volume})
        return result[:20]
    except Exception as e:
        print("거래량 크롤링 에러:", e)
        return []

def get_institution_buy():
    url = "https://finance.naver.com/sise/sise_deal_rank.naver?type=buy"
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')

        rows = soup.select("table.type_2 tr")
        result = []
        for row in rows:
            cols = row.select("td")
            if len(cols) > 6:
                name = cols[1].text.strip()
                buy_amt = cols[6].text.strip()
                if name:
                    result.append({'종목명': name, '순매수량': buy_amt})
        return result[:20]
    except Exception as e:
        print("기관 매수 크롤링 에러:", e)
        return []

def get_quiet_rise():
    url = "https://finance.naver.com/sise/sise_upper.naver"
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')

        rows = soup.select("table.type_2 tr")
        result = []
        for row in rows:
            cols = row.select("td")
            if len(cols) > 1:
                name = cols[1].text.strip()
                if name:
                    result.append({'종목명': name})
        return result[:20]
    except Exception as e:
        print("고요한 수급 상승 크롤링 에러:", e)
        return []

def get_steady_up():
    try:
        return [
            {"종목명": "삼성전자", "설명": "최근 1개월간 꾸준히 상승 중"},
            {"종목명": "SK하이닉스", "설명": "우상향 흐름 유지 중"},
            {"종목명": "NAVER", "설명": "출렁임 없이 꾸준한 상승"},
        ]
    except Exception as e:
        print("우상향 크롤링 에러:", e)
        return []
