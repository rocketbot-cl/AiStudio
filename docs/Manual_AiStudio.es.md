



# AiStudio
  
Módulo para trabajar con la API de Ai Studio Rocketbot  

*Read this in other languages: [English](Manual_AiStudio.md), [Português](Manual_AiStudio.pr.md), [Español](Manual_AiStudio.es.md)*
  
![banner](imgs/Banner_AiStudio.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Iniciar Sesión
  
Inicia sesión en Ai Studio
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|API Key|API Key generada en Ai Studio.|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey...|
|Servidor|Servidor de Ai Studio a utilizar.|PROD|
|Asignar resultado a variable|Variable donde se almacenará el resultado.|Variable|

### Obtener tasks
  
Obtiene las tasks del usuario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable|Variable donde se almacenará el resultado.|Variable|

### Ejecutar task
  
Ejecuta una task del usuario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Task ID|ID de la task a ejecutar.|d0877abb7789b897e0b0|
|Modo de ejecución|Modo de ejecución de la task. Wait for response espera a que la task termine y devuelve el resultado. Run in background ejecuta la task en segundo plano y no espera a que termine.|WAIT|
|Fecha de inicio (EMAIL task)|Fecha de inicio desde la cual se buscarán los correos electrónicos. Obligatorio en caso de que la task sea de tipo EMAIL.|30/10/2021|
|Fecha de fin (EMAIL task)|Fecha de fin hasta la cual se buscarán los correos electrónicos. Obligatorio en caso de que la task sea de tipo EMAIL.|30/10/2021|
|Texto (tareas tipo text)|Texto a enviar para procesamiento AiStudio.|Lorem ipsum dolor sit amet consectetur adipiscing elit lacinia varius, facilisi venenatis ornare mattis eget nisl curae integer montes molestie, lectus felis ultricies tempor neque mauris nam aptent.|
|Archivo de entrada|Archivo que se enviará a la task. Requerido en caso de que la task lo necesite.|Archivo|
|Asignar resultado a variable|Variable donde se almacenará el resultado.|Variable|

### Obtener resultados
  
Obtiene los resultados de una task por ID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Task ID|ID de la task a obtener resultados.|d0877abb7789b897e0b0|
|Asignar resultado a variable|Variable donde se almacenará el resultado.|Variable|
