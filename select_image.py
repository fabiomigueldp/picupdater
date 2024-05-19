import random
import os

images = [f'http://torbware.space/images/owner{i}.jpg' for i in range(1, 58)]
selected_image = random.choice(images)
print(selected_image)
