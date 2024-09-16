from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get('/')
def home():
    return { 'data': 'Welcome to Fast API home' }

@app.get('/contact')
def contact():
    return { 'data': 'Welcome to Fast API contact' }

@app.post('/upload')
def uploadFile(files: list[UploadFile]):
    print('Uploaded files: ', files)

# import uvicorn
# uvicorn.run(app)