<img src="../../img/encabezado_git.png">

# Biopython

>
> **LICENSE**: This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].
>
>[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
> Autor: Guillermo I. Benítez y Dra. Ana Julia Velez Rueda


### Indice
* [1-Instalacion](#1-instalacion)
* [2-Alineamientos de Secuencias de a pares](#2-Alineamientos)



### [1-Instalacion](#1-instalacion)
Esta biblioteca de python, como su nombre lo indica, está enfocada al tratamiento de datos biológicos. Como ya hemos visto existen muchos tratamientos que se le pueden hacer a los datos biológicos y en bioinformática es bastante común tener que usar distintas herramientas, muchas veces escritas en distintos lenguajes de programación, para realizar el pipeline que necesita para obtener los resultados, por lo que nos resulta bastante útil y cómodo poder hacerlos con una misma biblioteca.

La biblioteca tiene muchísimas herramientas y utilidades que se detallan en la [documentación](https://biopython.org/wiki/Documentation). No solo hay herramientas propias de la biblioteca, sino otras utilidades, tales como algoritmos de alineamiento o de búsqueda de secuencias, etc. 

Para comenzar a usarlas, debes instalarla usando el instalador de `Python`:

```bash
pip install biopython
``` 

### [2-Alineamientos de Secuencias de a pares](#2-Alineamientos)

Los alineamientos de secuencias de a pares se utilizas para identificar regiones de similitud que pueden indicar relaciones funcionales, estructurales y/o evolutivas entre dos secuencias biológicas (proteína o ácido nucleico). Esta información nos permitirá luego realizar inferencias sobre los rasgos que se conservan entre las especies, o qué tan cerca genéticamente están las diferentes especies, cómo evolucionan las especies, etc.

Este tipo dde algoritmos utiliza programación dinámica para encontrar el alineamiento óptimoo entre las dos secuencias, puntuando en función de su similitud (cuán similares son) o distancia (cuán diferentes son), y luego evalúa la importancia de esta puntuación.

### Tipos de alineaciones por pares

- Alineamiento global:  encuentra la mejor alineamiento en toda la longitud de las 2 secuencias. Busca cuál es la máxima similitud entre las secuencias X e Y.

- Alineamiento local: encuentra las subsecuencias más similares entre las 2 secuencias. Busca la máxima similitud entre una subsecuencia de X y una subsecuencia de Y

La puntuación de coincidencia (match) indica la coincidencia entre un alineamiento de dos caracteres en las secuencias. Los caracteres altamente compatibles deben recibir puntajes positivos y los incompatibles deben recibir puntajes negativos o 0. Las penalizaciones por gaps deben ser negativas.

## Bio.pairwise2

Biopython incluye métodos de alineamentos de a pares incorporados: el módulo Bio.pairwise2 y la clase PairwiseAligner dentro del módulo Bio.Align. Ambos pueden realizar alineamientos globales y locales. 

Los nombres de las funciones de alineamientos en este módulo siguen la convención del tipo de alineamientos XY, donde el tipo de alineamientos es "global" o "local" y XY es un código de 2 caracteres que indica los parámetros que toma. El primer carácter X indica los parámetros para coincidencias y diferencias (matches y mistaches), y el segundo Y indica los parámetros para penalizaciones por gap.

#### Ejemplos de alineamientos usando Biopython
Tanto para alineamientos locales, como para globales usamos las mismas funciones, solo que en lugar de llamar global, llamamos local, y viceversa.

Veamos un ejemplo de alineamiento de dos secuencias de manera global:

```python
from Bio import pairwise2

alignments = pairwise2.align.globalxx("ACCGGT", "ACGT") 
## De este modo grficamos el alineamiento
for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))
```
En este caso el alineamiento `globalxx`, computa las coincidencia (matches) con un score=1, los mismatches con un score=0 y no le computa ningúna penalidad a los gaps.

Veamos el ejemplo del alineamiento `globalmx`:

```python
alignments = pairwise2.align.globalmx("ACCGGT", "ACGT", match=2, mismatch=-1) 

for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))
```

>🤔 ¿Cómo crees que computó en este caso los matches, mismatches y gaps?
>

Ahora observemos el resultado obtenido con el siguiente código:
```python
alignments = pairwise2.align.globalxs("ACCGGT", "ACGT", open=-2, extend=-1)

for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))
```
> 🤔 ¿Cómo crees que computó en este caso los matches, mismatches y gaps?
>

Como bien vimos en la teoría en el caso de las proteínas es necesario definir la similitud entre las secuencia teniendo utilizando matrices de siustitución, como por ejemplo `BLOSUM62`:

```python
from Bio.Align import substitution_matrices

matrix = substitution_matrices.load("BLOSUM62") 

alignments = pairwise2.align.globaldx("KEVLA", "EVL", match_dict=matrix)
for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))
```

> Desafío I: Averiguá como leer las secuencias para alinear desde un archivo fasta