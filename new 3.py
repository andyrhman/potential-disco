import pygame
import os
import random
pygame.init()


lebar = 530
panjang = 650 
jend = pygame.display.set_mode((lebar, panjang))
pygame.display.set_caption("asdfghjkl")

waktu = pygame.time.Clock()

gambarMobil = pygame.image.load(os.path.join("Mobil", "Ucycf5C2.png"))
gambarLawan = pygame.image.load(os.path.join("Mobil", "Lawan Arah.png"))
gambarBackground = pygame.image.load("701fed9bd55ea18.png")

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
		pygame.draw.rect(jend, (255,0,0), self.hitbox, 2)
		
	def tabrakan(self):
		self.x = (random.randrange(0, lebar))
		self.y = (random.randrange(0, panjang))
		font = pygame.font.SysFont("comicsans", 30, True)
		teks = font.render("Kamu Tabrakan Kawan :L", 1, (255,255,255))
		jend.blit(teks, (265 - (teks.get_width()/2), 200))
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
		pygame.draw.rect(jend, (255,0,0), self.hitbox, 2)
		
	
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
	teks_gambar = font.render(teks, True, (0,0,0))
	return teks_gambar, teks_gambar.get_rect()

def tombol(pesan, x, y, lebar, panjang, warna2, warna1, action=None):
	mouse = pygame.mouse.get_pos()
	klik = pygame.mouse.get_pressed()
	print(klik)
	
	if x+lebar > mouse[0] > x and y+panjang > mouse[1] > y:
		pygame.draw.rect(jend, warna2, (x, y, lebar, panjang))
		if klik[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(jend, warna1, (x, y, lebar, panjang))
		
	teksFont = pygame.font.SysFont("comicsans", 40)
	teksSurf, teksRect = teks_object(pesan, teksFont)
	teksRect.center = ( (x + (lebar/2)), (y + (panjang/2)) )
	jend.blit(teksSurf, teksRect)
	

def game_intro():
	intro = True
	
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		jend.fill((255,255,255))
		font = pygame.font.SysFont("comicsans", 70)
		teks = font.render("Mari Main Sini", 1, (0,0,0))
		jend.blit(teks, (265 - (teks.get_width()/2), 200))
		
		tombol("Mulai", 150, 280, 100, 50, merah, hijau, game_loop)
		tombol("Keluar", 280, 280, 100, 50, merah, biru, pygame_quit)
		
		pygame.display.update()
		waktu.tick(100)


mobil = mobil_player(265 - (gambarMobil.get_width()/2), 325, 67, 120)
mobil_musuh = mobil_lawan(random.randrange(0, lebar), -200, 67, 120)

def game_loop():
	run = True
	skor = 0
	while run:
		waktu.tick(30)
		font = pygame.font.SysFont("comicsans", 30)
		teks = font.render("Skor: 00" + str(skor), 1, (255,255,255))
		jend.blit(teks, (20,20))
		skor += 1
		
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
				mobil.tabrakan()
				mobil_musuh.kep = 7
		
		### Tabrak Border
		if mobil.x > lebar - mobil.lebar or mobil.x < 0:
			mobil.tabrakan()
			mobil_musuh.kep = 7
		
		
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
		
		
		

		
		gambarWindow()
	
game_intro()
game_loop()
pygame.quit()
quit()

	
	
	
	
	
	
	
	
	
	
	
	
	
	