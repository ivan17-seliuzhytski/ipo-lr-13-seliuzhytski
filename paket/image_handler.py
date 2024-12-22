from PIL import Image
import datetime

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        self.image = Image.open(self.image_path)
        return self.image

    def save_image(self, output_path):
        self.image.save(output_path)

    def scale_image(self, scale_factor=0.5):
        width, height = self.image.size
        new_size = (int(width * scale_factor), int(height * scale_factor))
        self.image = self.image.resize(new_size)
        return self.image

    def save_with_date(self):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        output_path = self.image_path.split('.')[0] + f"_{current_date}." + self.image_path.split('.')[1]
        self.save_image(output_path)