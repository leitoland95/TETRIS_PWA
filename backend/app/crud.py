from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TetrisGame(BaseModel):
    id: int
    score: int
    level: int

@app.get("/tetris_games/")
async def read_tetris_games():
    return [{"id": 1, "score": 100, "level": 1}]

@app.post("/tetris_games/")
async def create_tetris_game(tetris_game: TetrisGame):
    return tetris_game

@app.get("/tetris_games/{tetris_game_id}")
async def read_tetris_game(tetris_game_id: int):
    return {"id": tetris_game_id, "score": 100, "level": 1}

@app.put("/tetris_games/{tetris_game_id}")
async def update_tetris_game(tetris_game_id: int, tetris_game: TetrisGame):
    return tetris_game

@app.delete("/tetris_games/{tetris_game_id}")
async def delete_tetris_game(tetris_game_id: int):
    return {"message": "Tetris game deleted"}