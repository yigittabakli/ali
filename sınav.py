class doublyLinkedListNode(object):
def __init__(self, value): self.value = value self.nextnode = None
self.prevnode = None def setNextNode(self, node): self.nextnode = node def setPrevNode(self, node): self.prevnode = node def getNextNode(self):
return self.nextnode
def getPrevNode(self):
return self.prevnode def getNodeValue(self): return self.value
Türkiye = doublyLinkedListNode("Ankara") İspanya = doublyLinkedListNode("Madrid") Çekya = doublyLinkedListNode("Prag")
Türkiye.setNextNode(İspanya)
İspanya.setPrevNode(Türkiye) İspanya.setNextNode(Çekya)
Çekya.setPrevNode(İspanya)
print(Çekya.getPrevNode().getPrevNode().getNodeValue()) print(Türkiye.getNextNode().getNextNode().getNodeValue()) print (İspanya.getNextNode().getPrevNode().getNodeValue())