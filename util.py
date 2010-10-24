import pygame

def load_frames(filename, w, h, colorkey=None):
    image = pygame.image.load(filename)

    frames = []
    for y in range(image.get_rect()[3] // h):
        frame = image.subsurface(0, y * h, w, h)

        if colorkey:
            frame.set_colorkey(colorkey)

        frames.append(frame)

    return frames
