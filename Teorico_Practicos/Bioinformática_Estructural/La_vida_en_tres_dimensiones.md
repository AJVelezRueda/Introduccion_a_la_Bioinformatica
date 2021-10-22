# La vida en tres dimensiones
> Autora: Dra. Ana Julia Velez Rueda, Niolás Palopoli

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
>**PARA PENSAR** 🤔:Desplacémonos por el archivo hasta encontrar las líneas que comienzan con la palabra ATOM. ¿Qué tipo de información brinda esta sección?
>**PARA PENSAR** 🤔:¿Podríamos extraer de este archivo información sobre la estructura primaria de la proteína en cuestión? ¿Cómo se presenta dicha información y qué significa la representación? Desde el punto de vista computacional: ¿de qué tipo de dato se trata esta información?
>**PARA PENSAR** 🤔: ¿Considera que el formato PDB es útil para presentar los resultados del experimento?
>**PARA PENSAR** 🤔: Observamos que la información respeta cierta estructura interna. ¿Cuáles son los beneficios y las limitaciones de imponer una estructura para comunicar los resultados de un experimento? 


Hemos visto que las proteínas tienen estructura tridimensional y hemos podido observar algunas características de las mismas. ¿Será igual con los ácidos nucléicos?
Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. Contanos sobre los procedimientos que puso Rosalind.

Por supuesto, es difícil entender en qué consiste la estructura de una molécula simplemente mirando el contenido de un archivo PDB. Ya sabemos que existen formas de representar la información tridimensional en la computadora. Existen una multiplicidad de aplicaciones gratuitas que nos permita visualizar la estructura de una proteína. 
Te proponemos algunas aplicaciones para teléfonos celulares disponibles en las tiendas de nuestro teléfono (NDKmol - molecular viewer o RSCB PDB mobile) de sencilla instalación.