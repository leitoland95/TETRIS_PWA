```python
from pydantic import BaseModel

class TetrisGame(BaseModel):
    id: int
    score: int
    level: int

class TetrisGameCreate(BaseModel):
    score: int
    level: int

class TetrisGameUpdate(BaseModel):
    score: int | None
    level: int | None
```