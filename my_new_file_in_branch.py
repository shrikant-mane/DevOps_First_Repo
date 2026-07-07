from fastapi import FastAPI

app = FasrAPI()

@app.get('/')
async def hello_world():
	return {'message': 'Hello World'}

