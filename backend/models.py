from __future__ import annotations
from typing import Optional, List, Dict, Any
from sqlmodel import SQLModel, Field, Column, JSON

class Modifier(SQLModel):
    id: str
    name: str
    enabled: bool = True
    # Ejemplos de targets:
    # "attack_misc", "damage_misc", "ac_deflection", "save_resistance",
    # "ability_enhancement.DEX", "initiative_misc"
    target: str
    value: int
    type: str = "untyped"   # para stacking futuro
    source: str = "manual"

class CharacterData(SQLModel):
    # Base
    abilities_base: Dict[str, int] = {"STR":10, "DEX":10, "CON":10, "INT":10, "WIS":10, "CHA":10}
    size_mod: int = 0  # 3.5: Small +1 AC/atk, Large -1, etc.

    # Combate
    hp_max: int = 10
    hp_current: int = 10

    armor_bonus: int = 0
    shield_bonus: int = 0
    natural_armor: int = 0

    # Clases/niveles (MVP simple: un total de BAB y saves; luego lo hacemos por clase)
    bab: int = 0
    save_fort_base: int = 0
    save_ref_base: int = 0
    save_will_base: int = 0

    # Misceláneos
    ac_misc: int = 0
    attack_misc: int = 0
    damage_misc: int = 0
    init_misc: int = 0
    speed: int = 30

    modifiers: List[Modifier] = []

class Character(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = ""
    player: str = ""
    data: Dict[str, Any] = Field(default_factory=dict, sa_column=Column(JSON))
