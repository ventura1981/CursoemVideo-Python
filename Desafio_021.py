# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
import os

pygame.init()
pygame.display.set_mode((200,100))
if os.path.exists('exalta.mp3'):
    print("Arquivo encontrado")
else:
    print("Arquivo não encontrado")
pygame.mixer.music.load('exalta.mp3')
pygame.mixer.music.play(0)
pygame.mixer.music.set_volume(5)

clock = pygame.time.Clock()
clock.tick(10)

while pygame.mixer.music.get_busy():
   pygame.event.poll()
   clock.tick(10)

print("Chupa Mundo!!! MP3 Player Funfando")
pygame.


