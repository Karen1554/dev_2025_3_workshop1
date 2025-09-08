import random

class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):

        jugador1 = str(jugador1).strip().lower()
        jugador2 = str(jugador2).strip().lower()
        validos = {"piedra", "papel", "tijera"}

        if jugador1 not in validos or jugador2 not in validos:
            return "invalid"

        if jugador1 == jugador2:
            return "empate"

        gana = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra",
        }
        return "jugador1" if gana[jugador1] == jugador2 else "jugador2"
    
    def adivinar_numero_pista(self, numero_secreto, intento):

        if intento == numero_secreto:
            return "correcto"
        return "muy alto" if intento > numero_secreto else "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):

        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                return fila[0]
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
                return tablero[0][col]
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
            return tablero[0][2]
        for fila in tablero:
            if " " in fila:
                return "continua"
        return "empate"

        
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):

        return [random.choice(colores_disponibles) for _ in range(longitud)]
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):

        for v in (desde_fila, desde_col, hasta_fila, hasta_col):
            if not (0 <= v <= 7):
                return False
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        if (desde_fila != hasta_fila) and (desde_col != hasta_col):
            return False
        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False
        else:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False

        return True