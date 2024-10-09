
# Algoritmos 

Este proyecto fue desarrollado en equipo para la asignatura **"Computación Gráfica y Visual"**. Su objetivo principal es profundizar en los fundamentos teóricos de los algoritmos de discretización de líneas, círculos y elipses.


## Librerias

Para ejecutar este proyecto, es necesario configurar varias variables de entorno, las cuales son:

`customtkinter`
`tkinter`
`PIL` 
`os`

A continuación, se proporcionan los enlaces a los sitios oficiales de las herramientas utilizadas, aunque también se mencionan brevemente en la documentación del código:

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Tkinter](https://wiki.python.org/moin/TkInter)
- [PIL (Pillow)](https://pillow.readthedocs.io/en/stable/)
- [OS Module](https://docs.python.org/3/library/os.html)


## Algoritmos Utilizados 
1. **Algoritmo DDA (Digital Differential Analyzer) para líneas**
El algoritmo DDA es uno de los métodos más simples para trazar líneas en gráficos rasterizados (como una pantalla de computadora). Se basa en el cálculo de los incrementos de las coordenadas de píxeles a lo largo de la línea que se quiere dibujar.

2. **Algoritmo de Bresenham para líneas**
El algoritmo de Bresenham es una mejora respecto al DDA para trazar líneas, optimizando el rendimiento al evitar cálculos con punto flotante y utilizando únicamente operaciones enteras.

3. **Algoritmo de Bresenham para círculos**
El algoritmo de Bresenham para círculos es una extensión del algoritmo para líneas, y se utiliza para trazar un círculo utilizando simetría. En lugar de dibujar cada punto del círculo, este algoritmo calcula solo una octava parte del círculo y refleja esos puntos en las otras secciones.

4. **Algoritmo de Bresenham para elipses**
El algoritmo de Bresenham para elipses es una variante del algoritmo para círculos y sigue el mismo principio de utilizar enteros y simetría, pero adaptado a las propiedades geométricas de la elipse.
## Desarrollo
Este proyecto fue desarrollado de manera individual, donde cada integrante asumió responsabilidades específicas: uno se encargó de los algoritmos y la lógica de la GUI, mientras que otro se ocupó de la estética de la interfaz. Debido a esta distribución, optamos por modular gran parte del código y distribuirlo en diferentes archivos, evitando una programación en cascada y respetando los principios de la programación mantenible.
## Capturas
![image](https://github.com/user-attachments/assets/afe5d15a-f7f8-4cbb-8fb7-f20b7786604d)
![image](https://github.com/user-attachments/assets/a832e1ea-6bcc-4689-87cd-3322adc3cc45)
![image](https://github.com/user-attachments/assets/ce73170c-820f-4f1d-ac72-45ea8e2dea19)


