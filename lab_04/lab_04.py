import math

def infix_to_rpn(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output, stack = [], []

    def is_operator(c):
        return c in precedence

    def tokenize(expr):
        tokens, number = [], ''
        for char in expr:
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    tokens.append(number)
                    number = ''
                if char.strip():
                    tokens.append(char)
        if number:
            tokens.append(number)
        return tokens

    tokens = tokenize(expression)
    for token in tokens:
        if token.isdigit() or token.replace('.', '', 1).isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif is_operator(token):
            while stack and stack[-1] != '(' and precedence[token] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output

def evaluate_rpn(rpn):
    stack = []

    def apply_op(a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a / b if b != 0 else float('inf')
        if op == '^': return math.pow(a, b)

    for token in rpn:
        if token.replace('.', '', 1).isdigit():
            stack.append(float(token))
        else:
            b, a = stack.pop(), stack.pop()
            stack.append(apply_op(a, b, token))

    return stack[0]

def main():
    expression = input("Enter a mathematical expression: ").strip()
    try:
        rpn = infix_to_rpn(expression)
        print("RPN:", " ".join(rpn))
        print("Result:", evaluate_rpn(rpn))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
