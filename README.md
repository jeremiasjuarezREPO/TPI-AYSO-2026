# Trabajo Integrador – Virtualización con VirtualBox y Ubuntu

## Descripción

Este proyecto fue desarrollado como Trabajo Integrador para la materia Arquitectura y Sistemas Operativos de la Tecnicatura Universitaria en Programación a Distancia (UTN).

El objetivo consiste en estudiar los conceptos fundamentales de la virtualización mediante la instalación y configuración de una máquina virtual utilizando Oracle VirtualBox, la instalación del sistema operativo Ubuntu y la ejecución de un programa desarrollado en Python dentro del entorno virtualizado.

## Objetivos

- Comprender los fundamentos de la virtualización.
- Diferenciar hipervisores de Tipo 1 y Tipo 2.
- Configurar una máquina virtual utilizando VirtualBox.
- Instalar Ubuntu como sistema operativo invitado.
- Preparar un entorno de desarrollo con Python y Visual Studio Code.
- Ejecutar y validar un programa Python dentro de una máquina virtual.

## Tecnologías utilizadas

- Oracle VirtualBox
- VirtualBox Extension Pack
- Ubuntu 26.04 LTS
- Python 3
- Visual Studio Code
- Windows (Sistema Operativo anfitrión)

## Contenidos del proyecto

El trabajo aborda:

1. Conceptos teóricos de virtualización.
2. Funcionamiento de los hipervisores.
3. Configuración de recursos virtualizados:
   - CPU
   - Memoria RAM
   - Almacenamiento
   - Dispositivos de entrada y salida
4. Instalación y configuración de VirtualBox.
5. Instalación de Ubuntu en una máquina virtual.
6. Configuración del entorno de desarrollo.
7. Creación y ejecución de un script Python.

## Procedimiento realizado

### 1. Verificación de soporte de virtualización

Se comprobó que la tecnología de virtualización estuviera habilitada en la BIOS/UEFI del equipo anfitrión.

### 2. Instalación de VirtualBox

Se instaló Oracle VirtualBox junto con el Extension Pack oficial.

### 3. Instalación de Ubuntu

Se descargó la imagen ISO oficial de Ubuntu y se creó una máquina virtual configurando:

- Memoria RAM
- Núcleos de CPU
- Espacio de almacenamiento

### 4. Configuración del entorno de desarrollo

Dentro de Ubuntu se instaló:

- Python 3
- Visual Studio Code

### 5. Ejecución de un programa Python

Se desarrolló y ejecutó un script Python desde la terminal de Ubuntu para verificar el correcto funcionamiento del entorno virtualizado.

## Instrucciones de ejecucion del programa

### Requisitos

* Tener instalado Python 3.10 o superior.

---

### Ejecutar desde Linux

1. Abrir una terminal.
2. Navegar hasta la carpeta donde se encuentra el archivo `Operaciones.py`:

```bash
cd ruta_al_proyecto
```

3. Ejecutar el programa:

```bash
python3 Operaciones.py
```

---

### Ejecutar desde Windows

1. Abrir **Símbolo del sistema (CMD)** o **PowerShell**.
2. Navegar hasta la carpeta donde se encuentra el archivo `Operaciones.py`:

```cmd
cd C:/ruta_proyecto
```

3. Ejecutar el programa:

```cmd
python Operaciones.py
```

---

### Ejemplo de ejecución

```text
--- Bienvenido al sistema de operaciones numéricas ---

Ingresa el primer número entero: 10
Ingresa el segundo número entero: 5
Ingresa el tercer número entero: 3

--- Resultados de las Operaciones ---

🔹 Suma de los números: 18
🔹 Multiplicación de los números: 150
🔹 Promedio de los números: 6.00
🔹 Números ordenados de menor a mayor: [3, 5, 10]
```

## Resultados

Se logró:

- Crear una máquina virtual completamente funcional.
- Instalar Ubuntu correctamente.
- Configurar un entorno de desarrollo con Python.
- Ejecutar programas desde la terminal del sistema virtualizado.
- Comprender la administración de recursos realizada por el hipervisor.

## Estructura del repositorio

```text
📦 TRABAJO PRACTICO INTEGRADOR
│
├── 📁 Capturas y recursos visuales
│   ├── Capturas BIOS activacion de virtualizacion
│   ├── Capturas Escritura codigo python y ejecucion
│   ├── Capturas Instalacion de VSC y Python
│   ├── Capturas Instalacion Maquina Virtual
│   ├── Capturas Instalacion VirtualBox
│   └── Imagenes para el Informe
│
├── 📁 Codigo python
│   └── Operaciones.py
│
├── 📁 Presentacion
│   └── Virtualizacion_TPI.pptx
│
├── 📁 Video Explicativo
│   └── video.txt
│
├── 📁 Informe
│   └── TPI AySO Jeremias Juarez- Elias Ceballos Rey - 2026.pdf
│
└── README.md
```

## Conclusiones

La virtualización permite ejecutar múltiples sistemas operativos sobre un mismo equipo físico de forma aislada y segura. Mediante este trabajo fue posible comprender el funcionamiento de los hipervisores, la asignación de recursos virtuales y la implementación de entornos de desarrollo completos utilizando máquinas virtuales.

## Autores

- Jeremias Juarez
- Elias Ceballos Rey

## Institución

Arquitectura y Sistemas Operativos
Tecnicatura Universitaria en Programación a Distancia
Universidad Tecnológica Nacional (UTN)
Año 2026

## Link a video explicativo en youtube.com

