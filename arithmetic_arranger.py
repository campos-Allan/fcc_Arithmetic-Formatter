"""first challenge from "Scientific Computing with Python"
on FreeCodeCamp.org
"""
from typing import List


def arithmetic_arranger(problems: List, answer: bool = False) -> str:
    """making arithmetic representations
    with strings

    Args:
        problems (List): operations with numbers
        answer (bool, optional): results Defaults to False.

    Returns:
        str: final formatting
    """
    if len(problems) > 5:
        return 'Error: Too many problems.'
    first_line = []
    second_line = []
    third_line = []
    forth_line = []

    arranged_problems = ''
    for i in problems:
        number1 = i.split(' ')[0]
        operation = i.split(' ')[1]
        number2 = i.split(' ')[2]

        try:
            int(number1)
            int(number2)
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        if operation != '+' and operation != '-':
            return "Error: Operator must be '+' or '-'."
        if len(number1) > 4 or len(number2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if len(number1) > len(number2):
            first_line.append('  '+number1)
            second_line.append(
                operation+' '*(len(number1)-len(number2)+1)+number2)
            third_line.append('-'*(len(number1)+2))
        else:
            first_line.append(
                ' '*((len(number2)-len(number1))+2)+number1)
            second_line.append(operation+' '+number2)
            third_line.append('-'*(len(number2)+2))

        if answer is True:
            if operation == '+':
                forth_line.append(
                    ' '*(len(third_line[-1])-len(str(int(number1)+int(number2)))) +
                    str(int(number1)+int(number2))
                )
            else:
                forth_line.append(
                    ' '*(len(third_line[-1])-len(str(int(number1)-int(number2)))) +
                    str(int(number1)-int(number2))
                )
    if answer is True:
        arranged_problems = '    '.join(
            first_line)+'\n'+'    '.join(
            second_line)+'\n'+'    '.join(
            third_line)+'\n'+'    '.join(
                forth_line)
    else:
        arranged_problems = '    '.join(
            first_line)+'\n'+'    '.join(second_line)+'\n'+'    '.join(third_line)
    return arranged_problems
