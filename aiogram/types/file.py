from . import Deserializable


class File(Deserializable):
    __slots__ = ('file_id', 'file_size', 'file_path')

    def __init__(self, file_id, file_size, file_path):
        self.file_id = file_id
        self.file_size = file_size
        self.file_path = file_path

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        file_id = raw_data.get('file_id')
        file_size = raw_data.get('file_size')
        file_path = raw_data.get('file_path')

        return File(file_id, file_size, file_path)