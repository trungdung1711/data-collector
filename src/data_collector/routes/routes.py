from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/test')
async def test():
    return {
        'data' : 'Hello world'
    }