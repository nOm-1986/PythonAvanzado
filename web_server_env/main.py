from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/numbers')
def get_list():
    return [x for x in range(1, 30)]

@app.get('/contact')
def get_list():
    return {'name': 'Hola gente'}

@app.get('/items')
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
