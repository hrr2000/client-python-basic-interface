from server import BaseMLModel

def myfunc(name):
    return "Hello " + name

class TestModel(BaseMLModel):
    def run(self, **kwargs):
        return myfunc(name=kwargs['name'])