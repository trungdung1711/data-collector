from fastapi import FastAPI
from data_collector.routes import router



app = FastAPI(title='Data collector')
app.include_router(router=router, prefix='/api/v1', tags=['sessions'])