import pygame # import library
pygame.init()

# Create the window
win = pygame.display.set_mode((800, 600))

imge = pygame.image.load('assets\mountains.gif')
imge = pygame.transform.scale(imge, (800, 450))


spritesheet = pygame.image.load('assets\mountains.gif').convert()

img = pygame.image.load('assets\hero\sliced\spellun-sprite.png')
x= 200
y=400

spritesheet = pygame.image.load('assets\hero\sliced\spellun-sprite.png').convert()

prin = pygame.image.load('assets\hero\princess.png').convert_alpha()
prin = pygame.transform.scale(prin, (50, 80))

spritesheet = pygame.image.load('assets\hero\princess.png').convert_alpha()

font = pygame.font.SysFont("arial", 72)
text = font.render("The brave knight", True, (255, 255, 255))


smol_img = pygame.Surface([16, 16]).convert()
smol_img.blit(spritesheet, (0, 0), (0, 0, 16, 16))

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

      
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    x -= 1
  if keys[pygame.K_RIGHT]:
    x += 1
  if keys[pygame.K_UP]:
    y -= 1
  if y<410:
    y += 0.5
  
  


# Game code starts here ---------------------
  win.fill((192, 167, 135))
  win.blit(imge, (0, 0))
  win.blit(img, (x, y))
  win.blit(prin, (500, 410))
  win.blit(text, (120, 160))
  keys=pygame.key.get_pressed()

  
  
  
  



  
  #Update the display
  pygame.display.update()

print("Ending game")
pygame.quit()
