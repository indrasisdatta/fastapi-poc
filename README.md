# Create a POC using Fast API

```bash
uv venv .venv
```

Activate with: `bash.venv\Scripts\activate`

## For "pip module not found" error - run the below command

```bash
uv ensurepip --upgrade
```

## Install necessary modules and add to requirements.txt

```bash
uv pip freeze > requirements.txt
```

## Other devs can install the dependencies in requirements.txt

```bash
uv pip install -r requirements.txt
```

## To start the application:

```bash
uvicorn app.main:app --reload
```

[In buid Swagger doc for APIs](http://localhost:8000/docs)

[Fast API Udemy course](https://cognizant.udemy.com/course/fastapi-the-complete-course/learn/lecture/29025340#overview)
