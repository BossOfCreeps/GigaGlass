from io import BytesIO


class AiProvider:
    def __init__(self, model: str, token: str):
        self.model = model
        self.token = token

    def upload_file(self, file: BytesIO):
        pass

    def list_files(self):
        pass

    def download_file(self, file_id: str):
        pass
