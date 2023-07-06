# Proyecto de Sistema de Recomendación de Películas

Este proyecto tiene como objetivo desarrollar un sistema de recomendación de películas basado en un modelo de Machine Learning. El sistema permite recomendar películas a los usuarios en función de su similitud con otras películas.

## Desarrollo del Proyecto

El proyecto se divide en varias etapas, que incluyen transformaciones de datos, desarrollo de una API utilizando FastAPI, análisis exploratorio de datos (EDA) y entrenamiento del modelo de recomendación.

### Transformaciones de Datos

En esta etapa, se realiza un trabajo rápido de Data Engineering para preparar los datos. Se aplican las siguientes transformaciones a los datos:

- Desanidar algunos campos anidados, como `belongs_to_collection`, `production_companies`, entre otros.
- Rellenar los valores nulos de los campos `revenue` y `budget` con el número 0.
- Eliminar los valores nulos del campo `release_date`.
- Formatear las fechas en el formato AAAA-mm-dd y extraer el año de la fecha de estreno en la columna `release_year`.
- Crear la columna de retorno de inversión llamada `return`, calculada como el cociente entre `revenue` y `budget`, con valor 0 en caso de datos faltantes.
- Eliminar las columnas no utilizadas, como `video`, `imdb_id`, `adult`, `original_title`, `poster_path` y `homepage`.

### Desarrollo de la API

En esta etapa, se utiliza el framework FastAPI para disponibilizar los datos. Se implementan las siguientes funciones para los endpoints que se consumirán en la API:

- `peliculas_idioma(Idioma: str)`: Devuelve la cantidad de películas producidas en un idioma específico.
- `peliculas_duracion(Pelicula: str)`: Devuelve la duración y el año de una película específica.
- `franquicia(Franquicia: str)`: Devuelve la cantidad de películas, la ganancia total y la ganancia promedio de una franquicia específica.
- `peliculas_pais(Pais: str)`: Devuelve la cantidad de películas producidas en un país específico.
- `productoras_exitosas(Productora: str)`: Devuelve la ganancia total y la cantidad de películas realizadas por una productora específica.
- `get_director(nombre_director)`: Devuelve el éxito de un director específico medido a través del retorno, junto con el nombre, fecha de lanzamiento, costo y ganancia de cada película en formato de lista.

### Deployment

Se utiliza el servicio de Render para desplegar la API y permitir su uso desde la web.

### Análisis Exploratorio de Datos (EDA)

Se realiza un análisis exploratorio de los datos para investigar las relaciones entre las variables, detectar outliers o anomalías, y encontrar patrones. Se usan algunas librerías como pandas, missingno, sklearn, entre otras, para obtener conclusiones a partir de estos datos.

### Sistema de recomendación 

Una vez que se puede acceder los datos  a través de la API y se ha realizado el análisis exploratorio, se entrena un modelo de machine learning para construir un sistema de recomendación de películas. El sistema recomienda películas basándose en la similitud de puntuación con otras películas. Las películas se ordenan según el score de similitud y se devuelve una lista con los 5 nombres de las películas más similares, en orden descendente.

## Configuración y ejecución del proyecto

Ejecuta el proyecto: https://project-deployment-fpoa.onrender.com/

Para acceder al archivo credits.csv:      
https://drive.google.com/file/d/1TRrSpgMs-T-3qVb77dxeKa_LRJ1OziFA/view?usp=sharing