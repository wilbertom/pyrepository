from .repository import Repository
import uuid


class InMemoryRepository(Repository):

    def __init__(self):
        self._store = {}

    def add(self, record):
        record.uid = self._new_uid()
        self._store[record.uid] = record
        
        return self

    def get(self, uid):
        return self._store.get(uid)

    def all(self):
        return list(self._store.values())

    def delete(self, uid):
        return self._store.pop(uid, None) is not None

    def update(self, record):
        raise NotImplementedError

    def _new_uid(self):
        return uuid.uuid4()
