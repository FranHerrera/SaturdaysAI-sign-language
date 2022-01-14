![Saturdays.AI - Online Edition](https://github.com/FranHerrera/SaturdaysAI-sign-language/blob/main/assets/logo-saturdaysAI.png)

# Lenguage de Signos

![Saturdays.AI](https://img.shields.io/badge/status-active-brightgreen)

![GitHub contributors](https://img.shields.io/github/contributors/FranHerrera/SaturdaysAI-sign-language)

![GitHub](https://img.shields.io/github/license/FranHerrera/SaturdaysAI-sign-language)


[Saturdays.AI](https://saturdays.ai) Saturdays.ai es una iniciativa global para democratizar el acceso a la educación en Inteligencia Artificial con la calidad y el rigor de las mejores universidades del mundo, en forma de bootcamps de 14 semanas.



## Objetivo del proyecto

El objetivo de este proyecto de la 1ª Edición de AI Saturdays Online es demostrar que, utilizando las nuevas posibilidades que aportan tecnologías, en concreto la visión por ordenador y el aprendizaje automático, se puede democratizar el aprendizaje de la lengua de signos española (LSE) y de esta forma facilitar la inclusión de las personas que requieran de la lengua de signos para comunicarse en la sociedad.

## Implementación
### Pasos

1. Se ha generado un conjunto de datos a partir de videos de palabras pertenecientes al LSE.

![GIF Videos](assets\gif_videos.gif)

2. Se han generado más videos a partir de modificaciones de los videos obtenidos (flips, rotaciones y traslaciones)

![GIF Videos modificados](assets\gif_videos_modificados.gif)

3. Se ha utilizado el framework [Mediapipe](https://google.github.io/mediapipe/solutions/holistic) para extraer las coordenadas de las diferentes partes del cuerpo que se utilizan para generar el gesto y almacenarlas en un dataframe

![GIF Video con mediapipe](assets\gif_videos_mediapipe.gif)

4. Se ha entrenado un modelo de machine learning con el algoritmo SVC
5. Se han obtenido los siguiente resultados

![GIF Resultados](assets\gif_resultados.gif)