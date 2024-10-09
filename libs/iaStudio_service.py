import ia_requests as requests

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
    "txt": "text/plain"
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
    
    def run_task(self, task_id, mode, file_path):
        file_name = file_path.split("/")[-1]
        file_extension = file_name.split(".")[-1]
        if file_extension not in FILE_TYPES:
            raise Exception("Invalid file extension. Supported extensions: mp3 for VOICE tasks, txt for TEXT tasks.")

        url = self.url + f"api/tasks/run/{task_id}"
        headers = {'Authorization': f"Bearer {self.api_key}"}
        data = {'runMode': mode}
        files=[
            ('file', (file_name, open(file_path, 'rb'), FILE_TYPES[file_extension]))
        ]
        response = requests.post(url, headers=headers, data=data, files=files)
        return response.json()
    
    def get_entities(self):
        url = self.url + "api/entities/all"
        headers = {'Authorization': f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        if response.json().get('error'):
            raise Exception(response.json().get('error'))