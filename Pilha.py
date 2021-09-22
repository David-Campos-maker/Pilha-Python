class Node:
    def __init__(self):
        self.value = 0
        self.next = None

class Pilha:
    def __init__(self):
        self.topo = None

    def pop(self , pilha):
        if pilha.topo != None:
            apagar = Node()
            apagar = pilha.topo
            pilha.topo = apagar.next
            apagar = None

    def push(self , pilha , value):
        novo = Node()
        novo.value = value
        novo.next = pilha.topo
        pilha.topo = novo

    def print_pilha(self , pilha):
        element = Node()
        element = pilha.topo
        while element != None:
            print(element.value)
            element = element.next

        print()

    def pilha_lenght(self , pilha):
        element = Node()
        element = pilha.topo
        count = 0
        while element != None:
            count += 1
            element = element.next

        return count
