from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI
from datetime import datetime
import pandas as pd

app = FastAPI()


df_final = pd.read_csv('datasets/final_movies_dataset.csv')
df_final['release_date'] = pd.to_datetime(df_final['release_date'], format="%Y-%m-%d")

<<<<<<< HEAD
belongs_collection = pd.read_csv('datasets/belongs_collection.csv')
df_production_countries = pd.read_csv('datasets/production_countries.csv')
df_production_companies = pd.read_csv('datasets/production_companies.csv')
=======
df_cast = pd.read_csv('datasets/data_cast.csv')
>>>>>>> acd676ef03377938625aba8cee5328d5131ef80a
df_crew = pd.read_csv('datasets/data_crew.csv')

df = df_final.drop(columns=['id', 'original_language','release_year','runtime', 'status','tagline','budget','release_date','revenue','vote_average','vote_count','return'])
df = df[:2000]


@app.get('/')
def index():

<<<<<<< HEAD
    return 'Hola, bienvenido. Para acceder a las consultas de este proyecto debes agregar /docs a tu URL actual'


@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma: str):
    
    idioma = idioma.lower()
    
    total_movies = len(df_final[df_final['original_language'] == idioma])
    
    return f"{total_movies} películas fueron estrenadas en idioma {idioma}"


@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula:str):
    
    try:
    
        pelicula = pelicula.title()

        anio = int(df_final['release_year'][df_final['title'] == pelicula].values[0])

        minutos = df_final['runtime'][df_final['title'] == pelicula].values[0]

        horas, minutos = divmod(minutos, 60)

        duracion = f"{int(horas)}h {int(minutos)}m"

        return {'titulo':pelicula, 'duracion': duracion, 'anio': anio}
    
    except IndexError:

        return {'mensaje' : f'La película {pelicula} no se encuentra'}


@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    
    franquicia = franquicia.title()
    
    movies = belongs_collection['id_movie'][belongs_collection['name'] == franquicia].unique()
    
    if len(movies) == 0:
        
        return {'mensaje': f'El nombre del la franquicia {franquicia} no se encuentra'}
    else:
    
        num_movies = len(movies)

        ganancia_total = df_final['revenue'][df_final['id'].isin(movies)].sum()

        ganancia_promedio = df_final['revenue'][df_final['id'].isin(movies)].mean()

        return {'franquicia': franquicia, 'total_peliculas': num_movies, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}
    

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    
    pais = pais.title()
    
    num_movies = len(df_production_countries[df_production_countries['name'] == pais])
    
    if num_movies == 0:
        
        return {'mensaje': f'El país {pais} no se encuentra'}
    
    else:
    
        return {'pais': pais, 'num_movies': num_movies}


@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora:str): 
    
    productora = productora.title()
    
    movies = df_production_companies['id_movie'][df_production_companies['name'] == productora]
    
    num_movies = len(movies)
    
    if num_movies == 0:
        
        return {'mensaje': f'La productora {productora} no se encuentra'}
    else:
    
        ganancia_total = df_final['revenue'][df_final['id'].isin(movies)].sum()

        return {'productora': productora, 'num_peliculas': num_movies, 'ganancia_total': ganancia_total}
=======
    return 'hola'


@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes:str):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente'''
    meses_dict = {
        'enero': 1,
        'febrero': 2,
        'marzo': 3,
        'abril': 4,
        'mayo': 5,
        'junio': 6,
        'julio': 7,
        'agosto': 8,
        'septiembre': 9,
        'octubre': 10,
        'noviembre': 11,
        'diciembre': 12
    }
    
    mes_numero = meses_dict.get(mes.lower())

    peliculas_mes = df_final[df_final['release_date'].dt.month == mes_numero]

    cantidad_peliculas = len(peliculas_mes)

    return {'mes': mes, 'cantidad': cantidad_peliculas}


@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia:str):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrebaron ese dia historicamente'''

    dias_dict = {
        'lunes': 0,
        'martes': 1,
        'miercoles': 2,
        'jueves': 3,
        'viernes': 4,
        'sabado': 5,
        'domingo': 6
    }
    
    dia_numero = dias_dict.get(dia.lower())
    
    peliculas_dia = df_final[df_final['release_date'].dt.dayofweek == dia_numero]
    
    cantidad_peliculas = len(peliculas_dia)

    return {'dia':dia, 'cantidad':cantidad_peliculas}


@app.get('/score_titulo/{titulo}')
def score_titulo(titulo:str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score'''

    try:
        
        nombre = titulo.title()
        pelicula = df_final[df_final['title'] == nombre]
        
        anio = int(pelicula['release_year'].values[0])
        
        popularidad = pelicula['popularity'].values[0]
        
        return {'titulo': nombre, 'anio': anio, 'popularidad': popularidad}
    
    except IndexError:

        return {'mensaje' : f'La película {titulo} no se encuentra'}
    


@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo:str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. 
    La misma variable deberá de contar con al menos 2000 valoraciones, 
    caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.'''

    try:
        
        nombre = titulo.title()
        pelicula = df_final[df_final['title'] == nombre]
        
        if pelicula['vote_count'].values[0] < 2000:
            return {'mensaje':'La película debe contar con al menos 2000 valoraciones'}
        
        else:
            
            anio = int(pelicula['release_year'].values[0])
            
            valoraciones = pelicula['vote_count'].values[0]
            
            promedio = pelicula['vote_average'].values[0]
            
            
            return {'titulo':titulo, 'anio':anio, 'voto_total':valoraciones, 'voto_promedio':promedio}
        
    except IndexError:
        
        return {'message': f'La película {titulo} no se encuentra'}



@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor:str):
    '''Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, la cantidad de películas que en las que ha participado y el promedio de retorno'''

    nombre = nombre_actor.title()
        
    df_nombre = df_cast[df_cast['name'] == nombre]

    if len(df_nombre) == 0:
        
        return {'mensaje': f'El nombre del actor {nombre_actor} no se encuentra'}
    
    else:
        peliculas = df_nombre['id_movie'].unique()

        count_movie = len(peliculas)

        df_datos = df_final[df_final['id'].isin(peliculas)]
        
        rertorno = df_datos['return'].sum()

        media = round(df_datos['return'].mean(), 2)

        return {'actor':nombre, 'cantidad_filmaciones':count_movie, 'retorno_total':rertorno, 'retorno_promedio':media}
>>>>>>> acd676ef03377938625aba8cee5328d5131ef80a
    
    
@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:str):
    ''' Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.'''

    nombre = nombre_director.title()
    
    df_director = df_crew[(df_crew['name'] == nombre) & (df_crew['job'] == 'Director')]
    
    if len(df_director) == 0:
        
        mensaje = f'El nombre del Director {nombre_director} no se encuentra'
        
        return mensaje
    
    else:
        peliculas = df_director['id_movie'].unique()
        
        df_peliculas = df_final[df_final['id'].isin(peliculas)]
        
        exito_director = round(df_peliculas['return'].sum(),2)

        movies = df_peliculas['title'].to_list()

        anio = df_peliculas['release_year'].to_list()

        retorno = df_peliculas['return'].to_list()

        budget = df_peliculas['budget'].to_list()

        revenue = df_peliculas['revenue'].to_list()

        
        return {'director':nombre, 'retorno_total_director':exito_director, 
        'peliculas':movies, 'anio':anio,'retorno_pelicula':retorno, 
        'budget_pelicula':budget, 'revenue_pelicula':revenue}

# ML
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista
        solo se cuenta con 2000 registros debido al costo computacional'''

    try:
    
        titulo = titulo.title()
        # Obtener el índice  
        indice_pelicula = df[df['title'] == titulo].index[0] 

        # Calcularmos la similitud de puntuación entre películas 
        vectorizer = TfidfVectorizer(stop_words='english') 
        tfidf_matrix = vectorizer.fit_transform(df['title'].values.astype('U'))  
        similarity_matrix = cosine_similarity(tfidf_matrix) 

        # Obtener las películas más similares en función de la puntuación 
        similar_movies = list(enumerate(similarity_matrix[indice_pelicula])) 
        similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True) 
        top_similar_movies = similar_movies[1:6]  # Excluye la película de interés y toma las 5 más similares 

        # Obtiene los nombres de las películas recomendadas 
        recommended_movies = [df.iloc[movie[0]]['title'] for movie in top_similar_movies] 

        return {'lista recomendada': recommended_movies}
    
    except IndexError:
        
        return {'mensaje' : f'La película {titulo} no se encuentra'}
