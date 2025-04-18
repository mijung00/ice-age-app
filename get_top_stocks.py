import requests
from bs4 import BeautifulSoup

def get_top_stocks():
    url = "https://finance.naver.com/sise/sise_rise.nhn"  # 코스피 상승률 상위 페이지
    response = requests.get(url)
    response.encoding = "euc-kr"

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="type_2")

    result = []
    rows = table.find_all("tr")[2:]  # 헤더 두 줄 제외

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 10:
            continue

        rank = len(result) + 1
        name = cols[1].get_text(strip=True)
        rate = cols[4].get_text(strip=True)  # ✅ 수익률 (등락률) 컬럼으로 변경

        result.append({
            "rank": rank,
            "symbol": name,
            "return": rate
        })

        if rank >= 5:
            break

    return result

# 테스트용
if __name__ == "__main__":
    from pprint import pprint
    pprint(get_top_stocks())
