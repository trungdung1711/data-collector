from fastapi import APIRouter, Depends
from data_collector.auth import verify_token


router = APIRouter(
    prefix='/api/v1/private',
    tags=['private'],
    dependencies=[Depends(verify_token)]
)


@router.get('/')
def get():
    return {
        'status' : 'successfully'
    }