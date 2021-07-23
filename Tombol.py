'''
import pygame
pygame.init()

lebar = 530
panjang = 650
jend = pygame.display.set_mode((lebar, panjang))

class tombol():
	def __init__(self, color, x, y, lebar, panjang, teks=''):
		self.color = color
		self.x = x
		self.y = y
		self.lebar = lebar
		self.panjang = panjang
		self.teks = teks
		
	def draw(self, win, outline=None):
		if outline:
			pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.lebar+4, self.panjang+4), 0)
		
		pygame.draw.rect(win, self.color, (self.x, self.y, self.lebar, self.panjang), 0)
		
		if self.teks != '':
			font = pygame.font.SysFont("comicsans", 30)
			teks = font.render(self.teks, 1, (0,0,0))
			win.blit(teks, (self.x + (self.lebar/2 - teks.get_width()/2), self.y + (self.panjang/2 - teks.get_height()/2)))
	
	def isOver(self, pos):
		if pos[0] > self.x and pos[0] < self.x + self.lebar:
			if pos[1] > self.y and pos[1] < self.y + self.panjang:
				return True
		
		return False
		
		
		
def GambarWindow():
	jend.fill((255,255,255))
	tombol_game.draw(jend)
 
run = True
tombol_game = tombol((0,255,0), 100, 330, 100, 50, "Mulai!!!")		
while run:
	GambarWindow()
	pygame.display.update()

	for event in pygame.event.get():
		pos = pygame.mouse.get_pos()
		
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			if tombol_game.isOver(pos):
				print("Oke!")
		
		if event.type == pygame.MOUSEMOTION:
			if tombol_game.isOver(pos):
				tombol_game.color = (255,0,0)
			else:
				tombol_game.color = (0,255,0)
'''
import pygame
import os
import random
pygame.init()


lebar = 530
panjang = 650 
jend = pygame.display.set_mode((lebar, panjang))
pygame.display.set_caption("Game Tabrak Lari")

waktu = pygame.time.Clock()

gambarMobil = pygame.image.load("Ucycf5C2.png")
gambarLawan = pygame.image.load("Lawan Arah.png")
gambarBackground = pygame.image.load("701fed9bd55ea18.png")
gambarIcon = pygame.image.load("Lawan Arah Icon.png")

pygame.display.set_icon(gambarIcon)

laguBackground = pygame.mixer.music.load("Undertale OST - Snowy Extended.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

laguTabrak = pygame.mixer.Sound("bounce.wav")

hijau = (0, 255, 0)
merah = (255, 0, 0)
biru = (0, 0, 255)
class mobil_player(object):
	def __init__(self, x, y, lebar, panjang):
		self.x = x
		self.y = y
		self.lebar = lebar
		self.panjang = panjang
		self.kep = 10
		self.hitbox = (self.x + 0, self.y + 0, 67, 120)
		
	def draw(self, jend):
		jend.blit(gambarMobil, (self.x, self.y))
		self.hitbox = (self.x + 2, self.y + 0, 62, 120)
		#pygame.draw.rect(jend, (255,0,0), self.hitbox, 2)
	'''
	def tabrakan(self):
		global skor 
		self.x = (random.randrange(0, lebar))
		self.y = (random.randrange(0, panjang))
		
		font = pygame.font.SysFont("comicsans", 30, True)
		teks = font.render("Kamu Tabrakan Kawan :L", 1, (255,255,255))
		jend.blit(teks, (265 - (teks.get_width()/2), 200))
		
		font = pygame.font.SysFont("comicsans", 30, True)
		teks = font.render("Skor: "+ str(skor), 1, (255,255,255))
		jend.blit(teks, (265 - (teks.get_width()/2), 300))
		
		pygame.display.update()
		
		i = 0 
		while i < 200:
			pygame.time.delay(10)
			i += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
					i = 301
					jend.blit(gambarBackground, (0,0))
					mobil.draw(jend)
	'''		
class mobil_lawan(object):
	def __init__(self, x, y, lebar, panjang):
		self.x = x
		self.y = y
		self.lebar = lebar
		self.panjang = panjang 
		self.kep = 7
		self.hitbox = (self.x + 20, self.y + 12, 44, 44)
	
	def draw(self, jend):
		self.gerakkan()
		jend.blit(gambarLawan, (self.x, self.y))
		self.hitbox = (self.x + 2, self.y + 0, 62, 120)
		#pygame.draw.rect(jend, (255,0,0), self.hitbox, 2)
		
	
	def gerakkan(self):
		self.y += self.kep
		

		
def gambarWindow():
	jend.blit(gambarBackground, (0,0))
	mobil.draw(jend)
	mobil_musuh.draw(jend)

def pygame_quit():
	pygame.quit()
	quit()

def teks_object(teks, font):
	teksSurf = font.render(teks, True, (0,0,0))
	return teksSurf, teksSurf.get_rect()
	
def tombol(pesan, x, y, lebar, panjang, warna2, warna1, action=None):
	mouse = pygame.mouse.get_pos()
	klik = pygame.mouse.get_pressed()
	#print(klik)

	if x+lebar > mouse[0] > x and y+panjang > mouse[1] > y:
		pygame.draw.rect(jend, warna2, (x,y,lebar,panjang))
		if klik[0] == 1 and action != None:
			action()
	
	else:
		pygame.draw.rect(jend, warna1, (x,y,lebar,panjang))
	
	teksKecil = pygame.font.SysFont("comicsans", 40)
	teksSurf, teksRect = teks_object(pesan, teksKecil)
	teksRect.center = ((x+(lebar/2)), (y + (panjang/2)))
	jend.blit(teksSurf, teksRect)

def game_intro():
	intro = True
	
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		jend.blit(gambarBackground, (0,0))
		font = pygame.font.SysFont("comicsans", 50)
		teks = font.render("Mari Main Sini :>", 1, (0,0,0))
		jend.blit(teks, (265 - (teks.get_width()/2), 250))
		
		font = pygame.font.SysFont("comicsans", 20)
		teks = font.render("Musik Oleh Toby Fox", 1, (0,0,0))
		jend.blit(teks, (20, 10))
		
		tombol("Mulai!", 100, 300, 100, 50, merah, hijau, game_loop)
		tombol("Keluar!", 300, 300, 100, 50, merah, biru, pygame_quit)
		
		pygame.display.update()
		waktu.tick(200)

def game_kalah():
	global mobil, mobil_musuh, skor, speed
	mobil = mobil_player(265 - (gambarMobil.get_width()/2), 325, 67, 120)
	mobil_musuh = mobil_lawan(random.randrange(0, lebar), -200, 67, 120)
	speed = 30
	skor = 0
	
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
	
		#jend.blit(bg, (0,0))
		font = pygame.font.SysFont("comicsans", 80)
		teks = font.render("Kamu Mati!", 1, (merah))
		jend.blit(teks, (265 - (teks.get_width()/2), 250))
		
		tombol("Lanjut!", 100, 300, 100, 50, merah, hijau, game_loop)
		tombol("Keluar!", 300, 300, 100, 50, merah, biru, pygame_quit)
		
		pygame.display.update()
		waktu.tick(200)
	
	
	
def unpause():
	global pause
	pause = False

def paused():
	global pause
	
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		#jend.blit(gambarBackground, (0,0))
		font = pygame.font.SysFont("comicsans", 50)
		teks = font.render("Game Paused", 1, (0,0,0))
		jend.blit(teks, (265 - (teks.get_width()/2), 250))
		
		font = pygame.font.SysFont("comicsans", 20)
		teks = font.render("Musik Oleh Toby Fox", 1, (0,0,0))
		jend.blit(teks, (20, 10))
		
		tombol("Lanjut!", 100, 300, 100, 50, merah, hijau, unpause)
		tombol("Keluar!", 300, 300, 100, 50, merah, biru, pygame_quit)
		
		pygame.display.update()
		waktu.tick(200)
'''
def crash():

	font = pygame.font.SysFont("comicsans", 50)
	teks = font.render("Kamu Tabrakan", 1, (0,0,0))
	jend.blit(teks, (265 - (teks.get_width()/2), 250))
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		#jend.blit(gambarBackground, (0,0))
		
		font = pygame.font.SysFont("comicsans", 20)
		teks = font.render("Musik Oleh Toby Fox", 1, (0,0,0))
		jend.blit(teks, (20, 10))
		
		tombol("Mulai!", 100, 300, 100, 50, merah, hijau, game_loop)
		tombol("Keluar!", 300, 300, 100, 50, merah, biru, pygame_quit)
		
		pygame.display.update()
		waktu.tick(200)
'''
pause = True
mobil = mobil_player(265 - (gambarMobil.get_width()/2), 325, 67, 120)
mobil_musuh = mobil_lawan(random.randrange(0, lebar), -200, 67, 120)
skor = 0
paused = 0
tabrakspeed = 0
speed = 30

def game_loop():
	global skor
	global pause
	global paused, tabrakspeed, speed
	run = True

	
	while run:
		
		skor += 1
		font = pygame.font.SysFont("comicsans", 30)
		teks = font.render("Skor: 00" + str(skor), 1, (255,255,255))
		jend.blit(teks, (20,20))
		
		waktu.tick(speed)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		## Mobil random keluar
		if mobil_musuh.y > panjang:
			mobil_musuh.x = random.randrange(0, lebar)
			mobil_musuh.y = 0 - mobil_musuh.panjang
			mobil_musuh.kep += 1
		
		### Tabrak mobil 
		if mobil.hitbox[1] < mobil_musuh.hitbox[1] + mobil_musuh.hitbox[3] and mobil.hitbox[1] + mobil.hitbox[3] > mobil_musuh.hitbox[1]:
			if mobil.hitbox[0] + mobil_musuh.hitbox[2] > mobil_musuh.hitbox[0] and mobil.hitbox[0] < mobil_musuh.hitbox[0] + mobil_musuh.hitbox[2]:
				laguTabrak.play()
				mobil_musuh.kep = 7
				skor = 0
				game_kalah()
				#if paused == 0:
					#tabrakspeed = speed
					#paused = 1
					
		
		### Tabrak Border
		if mobil.x > lebar - mobil.lebar or mobil.x < 0:
			laguTabrak.play()
			mobil_musuh.kep = 7
			skor = 0
			game_kalah()
			#if paused == 0:
				#tabrakspeed = speed
				#paused = 1
		
		
		### Tombol
		tombol = pygame.key.get_pressed()
		
		if tombol[pygame.K_w]:
			mobil.y -= mobil.kep
		
		if tombol[pygame.K_s]:
			mobil.y += mobil.kep
		
		if tombol[pygame.K_a]:
			mobil.x -= mobil.kep
		
		if tombol[pygame.K_d]:
			mobil.x += mobil.kep
		
		if tombol[pygame.K_ESCAPE]:
			pause = True
			paused()
			
		
		gambarWindow()
	
game_intro()
game_loop()
pygame.quit()
quit()

	
	
	
	
	
	
	
	
	
	
	
	
	
	