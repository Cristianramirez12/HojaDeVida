
class Medico():
    def __init__(self):
        self.nombre = ""
        self.especialidad = ""
        self.dni = ""


def CreateMedico(Nom, Esp, Dni):
    NewMedico = Medico()

    NewMedico.nombre = Nom
    NewMedico.especialidad = Esp
    NewMedico.dni = Dni
    return NewMedico



    