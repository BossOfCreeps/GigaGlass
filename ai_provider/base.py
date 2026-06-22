from io import BytesIO


class AiProvider:
    def __init__(self, model: str, token: str):
        self.model = model
        self.token = token

    def upload_file(self, file: BytesIO, *, name: str, format_: str) -> str:
        raise NotImplementedError()

    def list_files(self) -> list[dict[str, str]]:
        raise NotImplementedError()

    def get_file(self, file_id: str) -> dict[str, str]:
        raise NotImplementedError()

    def models_list(self) -> list[str]:
        raise NotImplementedError()
