from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.recommend import get_top_n
from src.item_recom import get_similar_movies

#defining app
app = FastAPI()

#data validation class for user request
class UserRequest(BaseModel):
    user_id: int
    n: int = 10

#data validation class for item request
class ItemRequest(BaseModel):
    item: str

#data validation class for response
class Response(BaseModel):
    recommendations: list[str]

#health check
@app.get('/')
async def health_check():
    return {'status': 'up'}

#endpoint post request for user based
@app.post('/recommend', response_model = Response)

#defining async function that get n top predicted movies
async def user_recommend(req: UserRequest):
    try:
        titles = get_top_n(req.user_id, req.n)#getting the movie titles
    except:
        raise HTTPException(status_code=404, detail='User not found')
    
    return Response(recommendations=titles) #validating the response

#endpoint for item based
@app.post('/similar', response_model=Response)

async def item_recommend(req: ItemRequest):
    try:
        titles = get_similar_movies(req.item)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return Response(recommendations=titles)

'''Run python -m app.main because src.recommend, src.item_recom and main.py are not on same level'''