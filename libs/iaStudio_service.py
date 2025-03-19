import ia_requests as requests
from datetime import datetime

SERVERS = {
    "PROD": "https://api-emailgpt.rocketbot.com/",
    "QA": "https://qa-api-emailgpt.myrb.io/",
    "DEV": "https://dev-api-emailgpt.myrb.io/"
}

STATUS = {
    1: "RUNNING",
    2: "PAUSED"
}

FILE_TYPES = {
    "mp3": "audio/mpeg",
    "wav": "audio/wav",
    "ogg": "audio/ogg",
    "txt": "text/plain",
    "pdf": "application/pdf",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
}

STATUS = {
    1: "running",
    2: "paused"
}

class IAStudio:
    def __init__(self, api_key, server):
        self.api_key = api_key
        self.url = SERVERS[server]

    def get_tasks(self):
        url = self.url + "api/tasks"
        headers = {'Authorization': f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        tasks = response.json().get("data")
        tasks_list = []
        for task in tasks:
            if task.get('status') != 3:
                tasks_list.append({
                    "id": task.get("uuid"),
                    "entity_id": task.get("entity_id"),
                    "name": task.get("name"),
                    "type": task.get("type"),
                    "status": STATUS[task.get("status")],
                })
        return tasks_list
    
    def run_task(self, task_id, mode, file_path=None, range_=None):
        if file_path:
            file_name = file_path.split("/")[-1]
            file_extension = file_name.split(".")[-1]
            if file_extension not in FILE_TYPES:
                raise Exception("Invalid file extension. Supported extensions: mp3, wav, ogg for VOICE tasks, txt and pdf for TEXT tasks, jpg, jpeg, png and pdf for IMAGE tasks")
            files=[
                ('file', (file_name, open(file_path, 'rb'), FILE_TYPES[file_extension]))
            ]
        else:
            files = None

        data = {'runMode': mode}
        if range_:
            try:
                after_date = datetime.strptime(range_[0], "%d/%m/%Y").strftime("%Y-%m-%d")
                before_date = datetime.strptime(range_[1], "%d/%m/%Y").strftime("%Y-%m-%d")
                data['afterDate'] = after_date
                data['beforeDate'] = before_date
            except ValueError:
                raise Exception("Invalid date format. Use dd/mm/yyyy")

        url = self.url + f"api/tasks/run/{task_id}"
        headers = {'Authorization': f"Bearer {self.api_key}"}
        
        response = requests.post(url, headers=headers, data=data, files=files)
        return response.json()
    
    def get_entities(self):
        url = self.url + "api/entities/all"
        headers = {'Authorization': f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        if response.json().get('error'):
            raise Exception(response.json().get('error'))
        
    def get_results(self, task_id):
        url = self.url + f"api/tasks/results/{task_id}"
        headers = {'Authorization': f"Bearer {self.api_key}"}

        response = requests.get(url, headers=headers)
        response_data = response.json()

        results = [item['result'] for item in response_data.get('data', [])]
        return results