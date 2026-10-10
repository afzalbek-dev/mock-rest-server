import argparse
import sys
import json
from .server import MockRESTEngine


def main():
    parser = argparse.ArgumentParser(description="Mock REST Server CLI - Sinov API xizmati")
    parser.add_argument("--resource", default="products", help="Resurs nomi (masalan: users, products)")
    parser.add_argument("--schema", help="JSON formatidagi maydonlar sxemasi (masalan: '{\"name\":\"name\",\"price\":\"price\"}')")
    parser.add_argument("--count", type=int, default=5, help="Boshlang'ich yozuvlar soni")
    parser.add_argument("--delay", type=float, default=0.0, help="Kechikish (ms)")
    parser.add_argument("--error-rate", type=float, default=0.0, help="Simulyatsiya qilinuvchi xatolik foizi (0.0 - 1.0)")

    args = parser.parse_args()

    schema = json.loads(args.schema) if args.schema else {"id": "id", "name": "name", "price": "price", "status": "status"}
    engine = MockRESTEngine(
        resource_name=args.resource,
        schema=schema,
        initial_count=args.count,
        delay_ms=args.delay,
        error_rate=args.error_rate,
    )

    print(f"🚀 Mock REST dvigateli ishga tushdi: /{args.resource}")
    status, items = engine.list_items()
    print(f"Yuklangan yozuvlar soni: {len(items)}")
    print(json.dumps(items[:2], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
