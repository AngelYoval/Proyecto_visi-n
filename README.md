# Proyecto_visión
# Repositorio de procesamiento de imagenes
Este repositorio contiene el trabajo desarrollado en el marco de la experiencia educativa "Técnicas de Inteligencia Artificial". El objetivo principal de este proyecto es abordar el desafío del procesar una imagen atravez del metodo de promedio ponderado

## Descripción del Problema
El procesamiento de imágenes a través del método de promedio ponderado es una técnica importante en el campo de la visión por computadora y el procesamiento de imágenes, ya que permite el suabisado de una imagen aplicando un metodo llamado Blur, esto es until a la hora de querer sensuarar imagener o perder informacion visual:

El filtro de promedio ponderado se utiliza para difuminar una imagen de una manera controlada y suave, y la cantidad de suavizado se ajusta variando los valores en la máscara. Cuanto más grande sea la máscara o cuanto más se ponderen los píxeles cercanos al centro, mayor será el efecto de suavizado.
## Contenido del Repositorio
## Materiales y Métodos
1. **Python**: Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Fue creado por Guido van Rossum y su primera versión fue lanzada en 1991. Python se ha vuelto extremadamente popular debido a su sintaxis clara y legible, lo que facilita su aprendizaje y uso. Algunas características destacadas de Python incluyen: Sintaxis legible, Interpretado, Tipado dinámico, Multiplataforma, Amplia biblioteca estándar, Programación orientada a objetos, etec.
2. **OpenCV**: OpenCV, que significa Open Source Computer Vision, es una biblioteca de código abierto diseñada para el procesamiento de imágenes y visión por computadora. Fue inicialmente desarrollada por Intel y se ha convertido en una herramienta esencial en el ámbito de la visión por computadora debido a su versatilidad y eficiencia.
3. 

### Lenguaje de Programación

### Descripción de los metodos
El proceso de aplicar un filtro de promedio ponderado a una imagen generalmente implica los siguientes pasos:
1. Definición de una máscara o núcleo: La máscara es una matriz de números que especifica los pesos que se asignarán a los píxeles en la vecindad del píxel central. Los valores en la máscara determinan cómo se ponderan los píxeles circundantes. Por lo general, se utiliza una máscara simétrica y centrada, como una máscara gaussiana, que da más peso a los píxeles cercanos al centro y menos peso a los píxeles más alejados.
2. Colocación de la máscara en cada píxel de la imagen: La máscara se coloca sucesivamente en cada píxel de la imagen, y los valores de los píxeles subyacentes se multiplican por los valores correspondientes en la máscara.
3. Suma de los valores ponderados: Se suman los valores ponderados de los píxeles para obtener el valor del píxel resultante. Este valor reemplazará al píxel original en la imagen, lo que suavizará la imagen.
## Diseño
![Nombre de la ventana](https://github.com/AngelYoval/Proyecto_vision/assets/97262879/fd93b141-15e3-47dc-92ad-f9f156ec5324)

## Bibliografia
### Libros
1. "Digital Image Processing" de González y Woods
2. "Computer Vision: Algorithms and Applications" de Richard Szeliski
### paginas web

## Concluciones
**Nota:** Este repositorio se crea con fines educativos y de aprendizaje. ¡Agradecemos cualquier contribución y retroalimentación de la comunidad!
