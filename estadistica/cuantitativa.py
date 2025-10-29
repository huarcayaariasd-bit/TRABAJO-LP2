# estadistica/cuantitativa.py
 
from estadistica.base import EstadisticaBase

class EstadisticaCuantitativa(EstadisticaBase):
    def _init_(self, datos):
        super()._init_(datos)
        # Aseguramos que los datos sean numéricos
        self.datos = [float(x) for x in self.datos if self._es_numero(x)]
        self.datos.sort()

    def _es_numero(self, valor):
        try:
            float(valor)
            return True
        except:
            return False

    def media(self):
        suma = 0
        for valor in self.datos:
            suma += valor
        return suma / len(self.datos)

    def mediana(self):
        n = len(self.datos)
        mitad = n // 2
        if n % 2 == 0:
            return (self.datos[mitad - 1] + self.datos[mitad]) / 2
        else:
            return self.datos[mitad]

    def moda(self):
        frecuencias = {}
        for valor in self.datos:
            if valor in frecuencias:
                frecuencias[valor] += 1
            else:
                frecuencias[valor] = 1
        max_frec = max(frecuencias.values())
        modas = [k for k, v in frecuencias.items() if v == max_frec]
        return modas

    def varianza(self):
        media = self.media()
        suma = 0
        for valor in self.datos:
            suma += (valor - media) ** 2
        return suma / (len(self.datos) - 1)

    def desviacion_estandar(self):
        return self.varianza() ** 0.5

    def percentil(self, p):
        """
        Calcula el percentil p (entre 0 y 100) manualmente.
        """
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