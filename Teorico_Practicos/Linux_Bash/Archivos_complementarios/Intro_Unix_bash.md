# *Introducción al Command Line Interface*
> 🚨 WARNING: este tutorial asume que tenés un sistema operativo tipo _UNIX_, de no tenerlo te sugerimos instalar [Ubuntu](https://ubuntu.com/download/desktop) 
>
> Autores: Dra. Marcia A. Hasenahuer - Dra. Ana Julia Velez Rueda - Lic. Guillermo Benitez


# Guias de Trabajo
* [1-GNU/Linux: historia, filosofía y terminología](#1-Historia)
* [2-Algunos términos básicos](#2-Terminos)
* [3-Usuarios y superusuario](#3-usuarios)
* [4-¿Qué es el shell y que es un terminal? ¿Por qué usar la línea de comandos? ](#4-shell)
* [5-Estructura general de los comandos](#5-comandos)
* [6-Atajos](#6-atajos)
* [7-¿Quién soy? ¿Dónde estoy? ¿Dónde está ...?](#7-pwd)



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