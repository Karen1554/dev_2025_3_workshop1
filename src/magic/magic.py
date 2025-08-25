import math
import random

class Magic:
    def fibonacci(self, n):
        if n < 0:
            raise ValueError("n debe ser >= 0")
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def secuencia_fibonacci(self, n):
        if n < 0:
            raise ValueError("n debe ser >= 0")
        seq = []
        a, b = 0, 1
        for _ in range(n):
            seq.append(a)
            a, b = b, a + b
        return seq

    def es_primo(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        return [x for x in range(2, n+1) if self.es_primo(x)]

    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        suma = 1
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                suma += i
                if i != n // i:
                    suma += n // i
        return suma == n

    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []
        triangulo = [[1]]
        for _ in range(1, filas):
            prev = triangulo[-1]
            fila = [1]
            for j in range(len(prev) - 1):
                fila.append(prev[j] + prev[j+1])
            fila.append(1)
            triangulo.append(fila)
        return triangulo

    def factorial(self, n):
        if n < 0:
            raise ValueError("n debe ser >= 0")
        res = 1
        for i in range(2, n+1):
            res *= i
        return res

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a*b) // self.mcd(a, b)

    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        digitos = str(n)
        potencia = len(digitos)
        return sum(int(d)**potencia for d in digitos) == n

    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        if any(len(fila) != n for fila in matriz):
            return False
        suma_objetivo = sum(matriz[0])
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        for j in range(n):
            if sum(matriz[i][j] for i in range(n)) != suma_objetivo:
                return False
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
        if sum(matriz[i][n-1-i] for i in range(n)) != suma_objetivo:
            return False
        return True
