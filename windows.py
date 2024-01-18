class Window:
    def __init__(self):
        self.elements = []

    def add_elements(self, elements):
        self.elements.extend(elements)

    def render(self, screen):
        for el in self.elements:
            el.render(screen)
