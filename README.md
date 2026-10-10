# Mock REST Server

Frontend va mobil dasturchilar uchun tezkor soxta ma'lumotlar bilan CRUD amaliyotlarini sinash, tarmoq kechikishi (network latency) va xatoliklar (chaos testing) simulyatsiyasini amalga oshiruvchi dinamik Mock API dvigateli.

## Xususiyatlari
- **Dinamik Sxema**: JSON sxema orqali ismlar, email, narxlar va statuslarni avtomatik generatsiya qilish.
- **To'liq CRUD**: `GET`, `POST`, `PUT`, `DELETE` amaliyotlarini xotirada tezkor amalga oshirish.
- **Xatoliklar va Kechikish Simulyatsiyasi**: Tarmoqdagi sekinlashuv yoki 500 server xatolarini sun'iy hosil qilish orqali frontend barqarorligini sinash.
- **CLI & Python SDK**: Bir qator buyruq bilan test API ni ishga tushirish.

## Foydalanish (Python)
```python
from mock_server import MockRESTEngine

schema = {"id": "id", "name": "name", "price": "price", "status": "status"}
engine = MockRESTEngine("products", schema, initial_count=10, delay_ms=100)

status, items = engine.list_items()
print(f"Status: {status}, Elementlar: {len(items)}")

code, new_product = engine.create_item({"name": "MacBook Pro", "price": 1999.0})
print("Yaratildi:", new_product)
```

## CLI
```bash
mock-rest --resource users --count 10
```

## Testlar
```bash
pytest tests/ -v
```

## Litsenziya
MIT
