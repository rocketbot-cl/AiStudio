# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import sys

base_path = tmp_global_obj["basepath"] # type:ignore
cur_path = base_path + 'modules' + os.sep + 'AiStudio' + os.sep + 'libs' + os.sep
GetParams = GetParams # type:ignore
SetVar = SetVar # type:ignore
PrintException = PrintException # type:ignore

if cur_path not in sys.path:
    sys.path.append(cur_path)

from iaStudio_service import IAStudio # type:ignore

module = GetParams("module")

global mod_iaStudio


try:
    if module == "login":
        api_key = GetParams("api_key")
        server = GetParams("server")
        result = GetParams("result")

        try:
            mod_iaStudio = IAStudio(api_key, server)
            mod_iaStudio.get_entities()
            SetVar(result, True)

        except Exception as e:
            SetVar(result, False)
            PrintException()
            raise e
    try:
        if module == "get_tasks":
            result = GetParams("result")

            try:
                res = mod_iaStudio.get_tasks()
                SetVar(result, res)

            except Exception as e:
                SetVar(result, False)
                PrintException()
                raise e
            
        if module == "run_task":
            task_id = GetParams("task_id")
            mode = GetParams("mode")
            file = GetParams("file")
            start_date = GetParams("start_date")
            end_date = GetParams("end_date")
            result = GetParams("result")

            try:
                range_ = None
                if start_date and end_date:
                    range_ = [start_date, end_date]
                
                res = mod_iaStudio.run_task(task_id, mode, file, range_)
                if res.get('status') == False:
                    if 'You need to provide afterDate and beforeDate' in res.get('message'):
                        raise Exception("To run this task you must specify the start and end range date.")
                    raise Exception(res.get('message'))
                SetVar(result, res)

            except Exception as e:
                SetVar(result, False)
                PrintException()
                raise e
            
        if module == "get_results":
            task_id = GetParams("task_id")
            result = GetParams("result")

            try:
                res = mod_iaStudio.get_results(task_id)
                SetVar(result, res)

            except Exception as e:
                SetVar(result, False)
                PrintException()
                raise e
    except NameError as e:
        raise Exception("You must login first.")
        
except Exception as e:
    import traceback
    traceback.print_exc()
    PrintException()
    raise e