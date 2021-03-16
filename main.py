import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
    # app:app  first app refers to app.py second app is the "app" used by uvicorn
