import pygame

pygame.init()
ancho, alto = 800, 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Atari Pong - Estudiante 1er Semestre")

blanco = (255, 255, 255)
negro = (0, 0, 0)
reloj = pygame.time.Clock()

jugador = pygame.Rect(20, 160, 10, 80)
cpu = pygame.Rect(770, 160, 10, 80)
pelota = pygame.Rect(392, 192, 15, 15)
vel_x, vel_y = 4, 4

juego_activo = True

while juego_activo:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_activo = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and jugador.top > 0:
        jugador.y -= 5
    if teclas[pygame.K_DOWN] and jugador.bottom < alto:
        jugador.y += 5

    pelota.x += vel_x
    pelota.y += vel_y

    if pelota.top <= 0 or pelota.bottom >= alto:
        vel_y *= -1

    if pelota.colliderect(jugador) or pelota.colliderect(cpu):
        vel_x *= -1

    if pelota.left <= 0 or pelota.right >= ancho:
        pelota.center = (ancho // 2, alto // 2)
        vel_x *= -1

    pantalla.fill(negro)
    pygame.draw.rect(pantalla, blanco, jugador)
    pygame.draw.rect(pantalla, blanco, cpu)
    pygame.draw.ellipse(pantalla, blanco, pelota)
    
    pygame.display.update()
    reloj.tick(60)

pygame.quit()