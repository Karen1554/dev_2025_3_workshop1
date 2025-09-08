class Strings:
    
    def es_palindromo(self, texto):
        if texto is None:
            return False
        limpio = "".join(ch.lower() for ch in texto if ch.isalnum())
        return limpio == limpio[::-1]

    def invertir_cadena(self, texto):
        resultado = ""
        for ch in texto:
            resultado = ch + resultado
        return resultado

    def contar_vocales(self, texto):
        if not texto:
            return 0
        vocales = set("aeiouAEIOU")
        return sum(1 for ch in texto if ch in vocales)

    def contar_consonantes(self, texto):
        if not texto:
            return 0
        vocales = set("aeiouAEIOU")
        return sum(1 for ch in texto if ch.isalpha() and ch not in vocales)

    def es_anagrama(self, texto1, texto2):
        if texto1 is None or texto2 is None:
            return False
        a = "".join(ch.lower() for ch in texto1 if ch.isalnum())
        b = "".join(ch.lower() for ch in texto2 if ch.isalnum())
        return sorted(a) == sorted(b) and a != ""

    def contar_palabras(self, texto):
        if not texto or texto.strip() == "":
            return 0
        return len(texto.split())

    def palabras_mayus(self, texto):
        res = []
        mayus = True
        for ch in texto:
            if mayus and ch.isalpha():
                res.append(ch.upper())
                mayus = False
            else:
                res.append(ch)
                if ch.isspace():
                    mayus = True
        return "".join(res)

    def eliminar_espacios_duplicados(self, texto):
        out = []
        i = 0
        n = len(texto)
        while i < n:
            out.append(texto[i])
            if texto[i] == " ":
                while i + 1 < n and texto[i + 1] == " ":
                    i += 1
            i += 1
        return "".join(out)

    def es_numero_entero(self, texto):
        if texto is None:
            return False
        t = texto.strip()
        if t in ("+", "-") or t == "":
            return False
        if t[0] in "+-":
            t = t[1:]
        return t.isdigit()

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for ch in texto:
            if ch.isalpha():
                base = ord("A") if ch.isupper() else ord("a")
                resultado += chr((ord(ch) - base + desplazamiento) % 26 + base)
            else:
                resultado += ch
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        if not subcadena:
            return []
        posiciones = []
        L = len(subcadena)
        for i in range(len(texto) - L + 1):
            if texto[i:i+L] == subcadena:
                posiciones.append(i)
        return posiciones
