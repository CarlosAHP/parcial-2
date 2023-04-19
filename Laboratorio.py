import graphviz

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(expression):
    stack = []
    current = None
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    for char in expression:
        if char.isdigit():
            if current is None:
                current = Node(int(char))
            else:
                current.value = current.value * 10 + int(char)
        elif char == " ":
            continue
        else:
            if current is not None:
                stack.append(current)
                current = None
            if char == "(":
                stack.append(char)
            elif char == ")":
                while len(stack) > 0 and stack[-1] != "(":
                    right = stack.pop()
                    op = stack.pop()
                    left = stack.pop()
                    node = Node(op)
                    node.left = left
                    node.right = right
                    stack.append(node)
                if len(stack) > 0:
                    stack.pop()
            else:
                while len(stack) > 0 and isinstance(stack[-1], Node) and precedence[char] <= precedence[stack[-1].value]:
                    right = stack.pop()
                    op = stack.pop()
                    left = stack.pop()
                    node = Node(op)
                    node.left = left
                    node.right = right
                    stack.append(node)
                stack.append(char)
    if current is not None:
        stack.append(current)
    while len(stack) > 1:
        right = stack.pop()
        op = stack.pop()
        left = stack.pop()
        node = Node(op)
        node.left = left
        node.right = right
        stack.append(node)
    return stack[0]

def plot_expression_tree(root):
    dot = graphviz.Digraph()
    def visit(node, parent=None):
        if node is None:
            return
        id = str(id(node))
        dot.node(id, str(node.value))
        if parent is not None:
            dot.edge(str(id(parent)), id)
        visit(node.left, node)
        visit(node.right, node)
    visit(root)
    dot.view()

def main():
    expression = input("Ingrese la expresión aritmética: ")
    root = build_expression_tree(expression)
    plot_expression_tree(root)

if __name__ == "__main__":
    main()
