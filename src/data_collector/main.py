from data_collector.configs import app


def main():
    import uvicorn

    app_loc = "data_collector.app:app"
    uvicorn.run(app_loc, host=app.HOST, port=app.PORT, reload=True)


if __name__ == "__main__":
    main()
