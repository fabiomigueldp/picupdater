import random
import os

images_dir = 'images'
images = [f for f in os.listdir(images_dir) if f.startswith('owner') and f.endswith('.jpg')]
selected_image = random.choice(images)
print(selected_image)
