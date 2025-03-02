from hw_1.model import model
from fastapi import FastAPI

app = FastAPI()

@app.get('/password')
def get_password(length: str):
    result = model.generates_a_password(length)
    return result


@app.get('/gravity')
def get_force_of_attraction():
    pass


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)



















# 'http://localhost:8000/length'