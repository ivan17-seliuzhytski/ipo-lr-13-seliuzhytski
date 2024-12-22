from PIL import ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_emboss_filter(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        return self.imagefrom PIL import ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_emboss(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.EMBOSS)

    def add_text(self, text="Вариант 5", font_path='arial.ttf', font_size=20):
        if self.image:
            draw = ImageDraw.Draw(self.image)
            font = ImageFont.truetype(font_path, font_size)
            # Исправляем на использование textbbox
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            position = (self.image.width - text_width - 10, self.image.height - text_height - 10)
            draw.text(position, text, font=font, fill='white')

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
