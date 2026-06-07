import os
import re
import zipfile

from models.message import Message


class WhatsAppParser:

    def extract_zip(
        self,
        zip_path
    ):

        extract_dir = (
            f"storage/extracted/"
            f"{os.path.basename(zip_path)}"
        )

        os.makedirs(
            extract_dir,
            exist_ok=True
        )

        with zipfile.ZipFile(
            zip_path,
            "r"
        ) as zip_ref:

            zip_ref.extractall(
                extract_dir
            )

        return extract_dir


    def find_chat_file(
        self,
        extract_dir
    ):

        for root, dirs, files in os.walk(
            extract_dir
        ):

            for file in files:

                if file.endswith(".txt"):

                    return os.path.join(
                        root,
                        file
                    )

        return None


    def parse_chat(
        self,
        chat_file,
        persona_id
    ):

        pattern = re.compile(
            r"^(\d{1,2}/\d{1,2}/\d{2,4}),\s(.*?)\s-\s(.*?):\s(.*)"
        )

        messages = []

        with open(
            chat_file,
            "r",
            encoding="utf-8"
        ) as file:

            lines = file.readlines()

        for line in lines:

            match = pattern.match(
                line.strip()
            )

            if not match:
                continue

            date = match.group(1)

            sender = match.group(3)

            content = match.group(4)

            messages.append(
                Message(
                    persona_id=persona_id,
                    sender=sender,
                    content=content,
                    message_date=date
                )
            )

        return messages