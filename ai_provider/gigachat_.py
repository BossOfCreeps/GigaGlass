import uuid
from io import BytesIO

import requests
from gigachat import GigaChat

from ai_provider.base import AiProvider


class GigaChatProvider(AiProvider):
    def upload_file(self, file: BytesIO, *, name: str = "document.jpg", format_: str = "image/jpeg") -> str:
        file.seek(0)
        with GigaChat(model=self.model, credentials=self.token, verify_ssl_certs=False) as giga:
            uploaded = giga.upload_file((name, file, format_), purpose="general")
            return uploaded.id_

    def list_files(self):
        with GigaChat(model=self.model, credentials=self.token, verify_ssl_certs=False) as giga:
            files = giga.get_files()
            return [{"id": file.id_, "name": file.filename} for file in files.data]

    def _get_access_token(self):
        response = requests.post(
            "https://ngw.devices.sberbank.ru:9443/api/v2/oauth",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json",
                "RqUID": str(uuid.uuid4()),
                "Authorization": f"Basic {self.token}",
            },
            data="scope=GIGACHAT_API_PERS",
            verify=False,
        )
        response.raise_for_status()
        return response.json()["access_token"]

    def get_file(self, file_id: str):
        access_token = self._get_access_token()

        response = requests.get(
            f"https://gigachat.devices.sberbank.ru/api/v1/files/{file_id}",
            headers={"Accept": "application/json", "Authorization": f"Bearer {access_token}"},
            verify=False,
        )
        response.raise_for_status()
        data = response.json()
        return {"id": data["id"], "name": data["filename"]}


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    provider = GigaChatProvider("GigaChat-2-Lite", str(os.getenv("GIGACHAT_AUTH_KEY")))
    with open("1.jpg", "rb") as img_file:
        id_ = "0b8ff518-d696-4520-9729-bf3e11ff4ada"  # provider.upload_file(BytesIO(img_file.read()))

    provider.download_file(id_)
