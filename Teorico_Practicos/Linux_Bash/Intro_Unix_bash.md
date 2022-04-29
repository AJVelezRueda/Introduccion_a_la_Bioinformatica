# *Introducción al Command Line Interface*
> 🚨 WARNING: este tutorial asume que tenés un sistema operativo tipo _UNIX_, de no tenerlo te sugerimos instalar [Ubuntu](https://ubuntu.com/download/desktop) 
>
> Autores: Dra. Marcia A. Hasenahuer - Dra. Ana Julia Velez Rueda - Lic. Guillermo Benitez
>
> **LICENSE**: This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].
>
>[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


# Guias de Trabajo
* [1-GNU/Linux: historia, filosofía y terminología](#1-Historia)
* [2-Algunos términos básicos](#2-Terminos)
* [3-Usuarios y superusuario](#3-usuarios)
* [4-¿Qué es el shell y que es un terminal? ¿Por qué usar la línea de comandos? ](#4-shell)
* [5-Estructura general de los comandos](#5-comandos)
* [6-Atajos](#6-atajos)
* [7-¿Quién soy? ¿Dónde estoy? ¿Dónde está ...?](#7-pwd)
* [8-Navegar y administrar archivos, carpetas y sus permisos](#8-ls)
* [9-Instalar programas desde repositorios](#9-sudo)
* [10-GREP - Búsqueda de patrones](#10-GREP)
* [11-Integración con Bash](#11bash)


[1-GNU/Linux: historia, filosofía y terminología](#1-Historia)
Usas GNU/Linux todos los días, lo sepas o no. Más de 850.000 teléfonos Android que ejecutan Linux se activan todos los días. Nueve de cada diez supercomputadoras del mundo ejecutan Linux. Los servidores de Google, Twitter, Facebook y Amazon funcionan con Linux.

GNU/Linux, también conocido como Linux, es un sistema operativo (SO) con ciertas características que lo diferencian de otras alternativas comerciales, como Windows e IOS. La más importante de todas ellas es que se compone de código abierto con licencia GNU GPL (General Public License), es decir, el desarrollo se hace abiertamente y cualquiera puede tomar el código, modificarlo y distribuirlo.

Todo comenzó en 1983, fecha en que Richard Stallman y la FSF (Free Software Foundation) iniciaron el Proyecto GNU. La sigla GNU significa «ñu» en inglés y es un acrónimo recursivo de «¡GNU No es Unix!». El SO GNU se desarrolló como una alternativa libre y abierta a Unix, (otro sistema operativo desarrollado por la AT&T, Inc. American Telephone & Telegraph)  con el objetivo de brindar una opción completamente compuesta  de software libre.
Más tarde, en 1991 Linus Torvalds escribió el núcleo del sistema operativo Linux propiamente dicho, empleando componentes del SO GNU y siguiendo la filosofía libre del proyecto GNU. El nombre Linux proviene de la conjunción Linus + Unix

A diferencia de otros sistemas operativos como Windows o IOS, Linux es mejorado y mantenido por una red de desarrolladores de todo el mundo que colaboran a través de Internet, con Linus Torvalds a la cabeza. Esto es GNU/Linux, el proyecto de desarrollo colaborativo más grande en la historia de la informática, donde colaboran miles de personas con el objetivo de mejorar un sistema operativo, y con la posibilidad de elegir entre distribuciones diferentes de un mismo SO que se adaptan a todo tipo de usuario, y donde cualquiera puede acceder, modificar y distribuir el código.


[2-Algunos términos básicos](#2-Terminos)

**Kernel**

El kernel o núcleo de un sistema operativo es la pieza de software o código fuente más importante del sistema. Es el encargado de que todo el sistema funcione, de administrar el orden en que corren los procesos, de facilitar la comunicación entre  los programas que tenemos instalados y el hardware de nuestra computadora.

**Distribuciones**

Una distribución o distro, es la colección de programas combinados con el Linux Kernel que en conjunto define un sistema operativo basado en Linux. Existen familias de distros como Debian y Fedora, y a su vez sub distros, como Ubuntu y Linux Mint que están basados en Debian. El Linux Kernel es el mismo, las diferencias están mayormente relacionadas a los programas que incluyen, las distintos repositorios de donde obtenerlos y cómo instalarlos, el diseño de la interfaz gráfica, y el target de usuarios.


[3-Usuarios y superusuario](#3-usuarios)

Los sistemas Linux permiten que múltiples usuarios tengan cuentas y estén usando la computadora al mismo momento. El usuario root en particular, también conocido como superusuario o administrador, es una cuenta de usuario especial en Linux que se utiliza para la administración del sistema. Es el usuario más privilegiado y tiene acceso a todos los comandos y archivos. root puede hacer muchas cosas que un usuario normal no puede hacer, como instalar nuevo software, cambiar la propiedad de los archivos y administrar otras cuentas de usuario.

No se recomienda utilizar root para tareas ordinarias, como navegar por la web, escribir textos. Es recomendable crear una cuenta de usuario normal para tales tareas. Si se necesitan permisos de root, se puede anteponer el comando sudo al correspondiente comando, o loguearse como tal en una terminal empleando sudo -i


[4-¿Qué es el shell y que es un terminal? ¿Por qué usar la línea de comandos? ](#4-shell)
Dicho de forma simple, el **shell** es un programa que captura comandos ingresados por teclado en una **interfaz de línea de comandos (CLIs)**  y se los da al sistema operativo para que los ejecute. En otros tiempos, esta era la única forma de comunicación con los sistemas operativos basados en Unix, como Linux. Hoy en dia tenemos interfaces gráficas de usuario (GUIs) que complementan a las CLIs


En la mayoría de los sistemas Linux, un programa llamado **bash** (que significa Bourne Again SHell, una versión mejorada del programa shell original de Unix, **sh**, escrito por Steve Bourne) actúa como programa shell. Además de bash, hay otros programas de shell disponibles para sistemas Linux. Estos incluyen: ksh, tcsh y zsh
Una terminal, o terminal emulator, es un programa que abre una ventana donde te permite interaccionar con el shell a través de la CLIs. Hay varias terminales que pueden usarse en  Linux: gnome-terminal (default en Ubuntu), konsole, xterm, rxvt, kvt, nxterm, and eterm.

Una **terminal**, o terminal emulator, es un programa que abre una ventana donde te permite interaccionar con el shell a través de la CLIs. Hay varias terminales que pueden usarse en  Linux: gnome-terminal (default en Ubuntu), konsole, xterm, rxvt, kvt, nxterm, and eterm.


    Las GUIs son muy útiles para ciertas tareas,  pero poco prácticas para otras. Las principales ventaja de usar la línea de comandos:
        - Te permite realizar tareas más rápido
        
        - Los comandos básicos de Linux son (casi) universales a todas las distribuciones

        - Muchas herramientas Bioinformáticas están desarrolladas para ser usadas por línea de comandos y ser incorporadas en scripts de bash, y por lo tanto poder ser corridas en clusters de computadoras que, por lo general, suelen usar sistemas Linux

        - “All is in commandland”. Linux es un libro abierto respecto a su código y a los comandos que un usuario puede usar. Hay miles de recursos y foros en internet donde podes aprender y pedir ayuda: por lo general, a alguien ya le sucedió

**¡Abrí una terminal con la combinación de teclas CTRL+ALT+T, y empecemos!**


[5-Estructura general de los comandos](#5-comandos)

Los comandos en Linux suelen tener opciones y aceptar argumentos. Las opciones funcionan como switches para ajustar parámetros y los argumentos suelen ser archivos de texto o flujos de información sobre los cuales operar. 

Si bien tanto las opciones como los argumentos pueden ser opcionales para algunos comandos, la sintaxis general de un comando podría simplificarse a:


```bash
$ comando [opción(es)] argumento(s)
    |           |           |
¿Qué hacer? ¿Cómo hacerlo? ¿Sobre qué aplicarlo?
```

Por ejemplo, el comando para listar archivos y carpetas es ls, y dependiendo de como lo empleemos, listara distintas cosas:


Contenido de la carpeta actual:
```bash
$ ls 
```


Contenido de mi carpeta home:
```bash
$ ls /home/miusuario/
```

Contenido de mi home, mostrando un poco más de información y organizada en líneas: 

```bash
$ ls -ltah /home/miusuario/
```

[6-Atajos](#6-atajos)
- Primero que nada, algunos tips y shortcuts para tener siempre en cuenta a lo largo de este tutorial, y para el uso de Linux en general: **A ≠ a, case always matters!**

- Evita usar caracteres especiales (espacios, “;”, “,”, “\”,”/”, etc)  en los nombres de archivos y escritorios, esto complica manipularlos usando la línea de comandos. Usa caracteres alfanuméricos (a-z, 0-9), puntos (“.”), guiones (“-”,”_”), adicionalmente, usar minúsculas ayuda a evitar errores de tipeo.

- Usar una  extensión en nombres de archivos no es obligatorio para el sistema, pero te ayudará a reconocer más fácilmente el tipo de tus archivos.

- Ahorra tiempo y esfuerzo: navegar comandos previos con flechas (↑↓), autocompletar nombres de archivos y comandos con TAB,  listar el historial de comandos con:
```bash
$ history
```
- Shortcut para abrir una terminal: **CTRL+ALT+T** , para cerrarla: **CTRL+D**

- Si un programa se cuelga en la terminal, o simplemente quieres detenerlo, usa CTRL+C

- Si la interfaz gráfica deja de funcionar correctamente usa ALT+F2 -> r -> ENTER 

- Terminal muy cargada de texto? despejala con:

```bash
$ clear
```

- Para obtener ayuda sobre las opciones de un comando, usa --help o  man para leer su manual completo (avanza con barra espaciadora, exit con q). Ejemplo:

```bash
$ history --help
$ man history
```

PS: Nota cómo cambia el orden en este caso. ¿Se te ocurre por qué?

[7-¿Quién soy? ¿Dónde estoy? ¿Dónde está ...?](#7-pwd)

Mi nombre de usuario en el sistema (Linux es multiusuario):

```bash
$ whoami
ana
```
El nombre de mi computadora:

```bash
$ hostname
Ana
```

Información sobre mi sistema:

```bash
$ uname -a
Linux absolem 5.11.0-27-generic #29~20.04.1-Ubuntu SMP Wed Aug 11 15:58:17 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

En que carpeta estoy parado:

```bash
$ pwd
/home/ana/Docencia/LINUX-workshop
```
Donde esta instalado el ejecutable de un programa, en este caso wget:

```bash
$ which wget 
/usr/bin/wget
```
Buscar en todo el sistema (/) archivos y carpetas que contengan la palabra ‘dataset’ :

```bash
$ find / -name *dataset*
/home/ana/PROGRAMAS/R-3.5.1/src/library/datasets
[…]
```


[8-Navegar y administrar archivos, carpetas y sus permisos](#8-ls)

#### **ls - listar contenido en una carpeta**

Como ya vimos en secciones anteriores, el comando ls sirve para listar el contenido de archivos y carpetas en la carpeta actual donde estemos parados:

```bash
$ ls -ltah /home/miusuario/
```

Estas son algunas de las opciones más frecuentes
-l: un elemento por línea, listando información de permisos
-t: ordenado por fecha de modificación
-a: mostrar todo sin ignorar archivos ocultos 
-h: tamaños de archivo “legibles para humanos”  
Y te permiten apreciar los permisos, autoría, tamaño y fecha de los archivos y carpetas 

```bash
$ ls -ltah /home/miusuario/
```
<pre>total 809M
drwxr-xr-x   10 ana  ana   28K abr 22 14:40  <font color="#34E2E2"><b>Descargas</b></font>
-rw-------    1 ana  ana     0 abr 21 08:11  .dbshell
drwxrwxr-x    1 ana  ana  1,1M abr 20 12:32  <font color="#34E2E2"><b>cavidb_workspace</b></font>
drwxrwxr-x   10 ana  ana  4,0K abr 20 09:56  <font color="#34E2E2"><b>CaviDB</b></font>
drwxr-xr-x    9 ana  ana   28K abr 13 14:29  <font color="#34E2E2"><b>Imágenes</b></font>
</pre>

> **Algunos significados**
> - = file
> d = directory
>rwx = Owner

> **Permissions**
> r = Readable / Lectura
> w = Writable / Escritura
> x = Executable / Ejecutable
> - = Denied / Denegado



#### **chmod - cambiar permisos de lectura, escritura, ejecución de archivos**

Cada archivo y carpeta en el sistema tiene asignados/denegados permisos de lectura (r), escritura (w) y ejecución (x) para el propietario (u), para un grupo al que pertenece (g) y para otros usuarios que no son parte de su grupo (o) 
El comando chmod se emplea para modificar estos permisos. 

Por ejemplo, el propietario y grupo estarán habilitados para ejecutar:
```bash
$ chmod ug+x archivo.txt
```

#### **mkdir - crear carpetas**

Permite crear carpetas, y también subcarpetas con al opción -p

```
$ mkdir  carpeta
$ mkdir -p carpeta/subcarpeta
```

#### **cd - cambiar localización de mi carpeta actual**

cd (change directory) permite movernos a otras localizaciones en el árbol de escritorios del SO, especificando una ruta hacia una carpeta

```
$ cd  /media/miusuario/
```


#### **touch - crear un archivo o cambiar su fecha de última modificación**

Si el archivo no existe, touch lo creara vacío. Si ya existe, solo cambiará su fecha de modificación:

```
$ touch archivo
$ ls -ltah archivo
```

<pre>-rw-rw-r-- 1 ana ana 37 abr 22 15:23 archivo.txt
</pre>

… luego de un par de minutos
```
$ touch archivo
$ ls -ltah archivo
```
<pre>-rw-rw-r-- 1 ana ana 37 abr 22 15:25 archivo.txt
</pre>

Existen otros programas que también pueden usarse para crear, acceder y modificar archivos, por ejemplo aquellos de uso por terminal: vi/vim, nano, Emacs, o con interfaz gráfica: gedit.

#### cat - mostrar el contenido de uno o más archivos
cat vuelca el contenido completo de un archivo en la terminal. Si más de un archivo se pasa por parámetro, concatenan sus líneas según el order en el comando

```
$ cat seq1.fasta seq2.fasta seq3.fasta
```


#### head - mostrar encabezado de las primeras N líneas de un archivo
head, por default, vuelca en la terminal las primeras 10 líneas de un archivo. El parámetro -n permite especificar otra cantidad.

```bash
$ head -n 7 /etc/ssh/ssh_config
```
Otra funcionalidad útil de head, es la de imprimir todo el archivo exceptuando las últimas n del final. Por ejemplo, para evitar las últimas 5 líneas:

```bash
$ head -n -5 /etc/ssh/ssh_config
```


#### tail - mostrar N líneas finales de un archivo
tail, por default, vuelca en la terminal las últimas 10 líneas de un archivo. El parámetro -n permite especificar otra cantidad, -f permite seguir el archivo a medida que nuevas líneas se imprimen en él. Útil para monitorear archivos que están siendo modificados por un programa

```bash
$ tail -n 7 /etc/ssh/ssh_config
```

Otra funcionalidad útil de tail, es la de imprimir solo a partir de una línea determinada hasta el final. Por ejemplo, para mostrar a partir de la línea 15 incluida:

```bash
$ tail -n +15 /etc/ssh/ssh_config
```

#### less - ver y navegar archivos, sin modificarlos

Puedes usar flechas  de teclado (↑↓) para subir y bajar, q para salir
```bash
$ less /etc/ssh/ssh_config
```

En este caso, para dejar de leer hay que apretar la tecla **q**.

#### **cut - extraer columnas de archivos**

Por default, cut asume que las columnas del archivo están separadas con tab. Emplea -d para especificar delimitador y -f para especificar columna(s) de interés a extraer


```bash
$ cut -d ',' -f 3,4  aac_coordinates.txt
```

#### wc - contar palabras, líneas, caracteres de un archivo

Por default, wc imprime número de líneas, palabras y caracteres (en ese orden) de un archivo. Especificando -l, -w o -c, obtendremos estos valores indivicualmente

```bash
$ wc aac_coordinates.txt
$ wc -l aac_coordinates.txt
```

Podemos concatenar las acciones de distintos comandos usando el pipe, `|`, el cual toma la salida o el resultado de las acciones que hay en el lado izquierdo y lo usa de entrada para el lado derecho.

```bash
cat archivo1 archivo2 | wc -l
```

Aquí en lugar de mostrarse la concatenación de _archivo1_ y _archivo2_ en la pantalla esto pasa a ser la entrada del comando `wc` y con la opción `-l` obtiene la cantidad de líneas, lo cual es lo que se termina mostrando en la pantalla.

>
> 🧗🏾‍♀️Desafío I: Concatená los archivos seq1.fasta seq2.fasta seq3.fasta y contá cuantas lineas tiene la resultante
>
> 🧗🏾‍♀️Desafío I: Concatená los archivos seq1.fasta seq2.fasta seq3.fasta y contá cuantas lineas tiene y guardá el valor resultante en un archivo de nombre conteo_de_lineas.txt
>



#### Wget - descarga de contenido desde servidores

**Wget** es una herramienta libre que permite la descarga de contenidos desde servidores web de una forma simple. 
```bash
$ wget http://unaURLcualquiera.zip
```

Tambien podríamos limitar la velocidad de descarga haciendo:
```bash
wget --limit-rate=500k http://unaURLcualquiera.zip
```
#### `rm` - para eliminar archivos. 

Se puede usar con la opción `-r` para eliminar una carpeta

	```bash
	rm archivo
	rm -r directorio
	```

[9-Instalar programas desde repositorios](#9-sudo)
Un repositorio de Linux es una ubicación de almacenamiento en un servidor remoto, desde la cual tu SO Linux descarga e instala actualizaciones y aplicaciones. 

_apt_ es una utilidad de línea de comandos para instalar, actualizar, eliminar y administrar paquetes *.deb (programas) en Ubuntu, Debian y algunas distribuciones de Linux relacionadas. La mayoría de los comandos de apt deben ejecutarse como un usuario root, con privilegios de sudo.

Actualiza la lista de paquetes disponibles, cada vez que quieras instalar un nuevo programa desde un repositorio de Linux:

```bash
$ sudo apt update 
```

Instala nuevos paquetes. Esto también instalará cualquier otro paquete dependencia necesario.
```bash
$ sudo apt install package1 package2
```

Periódicamente, actualiza tus programas a su versión mas nueva:
```bash
$ sudo apt upgrade package1
$ sudo apt upgrade
```

Para remover paquetes, es mejor “purgar” y eliminar cualquier dependencia que no sea necesaria para otros programas:

```bash
$ sudo apt purge package1
```

[10-GREP - Búsqueda de patrones](#10-GREP)

**grep** (Global Regular Expression Print) se emplea para encontrar líneas en un archivo de texto que contengan un patrón específico. Los patrones a buscar se describen con expresiones regulares (ER, regex). Estas pueden ser simples cadenas de caracteres o combinaciones con ciertos caracteres especiales o reservados, que permiten describir patrones de texto un poco más complejos.

**zgrep** puede emplearse sobre archivos de texto comprimidos.

```bash
Sintaxis: grep [opciones] ‘patrón’ [archivo(s)]
```

| Opción | Descripción|
|-------------	|----------|
|-i | Búsqueda insensible a mayúscula/minúscula|
|-c | Imprimir cantidad de líneas con matches|
|-l | Listar los archivos con matches, pero no las líneas matcheadas|
|-L | Listar archivos sin matches|
|-v | Imprimir líneas que no coinciden con el patrón|
|-o | Imprimir solo las palabras que coincidieron con el patrón, no las líneas completas|
|-E | interpretar expresiones regulares extendidas: los caracteres ?, +,  {, }, |, (, ) serán interpretados como caracteres con una función especial (meta caracteres), y no será necesario “escaparlos” con ‘\’ |


Ejemplos de expresiones regulares básicas para un Match literal, de un carácter o una cadena de caracteres simple:

- Contar el número de secuencias en un archivo multi fasta  (el encabezado de cada secuencia comienza con ‘>’):

```bash
$ grep -c '>' multiseq.fasta
```

- Obtener los encabezados fasta de las secuencias que contengan el string ‘Homo sapiens’ en un archivo multi fasta:
```bash
$ grep ‘Homo sapiens’ multiseq.fasta
```

- Extender esta búsqueda a todos los archivos *.fasta de mi localización actual, y capturar en otro archivo solamente el nombre de los archivos que contengan el patron:

```bash
$ grep -l ‘Homo sapiens’ *.fasta > files_with_human_seqs.txt
```

El signo mayor nos permite redireccionar la salida de la operación hacia el archivo _files_with_human_seqs.txt_

>
> 🧗🏾‍♀️Desafío: Probá ejecutar la linea anterior pero usando >> en lugar de > ¿Qué pasa?¿Qué hace >> ?
>

[11-Integración con Bash](#-11bash)

Ahora que hemos visto algunos pocos comandos, y sabemos lo útiles que pueden ser, la pregunta es... ¿cómo recordar entre los miles que hay disponibles aquellos que necesitamos para hacer una tarea en particular? No se puede, por eso escribimos scripts de shell. 

Un script no es más que una serie de comandos de terminal shell que se organizan en un archivo. Al ejecutar este archivo el shell lee, interpreta y ejecuta los comandos, como si estos se hubiesen ingresado por la consola de línea de comandos.

El script más simple que puedas hacer puede ser simplemente un one-liner que no quieras volver a pensar y repetir para volver a realizar una serie de procesos! Pero también puede volverse más complejo si se suman elementos de control como condiciones y bucles (if, for, while). Los scripts también pueden ser flexibles y aceptar parámetros de entrada, dependiendo de distintos escenarios de uso.


Para escribir un script de comandos, necesitamos usar un editor de texto. De los más comúnmente usados podemos mencionar de uso por terminal: vi/vim, nano, Emacs, con interfaz gráfica: gedit

#### Estructura recomendada para un script de bash 
La Figura 6 muestra una estructura recomendada, pero no mandatoria! para organizar un script de shell. La línea de shebang (“#!”) es importante! y debe ser la primera del archivo, especifica que intérprete debe ser invocado (en este caso bash). Cada línea empezando con ‘#’  es un comentario (excepto el shebang)
Es recomendable guardar el archivo con una extensión ‘.sh’, y que sea en la misma carpeta con los archivos a procesar.

Para poder correr nuestros scripts, hay que darles primero permiso de ejecución y luego simplemente ejecutar anteponiendo ‘./’:

```bash
$ chmod +x script.sh
$ ./script.sh
```


### Estructuras de control básicas
Las estructuras de control permiten modificar el flujo de ejecución de las instrucciones de un programa, permitiendo tomar decisiones o hacer ciclos hasta/mientras que se cumpla una condición. Sólo mencionamos aquí las estructuras de control más simples: if-then-else, for, while y until, pero primero hablaremos sobre cómo hacer las comparaciones.

**Operadores de comparación**: 

Sintaxis ejemplo | Significado
|-------------	|----------|
|if [ "$a" -eq "$b" ] | igual a|
|if [ "$a" -ne "$b" ] | distinto de|
|if [ "$a" -gt "$b" ] | mayor que|
|if [ "$a" -ge "$b" ] | mayor o igual que|
|if [ "$a" -lt "$b" ] | menor que|
|if [ "$a" -le "$b" ] | menor o igual que|


**Comparaciones para carpetas y archivos**:

|Sintaxis ejemplo | Significado|
|-------------	|----------|
|if [ -e "/etc/passwd" ] | el archivo existe|
|if [ -f "/etc/passwd" ] | es un archivo regular archivo (no un directorio)|
|if [ -s "/etc/passwd" ] | archivo is not zero size|
|if [ -d "/etc/" ] | es un directorio|
|if [ -r "/etc/passwd" ] | el archivo tiene permisos de lectura|
|if [ -O "/etc/passwd" ] | sos el dueño del archivo|

**if - then - else: ejecutará algo dependiendo de que se cumpla cierta condición**

Comprobar existencia de las carpetas ./sequence_folder o ./sequences
Imprimir las secuencias fasta si alguna de ellas existe:

```bash
if [ -e ./sequence_folder ]
then
   ls -l ./sequence_folder/*.fasta

elif [ -e ./sequences ]
then
   ls -l ./sequences/*.fasta
else
   echo “sequence folders don’t exist!“
fi
```

**for loop: ciclara a través de los elementos de una lista, y ejecuta la línea de comandos**
Listar archivos *.fasta en ./sequence_folder y ciclar a través de ellos, imprimiendo su nombre y obteniendo su cantidad de secuencias:

```bash
for FILE in `ls ./sequence_folder/*.fasta`
do
    echo " * $FILE"
    grep -c '>' $FILE
done
```
## Propuesta de ejercicio integrador

Te proponemos que sigas los ejercicios que están en este repositorio, que te servirán para integrar lo visto en esta guía:
https://github.com/AJVelezRueda/bashathon
Y seguí las instrucciones en el repo


Tip: para descargar el zip con todos los archivos, pode usar este link:
https://github.com/AJVelezRueda/bashathon/archive/refs/heads/master.zip
Y los comandos: wget y unzip

## Algunos recursos para ir más allá

Una especie de pocket book, pero online http://linuxcommand.org/index.php
Linux commands cheat-sheet: https://files.fosswire.com/2007/08/fwunixref.pdf
Regex cheatsheet https://cheatography.com/davechild/cheat-sheets/regular-expressions/pdf/
grep cheatsheet https://cheatography.com/tme520/cheat-sheets/grep-english/pdf/
One-liners utiles para Bioinformatica:  https://github.com/stephenturner/oneliners