class Strings:
    def es_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")
        invertida = ""
        for i in range(len(texto) - 1, -1, -1):
            invertida += texto[i]
        return texto == invertida
    
    def invertir_cadena(self, texto):
        resultado = ""
        for i in range(len(texto) - 1, -1, -1):
            resultado += texto[i]
        return resultado
    
    def contar_vocales(self, texto):
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
        contador = 0
        for c in texto:
            if c in vocales:
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
        contador = 0
        for c in texto:
            if c.isalpha() and c not in vocales:
                contador += 1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        t1 = sorted(texto1.replace(" ", "").lower())
        t2 = sorted(texto2.replace(" ", "").lower())
        return t1 == t2
    
    def contar_palabras(self, texto):
        palabras = [p for p in texto.strip().split(" ") if p]
        return len(palabras)
    
    def palabras_mayus(self, texto):
        palabras = texto.split()
        resultado = ""
        for p in palabras:
            resultado += p[0].upper() + p[1:] + " "
        return resultado.strip()
    
    def eliminar_espacios_duplicados(self, texto):
        resultado = ""
        espacio_anterior = False
        for c in texto:
            if c == " ":
                if not espacio_anterior:
                    resultado += c
                espacio_anterior = True
            else:
                resultado += c
                espacio_anterior = False
        return resultado.strip()
    
    def es_numero_entero(self, texto):
        if not texto:
            return False
        if texto[0] in "+-":
            texto = texto[1:]
        if not texto:
            return False
        for c in texto:
            if c < "0" or c > "9":
                return False
        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord("A") if c.isupper() else ord("a")
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        n, m = len(texto), len(subcadena)
        for i in range(n - m + 1):
            if texto[i:i + m] == subcadena:
                posiciones.append(i)
        return posiciones
