from typing import Tuple
from ..schema.symptom import Symptom, SymptomIn, Disease
from ..interface.symptom_repo import SymptomRepository


class SymptomUC:

    def __init__(self, repository: SymptomRepository) -> None:
        self._repo = repository

    def add_symptom(self, symptom: SymptomIn) -> Tuple:
        self._repo.add_symptom(symptom)
        result, next_symptom = None, None
        if self.is_finished():
            result = self.get_result()
        next_symptom = self.get_next_symptom()
        return result, next_symptom

    def get_next_symptom(self) -> Symptom:
        return self._repo.get_next_symptom()

    def is_finished(self) -> bool:
        return self._repo.is_finished()

    def get_result(self) -> Disease:
        return self._repo.get_result()
