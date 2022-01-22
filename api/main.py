import typing
import pandas as pd
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import create_engine, engine, text
from api import config
import orjson


class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return orjson.dumps(content)


app = FastAPI(default_response_class=ORJSONResponse)
root_router = APIRouter()


def get_mysql_jobdata_conn() -> engine.base.Connection:
    address = (
        f"mysql+pymysql://{config.MYSQL_DATA_USER}:{config.MYSQL_DATA_PASSWORD}"
        f"@{config.MYSQL_DATA_HOST}:{config.MYSQL_DATA_PORT}/{config.MYSQL_DATA_DATABASE}"
    )

    engine = create_engine(address)
    connect = engine.connect()
    return connect


@root_router.get("/")
def index(request: Request):
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the API - Job Analysis</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)


# @app.get("/")
# def read_root():
#     return {"API Health": "OK"}


# "job_key",
# "job_title",
# "company",
# "location",
# "salary",
# "jd",
# "post_date",
# "extract_date",
@root_router.get("/api/v1/indeed")
def indeed(
    position: str = "",
    location: str = "",
):
    sql = f"""
    select * from indeed
    where job_title LIKE '%{position}%'
    and location LIKE '%{location}%'
    """
    mysql_conn = get_mysql_jobdata_conn()
    data_df = pd.read_sql(text(sql), con=mysql_conn)
    data_dict = data_df.to_dict("records")
    return {"data": data_dict}


app.include_router(root_router)
