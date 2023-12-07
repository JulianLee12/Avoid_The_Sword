import pygame, random

# Initialize Surface
pygame.init()

#Display Surface
Width = 1000
Height  = 400
display = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Avoid the Sword or Die!!")


#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#Set the game values
LIVES = 5
DRAGON_SPEED = 5
SWORD_STARTING_SPEED = 2
SWORD_ACCELERATION = 0.005
SWORD_DISTANCE = 100



score = 0
dragon_lives = LIVES
sword_speed = SWORD_STARTING_SPEED









#Set colors
RED = (223,41,53)
BLUE = (55,114,225)
YElLOW = (253,202,64)
GREEN = (12,206,107)





#Set backround color
# display.fill(GREEN)
# pygame.display.flip()





#Set Fonts

font = pygame.font.Font('dragonFont.otf',32)












#Set texts



score_text = font.render(f"Score: {score}", True,BLUE)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10,10)



title_text = font.render(f"DODGE THE SWORD", True,BLUE)
title_text_rect = title_text.get_rect()
title_text_rect.y = 10
title_text_rect.centerx = Width/2


lives_text = font.render(f"Lives: {dragon_lives}", True,BLUE)
lives_text_rect = score_text.get_rect()
lives_text_rect.topright = (Width-10,10)


gameover_text = font.render(f"GAME OVER:", True,BLUE)
gameover_text_rect = gameover_text.get_rect()
gameover_text_rect.center = (Width//2,Height//2)

continue_text = font.render(f"PRESS ANY KEY TO CONTINUE", True,BLUE)
continue_text_rect = gameover_text.get_rect()
continue_text_rect.center = (Width//2,Height//2+35)




#Set sounds and Music

hit_sound = pygame.mixer.Sound("hitsword.mp3")
miss_sound = pygame.mixer.Sound("misssword.mp3")
hit_sound.set_volume(0.1)
miss_sound.set_volume(0.1)
pygame.mixer.music.load("dragonmusic.mp3")
pygame.mixer.music.set_volume(0.1)















#Set images


dragon_image = pygame.image.load("dragon.png")

dragon_image = pygame.transform.scale(dragon_image, (100,100))

dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.left = 32
dragon_image_rect.centery = Height/2

sword_image = pygame.image.load("sword.png")

sword_image = pygame.transform.scale(sword_image, (200,100))

sword_image_rect = sword_image.get_rect()
sword_image_rect.x = Width + SWORD_DISTANCE
sword_image_rect.y = random.randint(65,Height)














































































#The main game loop
pygame.mixer.music.play(-1,0,0)
gameOn = True
while gameOn:
    #Check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False





    keys = pygame.key.get_pressed()
    if(keys[pygame.K_UP] and dragon_image_rect.top > 65):
        dragon_image_rect.y -= DRAGON_SPEED
    if (keys[pygame.K_DOWN] and dragon_image_rect.bottom < Height):
        dragon_image_rect.y += DRAGON_SPEED


    if  sword_image_rect.x < 0:
        score += 1
        miss_sound.play()
        sword_image_rect.x = Width + SWORD_DISTANCE
        sword_image_rect.y = random.randint(65, Height - 32)
    else:
        sword_image_rect.x -= SWORD_STARTING_SPEED
        if(SWORD_STARTING_SPEED < 15):
            SWORD_STARTING_SPEED += SWORD_ACCELERATION


    if(dragon_image_rect.colliderect(sword_image_rect)):
        LIVES -=1
        hit_sound.play()
        sword_image_rect.x = Width + SWORD_DISTANCE
        sword_image_rect.y = random.randint(65, Height - 32)



    score_text = font.render("Score: " + str(score), True, BLUE)
    lives_text = font.render("Lives: " + str(LIVES), True, BLUE)

    if LIVES == 0:
        display.blit(gameover_text, gameover_text_rect)
        display.blit(continue_text, continue_text_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        isPaused = True
        while isPaused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    LIVES = 5
                    dragon_image_rect.y = Height/2
                    SWORD_STARTING_SPEED = 5
                    sword_speed = SWORD_STARTING_SPEED
                    pygame.mixer.music.play(-1,0,0)
                    isPaused = False
                if event.type == pygame.QUIT:
                    isPaused = False
                    gameOn = False



    display.fill(GREEN)

    #Put items onto our screen
    display.blit(score_text, score_text_rect)
    display.blit(title_text, title_text_rect)
    display.blit(lives_text, lives_text_rect)
    pygame.draw.line(display, RED, (0,65), (Width, 65), 2)

    display.blit(dragon_image,dragon_image_rect)
    display.blit(sword_image,sword_image_rect)

    pygame.display.update()
    clock.tick(FPS)

























#Exit the while loop, end the game!
pygame.quit()










