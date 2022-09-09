from unicodedata import name
from experta import *


class Symptom(Fact):
    name = Field(str)
    isExist = Field(str)


class Disease(Fact):
    name = Field(str)


class DiseasesKnowledgeEngine(KnowledgeEngine):
    next_symptom = None
    diagnosis_result = None

    @Rule(Disease(name=MATCH.name))
    def result(self, name):
        self.diagnosis_result = str(name)

    @Rule(NOT(Symptom()))
    def symptom_1(self):
        self.next_symptom = "headache"

    @Rule(Symptom(name="headache", isExist="yes"))
    def askForPulsingHeadache(self):
        self.next_symptom = "Pulsing Headache"

    @Rule(Symptom(name="headache", isExist="no"))
    def askForSyncope(self):
        self.next_symptom = "Syncope"

    @Rule(Symptom(name="Pulsing Headache", isExist="yes"))
    def askForPainInTheUpperPartOfTheHead(self):
        self.next_symptom = "Pain in the upper part of the head"

    @Rule(Symptom(name="Pulsing Headache", isExist="no"))
    def askForTightHeadache(self):
        self.next_symptom = "Tight headache"

    @Rule(Symptom(name="Pain in the upper part of the head", isExist="yes"))
    def printClusterHeadache(self):
        self.declare(Disease(name="Cluster Headache"))

    @Rule(Symptom(name="Pain in the upper part of the head", isExist="no"))
    def askForPainInPartOfTheHead(self):
        self.next_symptom = "Pain in the right/left part of the head"

    @Rule(Symptom(name="Pain in the right/left part of the head", isExist="yes"))
    def printMigraine(self):
        self.declare(Disease(name="Migraine"))

    @Rule(Symptom(name="Pain in the right/left part of the head", isExist="no"))
    def printNotInLeftOfHead(self):
        self.declare(Disease(name="NULL"))

    @Rule(Symptom(name="Pulsing Headache", isExist="no"))
    def askForTightHeadache(self):
        self.next_symptom = "Tight headache"

    @Rule(Symptom(name="Tight headache", isExist="yes"))
    def askForSpasmHeadache(self):
        self.next_symptom = "Spasm Headache"

    @Rule(Symptom(name="Tight headache", isExist="no"))
    def askForMadeYouWakingUpFromSleeping(self):
        self.next_symptom = "Made you waking up from sleeping"

    @Rule(Symptom(name="Spasm Headache", isExist="no"))
    def printPsychologicalDistress(self):
        self.declare(Disease(name="Psychological Distress"))

    @Rule(Symptom(name="Spasm Headache", isExist="yes"))
    def printNotPsychologicalDistress(self):
        self.declare(Disease(name="NULL"))

    @Rule(Symptom(name="Made you waking up from sleeping", isExist="no"))
    def printNotFromSleeping(self):
        self.declare(Disease(name="NULL"))

    @Rule(Symptom(name="Made you waking up from sleeping", isExist="yes"))
    def askForFountainVomit(self):
        self.next_symptom = "Fountain Vomit"

    @Rule(Symptom(name="Fountain Vomit", isExist="yes"))
    def printbrainTumor(self):
        self.declare(Disease(name="brain Tumor"))

    @Rule(Symptom(name="Fountain Vomit", isExist="no"))
    def printNotbrainTumor(self):
        self.declare(Disease(name="NULL"))

    @Rule(Symptom(name="Syncope", isExist="yes"))
    def askForHypotension(self):
        self.next_symptom = "Hypotension"

    @Rule(Symptom(name="Syncope", isExist="no"))
    def askForVertigo(self):
        self.next_symptom = "Vertigo"

    @Rule(Symptom(name="Hypotension", isExist="yes"))
    def printOrthostaticHypotension(self):
        self.declare(Disease(name="Orthostatic Hypotension"))

    @Rule(Symptom(name="Hypotension", isExist="no"))
    def askForWhilePeeing(self):
        self.next_symptom = "While Peeing"

    @Rule(Symptom(name="While Peeing", isExist="yes"))
    def printPeeSyncope(self):
        self.declare(Disease(name="Pee Syncope"))

    @Rule(Symptom(name="Hypotension", isExist="no"))
    def askForWhileMakingANecktie(self):
        self.next_symptom = "While making a Necktie"

    @Rule(Symptom(name="While making a Necktie", isExist="yes"))
    def printVagalSyncope(self):
        self.declare(Disease(name="Vagal Syncope"))

    @Rule(Symptom(name="While making a Necktie", isExist="no"))
    def askForPeripheralVasodilation(self):
        self.next_symptom = "Peripheral vasodilation"

    @Rule(Symptom(name="Peripheral vasodilation", isExist="yes"))
    def printAnotherVasovagalSyncope(self):
        self.declare(Disease(name="Vasovagal Syncope"))

    @Rule(Symptom(name="Peripheral vasodilation", isExist="no"))
    def printNotVasovagalSyncope(self):
        self.declare(Disease(name="Vagal Syncope"))

    @Rule(Symptom(name="Vertigo", isExist="yes"))
    def askForReal(self):
        self.next_symptom = "Real"

    @Rule(Symptom(name="Real", isExist="yes"))
    def printInnerEarInfection(self):
        self.declare(Disease(name="Inner ear infection"))

    @Rule(Symptom(name="Real", isExist="no"))
    def askForLie(self):
        self.next_symptom = "Lie"

    @Rule(Symptom(name="Real", isExist="yes"))
    def printPsychologicalProblem(self):
        self.declare(Disease(name="Psychological Problem"))

    @Rule(Symptom(name="Real", isExist="no"))
    def printNotPsychologicalProblem(self):
        self.declare(Disease(name="NULL"))

    @Rule(Symptom(name="Vertigo", isExist="no"))
    def askForGaitDisturbance(self):
        self.next_symptom = "Gait disturbance"

    @Rule(Symptom(name="Gait disturbance", isExist="yes"))
    def askForSpastic(self):
        self.next_symptom = "Spastic"

    @Rule(Symptom(name="Spastic", isExist="yes"))
    def printPyramidalInjury(self):
        self.declare(Disease(name="Pyramidal injury"))

    @Rule(Symptom(name="Spastic", isExist="no"))
    def askForStagger(self):
        self.next_symptom = "Stagger"

    @Rule(Symptom(name="Stagger", isExist="yes"))
    def printCerebellumInjury(self):
        self.declare(Disease(name="Cerebellum injury"))

    @Rule(Symptom(name="Stagger", isExist="no"))
    def askForGaitHemiphegiar(self):
        self.next_symptom = "Gait hemiphegia"

    @Rule(Symptom(name="Gait hemiphegia", isExist="yes"))
    def printHemiphegia(self):
        self.declare(Disease(name="Hemiphegia"))

    @Rule(Symptom(name="Gait hemiphegia", isExist="no"))
    def askForMilitary(self):
        self.next_symptom = "Military"

    @Rule(Symptom(name="Military", isExist="yes"))
    def printPosteriorCordInjury(self):
        self.declare(Disease(name="Posterior cord injury"))

    @Rule(Symptom(name="Military", isExist="no"))
    def askForTrendlenburg(self):
        self.next_symptom = "trendlenburg"

    @Rule(Symptom(name="trendlenburg", isExist="yes"))
    def printCongenitalHipDislocation(self):
        self.declare(Disease(name="Congenital hip dislocation"))

    @Rule(Symptom(name="trendlenburg", isExist="no"))
    def askForGaitParkinson(self):
        self.next_symptom = "Gait parkinson"

    @Rule(Symptom(name="Gait parkinson", isExist="yes"))
    def printParkinsonDisease(self):
        self.declare(Disease(name="Parkinson Disease"))

    @Rule(Symptom(name="Gait parkinson", isExist="no"))
    def askForNotParkinson(self):
        self.declare(Disease(name="NULL"))

    @Rule(Symptom(name="Gait disturbance", isExist="no"))
    def askForInvoluntaryMovement(self):
        self.next_symptom = "Involuntary movement"

    @Rule(Symptom(name="Involuntary movement", isExist="yes"))
    def askForShiver(self):
        self.next_symptom = "Shiver"

    @Rule(Symptom(name="Shiver", isExist="yes"))
    def askForSmooth(self):
        self.next_symptom = "Smooth"

    @Rule(Symptom(name="shiver", isExist="no"))
    def askForCanonMovements(self):
        self.next_symptom = "Canon movements"

    @Rule(Symptom(name="Smooth", isExist="yes"))
    def printHyperthyroidism(self):
        self.declare(Disease(name="Hyperthyroidism"))

    @Rule(Symptom(name="Smooth", isExist="no"))
    def askForRough(self):
        self.next_symptom = "Rough"

    @Rule(Symptom(name="Rough", isExist="yes"))
    def printDrugStopping(self):
        self.declare(Disease(name="A Drug Stopping"))

    @Rule(Symptom(name="Rough", isExist="no"))
    def askForIntentionally(self):
        self.next_symptom = "Intentionally"

    @Rule(Symptom(name="Intentionally", isExist="no"))
    def askForSpontaneous(self):
        self.next_symptom = "Spontaneous"

    @Rule(Symptom(name="Intentionally", isExist="yes"))
    def printCereblellumInjury(self):
        self.declare(Disease(name="Cerebellum injury"))

    @Rule(Symptom(name="Spontaneous", isExist="yes"))
    def printParkinsonDisease(self):
        self.declare(Disease(name="Parkinson disease"))

    @Rule(Symptom(name="Spontaneous", isExist="no"))
    def printSpontaneous(self):
        self.declare(Disease(name="Spontaneous"))

    @Rule(Symptom(name="Canon movements", isExist="yes"))
    def printOtriped(self):
        self.declare(Disease(name="Otriped body injury"))

    @Rule(Symptom(name="Canon movements", isExist="no"))
    def askForDancingMoving(self):
        self.next_symptom = "Dancing moving"

    @Rule(Symptom(name="Dancing moving", isExist="yes"))
    def askForAcute(self):
        self.next_symptom = "Acute"

    @Rule(Symptom(name="Dancing moving", isExist="no"))
    def printNotDancingMoving(self):
        self.declare(Disease(name="NULL"))

    @Rule(Symptom(name="Acute", isExist="yes"))
    def printSydenham(self):
        self.declare(Disease(name="Sydenham"))

    @Rule(Symptom(name="Acute", isExist="no"))
    def askForChronic(self):
        self.next_symptom = "Chronic"

    @Rule(Symptom(name="Chronic", isExist="yes"))
    def printHuntigton(self):
        self.declare(Disease(name="Huntigton"))

    @Rule(Symptom(name="Chronic", isExist="no"))
    def printChronic(self):
        self.declare(Disease(name="NULL"))

    @Rule(Symptom(name="Involuntary movement", isExist="no"))
    def askForInjuryInNerves(self):
        self.next_symptom = "Injury in nerves"

    @Rule(Symptom(name="Injury in nerves", isExist="yes"))
    def askForSeeingDifficulty(self):
        self.next_symptom = "Seeing Difficulty"

    @Rule(Symptom(name="Injury in nerves", isExist="no"))
    def printInjuryNerve(self):
        self.declare(Disease(name="NULL"))

    @Rule(Symptom(name="Seeing Difficulty", isExist="yes"))
    def PRintOpticalNerve(self):
        self.declare(Disease(name="Injury in optical nerve"))

    @Rule(Symptom(name="Seeing Difficulty", isExist="no"))
    def askForSmellingDifficulty(self):
        self.next_symptom = "Smelling Difficulty"

    @Rule(Symptom(name="Smelling Difficulty", isExist="yes"))
    def printAlfactoryNerve(self):
        self.declare(Disease(name="Injury in alfactory nerve"))

    @Rule(Symptom(name="Smelling Difficulty", isExist="no"))
    def askForMovingEyeDifficulty(self):
        self.next_symptom = "Moving eye Difficulty"

    @Rule(Symptom(name="Moving eye Difficultye", isExist="yes"))
    def printOcularNerve(self):
        self.declare(Disease(name="Injury in ocular nerve"))

    @Rule(Symptom(name="Moving eye Difficulty", isExist="no"))
    def askForDifficultyInAbducenteye(self):
        self.next_symptom = "Difficulty in abducenteye"

    @Rule(Symptom(name="Difficulty in abducenteye", isExist="yes"))
    def printAbducentNerve(self):
        self.declare(Disease(name="Injury in abducent nerve"))

    @Rule(Symptom(name="Difficulty in abducenteye", isExist="no"))
    def askForDifficultyInMovingFaceMuscler(self):
        self.next_symptom = "Difficulty in moving face muscle"

    @Rule(Symptom(name="Difficulty in moving face muscle", isExist="yes"))
    def printFacialNerve(self):
        self.declare(Disease(name="Injury in facial nerve"))

    @Rule(Symptom(name="Difficulty in moving face muscle", isExist="no"))
    def askForLossOfTaste(self):
        self.next_symptom = "Loss of taste sense in the posterior third"

    @Rule(Symptom(name="Loss of taste sense in the posterior third", isExist="yes"))
    def askForGlossopharyngeal(self):
        self.declare(Disease(name="Injury in glossopharyngeal nerve"))

    @Rule(Symptom(name="Loss of taste sense in the posterior third", isExist="no"))
    def askForUvulaDeviation(self):
        self.next_symptom = "Uvula deviation"

    @Rule(Symptom(name="Uvula deviation", isExist="yes"))
    def printVegal(self):
        self.declare(Disease(name="Injury in vegal nerve"))

    @Rule(Symptom(name="Uvula deviation", isExist="no"))
    def askForSternocleidomastoid(self):
        self.next_symptom = "Weakness of the Sternocleidomastoid"

    @Rule(Symptom(name="Weakness of the Sternocleidomastoid", isExist="yes"))
    def printAccesory(self):
        self.declare(Disease(name="Injury in accesory nerve"))

    @Rule(Symptom(name="Weakness of the Sternocleidomastoid", isExist="no"))
    def printSternocleidomastoid(self):
        self.declare(Disease(name="NULL"))

