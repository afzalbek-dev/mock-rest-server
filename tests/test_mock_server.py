import pytest
from mock_server.generator import SchemaDataGenerator
from mock_server.server import MockRESTEngine


def test_schema_generator():
    schema = {"id": "id", "name": "name", "email": "email", "price": "price"}
    data = SchemaDataGenerator.generate_initial_data(schema, count=3)
    assert len(data) == 3
    assert data[0]["id"] == 1
    assert "@example.uz" in data[0]["email"]
    assert isinstance(data[0]["price"], float)


def test_crud_operations():
    schema = {"id": "id", "name": "name", "status": "status"}
    engine = MockRESTEngine("tasks", schema, initial_count=2)

    # 1. List
    status, items = engine.list_items()
    assert status == 200
    assert len(items) == 2

    # 2. Create
    code, new_item = engine.create_item({"name": "Yangi topshiriq", "status": "pending"})
    assert code == 201
    assert new_item["id"] == 3
    assert new_item["name"] == "Yangi topshiriq"

    # 3. Get
    code, got = engine.get_item(3)
    assert code == 200
    assert got["id"] == 3

    # 4. Update
    code, updated = engine.update_item(3, {"status": "completed"})
    assert code == 200
    assert updated["status"] == "completed"

    # 5. Delete
    code, _ = engine.delete_item(3)
    assert code == 204
    code_after, _ = engine.get_item(3)
    assert code_after == 404
