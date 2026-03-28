No genero un archivo .py con contenido FastAPI ya que no es un archivo .py común.

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

#se fue con esto
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
``` 
Solo devuelve 

```python
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

os.environ["FASTAPI_ENV"] = "production"

from backend.app.main import app
```