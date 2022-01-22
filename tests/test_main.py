import time
from multiprocessing import Process

import pytest
import requests
import uvicorn
from fastapi.responses import HTMLResponse

from fastapi.testclient import (
    TestClient,
)
from sqlalchemy import engine

from api.main import (
    app,
    get_mysql_jobdata_conn,
)

client = TestClient(app)

# 測試對資料庫的連線
# assert 回傳的物件, 是一個 sqlalchemy 的 connect 物件
def test_get_mysql_jobdata_conn():
    conn = get_mysql_jobdata_conn()
    assert isinstance(conn, engine.Connection)


# 測試對 'http://127.0.0.1:5000/' 頁面發送 request,
# 得到的回應 response 的狀態 status_code, json data
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    # assert response.json() == {
    #     "Hello": "World"
    # }
    assert response == HTMLResponse(
        content=(
            "<html>"
            "<body style='padding: 10px;'>"
            "<h1>Welcome to the API - Job Analysis</h1>"
            "<div>"
            "Check the docs: <a href='/docs'>here</a>"
            "</div>"
            "</body>"
            "</html>"
        )
    )


# 測試對 'http://127.0.0.1:5000/api/v1/indeed' 頁面發送 request,
def test_indeed():
    response = client.get(
        "/api/v1/indeed",
        params=dict(
            position="Domains Team Senior Data Engineer",
            location="london",
        ),
    )
    assert response.status_code == 200
    # 以下特別重要, 需要把 response 結果寫死
    # 避免未來 api schema 改變時, 影響 api 的使用者
    assert response.json() == {
        "data": [
            {
                "job_key": "30cf7c9a02e83bda",
                "job_title": "Domains Team Senior Data Engineer",
                "company": "Government Digital Service",
                "location": "London",
                "salary": 54700,
                "jd": '{"7": 1, "16": 1, "37": 1, "uk": 1, "up": 2, "age": 1, "all": 1, "any": 1, "api": 2, "but": 1, "can": 9, "end": 1, "how": 6, "job": 3, "law": 1, "may": 2, "mix": 1, "out": 2, "pay": 1, "per": 1, "via": 2, "way": 1, "who": 5, "2022": 1, "also": 1, "area": 1, "band": 1, "base": 1, "best": 2, "cddo": 3, "code": 1, "cost": 1, "data": 27, "date": 1, "each": 1, "edge": 1, "find": 2, "full": 1, "have": 1, "know": 8, "like": 1, "live": 2, "made": 2, "more": 1, "most": 1, "name": 2, "need": 4, "owns": 1, "pace": 1, "page": 2, "part": 1, "play": 1, "read": 1, "role": 4, "sets": 1, "such": 1, "team": 4, "test": 1, "them": 1, "time": 1, "type": 1, "ways": 1, "week": 1, "well": 4, "what": 4, "when": 1, "work": 4, "about": 2, "above": 1, "align": 1, "apply": 1, "areas": 1, "build": 1, "cases": 1, "civil": 1, "clear": 1, "cyber": 1, "equal": 3, "gives": 1, "govuk": 1, "grade": 3, "helps": 2, "hours": 2, "ideal": 1, "large": 1, "model": 1, "occur": 1, "offer": 1, "party": 1, "place": 1, "right": 2, "share": 1, "stays": 1, "third": 2, "tools": 2, "truth": 1, "under": 1, "value": 2, "where": 2, "across": 2, "agreed": 2, "allows": 2, "appear": 1, "assess": 1, "assist": 1, "brings": 1, "builds": 2, "career": 1, "chance": 1, "design": 2, "domain": 1, "drives": 1, "easily": 1, "london": 3, "making": 2, "models": 3, "needed": 1, "office": 2, "others": 1, "owners": 1, "person": 2, "policy": 1, "public": 2, "record": 1, "remain": 1, "remedy": 1, "review": 1, "salary": 2, "sector": 2, "select": 1, "senior": 3, "single": 1, "skills": 3, "source": 2, "spaces": 2, "stable": 1, "switch": 1, "system": 3, "things": 2, "trends": 1, "vision": 2, "within": 1, "ability": 1, "achieve": 1, "actions": 1, "against": 1, "because": 1, "between": 1, "bristol": 1, "central": 1, "closing": 1, "compare": 1, "control": 1, "correct": 1, "deliver": 1, "depends": 1, "designs": 1, "details": 1, "digital": 2, "domains": 5, "dynamic": 1, "ensures": 1, "finding": 1, "handles": 1, "history": 1, "january": 1, "leaders": 1, "looking": 2, "managed": 1, "manager": 1, "members": 1, "monitor": 1, "parties": 1, "pattern": 1, "present": 1, "problem": 1, "process": 1, "produce": 1, "product": 1, "related": 1, "resolve": 1, "respond": 1, "scripts": 1, "service": 1, "similar": 1, "sources": 4, "storage": 1, "subject": 1, "succeed": 1, "success": 1, "support": 2, "systems": 1, "trusted": 1, "various": 1, "volumes": 1, "working": 5, "£49700": 2, "£54700": 2, "£55000": 1, "£62500": 1, "analysis": 2, "assessed": 1, "balances": 1, "branding": 1, "business": 1, "concepts": 1, "consider": 1, "defining": 1, "document": 1, "employer": 1, "engineer": 2, "equipped": 1, "exciting": 1, "external": 2, "flexible": 1, "historic": 1, "identify": 1, "improves": 1, "in-house": 1, "initiate": 1, "insights": 1, "internet": 2, "location": 1, "measures": 1, "multiple": 1, "national": 2, "patterns": 1, "position": 1, "possible": 1, "problems": 2, "products": 1, "profiles": 1, "programs": 1, "received": 1, "relevant": 3, "rightful": 1, "scalable": 1, "services": 3, "solution": 1, "specific": 1, "strategy": 1, "strength": 1, "team’s": 1, "together": 1, "advertise": 1, "allowance": 1, "condensed": 1, "databases": 2, "decisions": 1, "delivered": 1, "depending": 1, "determine": 1, "different": 3, "diversity": 4, "effective": 1, "expertise": 2, "extending": 1, "following": 2, "implement": 1, "inclusion": 2, "locations": 1, "modelling": 3, "necessary": 1, "operating": 1, "permanent": 1, "practical": 1, "processes": 1, "profiling": 1, "represent": 1, "resilient": 1, "resistant": 1, "resources": 1, "retrieved": 1, "solutions": 1, "standards": 3, "statement": 1, "synthesis": 1, "technical": 2, "undertake": 1, "accessible": 2, "aspiration": 1, "behaviours": 2, "capability": 2, "colleagues": 1, "commitment": 1, "compromise": 1, "delivering": 1, "developing": 1, "experience": 2, "formatting": 1, "government": 4, "implements": 1, "innovative": 1, "iterations": 1, "leadership": 1, "manchester": 1, "particular": 1, "principles": 1, "profession": 1, "represents": 1, "resolution": 1, "specialist": 2, "subsequent": 1, "successful": 1, "technology": 1, "understand": 2, "unexpected": 1, "application": 1, "appropriate": 3, "collaborate": 1, "demonstrate": 1, "differently": 1, "engineering": 1, "fascinating": 1, "inclusivity": 1, "information": 1, "integrating": 1, "integration": 1, "maintaining": 2, "opportunity": 1, "performance": 1, "programming": 1, "responsible": 4, "third-party": 2, "achievements": 1, "applications": 1, "digitisation": 1, "implementing": 1, "organisation": 2, "preventative": 1, "stakeholders": 1, "technologies": 1, "user-focused": 1, "contradictory": 1, "opportunities": 2, "organisations": 1, "working-level": 1, "future-proofed": 1, "implementation": 1, "simultaneously": 1, "specifications": 2, "transformation": 1, "forward-looking": 1, "reverse-engineer": 1, "industry-recognised": 1, "moderate-to-complex": 1}',
                "post_date": "2021-12-13",
                "extract_datetime": "2022-01-12T10:57:10",
            }
        ]
    }


# end to end 測試, 模擬真實使用 request 套件發送請求
# 使用 Process 開另一個進程, 模擬啟動 api
# 之後會在主進程, 對此 api 發送 request
@pytest.fixture(scope="module")
def setUp():
    proc = Process(
        target=uvicorn.run,
        args=(app,),
        kwargs={
            "host": "127.0.0.1",
            "port": 5000,
            "log_level": "info",
        },
        daemon=True,
    )
    proc.start()
    time.sleep(1)
    return 1


# 測試對 api 發送 requests,
# assert 回傳結果是 {"Hello": "World"}
def test_index(setUp):
    response = requests.get("http://127.0.0.1:5000")
    # assert response.json() == {
    #     "Hello": "World"
    # }
    res_content="<html><body style='padding: 10px;'><h1>Welcome to the API - Job Analysis</h1><div>Check the docs: <a href='/docs'>here</a></div></body></html>"
    assert response.text == res_content
    
# 測試對 api 發送 requests
# assert 回傳的 data, 這裡把真實的 case 寫下來
# 真實場景, 對 api 發送 requests
def test_IndeedID(setUp):
    payload = {"position": "Domains Team Senior Data Engineer", "location": "london"}
    res = requests.get(
        "http://127.0.0.1:5000/api/v1/indeed",
        params=payload,
    )
    resp = res.json()["data"]
    assert resp == [
        {
            "job_key": "30cf7c9a02e83bda",
            "job_title": "Domains Team Senior Data Engineer",
            "company": "Government Digital Service",
            "location": "London",
            "salary": 54700,
            "jd": '{"7": 1, "16": 1, "37": 1, "uk": 1, "up": 2, "age": 1, "all": 1, "any": 1, "api": 2, "but": 1, "can": 9, "end": 1, "how": 6, "job": 3, "law": 1, "may": 2, "mix": 1, "out": 2, "pay": 1, "per": 1, "via": 2, "way": 1, "who": 5, "2022": 1, "also": 1, "area": 1, "band": 1, "base": 1, "best": 2, "cddo": 3, "code": 1, "cost": 1, "data": 27, "date": 1, "each": 1, "edge": 1, "find": 2, "full": 1, "have": 1, "know": 8, "like": 1, "live": 2, "made": 2, "more": 1, "most": 1, "name": 2, "need": 4, "owns": 1, "pace": 1, "page": 2, "part": 1, "play": 1, "read": 1, "role": 4, "sets": 1, "such": 1, "team": 4, "test": 1, "them": 1, "time": 1, "type": 1, "ways": 1, "week": 1, "well": 4, "what": 4, "when": 1, "work": 4, "about": 2, "above": 1, "align": 1, "apply": 1, "areas": 1, "build": 1, "cases": 1, "civil": 1, "clear": 1, "cyber": 1, "equal": 3, "gives": 1, "govuk": 1, "grade": 3, "helps": 2, "hours": 2, "ideal": 1, "large": 1, "model": 1, "occur": 1, "offer": 1, "party": 1, "place": 1, "right": 2, "share": 1, "stays": 1, "third": 2, "tools": 2, "truth": 1, "under": 1, "value": 2, "where": 2, "across": 2, "agreed": 2, "allows": 2, "appear": 1, "assess": 1, "assist": 1, "brings": 1, "builds": 2, "career": 1, "chance": 1, "design": 2, "domain": 1, "drives": 1, "easily": 1, "london": 3, "making": 2, "models": 3, "needed": 1, "office": 2, "others": 1, "owners": 1, "person": 2, "policy": 1, "public": 2, "record": 1, "remain": 1, "remedy": 1, "review": 1, "salary": 2, "sector": 2, "select": 1, "senior": 3, "single": 1, "skills": 3, "source": 2, "spaces": 2, "stable": 1, "switch": 1, "system": 3, "things": 2, "trends": 1, "vision": 2, "within": 1, "ability": 1, "achieve": 1, "actions": 1, "against": 1, "because": 1, "between": 1, "bristol": 1, "central": 1, "closing": 1, "compare": 1, "control": 1, "correct": 1, "deliver": 1, "depends": 1, "designs": 1, "details": 1, "digital": 2, "domains": 5, "dynamic": 1, "ensures": 1, "finding": 1, "handles": 1, "history": 1, "january": 1, "leaders": 1, "looking": 2, "managed": 1, "manager": 1, "members": 1, "monitor": 1, "parties": 1, "pattern": 1, "present": 1, "problem": 1, "process": 1, "produce": 1, "product": 1, "related": 1, "resolve": 1, "respond": 1, "scripts": 1, "service": 1, "similar": 1, "sources": 4, "storage": 1, "subject": 1, "succeed": 1, "success": 1, "support": 2, "systems": 1, "trusted": 1, "various": 1, "volumes": 1, "working": 5, "£49700": 2, "£54700": 2, "£55000": 1, "£62500": 1, "analysis": 2, "assessed": 1, "balances": 1, "branding": 1, "business": 1, "concepts": 1, "consider": 1, "defining": 1, "document": 1, "employer": 1, "engineer": 2, "equipped": 1, "exciting": 1, "external": 2, "flexible": 1, "historic": 1, "identify": 1, "improves": 1, "in-house": 1, "initiate": 1, "insights": 1, "internet": 2, "location": 1, "measures": 1, "multiple": 1, "national": 2, "patterns": 1, "position": 1, "possible": 1, "problems": 2, "products": 1, "profiles": 1, "programs": 1, "received": 1, "relevant": 3, "rightful": 1, "scalable": 1, "services": 3, "solution": 1, "specific": 1, "strategy": 1, "strength": 1, "team’s": 1, "together": 1, "advertise": 1, "allowance": 1, "condensed": 1, "databases": 2, "decisions": 1, "delivered": 1, "depending": 1, "determine": 1, "different": 3, "diversity": 4, "effective": 1, "expertise": 2, "extending": 1, "following": 2, "implement": 1, "inclusion": 2, "locations": 1, "modelling": 3, "necessary": 1, "operating": 1, "permanent": 1, "practical": 1, "processes": 1, "profiling": 1, "represent": 1, "resilient": 1, "resistant": 1, "resources": 1, "retrieved": 1, "solutions": 1, "standards": 3, "statement": 1, "synthesis": 1, "technical": 2, "undertake": 1, "accessible": 2, "aspiration": 1, "behaviours": 2, "capability": 2, "colleagues": 1, "commitment": 1, "compromise": 1, "delivering": 1, "developing": 1, "experience": 2, "formatting": 1, "government": 4, "implements": 1, "innovative": 1, "iterations": 1, "leadership": 1, "manchester": 1, "particular": 1, "principles": 1, "profession": 1, "represents": 1, "resolution": 1, "specialist": 2, "subsequent": 1, "successful": 1, "technology": 1, "understand": 2, "unexpected": 1, "application": 1, "appropriate": 3, "collaborate": 1, "demonstrate": 1, "differently": 1, "engineering": 1, "fascinating": 1, "inclusivity": 1, "information": 1, "integrating": 1, "integration": 1, "maintaining": 2, "opportunity": 1, "performance": 1, "programming": 1, "responsible": 4, "third-party": 2, "achievements": 1, "applications": 1, "digitisation": 1, "implementing": 1, "organisation": 2, "preventative": 1, "stakeholders": 1, "technologies": 1, "user-focused": 1, "contradictory": 1, "opportunities": 2, "organisations": 1, "working-level": 1, "future-proofed": 1, "implementation": 1, "simultaneously": 1, "specifications": 2, "transformation": 1, "forward-looking": 1, "reverse-engineer": 1, "industry-recognised": 1, "moderate-to-complex": 1}',
            "post_date": "2021-12-13",
            "extract_datetime": "2022-01-12T10:57:10",
        }
    ]
