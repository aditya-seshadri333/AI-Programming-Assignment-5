class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []


def alpha_beta(node, depth, alpha, beta, maximizing_player):

    # Terminal node
    if len(node.children) == 0:
        return node.value

    if maximizing_player:

        best_value = float('-inf')

        for child in node.children:

            value = alpha_beta(
                child,
                depth + 1,
                alpha,
                beta,
                False
            )

            best_value = max(best_value, value)

            alpha = max(alpha, best_value)

            # Pruning condition
            if beta <= alpha:
                break

        return best_value

    else:

        best_value = float('inf')

        for child in node.children:

            value = alpha_beta(
                child,
                depth + 1,
                alpha,
                beta,
                True
            )

            best_value = min(best_value, value)

            beta = min(beta, best_value)

            # Pruning condition
            if beta <= alpha:
                break

        return best_value



n1 = Node(3)
n2 = Node(5)
n3 = Node(2)
n4 = Node(9)

left_min = Node()
left_min.children = [n1, n2]

right_min = Node()
right_min.children = [n3, n4]

root1 = Node()
root1.children = [left_min, right_min]

print("Test Case 1")
print(
    "Best Value =",
    alpha_beta(
        root1,
        0,
        float('-inf'),
        float('inf'),
        True
    )
)
print()




a = Node(8)
b = Node(4)
c = Node(6)
d = Node(2)

left_min = Node()
left_min.children = [a, b]

right_min = Node()
right_min.children = [c, d]

root2 = Node()
root2.children = [left_min, right_min]

print("Test Case 2")
print(
    "Best Value =",
    alpha_beta(
        root2,
        0,
        float('-inf'),
        float('inf'),
        True
    )
)
print()




a = Node(1)
b = Node(7)
c = Node(5)
d = Node(3)

left_min = Node()
left_min.children = [a, b]

right_min = Node()
right_min.children = [c, d]

root3 = Node()
root3.children = [left_min, right_min]

print("Test Case 3")
print(
    "Best Value =",
    alpha_beta(
        root3,
        0,
        float('-inf'),
        float('inf'),
        True
    )
)
