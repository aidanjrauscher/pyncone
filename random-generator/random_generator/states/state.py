import pynecone as pc
import requests
import json 

class State(pc.State):
    randomNumber: int = None
    maxNumberInput: str = None
    maxNumber: int = None


    def set_random(self):
        print("start")
        if self.maxNumber is None:
            print("hello")
            response = requests.get("https://random.aidanjrauscher.com/random")
            content = response.content.decode()
            data = json.loads(content)
            num = data["num"]
            self.randomNumber = num
        else:
            response = requests.get(f'https://random.aidanjrauscher.com/random/{self.maxNumber}')
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
        print(self.maxNumber)
