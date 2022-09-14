from app.data.expert_diagnosis_system_repo import ExpertDiagnosisSystemRepo
from app.domain.usecase.symptom_uc import SymptomUC


def get_symptom_repo():
    return ExpertDiagnosisSystemRepo()


def get_symptom_uc():
    return SymptomUC(get_symptom_repo())
