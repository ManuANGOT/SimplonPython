# Distanciel
from __future__ import annotations
import math
import random
 
class Node:
    def __init__(self, value:any) -> None:
        self.value = value
        self.children = []

    def __str__(self) -> str:
        return str(self.value)
    
    def add_road(self, node:Node) -> None:
        self.children.append(node)