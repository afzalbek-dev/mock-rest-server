import random
from typing import Dict, Any, List


class SchemaDataGenerator:
    """JSON sxema yoki shablon asosida soxta test ma'lumotlarini yaratish."""

    @classmethod
    def generate_record(cls, schema: Dict[str, str], record_id: int = 1) -> Dict[str, Any]:
        record = {}
        for field, f_type in schema.items():
            f_lower = f_type.lower()
            if f_lower == "id":
                record[field] = record_id
            elif f_lower == "name":
                names = ["Alisher", "Nodira", "Bobur", "Kamola", "Sardor", "Dilnoza"]
                record[field] = f"{random.choice(names)} #{record_id}"
            elif f_lower == "email":
                record[field] = f"user_{record_id}@example.uz"
            elif f_lower == "price":
                record[field] = round(random.uniform(10.0, 500.0), 2)
            elif f_lower == "boolean":
                record[field] = random.choice([True, False])
            elif f_lower == "status":
                record[field] = random.choice(["active", "pending", "completed"])
            else:
                record[field] = f"{field}_val_{record_id}"
        return record

    @classmethod
    def generate_initial_data(cls, schema: Dict[str, str], count: int = 5) -> List[Dict[str, Any]]:
        return [cls.generate_record(schema, i + 1) for i in range(count)]
