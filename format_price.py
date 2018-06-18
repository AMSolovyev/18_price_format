import math
import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--price', help='Input a price')
    return parser.parse_args()


def get_formatted_price(price):
    if isinstance(price, bool):
        return None
    try:
        float_price = float(price)
        formatted_price = '{:,.2f}'.format(float_price).rstrip('0').rstrip('.')
        return formatted_price

    except (TypeError, ValueError):
        return None


def print_price(formatted_price):
    print(formatted_price)


if __name__ == '__main__':
    args = get_parser()

    entered_price = get_formatted_price(args.price)
    print_price(entered_price)
