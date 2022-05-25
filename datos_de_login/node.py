from typing import Optional, TypeVar


T = TypeVar('T')


class Node:
    def __init__(self, correo: str, password: str, puesto: str, codigo: int, nombre: str, estado: bool):
        self.nombre: Optional[str] = nombre
        self.correo: Optional[str] = correo
        self.codigo: Optional[int] = codigo
        self.password: Optional[str] = password
        self.puesto: Optional[str] = puesto
        self.estado: bool = estado
        self.next: Optional[Node] = None

    def __str__(self):
        return f"{self.correo}"
