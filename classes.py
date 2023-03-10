class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
    
    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name not in self.members:
            raise Exception ("Member not in the group")
        if name in self.members:
            self.members.remove(name)

    def get_members(self):
        print(sorted(self.members))

    def merge(self, group):
        merged_group = self.members + group.members
        g3_group = Group("C-Team", merged_group)
        return g3_group
                    
g1 = Group("A-Team", ["Tim", "Clement"])
g2 = Group("B-Team", ["Antoine"])
g3 = g1.merge(g2)
print(g3.get_members())

