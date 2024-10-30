# AiStudio
  
Module to work with the Ai Studio API  

*Read this in other languages: [English](Manual_AiStudio.md), [Português](Manual_AiStudio.pr.md), [Español](Manual_AiStudio.es.md)*
  
![banner](imgs/Banner_AiStudio.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Login
  
Login to Ai Studio
|Parameters|Description|example|
| --- | --- | --- |
|API Key|API Key generated in Ai Studio.|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey...|
|Server|Ai Studio server to use.|PROD|
|Assign result to variable|Variable where the result will be stored.|Variable|

### Get tasks
  
Obtains the tasks of the user
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to variable|Variable where the result will be stored.|Variable|

### Run task
  
Runs a task of the user
|Parameters|Description|example|
| --- | --- | --- |
|Task ID|ID of the task to run.|d0877abb7789b897e0b0|
|Execution mode|Execution mode of the task. Wait for response waits for the task to finish and returns the result. Run in background runs the task in the background and does not wait for it to finish.|WAIT|
|Input file|File that will be sent to the task. Required in case the task needs it.|File|
|Assign result to variable|Variable where the result will be stored.|Variable|

### Get results
  
Get the results of a task by ID
|Parameters|Description|example|
| --- | --- | --- |
|Task ID|ID of the task to get results.|d0877abb7789b897e0b0|
|Assign result to variable|Variable where the result will be stored.|Variable|
