import pygame
from sys import exit
import math


pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Two Player Parking Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 45)


def rotate_image(image, angle, pos):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=pos).center)
    return rotated_image, new_rect


def stop_game():
    global running
    running = False


background = pygame.image.load('parking_assets_map (1).png').convert_alpha()
background = pygame.transform.scale(background, (400, 400))


pink_car = pygame.image.load('pinkcar.png').convert_alpha()
pink_car_rect = pink_car.get_rect(center=(200, 200))
pink_car_mask = pygame.mask.from_surface(pink_car)


parking_spot_1 = pygame.Surface((100, 45), pygame.SRCALPHA)
parking_spot_1.fill((245, 95, 205, 128))
parking_spot_mask_1 = pygame.mask.from_surface(parking_spot_1)


parking_spot_2 = pygame.Surface((100, 45), pygame.SRCALPHA)
parking_spot_2.fill((95, 183, 245, 128))
parking_spot_mask_2 = pygame.mask.from_surface(parking_spot_2)


sidewalk_1 = pygame.Surface((250, 65), pygame.SRCALPHA)
sidewalk_1_pos = (9, 27)
sidewalk_1.fill((252, 3, 3, 128))
sidewalk_1_mask = pygame.mask.from_surface(sidewalk_1)


sidewalk_2 = pygame.Surface((100, 265), pygame.SRCALPHA)
sidewalk_2_pos = (9, 90)
sidewalk_2.fill((252, 3, 3, 128))
sidewalk_2_mask = pygame.mask.from_surface(sidewalk_2)


sidewalk_3 = pygame.Surface((155, 65), pygame.SRCALPHA)
sidewalk_3_pos = (108, 288)
sidewalk_3.fill((252, 3, 3, 128))
sidewalk_3_mask = pygame.mask.from_surface(sidewalk_3)


blue_car = pygame.image.load('bluecar.png').convert_alpha()
blue_car_rect = blue_car.get_rect(center=(200, 300))
blue_car_mask = pygame.mask.from_surface(blue_car)


text_surface = test_font.render('2 Player Parking Game', False, 'Black')
blue_win_surface = test_font.render('Blue Wins', False, 'Green')
pink_win_surface = test_font.render('Pink Wins', False, 'Green')
both_win_surface = test_font.render('Double Win', False, 'Green')
lose_surface = test_font.render('You Lose', False, 'Red')


pink_car_pos = [20, 360]
pink_car_angle = 0
blue_car_pos = [20, 378]
blue_car_angle = 0


running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_game()


    control = pygame.key.get_pressed()
    if control[pygame.K_LEFT]:
        pink_car_angle += 5
    elif control[pygame.K_RIGHT]:
        pink_car_angle -= 5
    elif control[pygame.K_UP]:
        pink_car_pos[0] += 5 * math.cos(math.radians(-pink_car_angle))
        pink_car_pos[1] += 5 * math.sin(math.radians(-pink_car_angle))
    elif control[pygame.K_DOWN]:
        pink_car_pos[0] -= 5 * math.cos(math.radians(-pink_car_angle))
        pink_car_pos[1] -= 5 * math.sin(math.radians(-pink_car_angle))


    if control[pygame.K_a]:
        blue_car_angle += 5
    elif control[pygame.K_d]:
        blue_car_angle -= 5
    elif control[pygame.K_w]:
        blue_car_pos[0] += 5 * math.cos(math.radians(-blue_car_angle))
        blue_car_pos[1] += 5 * math.sin(math.radians(-blue_car_angle))
    elif control[pygame.K_s]:
        blue_car_pos[0] -= 5 * math.cos(math.radians(-blue_car_angle))
        blue_car_pos[1] -= 5 * math.sin(math.radians(-blue_car_angle))


    if pink_car_pos[0] < 0 or pink_car_pos[0] > 400 or pink_car_pos[1] < 0 or pink_car_pos[1] > 390:
        pink_car_pos = [20, 360]
        pink_car_angle = 0


    if blue_car_pos[0] < 0 or blue_car_pos[0] > 390 or blue_car_pos[1] < 0 or blue_car_pos[1] > 390:
        blue_car_pos = [20, 378]
        blue_car_angle = 0


    screen.blit(background, (0, 0))
    screen.blit(parking_spot_1, (130, 95))
    screen.blit(parking_spot_2, (130, 145))
    screen.blit(sidewalk_1, (9, 27))
    screen.blit(sidewalk_2, (9, 90))
    screen.blit(sidewalk_3, (108, 288))


    rotated_pink_car, pink_car_rect = rotate_image(pink_car, pink_car_angle, pink_car_pos)
    rotated_blue_car, blue_car_rect = rotate_image(blue_car, blue_car_angle, blue_car_pos)


    screen.blit(rotated_pink_car, pink_car_rect.topleft)
    screen.blit(rotated_blue_car, blue_car_rect.topleft)


    if pink_car_mask.overlap(parking_spot_mask_1, (pink_car_pos[0] - 130, pink_car_pos[1] - 95)) and blue_car_mask.overlap(parking_spot_mask_2, (blue_car_pos[0] - 130, blue_car_pos[1] - 150)):
        screen.blit(both_win_surface, (230, 100))
    elif pink_car_mask.overlap(parking_spot_mask_1, (pink_car_pos[0] - 130, pink_car_pos[1] - 95)):
        screen.blit(pink_win_surface, (230, 100))
    elif blue_car_mask.overlap(parking_spot_mask_2, (blue_car_pos[0] - 130, blue_car_pos[1] - 150)):
        screen.blit(blue_win_surface, (230, 100))


    if pink_car_mask.overlap(sidewalk_1_mask, (sidewalk_1_pos[0] - pink_car_pos[0], sidewalk_1_pos[1] - pink_car_pos[1])):
        screen.blit(lose_surface, (230, 100))
        stop_game()
    elif blue_car_mask.overlap(sidewalk_1_mask, (sidewalk_1_pos[0] - blue_car_pos[0], sidewalk_1_pos[1] - blue_car_pos[1])):
        screen.blit(lose_surface, (230, 100))
        stop_game()
    elif pink_car_mask.overlap(sidewalk_2_mask, (sidewalk_2_pos[0] - pink_car_pos[0], sidewalk_2_pos[1] - pink_car_pos[1])):
        screen.blit(lose_surface, (230, 100))
        stop_game()
    elif blue_car_mask.overlap(sidewalk_2_mask, (sidewalk_2_pos[0] - blue_car_pos[0], sidewalk_2_pos[1] - blue_car_pos[1])):
        screen.blit(lose_surface, (230, 100))
        stop_game()
    elif pink_car_mask.overlap(sidewalk_3_mask, (sidewalk_3_pos[0] - pink_car_pos[0], sidewalk_3_pos[1] - pink_car_pos[1])):
        screen.blit(lose_surface, (230, 100))
        stop_game()
    elif blue_car_mask.overlap(sidewalk_3_mask, (sidewalk_3_pos[0] - blue_car_pos[0], sidewalk_3_pos[1] - blue_car_pos[1])):
        screen.blit(lose_surface, (230, 100))
        stop_game()


    screen.blit(text_surface, (10, 10))


    pygame.display.update()
    clock.tick(60)
