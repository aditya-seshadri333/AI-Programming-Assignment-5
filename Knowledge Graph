class KnowledgeGraph:

    def __init__(self):
        self.graph = {}

    def add_relation(self, source, relation, target):

        if source not in self.graph:
            self.graph[source] = []

        self.graph[source].append((relation, target))

    def display(self):

        print("Knowledge Graph\n")

        for source in self.graph:

            for relation, target in self.graph[source]:

                print(
                    f"{source} --{relation}--> {target}"
                )


kg = KnowledgeGraph()

kg.add_relation(
    "India",
    "contains",
    "Hyderabad"
)

kg.add_relation(
    "Hyderabad",
    "contains",
    "Charminar"
)

kg.add_relation(
    "Hyderabad",
    "famous_for",
    "Biryani"
)

kg.add_relation(
    "Charminar",
    "is_a",
    "Tourist Place"
)

kg.display()
