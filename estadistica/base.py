class EstadisticaBase:
    
    def __init__(self, datos):
        self.datos = datos

    def resumen(self):
        """Método que debe implementar la subclase"""
        raise NotImplementedError("Este método debe implementarse en la subclase.")
