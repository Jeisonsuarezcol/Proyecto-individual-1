# Proyecto de Sistema de Recomendación de Películas

<<<<<<< HEAD
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
=======
Este proyecto consiste en el desarrollo de un sistema de recomendación de películas para una startup que provee servicios de agregación de plataformas de streaming. El objetivo es crear un modelo de machine learning que recomiende películas a los usuarios en función de su similitud con otras películas.

## Ciclo de vida del proyecto

El proyecto sigue el siguiente ciclo de vida:

1. **Tratamiento y recolección de datos**: Se realiza un trabajo de Data Engineering para transformar los datos en un formato adecuado para su procesamiento y análisis. Se aplican las siguientes transformaciones:

    - Desanidado de campos: Se desanidan los campos anidados, como belongs_to_collection, production_companies, entre otros, para que puedan ser utilizados en consultas posteriores.
    - Relleno de valores nulos: Los campos revenue y budget se rellenan con el valor 0 en caso de ser nulos.
    - Eliminación de valores nulos: Se eliminan las filas que tienen valores nulos en el campo release date.
    - Formato de fechas: Las fechas se ajustan al formato AAAA-mm-dd, y se crea una nueva columna llamada release_year que contiene el año de estreno.
    - Cálculo del retorno de inversión: Se crea la columna "return" que representa el retorno de inversión calculado como revenue / budget.
    - Eliminación de columnas no utilizadas: Se eliminan las columnas video, imdb_id, adult, original_title, poster_path, homepage, entre otras, no serán relevantes para este modelo.

2. **Desarrollo de la API**: Se utiliza el framework FastAPI para disponibilizar los datos. Se crean 6 funciones para los endpoints de la API:

    - `cantidad_filmaciones_mes(Mes)`: Devuelve la cantidad de películas estrenadas en un mes específico.
    - `cantidad_filmaciones_dia(Dia)`: Devuelve la cantidad de películas estrenadas en un día específico.
    - `score_titulo(titulo_de_la_filmación)`: Devuelve el título, año de estreno y score/popularidad de una película según su título.
    - `votos_titulo(titulo_de_la_filmación)`: Devuelve el título, cantidad de votos y promedio de votaciones de una película según su título. Se requiere que la película tenga al menos 2000 valoraciones; de lo contrario, se muestra un mensaje indicando que no cumple con este requisito.
    - `get_actor(nombre_actor)`: Devuelve la cantidad de filmaciones en las que ha participado un actor, su éxito medido a través del retorno y el promedio de retorno por filmación.
    - `get_director(nombre_director)`: Devuelve el éxito de un director medido a través del retorno, y para cada película en la que ha participado, muestra el título, fecha de lanzamiento, retorno individual, costo y ganancia.

3. **Deployment**: Se utiliza el servicio de Render para desplegar la API y permitir su uso desde la web.

4. **Análisis exploratorio de los datos (EDA)**: Se realiza un análisis exploratorio de los datos para investigar las relaciones entre las variables, detectar outliers o anomalías, y encontrar patrones. Se usan algunas librerías como pandas, missingno, sklearn, entre otras, para obtener conclusiones a partir de estos datos.

5. **Sistema de recomendación**: Una vez que se puede acceder los datos  a través de la API y se ha realizado el análisis exploratorio, se entrena un modelo de machine learning para construir un sistema de recomendación de películas. El sistema recomienda películas basándose en la similitud de puntuación con otras películas. Las películas se ordenan según el score de similitud y se devuelve una lista con los 5 nombres de las películas más similares, en orden descendente.
>>>>>>> acd676ef03377938625aba8cee5328d5131ef80a

## Configuración y ejecución del proyecto

Ejecuta el proyecto: https://project-deployment-fpoa.onrender.com/

<<<<<<< HEAD
Para acceder al archivo credits.csv:      
https://drive.google.com/file/d/1TRrSpgMs-T-3qVb77dxeKa_LRJ1OziFA/view?usp=sharing
=======
Para acceder al archivo credits.csv : https://drive.google.com/file/d/1TRrSpgMs-T-3qVb77dxeKa_LRJ1OziFA/view?usp=sharing
>>>>>>> acd676ef03377938625aba8cee5328d5131ef80a
