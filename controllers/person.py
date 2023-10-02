from models.person import Person
from fastapi import APIRouter

router = APIRouter()

@router.post("/person")
async def add_person(person: Person):
    await person.save()
    return person

@router.get("/people")
async def list_people():
    return await Person.objects.all()