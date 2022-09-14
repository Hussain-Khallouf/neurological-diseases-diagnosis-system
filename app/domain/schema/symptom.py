from pydantic import BaseModel


class Symptom(BaseModel):
    name: str


class SymptomIn(Symptom):
    answer: str


class Disease(BaseModel):
    disease: str

