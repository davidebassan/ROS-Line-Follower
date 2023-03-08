import random

# Definizione dei tipi di mattonelle
STRAIGHT = "S"
LEFT_CURVE = "L"
RIGHT_CURVE = "R"
CROSSROADS = "X"

# Definizione delle rotazioni delle mattonelle
ROTATIONS = {
    STRAIGHT: [0, 90, 180, 270],
    LEFT_CURVE: [0, 180],
    RIGHT_CURVE: [0, 180],
    CROSSROADS: [0]
}

# Definizione delle mattonelle
TILES = {
    STRAIGHT: ["|", "-"],
    LEFT_CURVE: ["L", "J"],
    RIGHT_CURVE: ["J", "L"],
    CROSSROADS: ["+", "+"]
}

# Funzione per generare un percorso
def generate_path(length):
    # Inizializzazione del percorso
    path = []
    # Generazione casuale della prima mattonella (senza rotazione)
    first_tile_type = random.choice([STRAIGHT, LEFT_CURVE, RIGHT_CURVE])
    first_tile_rotation = 0
    first_tile = (first_tile_type, first_tile_rotation)
    path.append(first_tile)
    # Generazione del resto del percorso
    for i in range(length-1):
        # Recupero l'ultima mattonella del percorso
        last_tile = path[-1]
        # Scelgo la mattonella successiva in modo casuale (senza rotazione)
        next_tile_type = random.choice([STRAIGHT, LEFT_CURVE, RIGHT_CURVE, CROSSROADS])
        next_tile_rotation = random.choice(ROTATIONS[next_tile_type])
        next_tile = (next_tile_type, next_tile_rotation)
        # Controllo che la nuova mattonella sia compatibile con quella precedente
        if not is_compatible(last_tile, next_tile):
            # Se la nuova mattonella non è compatibile, la ruoto finché non lo diventa
            while not is_compatible(last_tile, next_tile):
                next_tile_rotation = (next_tile_rotation + 90) % 360
                next_tile = (next_tile_type, next_tile_rotation)
        # Aggiungo la nuova mattonella al percorso
        path.append(next_tile)
    # Aggiungo la mattonella finale (dritta senza rotazione)
    last_tile = path[-1]
    next_tile_type = STRAIGHT
    next_tile_rotation = 0
    next_tile = (next_tile_type, next_tile_rotation)
    if not is_compatible(last_tile, next_tile):
        # Se la nuova mattonella non è compatibile, la ruoto finché non lo diventa
        while not is_compatible(last_tile, next_tile):
            next_tile_rotation = (next_tile_rotation + 90) % 360
            next_tile = (next_tile_type, next_tile_rotation)
    path.append(next_tile)
    return path

# Funzione per verificare la compatibilità tra due mattonelle
def is_compatible(tile1, tile2):
    type1, rotation1 = tile1
    type2, rotation2 = tile2
    # Controllo la compatibilità tra le mattonelle basandosi sulla loro rotazione
    if type1 == STRAIGHT and type2 == STRAIGHT:
        if rotation1 in [0, 180] and rotation2 in [0, 180]:
            return True
    elif type1 == STRAIGHT and type2 in [LEFT_CURVE, RIGHT_CURVE]:
        if rotation1 in [0, 180] and rotation2 in [0, 180]:
            return True
    elif type1 in [LEFT_CURVE, RIGHT_CURVE] and type2 == STRAIGHT:
        if rotation1 in [0, 180] and rotation2 in [0, 180]:
            return True
    elif type1 in [LEFT_CURVE, RIGHT_CURVE] and type2 in [LEFT_CURVE, RIGHT_CURVE]:
        if (rotation1 + 180) % 360 == rotation2:
            return True
    elif type1 == CROSSROADS and type2 == STRAIGHT:
        if rotation2 in [0, 180]:
            return True
    elif type1 == STRAIGHT and type2 == CROSSROADS:
        if rotation1 in [0, 180]:
            return True
    elif type1 == CROSSROADS and type2 in [LEFT_CURVE, RIGHT_CURVE]:
        if (rotation2 + 90) % 360 in ROTATIONS[type1]:
            return True
    elif type1 in [LEFT_CURVE, RIGHT_CURVE] and type2 == CROSSROADS:
        if (rotation1 + 90) % 360 in ROTATIONS[type2]:
            return True
    elif type1 == CROSSROADS and type2 == CROSSROADS:
        return True
    # Se non c'è compatibilità, restituisco False
    return False
