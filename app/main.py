import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException


from app.services.parsers import Parser
from app.models.cart import Cart
from app.services.discount import Discount

templates = Jinja2Templates(directory="templates")

app = FastAPI()

# Page d'accueil avec le formulaire pour saisir les films
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request,"index.html")

# Route pour le traitement du formulaire et le calcul du prix total
@app.post("/")
async def get_cart_total_price(request: Request, movies_input: str = Form("")):

    try:
        movies = Parser(movies_input).parse()
        cart = Cart(movies)
        cart.apply_discount(Discount())
        return templates.TemplateResponse(request, "index.html", {"movies": cart.movies, "total_price": cart.total_price})

    except Exception as e:
        raise HTTPException(status_code=400, detail="Une erreur est survenue")
