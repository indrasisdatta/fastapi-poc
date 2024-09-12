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
