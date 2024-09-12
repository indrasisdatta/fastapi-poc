# Create a POC using Fast API

```bash
uv venv
```

Activate with: `bash.venv\Scripts\activate`

## For "pip module not found" error - run the below command

```bash
py -m ensurepip --upgrade
```

## Install necessary modules and add to requirements.txt

```bash
py -m pip install fastapi uvcorn
py -m pip freeze > requirements.txt
```

## Other devs can install the dependencies in requirements.txt

```bash
py -m pip install -r requirements.txt
```

### For file upload, install package:

```bash
py -m pip install python-multipart
```

[In buid Swagger doc for APIs](http://localhost:8000/docs)

[Fast API Udemy course](https://cognizant.udemy.com/course/fastapi-the-complete-course/learn/lecture/29025340#overview)
