from .inmemory_repository import InmemoryRepository as Repository


class Record():
    
    def __init__(self):
        self.uid = None


def test_adding_a_record():
    repository = Repository()
    record = Record()
    assert repository.all() == []

    repository.add(record)

    assert repository.all() == [record]


def test_adding_a_record_sets_the_records_uid():
    repository = Repository()
    record = Record()
    assert record.uid is None

    repository.add(record)

    assert record.uid is not None


def test_adding_a_record_returns_the_repository():
    repository = Repository()
    record = Record()

    assert repository.add(record) == repository


def test_all():
    repository = Repository()
    record_1 = Record()
    record_2 = Record()
    record_3 = Record()

    repository \
        .add(record_1) \
        .add(record_2) \
        .add(record_3)

    assert repository.all() == [record_1, record_2, record_3]


def test_all_doesnt_include_records_not_added():
    repository = Repository()
    record_1 = Record()
    record_2 = Record()
    record_3 = Record()

    repository \
        .add(record_1) \
        .add(record_3)

    assert record_2 not in repository.all()


def test_get():
    repository = Repository()
    record = Record()
    repository.add(record)
    uid = record.uid

    assert repository.get(uid) == record


def test_get_returns_the_correct_record():
    repository = Repository()
    correct_record = Record()
    incorrect_record = Record()
    repository.add(correct_record)
    repository.add(incorrect_record)
    uid = correct_record.uid

    assert repository.get(uid) == correct_record


def test_get_when_a_record_doesnt_exist_by_the_uid_it_returns_none():
    repository = Repository()
    uid = 1

    assert repository.get(uid) is None


def test_delete():
    repository = Repository()
    record = Record()
    repository.add(record)
    uid = record.uid

    repository.delete(uid)

    assert repository.get(uid) is None


def test_delete_when_a_record_is_deleted_it_returns_true():
    repository = Repository()
    record = Record()
    repository.add(record)
    uid = record.uid

    assert repository.delete(uid) is True


def test_delete_when_a_record_is_not_found_it_returns_false():
    repository = Repository()
    record = Record()
    repository.add(record)
    uid = record.uid
    repository.delete(uid)

    assert repository.delete(uid) is False
