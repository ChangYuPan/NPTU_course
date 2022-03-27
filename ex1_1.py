from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('--input', default='n')
args = parser.parse_args()
if args.input == 'n':
    num1 = 23.12
    num2 = 359.3
    num3 = 100.4617
    num4 = 564.329
else:
    num1 = eval(input('Please enter the first floating point: '))
    num2 = eval(input('Please enter the second floating point: '))
    num3 = eval(input('Please enter the third floating point: '))
    num4 = eval(input('Please enter the fourth floating point: '))
print(f'|{num1:>7.2f}:{num2:>7.2f}|')
print(f'|{num3:>7.2f}:{num4:>7.2f}|')
print(f'|{num1:<7.2f}:{num2:<7.2f}|')
print(f'|{num3:<7.2f}:{num4:<7.2f}|')
