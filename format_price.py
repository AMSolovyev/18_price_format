import math
import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--price', type=float, help='Input a price')
    return parser


def validate_args(argument_parser):
    args = argument_parser.parse_args()
    if not args.price:
        argument_parser.error(
            'You need input any number!'
        )
        if str(args.price):
            argument_parser.error(
                'You input string!'
            )
        if args.price and args.price < 0:
            argument_parser.error(
                'You need input a positive number'
            )
    return args


def get_format_price(number):
    try:
        price = float(number)
    except (TypeError, ValueError):
        return None
    # проверить принадлежность данных определенному классу(типу данных)
    if isinstance(number, (float)):
        price = round(number)
        return price
    else:
        None
    # проверить на целое число
    if price.is_integer():
        formatted_price = '{:,.0f}'.format(price).replace(',', '')
    else:
        formatted_price = '{:,}'.format(price).replace('.', '')
    return formatted_price


def printer_price(formatted_price):
    print(formatted_price)


if __name__ == '__main__':
    argument_parser = get_parser()
    valid_args = validate_args(argument_parser)

    my_number = get_format_price(valid_args.price)
    printer_price(my_number)
