import logging
from fastapi import APIRouter
from . import crud, models, schemas

router = APIRouter()

@router.get("/api/v1/tetris")
async def get_tetris():
    return {"message": "Bienvenido al API de Tetris"}

@router.post("/api/v1/tetris")
async def create_tetris(tetris: schemas.Tetris):
    return crud.create_tetris(tetris)

@router.get("/api/v1/tetris/{tetris_id}")
async def get_tetris_by_id(tetris_id: int):
    return crud.get_tetris_by_id(tetris_id)

@router.put("/api/v1/tetris/{tetris_id}")
async def update_tetris(tetris_id: int, tetris: schemas.Tetris):
    return crud.update_tetris(tetris_id, tetris)

@router.delete("/api/v1/tetris/{tetris_id}")
async def delete_tetris(tetris_id: int):
    return crud.delete_tetris(tetris_id)