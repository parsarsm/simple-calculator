import math


class Colors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def get_float(prompt):
    while True:
        try:
            read = float(input(prompt))
            return read
        except ValueError:
            print('Please enter valid numeric value')


def main():
    commands = [
        # (command, name, operation, ),
        ('1', 'add', '+',),
        ('2', 'sub', '-',),
        ('3', 'mult', '*',),
        ('4', 'mod', '%',),
        ('5', 'power', '**',),
        ('6', 'sin', 'sin',),
        ('7', 'cos', 'cos',),
        ('8', 'tan', 'tan',),
        ('9', 'rad', 'radians',),
        ('10', 'sqrt', 'sqrt',),
        ('11', 'abs', 'fabs',),
        ('0', 'exit', '',),
    ]

    while True:
        print(
            Colors.HEADER + 'choose one of the commands bellow:\n' + Colors.ENDC +
            ('\n'.join([
                Colors.OKCYAN + f'{command[0]})' + Colors.ENDC + Colors.BOLD + f' {command[1]}' + Colors.ENDC
                for command in commands
            ])) +
            '\n'
        )

        option = input('Option: ')
        for command in commands:
            if option == command[0]:
                if command[2] == '':
                    return

                if int(option) > 5:
                    operand = get_float('operand: ')
                    operation = f'math.{command[2]}({operand:.2f})'
                    print(Colors.BOLD + f'{operation[5:]}' + Colors.ENDC + f' = {eval(operation):.2f}\n')
                else:
                    operands = get_float('1st operand: '), get_float('2nd operand: ')
                    operation = f'{operands[0]:.2f} {command[2]} {operands[1]:.2f}'
                    print(Colors.BOLD + f'{operation}' + Colors.ENDC + f' = {eval(operation):.2f}\n')


if __name__ == '__main__':
    main()
    print('bye bye!')
