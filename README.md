# scraper_TCVD
## Introducción
¿Existen diferentes clases de evoluciones para un valor en bolsa? ¿y para una cuota de una apuesta? ¿Cómo afectan las noticias a los espectadores en la visión del resultado final de un partido?¿Se puede visualizar la esperanza del público? ¿Cómo juegan y cómo jugar con el dinero y el futuro? Estas son las que nos hemos hecho poniendo el foco en las “Casas de Apuestas”. Con el fin de comprender su comportamiento necesitamos extraer los datos con los que generar información y conocimiento respondiendo a estas y otras preguntas.

## Contexto
De primeras estuvimos comentando la idea de las Casas de Apuestas pero en esta época los deportes tradicionales y mayoritarios no tienen partidos. Sin embargo, vimos que los e-Sports seguían con los partidos organizados, resultados, apuestas en directo, etc. Con lo que elegimos ese área del deporte.

Tras esa elección se buscó la mejor fuente de datos y encontramos que hltv era una plataforma genial donde se mostraba mucha información de muchos de los partidos que sucedían. Además existían las cuotas de diferentes Casas de Apuestas y se juntaba con la información oficial de cada partido: resultado, jugadores, racha, etc. Al no tener una API oficial tuvimos que decantarnos por hacer scraping al código fuente de las páginas.

A pesar de esta organización visualmente sencilla, hemos comprobado las dificultades del proceso de scrapping ya que, por ejemplo, teníamos que la relación entre resultados o jugadores y partido no era directa y se tenía que hacer pasos intermedios para crear esa conexión y componer un dataset completo.

Las ideas que nos habíamos planteado en la introducción se iban viendo posibles de responder a medida que estudiabamos la estructura de la web y la posibilidad del código.


## Dataset

### Título
CS:GO Bets Time series

### Descripción breve


### Contenido

### Representación gráfica

### Inspiración

### Licencia y agradecimientos
Tanto el código como los datos pueden ser usados por terceros pero teniendo que hacer referencia y dar crédito a nosotros como autores. Por tanto elegimos la licencia CC BY-SA 4.0 que permite seguir la traza de la autoría de los datos y del código, tal y como se explica en https://creativecommons.org/licenses/by-sa/4.0/ . La cláusula sobre el uso comercial no nos interesa ya que probablemente perderíamos bastantes usuarios. Y la ODbL o la CC0 eran demasiado libres y ponían en peligro la autoría de nuestro producto.

## Metodología del scraping
Primero 


Hemos cambiado las cabeceras para ser distinguidos de los scripts
Controlamos el tema de timeouts por si se bloquea la página o perdemos la conexión
No usamos sesiones porque no es necesario loguearse en la página

) el archivo robots.txt,
2) el mapa del sitio web,
3) su tamaño,
4) la tecnología usada y
5) el propietario del mismo.

https://www.hltv.org/robots.txt
User-agent: 360Spider
Disallow: /stats

User-agent: *
crawl-delay: 1

User-agent: Yandex
crawl-delay: 1

User-agent: Yandex
Disallow: /stats

User-agent: coccocbot-web
Disallow: /stats