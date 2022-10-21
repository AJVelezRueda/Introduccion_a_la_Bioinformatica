
En resumen

**Los parámetros de match son:**

1. x - Sin parámetros. Los caracteres idénticos tienen una puntuación de 1, de lo contrario 0

2. m: una puntuación de match es la puntuación de caracteres idénticos; de lo contrario, la puntuación no coincide. Palabras clave: match, mismatch

3. d - Un diccionario devuelve la puntuación de cualquier par de caracteres. Palabra clave: match_dict

4. c - Un función callback que devuelve puntuaciones. Palabra clave: match_fn

**Los parámetros de penalización por gap son:**

1. x - Sin penalizaciones por hueco

2. s - Mismas penalizaciones de espacio abierto y extendido para ambas secuencias. Palabras clave: abrir, extender

3. d - Las secuencias tienen diferentes penalizaciones de espacios abiertos y extendidos. Palabras clave: abrirA, extenderA, abrirB, extenderB

4. c - Una función de devolución de llamada devuelve las penalizaciones de brecha. Palabras clave: gap_A_fn, gap_B_fn
