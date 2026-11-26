class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.order=[]
        

    def get(self, key: int) -> int:
        value=self.cache.get(key,-1)
        if value!=-1:
            self.order.remove(key)
            self.order.append(key)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)
        self.cache[key]=value
        if len(self.order)>self.capacity:
            first_key=self.order[0]
            self.order.remove(first_key)
            del self.cache[first_key]



        
