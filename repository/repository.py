import abc


class Repository(abc.ABC):

    @abc.abstractmethod
    def add(self, record):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, uid):
        raise NotImplementedError

    @abc.abstractmethod
    def all(self):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, record):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, record):
        raise NotImplementedError
