# La vida en tres dimensiones
> Autores: Dra. Ana Julia Velez Rueda, Niolás Palopoli
>
> **LICENSE**: This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].
>
>[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

## Un problema estructural

Un gran número de proteínas requieren una determinada estructura terciaria (como llamamos a su estructura tridimensional) para cumplir con sus funciones biológicas. Por ejemplo, la ubiquitina (ubiquitin en inglés) es una proteína pequeña que ha sido encontrada en casi todas las células eucariotas (de allí viene su nombre: ubiquo significa omnipresente). Esta proteína es la encargada de la marcación química de las proteínas que ya no son necesarias, para que sean reconocidas y destruidas por otras proteínas. 

>**PARA PENSAR** 🤔:¿Por qué una célula querría destruir sus propias proteínas?

Descubramos un poco más acerca de la estructura terciaria de la ubiquitina. Para esto ingresemos al sitio web del Banco de Datos de Proteínas (Protein Data Bank, o PDB) (https://www.rcsb.org/). Esta página web corresponde a una de las bases de datos más utilizadas en la bioinformática, donde se encuentran almacenadas todas las estructuras de macromoléculas biológicas obtenidas hasta el momento. Las estructuras se almacenan en forma de archivos que contienen las coordenadas en el espacio, en ejes imaginarios X, Z e Y, de todos los átomos de una molécula dada. Estas coordenadas pueden ser interpretadas por algunos programas gráficos para mostrar de forma tridimensional cómo se vería, por ejemplo, una proteína en una célula o en una membrana.

En el cuadro de búsqueda de la PDB, ingresemos el código identificador de la ubiquitina humana: 1UBQ.

![PBD_database](pdb_home_page.png)


La página correspondiente a la 1UBQ contiene toda la información disponible sobre el experimento en el que se determinó la estructura terciaria de la ubiquitina humana. Incluye información adicional sobre la proteína extraída de otras bases de datos, que permiten conocer más sobre su secuencia, otras proteínas similares, etc. La primera pantalla que vemos es un resumen de la información estructural (Structure Summary).

>**PARA PENSAR** 🤔:¿Qué información nos provee esta página?
>**PARA PENSAR** 🤔:¿Cómo se determinó la estructura de esta proteína?
>A la izquierda vemos una representación de la estructura de ubiquitina. ¿Qué significan las cintas, las flechas y las regiones angostas?
>**PARA PENSAR** 🤔:¿Representa esa imagen a la realidad del sistema biológico?
>**PARA PENSAR** 🤔:La estructura 1UBQ fue “refinada a una resolución de 1.8 Angstroms”. Éste es el error asociado al experimento: mientras mayor es la resolución, menor es la certeza al determinar la posición de cada átomo ¿Cuál es la utilidad y los condicionamientos de usar un modelo científico que sabemos inexacto?

Exploremos la pestaña de visualización tridimensional (3D View). Con el mouse podemos rotar, acercar y desplazar a la molécula. El menú de la derecha nos permite cambiar el modo de representación. 
En la pantalla principal vemos una representación de la estructura de ubiquitina. 

![PBD_database](pdb_protein_page.png)


>**PARA PENSAR** 🤔: ¿Qué significan las cintas, las flechas y las regiones angostas?
>**PARA PENSAR** 🤔:¿Qué diferencias y similitudes notamos respecto de la representación inicial? 
>**PARA PENSAR** 🤔: En el menú de la izquierda hay opciones de distintos tipos de representación y formas de colorear la estructura tridimensional. ¿Para qué podría ser útil visualizar lo mismo de distintas maneras?


Volviendo a la página principal de la estructura, podemos usar el menú derecho para descargar un archivo (Download files) con las coordenadas espaciales de cada átomo de esta proteína. En el pequeño menú que se despliegue, elegiremos descargar la estructura de la proteína en formato PDB (PDB format), el estándar para estructuras de biomoléculas. 

![PBD_database](pdb_protein_page.png)

>**PARA PENSAR** 🤔:¿Qué información esperaría encontrar como resultado un experimento destinado a determinar la estructura terciaria de una molécula biológica?

Podemos explorar el contenido del archivo que acabamos de descargar si lo observamos con un editor de texto. Haciendo clic con el botón derecho del mouse sobre el archivo descargado, usemos la opción Abrir con y seleccionemos el Bloc de Notas u otro editor de texto.

>**PARA PENSAR** 🤔: ¿En qué consiste un archivo PDB? 
>
>**PARA PENSAR** 🤔:Desplacémonos por el archivo hasta encontrar las líneas que comienzan con la palabra ATOM. ¿Qué tipo de información brinda esta sección?
>
>**PARA PENSAR** 🤔:¿Podríamos extraer de este archivo información sobre la estructura primaria de la proteína en cuestión? ¿Cómo se presenta dicha información y qué significa la representación? Desde el punto de vista computacional: ¿de qué tipo de dato se trata esta información?
>
>**PARA PENSAR** 🤔: ¿Considera que el formato PDB es útil para presentar los resultados del experimento?
>
>**PARA PENSAR** 🤔: Observamos que la información respeta cierta estructura interna. ¿Cuáles son los beneficios y las limitaciones de imponer una estructura para comunicar los resultados de un experimento? 
>
>Hemos visto que las proteínas tienen estructura tridimensional y hemos podido observar algunas características de las mismas. ¿Será igual con los ácidos nucléicos?
Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. Contanos sobre los procedimientos que puso Rosalind.


## Una solución en el bolsillo

Por supuesto, es difícil entender en qué consiste la estructura de una molécula simplemente mirando el contenido de un archivo PDB. Ya sabemos que existen formas de representar la información tridimensional en la computadora. Existen una multiplicidad de aplicaciones gratuitas que nos permita visualizar la estructura de una proteína y que nos permiten además explorar las subestructuras proteicas más en profundidad.

Como sabrás, las proteínas son las unidades funcionales, estructurales y evolutivas de las células. Sabemos desde los primeros trabajos realizados por Anfinsen, que **existe una fuerte relación entre estructura y función**, es decir que la actividad biológica de una proteína depende de la disposición espacial de su cadena polipeptídica. 

Las proteínas no son un ovillo, sino que la mayoría adopta una estructura dada en el espacio. Se definen cuatro niveles distintos, conocidos como estructura primaria, secundaria, terciaria, y cuaternaria, y, cada uno de ellos se constituye a partir del anterior. Hoy en día sabemos que aunque adopten una estructura definida, las proteínas no están quietas y que existen muchos plegamientos posibles que explican su funcionalidad.

En su superficie, las proteínas tienen forma de numerosas cavidades y protuberancias que crean microambientes únicos para la unión de ligandos o la catálisis. Y como las proteínas se mueven, las cavidades también tienen topologías dinámicas, con características que también podrán cambiar de una conformación a otra. 

La dinámica de estas cavidades es fundamental para comprender la función de las proteínas. 
Existen una gran variedad de softwares capaces de predecir la ubicación de estas subestructuras proteicas y sus propiedades. Y esta información combinada con la información evolutiva y secuencial, puede ser de gran utilidad en campos de aplicación de lo más diversos, desde el diseño de fármacos, hasta el desarrollo de alimentos.

¡Vamos a adentrarnos en la anatomía de las proteínas!

## El futuro está aquí 📍

El estudio estructural de proteínas nos proporciona múltiples campos de aplicación, por ejemplo uno de los más explorados en la actualidad es el diseño racional de fármacos. Si se conoce la base biológica de una enfermedad, es decir se conocen las moléculas implicadas, es posible diseñar medicamentos que interactúen con la molécula responsable, de tal forma que la modifique y se modifique el cuadro patológico. En otras palabras, el diseño racional de fármacos consiste en la aplicación del conocimiento biológico y estructural de los receptores (proteínas involucradas en una dada enfermedad) para diseñar moléculas que interactúen sólo con estos… dentro de lo posible!

Un caso interesante es el [EGFR](https://www.uniprot.org/uniprotkb/P00533/entry) es uno de los principales marcadores de cáncer de pulmón. Para estudiar esta proteína, utilizaremos [CaviDB](https://cavidb.org),  una base de datos en línea gratuita que provee información sobre las cavidades proteicas y sus propiedades. 
Sabemos que la estructura 1M14 se corresponde con un confórmero activo, es decir una estructura con actividad, mientras que la estructura 3W32 se corresponde con una conformación inactiva. 

> 
>🧗🏻‍♀️DESAFÍO I: Compará el sitio activo de ambos confórmeros (posición 837) así como también los tamaños de los pockets. ¿Qué observás?
> 

Veamos ahora el ejemplo de la proteína Acetil-CoA sintetasa de humano, involucrada en cáncer de mamas. Como bien sabemos para que una droga pueda unirse a la proteína y modificar su función debe tener dónde hacerlo. 

> 
>🧗🏻‍♀️DESAFÍO II: Investigá la proteína usando la base de datos [Uniprot](https://www.uniprot.org/) y anotá los sitios relevantes biológicamente
>
>🧗🏻‍♀️DESAFÍO III: Tomando como base la estructura PDB 3GPC, estudiá sus túneles cavidades ¿Encontrás algúna/s cavidad/es en la proteína donde pueda unirse algún fármaco? ¿Qué residuos se encuentran en dicha cavidad?
>