from paket.image_handler import ImageHandler
from paket.image_processor import ImageProcessor

if __name__ == "__main__":
    handler = ImageHandler("paket/image_1.jpg")
    handler.load_image()
    handler.scale_image()
    handler.save_with_date()
    processor = ImageProcessor(handler.image)
    processor.apply_emboss_filter()
    processor.add_watermark()
    processor.image.save("paket/processed_image.jpg")
