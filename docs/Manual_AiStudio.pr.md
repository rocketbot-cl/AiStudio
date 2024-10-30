# AiStudio
  
Módulo para trabalhar com a API do Ai Studio Rocketbot  

*Read this in other languages: [English](Manual_AiStudio.md), [Português](Manual_AiStudio.pr.md), [Español](Manual_AiStudio.es.md)*
  
![banner](imgs/Banner_AiStudio.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Login
  
Login no Ai Studio
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|API Key|API Key gerada no Ai Studio.|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey...|
|Servidor|Servidor do Ai Studio a ser utilizado.|PROD|
|Atribuir resultado à variável|Variável onde o resultado será armazenado.|Variável|

### Obter tasks
  
Obtém as tasks do usuário
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado à variável|Variável onde o resultado será armazenado.|Variável|

### Executar task
  
Executa uma task do usuário
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Task ID|ID da task a ser executada.|d0877abb7789b897e0b0|
|Modo de execução|Modo de execução da task. Wait for response espera a task terminar e retorna o resultado. Run in background executa a task em segundo plano e não espera terminar.|WAIT|
|Arquivo de entrada|Arquivo que será enviado à task. Necessário caso a task precise.|Arquivo|
|Atribuir resultado à variável|Variável onde o resultado será armazenado.|Variável|

### Obter resultados
  
Obtém os resultados de uma task por ID
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Task ID|ID da task para obter resultados.|d0877abb7789b897e0b0|
|Atribuir resultado à variável|Variável onde o resultado será armazenado.|Variável|
