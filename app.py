from typing import Optional, Text, Any
import PyBypass as bypasser
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/bypass")
def bypass(link: Text, bypass_args: Optional[Any] = None):
    try:
        bypassed_link = bypasser.bypass(link, bypass_args)
        return {'link': bypassed_link}
    except Exception as e:
        return {'error':  e.__str__()}


if __name__ == '__main__':
    uvicorn.run(app)