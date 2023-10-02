from fastapi import APIRouter
from controllers import person

router = APIRouter()

router.include_router(person.router, prefix='')