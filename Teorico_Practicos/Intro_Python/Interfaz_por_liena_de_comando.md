>
> **LICENSE**: This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].
>
>[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


# *Introducción al Command Line Interface*
> Este material se basa en la introducción a CLI de [Fundamentos de informatica](https://github.com/AJVelezRueda/Fundamentos_de_informatica)
# *Introducción al Command Line Interface*
> 🚨 WARNING: este tutorial asume que tenés un sistema operativo tipo _UNIX_, de no tenerlo te sugerimos instalar [Ubuntu](https://ubuntu.com/download/desktop) 

# Guias de Trabajo
* [1. Interfaces de Línea de Comandos](#1-cli)
* [2. Invocacion de comandos](#2-ivocaciones)
* [3. Argumentos](#3-argumentos)
* [4. Argparse](#3-argparse)



## [1. Interfaces de Línea de Comandos](#1-cli)

Las **Interfaces de Línea de Comandos** (CLI) son un medio para exponer de manera sencilla el código que desarrollamos, para que pueda ser usado por otras personas y/o programas.  Los **intérpretes** (BASH, CASH, etc.) permiten la recepción de los comandos ingresados desde desde un repl y los evía al sistema operativo para su evaluación.

Un CLI tiene que ser capaz de recibir argumentos de tipo string, interpretarlos y, en caso de ser necesario, dialogar con el sistema operativo. Después de escribir un comando, el resultado que se obtiene  es información de texto o una acción específica realizada por la computadora. Por ello, la clave es escribir el comando correcto, un punto que suele considerarse como una desventaja en este diseño de interfaz de usuario por linea de comando y por lo que se suelen utilizar formas más atractivas de interfaz como GUI (Graphical User Interaction) para usuarios finales.

Los comandos básicos que vienen con el sistema operativo en general se puede dividir en dos categorías: los que manejan los procesos y los que manejan los archivos. 

## [2. Invocacion de comandos](#2-ivocaciones)

La invocación de un comando consiste en la palabra (comando) en sí y los argumentos y opciones, y determinan el nombre del ejecutable que se va a usar. Podemos decir en general que los comandos siguen la siguiente estructura:

```bash
$ comando [argumentos] 
```

La invocación de los comandos puede ser modificada en su comportamiento por defecto mediante los argumentos. 


## [3. Argumentos](#3-argumentos)

Es muy común encontrar en las CLI dos tipos de argumentos: 

- posicionales, que por extensión se los suele denominar argumentos a secas

- los nombrados, que se los conocen como flags u opciones. 

Veamos el ejemplo de `ls`, un comando disponible en casi todos los sistemas _UNIX_. Este comando sirve para listar archivos del directorio actual:

<pre><font color="#4E9A06"><b>ana@ana-X541UAK</b></font>:<font color="#3465A4"><b>/</b></font>$ ls
<font color="#06989A"><b>bin</b></font>    <font color="#3465A4"><b>dev</b></font>   <font color="#06989A"><b>lib</b></font>    <font color="#06989A"><b>libx32</b></font>      <font color="#3465A4"><b>mnt</b></font>   <font color="#3465A4"><b>root</b></font>  <font color="#3465A4"><b>snap</b></font>      <font color="#3465A4"><b>sys</b></font>  <font color="#3465A4"><b>var</b></font>
<font color="#3465A4"><b>boot</b></font>   <font color="#3465A4"><b>etc</b></font>   <font color="#06989A"><b>lib32</b></font>  <font color="#3465A4"><b>lost+found</b></font>  <font color="#3465A4"><b>opt</b></font>   <font color="#3465A4"><b>run</b></font>   <font color="#3465A4"><b>srv</b></font>       <span style="background-color:#4E9A06"><font color="#2E3436">tmp</font></span>
<font color="#3465A4"><b>cdrom</b></font>  <font color="#3465A4"><b>home</b></font>  <font color="#06989A"><b>lib64</b></font>  <font color="#3465A4"><b>media</b></font>       <font color="#3465A4"><b>proc</b></font>  <font color="#06989A"><b>sbin</b></font>  swapfile  <font color="#3465A4"><b>usr</b></font>
</pre>


Vamos qué sucede cuando hacemos `ls /usr`:
<pre><font color="#4E9A06"><b>ana@ana-X541UAK</b></font>:<font color="#3465A4"><b>/</b></font>$ ls /usr
<font color="#3465A4"><b>bin</b></font>    <font color="#3465A4"><b>include</b></font>  <font color="#3465A4"><b>lib32</b></font>  <font color="#3465A4"><b>libexec</b></font>  <font color="#3465A4"><b>local</b></font>  <font color="#3465A4"><b>share</b></font>
<font color="#3465A4"><b>games</b></font>  <font color="#3465A4"><b>lib</b></font>      <font color="#3465A4"><b>lib64</b></font>  <font color="#3465A4"><b>libx32</b></font>   <font color="#3465A4"><b>sbin</b></font>   <font color="#3465A4"><b>src</b></font>
</pre>



Como vemos en este caso, mediante el uso del argumento `/usr` podemos especificar el directorio cuyos archivos vamos a listar. Pero podemos controlar la salida de esta invocación, adicionando la opción la opción `-l` obtenemos el listado de archivos dentro del directorio usr:

<pre><font color="#4E9A06"><b>ana@ana-X541UAK</b></font>:<font color="#3465A4"><b>/</b></font>$ ls -l /usr
total 128
drwxr-xr-x   2 root root 57344 ago 31 08:03 <font color="#3465A4"><b>bin</b></font>
drwxr-xr-x   2 root root  4096 jul 31  2020 <font color="#3465A4"><b>games</b></font>
drwxr-xr-x  45 root root  4096 jul 10 20:47 <font color="#3465A4"><b>include</b></font>
drwxr-xr-x 124 root root  4096 jul 25 18:19 <font color="#3465A4"><b>lib</b></font>
drwxr-xr-x   2 root root  4096 jul 31  2020 <font color="#3465A4"><b>lib32</b></font>
drwxr-xr-x   2 root root  4096 feb 23  2021 <font color="#3465A4"><b>lib64</b></font>
drwxr-xr-x  12 root root  4096 feb 23  2021 <font color="#3465A4"><b>libexec</b></font>
drwxr-xr-x   2 root root  4096 jul 31  2020 <font color="#3465A4"><b>libx32</b></font>
drwxr-xr-x  10 root root  4096 jul 31  2020 <font color="#3465A4"><b>local</b></font>
drwxr-xr-x   2 root root 20480 jul 25 18:19 <font color="#3465A4"><b>sbin</b></font>
drwxr-xr-x 272 root root 12288 jul 10 21:27 <font color="#3465A4"><b>share</b></font>
drwxr-xr-x   6 root root  4096 ago 24 18:51 <font color="#3465A4"><b>src</b></font>
</pre>

Estas diferencias que hacemos entre argumentos y opciones no las entiende el sistema operativo, que tan solo le pasa a nuestros programas una lista de string. Por ello contamos con bibliotecas como _argparse_, que nos permiten manipular de forma sencilla los paramátros de nuestro programa.

## [4. Argparse](#3-argparse)

Vamos un ejemplo de programa sencillo (un script o programa de secuencia de comandos), que recibe un argumento (el nombre de el usuario) por linea de comandos e imprime un saludo personalizado:

```python
#!/usr/bin/env python3
import sys

nombre = sys.argv[1]
print(f'Hola {nombre}')
```

Si querés probar este programa en tu computadora, copiá y pegá el código en un archivo saludador.py, guardalo y ejecutá el siguiente comando:


```bash
$ chmod u+x saludador.py
```

¿Pero qué hace este programa? Bueno, el camino más largo comienza con un paso 👣, así que vayamos en orden: ¿Qué significa la primer linea? 🤔

```python
#!/usr/bin/env python3
```
El par de caracteres `#!` se conoce como shebang o  hash-bang y típicamente abren el encabezado de los archivos ejecutables. Este encabezado define dónde se encuentra el intérprete del lenguaje en el que se escribió el script, en este caso _python3_. 

En la segunda linea importamos la biblioteca _[sys](https://docs.python.org/es/3/library/sys.html)_, que nos permite acceder a los comandos y argumentos ingresados desde el intérprete. En particular `.argv` es un método que devuelve una lista de los argumentos de la línea de comandos pasados a un script de Python:

- argv[0] se corresponde al nombre del script 

- argv[1] se corresponde con los argumentos propiamente dichos

>
> 🧗🏻‍♀️**Desafío I**: reescribí el script para que reciba como argumento también el apellido y, al igual que antes salude incorporando en el saludo también el apellido separado por un espacio del nombre
```python
"Hola Ana Velez"
```
>

Cómo verás parsear a mano los argumentos ingresados por terminal cuando son muchos pude resultar engorroso, sin mencionar la dificultad extra de la documentación de nuestro programa. Afortunadamente, existe una biblioteca que nos permite hacer esto de manera muy sencilla. Probá el siguiente código:

```python
#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Este es un saludador personalizado: ¡Toma tu nombre y apellido y te responde!')
parser.add_argument('-n', '--name',
                    type=str,
                    help='user name')

args = parser.parse_args()

print(f"¡Hola {args.name}! ¡Bienvendix!")
```

>
> 🧗🏻‍♀️**Desafío II**: armá un script llamado `saludador_mejorado.py` y ejecutalo haciendo 
```bash
./calculadora.py --help
```
> 🤔 ¿Qué obtuviste? ¿De dónde sale esa documentación?
>
> 🧗🏻‍♀️**Desafío III**: ahora reescribí el script `saludador_mejorado.py` para que reciba también el apellido de la persona
>


🤔 ¿Qué diferencia tan grande, no? como has podido observar _`Argparse`_ hace la recepción de y el parseo de argumentos mucho más sencilla.

> 🧗🏻‍♀️**Desafío IV**: investigá para que sirve el parámetro `required` del método `.add_argument()`
