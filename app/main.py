from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "johnny"}

@app.get("/wrong-url")
def read_item():
    print ("working")
    return {
        "name": "John",
        "age": 30,
        "youre": "retarded"
    }

@app.get("/way")
def read_item():
    print ("working")
    return {
        "name": "John",
        "age": 30,
        "yourenot": "retarded"
    }

