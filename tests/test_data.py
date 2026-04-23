from health_app.data import save, read, get_statistics
from health_app.health import Health
import json
import pytest

## Test save(records)
def test_save_single_user(tmp_path):
    user = Health("Nasir", 98, 1.85)
    filename = tmp_path / "testing.json"

    save([user], file=filename)

    with open(filename) as f:
        data = json.load(f)

    assert data[0]["name"] == "Nasir"
    assert data[0]["weight_kg"] == 98
    assert data[0]["height_m"] == 1.85
    assert data[0]["calculated_bmi"] == user.calculate_bmi()

def test_save_empty(tmp_path):
    filename = tmp_path / "test.json"

    save([], file=filename)
    with open(filename) as f:
        data = json.load(f)
        assert data == []

## Test read(file)
def test_read(tmp_path):
    filename = tmp_path / "test.json"
    user = Health("Marky", 31, 1.89)

    save([user], file=filename)
    result = read(filename)

    assert result[0].name == "Marky"
    assert result[0].weight_kg == 31
    assert  result[0].height_m == 1.89
    assert result[0].calculate_bmi() == user.calculate_bmi()

def test_read_file_notfound(tmp_path):
    filename = tmp_path / "404.json"

    result = read(filename)
    assert result == []

## Test get_statistics
def test_get_statistics(tmp_path):
    filename = tmp_path / "test.json"
    user1 = Health("Abe", 60, 1.6)
    user2 = Health("Bale", 200, 1.89)
    user3 = Health("Kate", 300, 1.67)

    save([user1, user2, user3], file=filename)

    results = get_statistics(filename)

    test_total_bmi = user1.calculate_bmi() + user2.calculate_bmi() + user3.calculate_bmi()
    test_avg_bmi = round((test_total_bmi / 3), 2)

    assert results["total_records"] == 3
    assert results["avg_bmi"] == test_avg_bmi
    assert results["most_common_category"] == "Obese"
    assert results["category_distribution"]["Normal"] == 1
    assert results["category_distribution"]["Obese"] == 2

