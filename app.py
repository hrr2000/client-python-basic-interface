class BaseMLModel():
    # this function receives the frontend parameters and sends them to your function ex: return myfunc(**kwargs)
    def run(self, **kwargs):
        return None

    # this function parses your "run function return value" to be a string 
    # so override this with your own parser if you have to do
    def parse(self, data):
        return str(data)

    def get_results(self, **kwargs):
        return self.parse(self.run(**kwargs))