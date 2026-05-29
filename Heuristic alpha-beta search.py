class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []


def heuristic(node):
    """
    Evaluation Function
    """
    if node.value is not None:
        return node.value
    return 0


def heuristic_alpha_beta(node, depth, max_depth,
                         alpha, beta,
                         maximizing_player):

    # Depth limit reached
    if depth == max_depth:
        return heuristic(node)

    # Terminal node
    if len(node.children) == 0:
        return heuristic(node)

    if maximizing_player:

        best_value = float('-inf')

        for child in node.children:

            value = heuristic_alpha_beta(
                child,
                depth + 1,
                max_depth,
                alpha,
                beta,
                False
            )

            best_value = max(best_value, value)

            alpha = max(alpha, best_value)

            if beta <= alpha:
                break

        return best_value

    else:

        best_value = float('inf')

        for child in node.children:

            value = heuristic_alpha_beta(
                child,
                depth + 1,
                max_depth,
                alpha,
                beta,
                True
            )

            best_value = min(best_value, value)

            beta = min(beta, best_value)

            if beta <= alpha:
                break

        return best_value


# -------------------------
# Test Case 1
# -------------------------

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
    heuristic_alpha_beta(
        root1,
        0,
        3,
        float('-inf'),
        float('inf'),
        True
    )
)
print()


# -------------------------
# Test Case 2
# -------------------------

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
    heuristic_alpha_beta(
        root2,
        0,
        3,
        float('-inf'),
        float('inf'),
        True
    )
)
print()


# -------------------------
# Test Case 3
# -------------------------

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
    heuristic_alpha_beta(
        root3,
        0,
        3,
        float('-inf'),
        float('inf'),
        True
    )
)
