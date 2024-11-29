import pygame
from game_logic import Snake, Food
from config import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, FPS, BACKGROUND_COLOR

def show_message(screen, message, font, color, position):
    """Función para mostrar un mensaje en pantalla."""
    text = font.render(message, True, color)
    screen.blit(text, position)

def reset_game():
    """Función para reiniciar el juego."""
    return Snake(), Food(), 0, 10  # Reinicia la serpiente, la comida, el puntaje y la velocidad del juego

def main():
    pygame.init()

    # Configurar la ventana del juego
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Juego Snake")

    clock = pygame.time.Clock()

    # Inicializar el estado del juego
    snake, food, score, game_speed = reset_game()

    font = pygame.font.Font(None, 36)

    # Pantalla de inicio
    show_message(screen, "Oprime cualquier tecla para iniciar", font, (255, 255, 255), (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    # Esperar a que el jugador oprima cualquier tecla para iniciar
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                waiting_for_key = False

    # Ciclo principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")

        # Mover la serpiente
        snake.move()

        # Verificar colisiones
        if snake.check_collision():
            running = False  # Fin del juego

        # Verificar si la serpiente ha comido la comida
        if snake.body[0] == food.position:
            snake.grow()  # La serpiente crece
            food.spawn()  # Generar un nuevo alimento
            score += 10  # Incrementar el puntaje
            game_speed += 1  # Aumentar la velocidad del juego

        # Dibujar fondo
        screen.fill(BACKGROUND_COLOR)

        # Dibujar la serpiente
        for segment in snake.body:
            pygame.draw.rect(screen, (0, 255, 0), (*segment, CELL_SIZE, CELL_SIZE))  # Serpiente en verde

        # Dibujar la comida
        pygame.draw.rect(screen, (255, 0, 0), (*food.position, CELL_SIZE, CELL_SIZE))  # Comida en rojo

        # Mostrar puntaje
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Actualizar la pantalla
        pygame.display.flip()

        # Ajustar FPS (velocidad del juego)
        clock.tick(game_speed)

    # Pantalla de fin de juego
    screen.fill(BACKGROUND_COLOR)
    show_message(screen, "Fin del Juego", font, (255, 0, 0), (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3))
    show_message(screen, f"Puntaje Final: {score}", font, (255, 255, 255), (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2))
    show_message(screen, "Presiona Enter para jugar de nuevo o P para salir", font, (255, 255, 255), (SCREEN_WIDTH // 6, SCREEN_HEIGHT // 1.5))
    pygame.display.flip()

    # Esperar entrada del usuario
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Tecla Enter
                    snake, food, score, game_speed = reset_game()  # Reiniciar el juego
                    main()  # Llamar de nuevo al ciclo principal del juego
                    return
                elif event.key == pygame.K_p:  # Tecla P
                    pygame.quit()  # Salir del juego
                    return

if __name__ == "__main__":
    main()

