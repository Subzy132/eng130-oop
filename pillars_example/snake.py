
from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return "If i can touch it i can then smell it aswell"

smart_snake = Snake()

print(f"This function is called from the grand parent class {smart_snake.breathe().upper()}")
print(f"This function is called from the parent class {smart_snake.hunt().upper()}")
print(f"This function is called from the current class {smart_snake.use_tongue_to_smell().upper()}")