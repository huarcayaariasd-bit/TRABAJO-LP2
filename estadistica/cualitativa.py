from estadistica.base import EstadisticaBase

class EstadisticaCualitativa(EstadisticaBase):
    def _init_(self, datos):
        super()._init_(datos)

    def frecuencias(self):
        conteo = {}
        for valor in self.datos:
            if valor in conteo:
                conteo[valor] += 1
            else:
                conteo[valor] = 1
        return conteo

    def porcentajes(self):
        frec = self.frecuencias()
        total = len(self.datos)
        return {k: (v / total) * 100 for k, v in frec.items()}

    def moda(self):
        frec = self.frecuencias()
        max_frec = max(frec.values())
        modas = [k for k, v in frec.items() if v == max_frec]
        return modas

    def resumen(self):
        return {
            "frecuencias": self.frecuencias(),
            "porcentajes": self.porcentajes(),
            "moda": self.moda()
        }
