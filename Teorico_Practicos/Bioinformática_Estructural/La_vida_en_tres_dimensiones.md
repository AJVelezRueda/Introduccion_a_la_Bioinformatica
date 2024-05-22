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
>
>**PARA PENSAR** 🤔:¿Cómo se determinó la estructura de esta proteína?
>A la izquierda vemos una representación de la estructura de ubiquitina. ¿Qué significan las cintas, las flechas y las regiones angostas?
>
>**PARA PENSAR** 🤔:¿Representa esa imagen a la realidad del sistema biológico?
>
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

Un caso de estudio interesante es el [EGFR](https://www.uniprot.org/uniprotkb/P00533/entry) es uno de los principales marcadores de cáncer de pulmón. Para estudiar esta proteína, utilizaremos [CaviDB](https://cavidb.org),  una base de datos en línea gratuita que provee información sobre las cavidades proteicas y sus propiedades. 
Sabemos que la estructura 1M14 se corresponde con un confórmero activo, es decir una estructura con actividad, mientras que la estructura 3W32 se corresponde con una conformación inactiva. 

> 
>🧗🏻‍♀️DESAFÍO I: Compará el sitio activo de ambos confórmeros (posición 837) así como también los tamaños de los pockets. ¿Qué observás?
> 

Las variantes de AKR1C4 están asociadas con el trastorno bipolar y otros trastornos del estado de ánimo y la resistencia a los medicamentos. 

> 
>🧗🏻‍♀️DESAFÍO II: Investigá la proteína usando la base de datos [Uniprot](https://www.uniprot.org/) y anotá los sitios relevantes biológicamente
>
> 🧗🏻‍♀️DESAFÍO III :Analizá la estructura PDB [2FVLB](https://www.cavidb.org/chains/62b9e24ad5e54dd8755ed134?q=2FVLB)) ¿Cuántas cavidades fueron predichas para dicha estructura? ¿Hay alguna cavidad drogable? ¿Coincide con algún sitio de relavancia biológica?
> 
> 💡 Para investigar: Investigá en qué consiste el docking, en qué ideas basa su funcionamiento ¿Cómo podría aprovecharse este método para tratar esta patología?
>


## Sobre las huellas de la evolución

Las albúminas son las proteínas sanguíneas más abundantes en los mamíferos y tienen la propiedad principal de unirse y transportar muchos compuestos endógenos y exógenos, en su mayoría hidrofóbicos. La proteína es globular y está compuesta por tres dominios homólogos (I, II y III), cada uno de los cuales contiene dos subdominios  similares (A y B). Las albúminas se conservan a lo largo de los vertebrados y los miembros de esta familia muestran una gran diversidad estructural a pesar de la conservación de la secuencia global. Es decir que, aún cuando su función biológica no es enzimática, se ha probado su capacidad catalítica para varias reacciones. Curiosamente, aunque todas las albúminas de mamíferos comparten la función principal de transporte de ligandos a través de la sangre, difieren en el tipo de reacciones que pueden catalizar. Además, la capacidad catalítica de las albúminas en solventes orgánicos las convierte en candidatas para económicas para manipulación biotecnológica para su aprovechamiento en procesos industriales.

En particulas la albúmina de suero humano (HSA) es la proteína principal en el plasma, se une a múltiples ligandos y recientemente se la ha descripto como un transportador de fármacos muy importante. Esta proteína monocatenaria tiene varios sitios de unión de fármacos y ácidos grasos, sin embargo, la mayoría de los fse unen a los llamados Sitios I (Met 1 a Asn 111) y II (de Gln 196 a Pro 303). En particular, los residuos Lys 199, Arg 410, Tyr 411, Cys 34 y Lys 195 de HSA se describen como algunos de los más importantes, no solo para la unión de ligandos sino también para las actividades catalíticas descritas para esta proteína. 


Se sabe que la capacidade catalítica de una cavidad suele asociarse con algunas características estructurales de las mismas, como la presencia de aminoácidos activados (con pKas anormales) en ambientes mayoritariamente hidrofóbicos

> 🧗🏻‍♀️DESAFÍO IV: Investigá en [CaviDB](https://cavidb.org) la las características estructurales de la Albúmina Humana sobre la estructura `1AO6A`:
>
> - ¿Cuántas cavidades fueron predichas para dicha estructura? ¿Cuáles son las pricipales cavidades en tanto a tamaño de la proteína? ¿Existen cavidades que se solapen con los residuos descritos como relavantes para la actividad enzimática de la albúmina?
>
> - ¿Alguna de las cavidades catalíticamente activas se encuentran activadas? ¿Qué rangos de pKa se observan en dichas cavidades? 
>
> 🧗🏻‍♀️DESAFÍO V: Se sabe que en la albúmina bovina el sitio activo se encuentra corrido respecto del humano, aunque también involucra un aminoácido cargado (Lys 221). Investigá  en [CaviDB](https://cavidb.org) las características estructurales de la estructura de albúmina bovina `4JK4A` y compará las características de su sitio activo con las características del sitio activo de la albúmina humana (Lys 199)
>
> 💡 Para investigar: Leé más sobre los [hallazgos](https://www.sciencedirect.com/science/article/abs/pii/S0300908422000426) hechos por l@s investigadores/as de la Universidad Nacional de Quilmes sobre la evolución de albúminas y contrastalo con lo que pusidte observar.
>


## Un modelo a seguir

La bioiformática estructural de proteínas tienen como base la existencia de estructuras tridimencionales de las mismas. Las técnicas de rayos X y resonancia magnética nuclear proporcionan estructuras de alta resolución y son el punto de partida para los análisis bioinfomático de predicción funcional, estructural y de unión a ligandos (diseño de fármacos). Lamentablemente estas técnicas de caracterización estructural solo pueden realizarse sobre un número acotado de proteínas. Para una gran parte de la fracción de secuencias cuya estructura no se puede determinar experimentalmente, los métodos computacionales de predicción de estructura nos ofrecen la información necesaria para explicar gran parte de los aspectos funcionales que se pueden derivar del conocimiento estructural.

Los algoritmos de modelado molecular emplean varias estrategias:
 
1. Modelado ab initio:  Los métodos ab initio, por ejemplo, utilizan modelos matemáticos para predecir estructuras de proteínas basándose únicamente en la secuencia de aminoácidos, sin depender de estructuras conocidas. Emplea modelos basados ​tanto ​en la física, como dinámica molecular y simulaciones de Monte carlo, para predecir estructuras de proteínas. Estos modelos simulan interacciones entre átomos, lo que permite explorar el espacio conformacional de la proteína e identificar estructuras energéticamente favorables. Los métodos ab initio pueden ser costosos desde el punto de vista computacional y propensos a imprecisiones.

2. Modelado de homología: este típo de algoritmos aprovecha la similitud entre la proteína objetivo y las proteínas homólogas con estructuras conocidas para generar predicciones confiables. Basado en alineamientos secuenciales, los algoritmos pueden generar un modelo confiable tomando como base la estructura de la proteína plantilla. El modelado de homología es particularmente útil cuando existe una proteína estrechamente relacionada con una estructura conocida, ya que proporciona predicciones precisas.


3. Enfoques de aprendizaje automático: en los últimos años, los algoritmos de aprendizaje automático, como el aprendizaje profundo, han ganado importancia en la predicción de la estructura de las proteínas. Estos métodos aprovechan grandes conjuntos de datos de estructuras de proteínas conocidas para entrenar modelos que puedan predecir la estructura de nuevas proteínas. Al aprender de patrones y correlaciones en los datos, los algoritmos de aprendizaje automático pueden hacer predicciones precisas, incluso para proteínas con datos experimentales limitados.

## Un ejemplo de tantos

Predecir la estructura tridimensional que adoptará una proteína basándose únicamente en su secuencia de aminoácidos ha sido un problema de investigación abierto durante más de 50 años. En el año 2021, AlphaFold proporciona el primer método computacional para predecir estructuras de proteínas con precisión atómica incluso en casos donde no se conoce una estructura similar. 

A partir de la secuencia primaria de una proteína, AlphaFold2 utiliza una red neuronal para la predicción estructural de alta precisión (en la mayoría de los casos), la cual aumenta con el uso de estructuras homólogas. AlphaFold2 puede incluso predecir con alta precisión las cadenas laterales si el backbone es preciso. Se basa en una arquitectura de red que utiliza como inputs alineamientos múltiples de secuencias (MSAs) y una representación tridimencional de todos los pares de residuos de la secuencia. 


La principal métrica de confianza utilizada en AlphaFold es el test pLDDT (predicted local-distance difference test), que avalua las diferencias en las distancias Carbonos α (IDDT-Cα) y evalúa principalmente la correctitud del modelo a nivel local (estimando el error en distancias de un Cα con Cα vecinos en un rango de 15Å). La segunda métrica se denomina PAE (por Predicted Aligned error) y compara el error en la predicción de pares de residuos, esto es el error sobre el residuo y cuando las estructuras real y predicha son alineadas sobre el residuo x. 

Exiten distribuciones de este modelo que permiten hacer corridas nos cutomizables en [Colab (Google)](https://github.com/sokrypton/ColabFold/blob/main/README.md) que permiten [obtener](https://www.ccp4.ac.uk/schools/DLS-2023/course_material/20231130%20-%20Alphafold%20tutorial%20-%20Adam%20Simpkin.pdf):

   - *_template_domain_names.json Tiene los templados utilizados por AlphaFold2 si es que se usaron.

   -  Cite.bibtex Contiene todas las citas correspondientes a los papers relacionados.
   
    - Config.json Contiene todos los parámetros utilizados en la corrida.
   
    - *.a3m Alineamiento
   
    - *_coverage.png Gráfico de la cobertura del alineamiento
   
    - *_PAE.png Gráfico del PAE por pares de residuos para todos los modelos.
   
    - *_plddt.png Gráfico del plddt por posición
   
    - *_predicted_aligned_error_v1.json Tiene los valores de PAE para todos los pares de todos los modelos.
   
    - *_relaxed_*_model_*.pdb Son los 5 modelos generados.
   
    - *_relaxed_*_model_*.json Son el PAE y pLDDT de cada modelo que se pueden utilizar para graficar.

>
> 🧗🏻‍♀️DESAFÍO VI: En el campo sequence query ingresá la sigueinte sequencia [colab](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb#scrollTo=kOblAo-xetgx), usando num_relax = 1 y  template_mode = pdb100: 
>
>sp|P03129|VE7_HPV16 Protein E7 OS=Human papillomavirus type 16 OX=333760 GN=E7 PE=1 SV=1
MHGDTPTLHEYMLDLQPETTDLYCYEQLNDSSEEEDEIDGPAGQAEPDRAHYNIVTFCCKCDSTLRLCVQSTHVDIRTLEDLLMGTLGIVCPICSQKP
>
> La corrida se ejecuta desde el `Runtime --> Run all` 
> - ¿Qué el campo template_mode? ¿Qué opciones pueden ser utilizadas? 
> - ¿Qué regiones de la estructura resultante tienen una mayor confianza? Desarrollar un script que permita graficar los pLDDT por posición
>
> [Nota]: Este último ejercicio se basa en la guía de [Modelado por Homología II de la UNSAM](https://bioinformatica-iib.github.io/estructural/practicos/modelado_alphafold/#ejercicio-1-modelado-de-un-monomero-de-e7)
>