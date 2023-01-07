# client-python-basic-interface
A simple interface that creates very basic http server with python to connect between python project like a ML model and JS clients or servers for demo purposes, DON'T USE IN PRODUCTION


## How To Use
- Put 3 files any where in your project.
- Open ``` use.py ``` file
- You will find a ``` TestModel ``` class, feel free to edit or remove it, It's just an example how you can use the script.
- Write your own class and extend it from ``` BaseMLModel ``` and override ``` run() ``` function with your logic like calling your model function

```py
# your function 
def myfunc(name):
    return "Hello " + name
    
# your class 
class TestModel(BaseMLModel):
    # **kwargs contains all parameters you have sent from your client ex. frontend.
    def run(self, **kwargs):
        # call your function
        return myfunc(name=kwargs['name'])
```

- Just run ``` python server.py ``` and you will see ``` Server started http://localhost:8080 ``` and you can stop it by interrupting the command.
- You are done now.

## Client side 
- You can call the host main endpoint and it supports only 1 POST request with.
- ``` model_name ``` string parameter which contains the exact name of your class
- ``` paramters ``` in a JSON form.
- Or just use the client function in the ``` MLInterface.js ``` file.
in HTML
```html
<script src="MLInterface.js"></script>
<script>
  runModel('TestModel', {
    name: "Mostafa"
  }).then((result) => {
    console.log(result)
  })
</script>
```

## Change port
- You can change your default port if you have a conflict from ``` server.py ``` file.
```py
# ...
# basic server

HOSTNAME = "localhost"
PORT = 8080
# ...
```
