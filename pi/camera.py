from picamera2 import Picamera2  # noqa
import io
from PIL import Image


class Camera:
    def __init__(self):
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_still_configuration())
        self.picam2.start()

    def capture(self):
        image_array = self.picam2.capture_array()

        # Конвертация в PIL Image
        image = Image.fromarray(image_array)

        # Сохранение в BytesIO
        bytes_io = io.BytesIO()
        image.save(bytes_io, format="JPEG", quality=85)
        bytes_io.seek(0)

        return bytes_io


# Использование
if __name__ == "__main__":
    camera = Camera()

    image_bytes = camera.capture()
    print(f"Размер изображения: {len(image_bytes.getvalue())} байт")

    # Можно сохранить в файл
    with open("capture.jpg", "wb") as f:
        f.write(image_bytes.getvalue())
