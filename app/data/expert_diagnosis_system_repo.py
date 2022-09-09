from .diagnosis_knowladge_engine import DiseasesKnowledgeEngine, Symptom as SymptomFact
from ..domain.interface.symptom_repo import SymptomRepository
from ..domain.schema.symptom import Symptom, SymptomIn, Disease


class ExpertDiagnosisSystemRepo(SymptomRepository):
    def __init__(self) -> None:
        self.kowladge_engine = DiseasesKnowledgeEngine()
        self.kowladge_engine.reset()
        self.kowladge_engine.run()

    def add_symptom(self, symptom: SymptomIn) -> Symptom:
        self.kowladge_engine.declare(
            SymptomFact(name=symptom.name, isExist=symptom.answer)
        )
        self.kowladge_engine.run()
        return Symptom(name=symptom.name)

    def get_next_symptom(self) -> Symptom:
        if self.is_finished():
            return None
        name = self.kowladge_engine.next_symptom
        return Symptom(name=name)

    def is_finished(self) -> bool:
        if self.kowladge_engine.diagnosis_result is not None:
            return True
        return False

    def get_result(self) -> Disease:
        disease = self.kowladge_engine.diagnosis_result
        return Disease(disease=disease)
