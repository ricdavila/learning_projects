"""
Sistema de Lista Encadeada Simples, por Ricardo d'Avila.
Github: https://github.com/ricdavila
"""


class Node():
    """Classe que representa o nó (elemento) da lista encadeada."""

    def __init__(self, initial_data):
        """Cria um node com os dados passados e com o sucessor a ser definido."""

        self.data = initial_data 
        self.next = None
    

class LinkedList():
    """Implementa uma Lista Encadeada Simples."""

    def __init__(self):
        """Inicializa uma lista vazia."""
        self.head = None # primeiro nó da lista
    

    def add_node(self, data):
        """Adiciona um novo nó/node na lista contendo os dados passados em 'data'."""

        node = Node(data) # cria um novo nó (com os dados passados)
        node.next = self.head # define a antiga head como o sucessor do novo node
        self.head = node # atualiza a head da lista para o novo node
    

    def display_nodes(self):
        """Exibe os dados de todos os nodes da lista, começando a partir da head."""

        actual = self.head

        # percorre a lista e exibe os dados decada node
        while actual != None:
            print(actual.data, end=" -> ")
            actual = actual.next
        
        print("None") # adiciona "None" ao fim da listagem para represntar o node inicial


    def size(self):
        """Retorna o número de nodes que essa lista possui."""

        count = 0
        actual = self.head
        
        # percorre a lista contando a quantidade de nodes até chegar ao fim (None).
        while actual != None:
            count += 1
            actual = actual.next

        return count


    def search(self, data):
        """Busca na lista um node com o valor especificado em 'data'."""

        current = self.head
        
        # realiza a busca até que o node seja encontrado ou até que current = None (o nó inicial)
        while current != None:
            if data == current.data:
                return current # retorna o nó, caso encontrado
            
            current = current.next

        return None # retorno caso o valor não seja encontrado na lista
    

    def del_node(self, data):
        """Remove da lista o node com o valor especificado em 'data'."""

        found = False
        current = self.head
        previous = None

        while not found and current != None:
            if data == current.data:
                found = True # sai do loop quando o valor for encontrado
            else:
                # avança na lista com o previous e com o current
                previous = current
                current = current.next
        
        if found:
            if previous:
                previous.next = current.next # conecta entre si os vizinhos do node atual
            else:
                # se não houver antecessor, quer dizer que o atual é a head
                # sendo assim, transforma o seu sucessor na head da lista
                self.head = current.next
            
            current = None # efetivamente apaga o node
            return True # retorno caso seja possível deletar o node
        
        return False # retorno caso não seja possível deletar o node


if __name__ == "__main__":

    # criação de uma lista
    linked_list = LinkedList()

    # adição de elementos na lista
    linked_list.add_node(5)
    linked_list.add_node(20)
    linked_list.add_node(32)
    linked_list.add_node(8)
    linked_list.add_node(95)
    linked_list.add_node(10)

    # exibição dos nodes da lista
    linked_list.display_nodes()

    # deleção de nodes da lista
    linked_list.del_node(95)
    linked_list.del_node(5)

    # exibição dos nodes após a deleção
    linked_list.display_nodes()

    # exibição do tamanho da lista
    print("\nTamanho da lista: ", +linked_list.size())

    # busca por nodes na lista
    print("\nBuscando pelo node com 10:", linked_list.search(10)) # retorna a representação do node na memória (caso o encontre)
    print("\nBuscando pelo node com 5:", linked_list.search(5)) # retornará None (caso não o encontre)