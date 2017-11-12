class DisJointSet:
    def __init__(self):
        self.parents = {}
        self.my_sets = {}

    def add_parent(self, x, y):
        if x not in self.parents:
            self.parents[x] = x

        if y not in self.parents:
            self.parents[y] = y

    def find(self, x):
        root = x
        while root != self.parents[root]:
            root = self.parents[root]

        while root != x:
            next_root = self.parents[x]
            self.parents[x] = root
            x = next_root

        return root

    def union(self, x, y):
        self.add_parent(x, y)

        root1 = self.find(x)
        root2 = self.find(y)

        if root1 == root2:
            return
        else:
            self.my_sets.setdefault(root1, set()).add(x)
            self.my_sets.setdefault(root2, set()).add(y)
            if len(self.my_sets[root1]) >= len(self.my_sets[root2]):
                self.parents[root2] = root1
                self.my_sets[root1].update(self.my_sets[root2])
                del self.my_sets[root2]
            else:
                self.parents[root1] = root2
                self.my_sets[root2].update(self.my_sets[root1])
                del self.my_sets[root1]
