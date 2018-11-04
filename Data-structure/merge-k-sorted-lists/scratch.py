class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


user_input = [ListNode(1), ListNode(3), ListNode(5)]


class Linked_List:
    def __init__(self, *values):
        for value in values:
            self.create(value)

    def create(self, value):
        node = ListNode(value)
        return node


second_input = Linked_List(1, 3, 5)
print(second_input)
