from estadistica.base import EstadisticaBase

class EstadisticaCualitativa(EstadisticaBase):
    def __init__(self, datos):
        super().__init__(datos)

    def frecuencias(self):
        conteo = {}
        for valor in self.datos:
            conteo[valor] = conteo.get(valor, 0) + 1
        return conteo

    def porcentajes(self):
        frec = self.frecuencias()
        total = len(self.datos)
        return {k: (v / total) * 100 for k, v in frec.items()}

    def moda(self):
        frec = self.frecuencias()
        max_frec = max(frec.values())
        return [k for k, v in frec.items() if v == max_frec]

    def resumen(self):
        return {
            "frecuencias": self.frecuencias(),
            "porcentajes": self.porcentajes(),
            "moda": self.moda()
}
