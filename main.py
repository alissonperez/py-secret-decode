import sys

from base64 import b64decode

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


from icecream import ic


if __name__ == "__main__":
    input_data = sys.stdin.read()

    if not input_data:
        print('No input data')
        exit(1)

    data = load(input_data, Loader=Loader)

    if not data:
        print('No data')
        exit(1)

    if data.get('kind', '').lower() != 'secret':
        print('Not a secret')
        exit(1)

    items = data.get('data', {})

    for item_key in items.keys():
        value = items[item_key]
        items[item_key] = b64decode(value).decode('utf-8')

    ic(items)
