class Stats:
    def promedio(self, numeros):
        return sum(numeros) / len(numeros) if numeros else 0
    
    def mediana(self, numeros):
        n = len(numeros)
        if n == 0:
            return 0
        numeros_ordenados = sorted(numeros)
        medio = n // 2
        if n % 2 == 0:
            return (numeros_ordenados[medio - 1] + numeros_ordenados[medio]) / 2
        else:
            return numeros_ordenados[medio]
    
    def moda(self, numeros):
        if not numeros:
            return None
        conteos = {}
        for num in numeros:
            conteos[num] = conteos.get(num, 0) + 1
        max_frecuencia = max(conteos.values())
        for num in numeros:
            if conteos[num] == max_frecuencia:
                return num
    
    def desviacion_estandar(self, numeros):
        if not numeros:
            return 0
        media = self.promedio(numeros)
        var = sum((x - media) ** 2 for x in numeros) / len(numeros)
        return var ** 0.5
    
    def varianza(self, numeros):
        if not numeros:
            return 0
        media = self.promedio(numeros)
        return sum((x - media) ** 2 for x in numeros) / len(numeros)
    
    def rango(self, numeros):
        if not numeros:
            return 0
        return max(numeros) - min(numeros)
