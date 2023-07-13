import data
import new_kit_of_user

def get_kit_name(name):
    current_name = data.kit_body.copy()
    current_name["name"] = name
    return current_name

def possitive_assert(name):
    kit_body = get_kit_name(name)
    kit_response = new_kit_of_user.new_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

def negative_assert(name):
    kit_body = get_kit_name(name)
    kit_response = new_kit_of_user.new_kit(kit_body)
    assert kit_response.status_code == 400

# Тест 1. Допустимое кол-во символов - 1.
def test_1():
    possitive_assert("a")

# Тест 2. Допустимое кол-во символов - 511.
def test_2():
    possitive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Кол-во символов меньше допустимого - 0.
def test_3():
    negative_assert("")

# Тест 4. Кол-во символов больше допустимого - 512.
def test_4():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Разрешены английские буквы
def test_5():
    possitive_assert("QWErty")

# Тест 6. Разрешены русские буквы:
def test_6():
    possitive_assert("Мария")

# Тест 7. Разрешены спецсимволы
def test_7():
    possitive_assert("\"№%@\",")

# Тест 8. Разрешены пробелы
def test_8():
    possitive_assert("Человек и Ко")

# Тест 9. Разрешены цифры
def test_9():
    possitive_assert("123")

# Тест 10. Праметр не передан в запросе
def test_10():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert(kit_body)

# тест 11. Передан другой тип параметра
def test_11():
    negative_assert(123)
