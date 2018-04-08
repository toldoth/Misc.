import random
import pygame
background_colour = (255,255,255)
(width, height) = (1280, 720)#<---WINDOW SIZE(width, height)---
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

Sorted = []
tempData = []
fps = 60# <---LOOP-SPEED---
stop = 0
rg = -1
rendering = True

lenOfArray = 150# <---LENGTH-OF-ARRAY---

Max = height - height/lenOfArray
data = []
i = 1
while i - 1 < lenOfArray:
	data.append((Max/lenOfArray)*i)
	i += 1
i = 0
while i < lenOfArray:
	randData = random.choice(data)
	tempData.append(randData)
	data.remove(randData)
	i += 1
data = tempData

Sorted.append(data[0])
del data[0]
running = True
while running:

	I = 1
	if len(data) > 0:
		Running = True
		Sorted.append(data[0])
		del data[0]
	while Running:	
		if Sorted[-I] < Sorted[-I - 1]:
			temp = Sorted[-I]
			Sorted[-I] = Sorted[-I - 1]
			Sorted[-I - 1] = temp
			I += 1
			if len(Sorted) == I:
				Running = False
		else:
			Running = False
		

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False


	if rendering:	
		screen.fill(background_colour)
	
	
		offset = 0
		Ri = 0
		while Ri < len(data):
			pygame.draw.rect(screen, (0, 0, 0), (offset + 1, height - data[Ri], (width/lenOfArray) - 2, data[Ri]))
			offset += width/lenOfArray
			Ri += 1
		Ri = 0
		if len(data) == 0:
			rg += 1
			fps = 600
			if rg > len(Sorted):
				fps = 10
				rendering = False
		while Ri < len(Sorted):
			if Ri < rg:
				pygame.draw.rect(screen, (0, 255, 0), (offset + 1, height - Sorted[Ri], (width/lenOfArray) - 2, Sorted[Ri]))
			else:
				pygame.draw.rect(screen, (0, 0, 0), (offset + 1, height - Sorted[Ri], (width/lenOfArray) - 2, Sorted[Ri]))
			offset += width/lenOfArray
			Ri += 1
		
		
		
		pygame.display.flip()
	clock.tick(fps)