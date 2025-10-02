from fastapi import FastAPI

from data_collector.routes import private, public, session

app = FastAPI(
    title="Data collector API",
    description="Simple data collector API",
    version="1.0.0",
    docs_url="/docs",
    contact={
        "name": "Le Bui Trung Dung",
        "email": "trungdunglebui17112004@gmail.com",
    },
)

app.include_router(router=public.router)
app.include_router(router=private.router)
app.include_router(router=session.router)
