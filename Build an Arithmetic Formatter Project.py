def arithmetic_arranger(problems, show_answers=False):

    
    if len(problems)>5:
        return "Error: Too many problems."
    
    top_row = ""
    bottom_row = ""
    lines = ""
    results_row = ""
    
    for i,problem in  enumerate(problems):
        
        parts=problem.split()

        if len(parts)>3:
            return "Error: Invalid problem format."
        
        num1,operator,num2 = parts

        if operator not in ['+','-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(num1)>4 or len(num2)>4:
            return "Error: Numbers cannot be more than four digits."

        if  show_answers:
            if operator == "+":
                result = str(int(num1)+int(num2))
            else:
                 result = str(int(num1) - int(num2))
        
        width = max(len(num1), len(num2)) + 2

        if i > 0:
            top_row += "    "
            bottom_row += "    "
            lines += "    "
            results_row += "    "
        top_row += num1.rjust(width)
        bottom_row += operator + num2.rjust(width - 1)
        lines += "-" * width
        if show_answers:
            results_row += result.rjust(width)

    if show_answers:
        return f"{top_row}\n{bottom_row}\n{lines}\n{results_row}"
    else:
        return f"{top_row}\n{bottom_row}\n{lines}"
    
        



    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "30a01 - 2", "45 + 43", "123 + 49"])}')
