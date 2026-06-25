from ai_provider.gigachat_ import GigaChatProvider
from pi.camera import Camera

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    provider = GigaChatProvider("GigaChat-2-Pro", str(os.getenv("GIGACHAT_AUTH_KEY")))
    camera = Camera()

    image = camera.capture()
    id_ = provider.upload_file(image)

    provider.call("Опиши фотографию", [id_])
