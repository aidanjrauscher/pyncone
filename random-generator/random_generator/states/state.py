import pynecone as pc
import requests
import json 

class State(pc.State):
    randomNumber: int = None
    maxNumber: int = None

    maxNumberInput: str = ""

    def set_random(self):
        url = self.api_url
        response = requests.get(url)
        content = response.content.decode()
        data = json.loads(content)
        num = data["num"]
        self.randomNumber = num

    def set_max(self, input):
        self.maxNumberInput = input
        if self.maxNumberInput.isdigit():
            self.maxNumber = int(self.maxNumberInput)
        else:
            self.maxNumber = None

    @pc.var
    def api_url(self) -> str:
        return f'https://random.aidanjrauscher.com/random/{self.maxNumber}' if self.maxNumber is not None else "https://random.aidanjrauscher.com/random"