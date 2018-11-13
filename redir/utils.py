import uuid
from .models import ShortURL


def code_generator():
    uri = str(uuid.uuid4())[:5]
    uri_exists = ShortURL.objects.filter(short_url=uri).exists()
    if uri_exists:
        code_generator()
    return uri
