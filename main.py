from typing import Union
from fastapi import FastAPI, HTTPException
from data import PERSONS
from schemas import GenderURLChoice, PersonBase, PersonCreate, PersonWithID

app = FastAPI()


@app.get("/persons/")
async def persons(gender: GenderURLChoice | None = None) -> list[PersonWithID]:
    if gender:
        return[
            PersonWithID(**p) for p in PERSONS if p["gender"].value.lower() == gender.value
        ]
    return [PersonWithID(**p) for p in PERSONS]


@app.get("/persons/{id}")
async def person(id: int) -> PersonWithID:
    person = next((PersonWithID(**p) for p in PERSONS if p["id"] == id), None)
    if person is None:
        raise HTTPException(status_code=404, detail="Band no found")
    return person


@app.get("/persons/geneder/{gender}")
async def get_person_for_gender(gender: GenderURLChoice) -> list[dict]:
    return [p for p in PERSONS if p["gender"].lower() == gender.value]


@app.post("/persons")
async def create_person(person_data: PersonCreate) -> PersonWithID:
    id = PERSONS[-1]['id'] + 1
    person = PersonWithID(id=id, **person_data.model_dump()).model_dump()
    PERSONS.append(person)
    return person
