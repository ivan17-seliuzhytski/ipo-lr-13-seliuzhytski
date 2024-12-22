from PIL import ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_emboss_filter(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        return self.image

    def add_watermark(self, text="Вариант 5"):
        width, height = self.image.size
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("arial.ttf", 40)
        
        # Используем textbbox для получения размеров текста
        textbbox = draw.textbbox((0, 0), text, font=font)
        textwidth = textbbox[2] - textbbox[0]
        textheight = textbbox[3] - textbbox[1]

        # Позиция текста в нижнем правом углу
        x = width - textwidth - 10
        y = height - textheight - 10

        # Добавление полупрозрачного текста
        draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))
        return self.image