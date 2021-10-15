# Biopython
Esta biblioteca de python, como su nombre lo indica, está enfocada al tratamiento de datos biológicos. Como ya hemos visto existen muchos tratamientos que se le pueden hacer a los datos biológicos y en bioinformática es bastante común tener que usar distintas herramientas, muchas veces escritas en distintos lenguajes de programación, para realizar el pipeline que necesita para obtener los resultados, por lo que nos resulta bastante útil y cómodo poder hacerlos con una misma biblioteca.
La biblioteca en sí tiene muchísimas herramientas y utilidades que podrán encontrar en la [documentación](https://biopython.org/wiki/Documentation), dentro de las cuales no solo hay herramientas propias de la biblioteca, sino otras utilidades, tales como algoritmos de alineamiento o de búsqueda de secuencias, etc. Ahora vamos a ver algunas pocas herramientas que les van a resultar de utilidad para resolver el trabajo de hoy, pero recomendamos fuertemente que se vayan interiorizando en su uso.

Una cuestión que se puede llegar a dar cuando estamos estudiando alguna estructura es saber exactamente su secuencia, pero solo tenemos la estructura (en formato .pdb o .cif o .ent), por lo que para obtener las secuencias de cada cadena podemos hacer:

```python
from Bio import SeqIO
chains = {record.id: record.seq for record in SeqIO.parse("fa/pdb1fat.ent", "pdb-atom")}
```

De esta forma, en el diccionario `chains` vamos a tener todas las secuencias de las cadenas, siendo las claves del diccionario el nombre de la estructura en mayúscula, seguido de dos puntos y la cadena, por ejemplo: `1FAT:A`, `1FAT:B`, etc.
Pero, ¿qué pasa si no tenemos la estructura, sino solo el código pdb? Para esto vamos a tener que descargar la estructura:

```python
from Bio.PDB import *
pdbl = PDBList() 
pdbl.download_pdb_files(["1fat"], file_format="pdb") #Se puede bajar más de una estructura a la vez
```

Por último, algo que es muy útil es una herramienta para alinear secuencias de a pares (también hay para alineamientos múltiples). Como recordarán a grosso modo hay dos tipos de alineamientos, local o global, donde el primero se centra más en las regiones dónde hay match y el segundo toma en cuenta toda la longitud de las secuencias. Para realizar estos alieamientos tenemos:

```python
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
alignment = pairwise2.align.localxx(seq1, seq2)

```

De esta manera `alignment` es una lista con un solo elemento, el cual tiene la información del alineamiento:

```python
[Alignment(seq1='SNDIYFNFQRFNETNLILQRDASVSSSGQLRLTNLNXNGEPRVGSLGRAFYSAPIQIWDNTTGTVASFATSFTFNIQVPNNAGPADGLAFA
LVPVGSQPKDKGGFLGLFDGSNSNFHTVAVEFDTLYNKDWDPTERHIGIDVNSIRSIKTTRWDFVNGENAEVLITYDSSTNLLVASLVYPSQKTSFIV
SDTVDLKSVLPEWVSVGFSATTGINKGNVETNDVLSWSFASKLS', seq2='--DIYFNFQRFNETNLILQRDASVSSSGQLRLTNLNXNGEPRVGSLGRAFY
SAPIQIWDNTTGTVASFATSFTFNIQVPNNAGPADGLAFALVPVGSQPKDKGGFLGLFDGSNSNFHTVAVEFDTLYNKDWDPTERHIGIDVNSIRSIKTTRWDFVN
GENAEVLITYDSSTNLLVASLVYPSQKTSFIVSDTVDLKSVLPEWVSVGFSATTGINKGNVETNDVLSWSFASK--', score=229.0, start=2, end=231)]
```

De esta manera podemos acceder al score del alineamiento mediante:

```python
alignment[0].score
```

Este método, como decía más arriba, nos permite elegir si el alineamiento es local o global y además tenemos dos parámetros que hay que aclarar justo después del tipo de alineamiento. Uno de los parámetros tiene que ver con los valores de score que le damos a los matches y a los mismatches, y el otro tiene que ver con la penalidad que le damos a la apertura de gaps:

```
Primer parámetro:
código	descripción
x	El match vale 1, el mismatch vale 0
m	Podemos configurar el valor del match y del mismatch
d	Un diccionario con valores de score para cada par
c	Se llama a una función que calcula los score

Segundo parámetro:
código	descripción
x	No hay penalidad por los gaps
s	Podemos configurar el valor de la apertura y de la extensión de gaps
d	Las secuencias tienen distinto valor de apertura y extensión de gaps
c	Se llama a una función que calcula los score
```

Teniendo en cuenta estos parámetros, un ejemplo distinto al dado anteriormente puede ser:

```python
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
alignment = pairwise2.align.globalms(seq1, seq2, 2, -1, -0.5, -0.1)
```

Aquí tenemos que el match vale 2, el mismatch -1, abrir un gap -0.5 y extenderlo -0.1 (por gap extendido)

> Ahora integremos un poco los conocimientos que obtuvimos hasta ahora poniéndonos en rol. Imaginemos que estamos estudiando una proteína de una especie de la cual no se tiene mucha información, más allá de tener una estructura y se nos pide que averigüemos con qué proteínas de otras especies está relacionada, para lo cual tenemos una serie de secuencias que podemos utilizar. También sabemos que una buena forma de visualizar esta relación es usar un árbol, por lo que el resultado final de la investigación tiene que ser este árbol.
> Realizá los pasos necesarios para que, a partir de un código pdb (3erf) y de un archivo con una serie de secuencias (db.fa), se pueda inferir con qué especies está relacionada.