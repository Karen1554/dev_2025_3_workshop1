class Magic:
    def fibonacci(self, n):
        if n < 0:
            raise ValueError("n debe ser un número no negativo")
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        sec = [0, 1]
        while len(sec) < n:
            sec.append(sec[-1] + sec[-2])
        return sec[:n]

    def es_primo(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False      
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        return [i for i in range(2, n + 1) if self.es_primo(i)]

    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        suma = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                suma += i
                if i != n // i:
                    suma += n // i
        return suma == n

    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []
        tri = [[1]]
        for i in range(1, filas):
            fila = [1]
            for j in range(1, i):
                fila.append(tri[i - 1][j - 1] + tri[i - 1][j])
            fila.append(1)
            tri.append(fila)
        return tri

    def factorial(self, n):
        if n < 0:
            raise ValueError("El factorial no está definido para negativos")
        res = 1
        for i in range(2, n + 1):
            res *= i
        return res

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        digitos = str(n)
        k = len(digitos)
        return n == sum(int(d) ** k for d in digitos)

    def es_cuadrado_magico(self, matriz):
        if not matriz or len(matriz) != len(matriz[0]):
            return False
        n = len(matriz)
        suma_ref = sum(matriz[0])
        for fila in matriz:
            if sum(fila) != suma_ref:
                return False
        for j in range(n):
            if sum(matriz[i][j] for i in range(n)) != suma_ref:
                return False
        if sum(matriz[i][i] for i in range(n)) != suma_ref:
            return False
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_ref:
            return False
        return True
