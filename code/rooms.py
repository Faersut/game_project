import pygame


class Room:
    def __init__(self):
        self.objects = []

    def add_objects(self, *obj):
        self.objects.extend(obj)

    def render(self, screen):
        for obj in self.objects:
            obj.render(screen)