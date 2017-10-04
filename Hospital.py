class Patient(object):
    def __init__(self, patientID, name, allergies):
        self.patientID = patientID
        self.name = name
        self.allergies = allergies
        self.bed = None

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = [None]*capacity
        self.name = name
        self.capacity = capacity
    def admit(self, patientID, name, allergies):
        for i in range(0, len(self.patients)):
            if self.patients[i] == None:
                self.patients[i] = Patient(patientID, name, allergies)
                return "Admission successful"
        return "Hospital full"
    def discharge(paitentID):
        for i in range(0, len(self.patients)):
            if self.patients[i] != None:
                if self.patients[i].paitentID == paitentID:
                    self.patients[i].bed = None
                    self.patients[i] = None
        return self