import pygame

class ReproductorAudio:
    def __init__(self, num_canales=2):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(num_canales)

    def reproducir_audio(self, ruta, canal=0):
        pygame.mixer.Channel(canal).play(pygame.mixer.Sound(ruta))

    def detener_audio(self, canal=0):
        pygame.mixer.Channel(canal).stop()

