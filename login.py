import pygame
from pygame.locals import *
import sys

class login_class:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([400, 200])
        self.base_font = pygame.font.Font(None, 32)
        self.user_text = ''
        self.input_rect = pygame.Rect(200, 200, 140, 32)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('chartreuse4')
        self.color = self.color_passive
        self.active = False
        self.clock = pygame.time.Clock()
        self.password = ''

    def gettext(self, text):
        label = self.base_font.render(text, 1, (255,255,0))
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_rect.collidepoint(event.pos):
                        self.active = True
                    else:
                        self.active = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if text == "Password":
                            if login_class.password_validation(self.password):
                                pygame.quit()
                                return self.password
                            else:
                                #Show error message
                                return None
                        else:
                            pygame.quit()
                            return self.user_text
                    if event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                        if text == "Password":
                            self.password = self.password[:-1]
                    else:
                        if text == "Password":
                            self.user_text += "*"
                            self.password += event.unicode
                        else:
                            self.user_text += event.unicode
            self.screen.fill((0, 0, 0))
            if self.active:
                self.color = self.color_active
            else:
                self.color = self.color_passive
            pygame.draw.rect(self.screen, self.color, self.input_rect)
            text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
            self.screen.blit(text_surface, (200, 100))
            self.screen.blit(label, (80, 100))
            self.input_rect.w = max(100, text_surface.get_width()+10)
            pygame.display.flip()
            self.clock.tick(60)
    
    @staticmethod
    def password_validation(text):
        return True



		
			
			