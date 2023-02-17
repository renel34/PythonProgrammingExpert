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

    def merge(self, g2):
        self.members.append(self.g2)
            
g1 = Group("A-Team", ["Tim", "Clement"])
g2 = Group("B-Team", ["Antoine"])
g3 = g1.merge(g2)
print(g3.get_members())