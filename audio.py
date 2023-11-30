# audio.py
import pygame
import threading

def play_audio(file_path):
    def audio_thread():
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    # Byrjar hljóðið í nýju thread
    thread = threading.Thread(target=audio_thread)
    thread.start()
