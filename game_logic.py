import random

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # Cuerpo de la serpiente (lista de coordenadas)
        self.direction = "RIGHT"  # Dirección inicial de la serpiente

    def change_direction(self, new_direction):
        """Cambiar la dirección de la serpiente."""
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    def move(self):
        """Mover la serpiente en la dirección actual."""
        head_x, head_y = self.body[0]
        if self.direction == "UP":
            new_head = (head_x, head_y - 20)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 20)
        elif self.direction == "LEFT":
            new_head = (head_x - 20, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 20, head_y)
        
        self.body.insert(0, new_head)  # Agregar la nueva cabeza en la dirección
        self.body.pop()  # Eliminar el último segmento (movimiento)

    def grow(self):
        """Hacer que la serpiente crezca."""
        self.body.append(self.body[-1])  # Añadir un segmento extra al final

    def check_collision(self):
        """Verificar si la serpiente choca con sí misma o con los bordes."""
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= 640 or head_y < 0 or head_y >= 480:
            return True  # La serpiente choca con el borde
        if (head_x, head_y) in self.body[1:]:
            return True  # La serpiente choca consigo misma
        return False


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn()

    def spawn(self):
        """Genera una nueva comida en una posición aleatoria."""
        self.position = (random.randint(0, 31) * 20, random.randint(0, 23) * 20)  # 20 es el tamaño de las celdas
