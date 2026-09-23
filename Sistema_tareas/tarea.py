class Tarea:
    # crear los atributos titulo, responsable y estado e inicializarlos
    def __init__(self, titulo, responsable, estado="Pendiente"):
         self.titulo = titulo
         self.responsable = responsable
         self.estado = estado

    # mostrar información de la tarea
    def mostrar_tarea(self):
        print("-----------------")
        print(f"Titulo: {self.titulo}\nResponsable: {self.responsable}\nEstado: {self.estado}")

    # completar tarea
    def completar_tarea(self):
        self.estado = "Completada"
