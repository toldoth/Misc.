import random
import pygame
background_colour = (255,255,255)
(width, height) = (1280, 720)#<---WINDOW SIZE(width, height)---
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

tempData = []
fps = 600# <---LOOP-SPEED---
stop = 0
rg = -1

lenOfArray = 50# <---LENGTH-OF-ARRAY---

Max = height - height/lenOfArray
data = []
i = 1
while i - 1 < lenOfArray:
	data.append((Max/lenOfArray)*i)
	i += 1
i = 0
print(data)
while i < lenOfArray:
	randData = random.choice(data)
	tempData.append(randData)
	data.remove(randData)
	i += 1
data = tempData

i = 0
running = True
while running:
	green = False
	if i == len(data) - 1:
		i = 0
	if(data[i] > data[i+1]):
		temp = data[i+1]
		data[i+1] = data[i]
		data[i] = temp
		green = True
		stop = 0

	else:
		stop += 1
		if stop > lenOfArray:
			rg += 1

	i += 1

	screen.fill(background_colour)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
	offset = 0
	Ri = 0
	while Ri < len(data):
		if green and Ri == i:
			pygame.draw.rect(screen, (0, 255, 0), (offset + 1, height - data[Ri], width/lenOfArray - 2, data[Ri]))
		elif rg + 1 > Ri:
			pygame.draw.rect(screen, (0, 255, 0), (offset + 1, height - data[Ri], width/lenOfArray - 2, data[Ri]))			
		else:
			pygame.draw.rect(screen, (0, 0, 0), (offset + 1, height - data[Ri], (width/lenOfArray) - 2, data[Ri]))
		offset += width/lenOfArray
		Ri += 1
	if rg == lenOfArray:
		fps = 15

	pygame.display.flip()
	clock.tick(fps)