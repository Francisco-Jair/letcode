
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:


    def returnNumber(self, lista):
        return [str(i) for i in lista]




    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        lista1 = []
        lista2 = []

        while(l1 != None or l2 != None):
            
            if l1 != None:
                lista1.append(l1.val)

            
            if l2 != None:
                lista2.append(l2.val)



            if l1 != None:
                l1 = l1.next
            
            if l2 != None:
                l2 = l2.next


        lista1 = list(reversed(lista1))
        lista2 = list(reversed(lista2))
        valor1 = int("".join(self.returnNumber(lista1)))
        valor2 = int("".join(self.returnNumber(lista2)))
        

        soma = valor1 + valor2
        inver = list(reversed(str(soma)))

        

        tam = len(str(soma))

        ini = ListNode(val=int(inver[0]))
        ant = ListNode(val=int(inver[0]))
        

        for i in range(1, tam):

            listaSolution = ListNode(val=int(inver[i]))

            if i == 1:
                ini.next = listaSolution
                ant = listaSolution
            else:
               ant.next = listaSolution
               ant = listaSolution

        return ini

        


if __name__ == "__main__":  

    l1 = ListNode(val=2)
    l1.next = ListNode(val=4)
    l1.next.next = ListNode(3)


    l2 = ListNode(val=5)
    l2.next = ListNode(val=6)
    l2.next.next = ListNode(4)

    s = Solution()
    s.addTwoNumbers(l1, l2)