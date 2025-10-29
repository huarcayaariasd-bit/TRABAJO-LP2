from estadistica.base import EstadisticaBase

class EstadisticaCuantitativa(EstadisticaBase):
    def __init__(self, datos):
        super().__init__(datos)
        self.datos = [float(x) for x in self.datos if self._es_numero(x)]
        self.datos.sort()

    def _es_numero(self, valor):
        try:
            float(valor)
            return True
        except:
            return False

    def media(self):
        return sum(self.datos) / len(self.datos)

    def mediana(self):
        n = len(self.datos)
        mitad = n // 2
        if n % 2 == 0:
            return (self.datos[mitad - 1] + self.datos[mitad]) / 2
        else:
            return self.datos[mitad]

    def moda(self):
        frec = {}
        for v in self.datos:
            frec[v] = frec.get(v, 0) + 1
        max_frec = max(frec.values())
        return [k for k, v in frec.items() if v == max_frec]

    def varianza(self):
        m = self.media()
        return sum((x - m) ** 2 for x in self.datos) / (len(self.datos) - 1)

    def desviacion_estandar(self):
        return self.varianza() ** 0.5

    def percentil(self, p):
        if not self.datos:
            return None
        k = (len(self.datos) - 1) * (p / 100)
        f = int(k)
        c = k - f
        if f + 1 < len(self.datos):
            return self.datos[f] + (self.datos[f + 1] - self.datos[f]) * c
        else:
            return self.datos[f]

    def resumen(self):
        return {
            "media": self.media(),
            "mediana": self.mediana(),
            "moda": self.moda(),
            "varianza": self.varianza(),
            "desviacion_estandar": self.desviacion_estandar(),
            "percentil_25": self.percentil(25),
            "percentil_50": self.percentil(50),
            "percentil_75": self.percentil(75),
}
