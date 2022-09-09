from abc import ABC, abstractmethod
from ..schema.symptom import Disease, Symptom, SymptomIn


class SymptomRepository(ABC):
    @abstractmethod
    def add_symptom(self, symptom: SymptomIn) -> Symptom:
        pass

    @abstractmethod
    def get_next_symptom(self) -> Symptom:
        pass

    @abstractmethod
    def is_finished(self) -> bool:
        pass

    @abstractmethod
    def get_result(self) -> Disease:
        pass
