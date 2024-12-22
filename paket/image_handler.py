from PIL import Image
import datetime
import os
class ImageHandler:
    def __init__(self):
        self.image = None

    def load_image(self, image_path):
        self.image = Image.open(image_path)

    def save_image(self, output_path):
        self.image.save(output_path)

    def scale_image(self, scale_factor=0.5):
        width, height = self.image.size
        new_size = (int(width * scale_factor), int(height * scale_factor))
        self.image = self.image.resize(new_size)
        return self.image
    
    def get_image(self):
        return self.image

    def save_with_date(self):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        filename, ext = os.path.splitext(output_path)
        output_path = self.image_path.split('.')[0] + f"{filename}_{current_date}{ext}"
        self.save_image(output_path)
