# Backend Prueba Solotodo
Este es el backend para ejecutar el ejercicio del cargo de FullStack Developer. Para iniciar el servidor debe seguir los siguientes pasos
## Instrucciones
- Para clonar el repositorio, ejecutar el comando `git clone https://github.com/JavierGonzalez998/Backend-prueba-solotodo.git` en la terminal.
- Una vez clonado el repositorio, ingresar a la raíz del repositorio y con python ejecutar el siguiente comando: `python -m venv .venv`. Esto genera el entorno virtual necesario para ejecutar el servicio.
- Para ingresar al entorno virtual, ejecutar el siguiente comando en la terminal `./.venv/Scripts/activate`
- Instalar dependencias con `pip install -r requirements`
- Una vez instaladas las dependencias ejecutar `python manage.py runserver` para ejecutar el servidor
## Migraciones
Si se realizan cambios en los modelos y se desea actualizar la base de datos, Se debe realizar las siguientes instrucciones:
 - Generar archivos de migraciones con `python manage.py makemigrations`
 - Ejecutar migraciones con `python manage.py migrate`

Esto actualizará la base de datos a la última "Versión" de los modelos.
## Endpoints
Los endpoints que conforman el servicio son los siguientes:
### Posts
Para la creación y visualización de posts, se configuraron los siquientes endpoints :
- `api/post`(GET): Este endpoint retorna un listado de todos los registros de los posts generados.
- `api/post`(POST): Este endpoint realiza el ingreso de un nuevo post, retorna el post creado.
- `api/post/<id>`(GET): Este endpoint entrega el detalle de una publicación en específico.
