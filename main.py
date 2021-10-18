def get_float(prompt):
    while True:
        try:
            read = float(input(prompt))
            return read
        except ValueError:
            print('Please enter valid numeric value')


def main():
    commands = [
        #(command, name, operation, ),
        ('1', 'add', '+', ),
        ('2', 'sub', '-', ),
        ('3', 'mult', '*', ),
        ('0', 'exit', '', ),
    ]

    while True:
        print(
            'choose one of the commands bellow:\n' +
            ('\n'.join([
                f'{command[0]}) {command[1]}'
                for command in commands
            ])) +
            '\n'
        )

        option = input('Option: ')
        for command in commands:
            if option == command[0]:
                if command[2] == '':
                    return
                operands = get_float('1st operand: '), get_float('2nd operand: ')
                operation = f'{operands[0]:.2f} {command[2]} {operands[1]:.2f}'
                print(f'{operation} = {eval(operation):.2f}\n')


if __name__ == '__main__':
    main()
    print('bye bye!')
