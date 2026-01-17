from node import Node


def main():
    node1 = None #no apunta a ningún lado
    node2 = Node("A", None) #No apunta a ningún lado
    node3 = Node("B", node2) # Apunta al nodo 2

    print(node1)
    print(node2)
    print(node3)
    print(node2.data)
    print(node3.next.data)
    
    node1 = Node("C", node3)
    print(node1.next.data)
    
    #creamos una serie de nodos refeernciados unos a otros
    head = None
    for count in range(1,5):
        head = Node(count, head)
        
    while head != None:
        print(head.data)
        head = head.next
    

    # prueba de linkedlist
    
    from singly_linked_list import SinglyLinkedList
    
    words = SinglyLinkedList()
    words.append("egg")
    words.append("ham")
    words.append("spam")
    current = words.tail
    
    for word in words.iter():
        print(word)
    
if __name__ == "__main__":
    main()

