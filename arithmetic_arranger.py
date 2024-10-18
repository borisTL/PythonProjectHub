def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_row = ""
    bottom_row = ""
    lines = ""
    results_row = ""

    for i, problem in enumerate(problems):
        # Split the problem into its parts
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        # Check if the operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if both numbers are digits
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check if the numbers have more than four digits
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the result if required
        if display_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))

        # Determine the width of the problem
        width = max(len(num1), len(num2)) + 2

        # Create the rows
        if i > 0:
            top_row += "    "
            bottom_row += "    "
            lines += "    "
            results_row += "    "

        top_row += num1.rjust(width)
        bottom_row += operator + num2.rjust(width - 1)
        lines += "-" * width
        if display_answers:
            results_row += result.rjust(width)

    if display_answers:
        return f"{top_row}\n{bottom_row}\n{lines}\n{results_row}"
    else:
        return f"{top_row}\n{bottom_row}\n{lines}"

# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
