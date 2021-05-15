#!/usr/bin/env python
# coding: utf-8

# In[8]:


from queue import Queue 

adj_list = {"A" :["B" , "D"] ,
            "B" : ["C" ,"A"],
            "C" :["B" ] ,
            "D" : ["B","F" ,"A"],
            "E" : ["D","F" ,"G"],
            "F" :["D","E" ,"H" ] ,
            "G" : ["E","H" ],
            "H" : ["F" ,"G"]
           }


# In[40]:


visited = {}
level  = {}  #dic distanse
parent = {}

bfs_traversal_output = []
queue = Queue()

for node in adj_list.keys() :
   visited[node] =False  
   level[node]   = None 
   parent[node] = -1 
    

print(visited) 
print(level) 
print(parent) 

start ="A"
visited[start] = True
level[start]   = 0
queue.put(start)

while not queue.empty():
    templet = queue.get()
    bfs_traversal_output.append(templet)
    
    for value in adj_list[templet]:

        if not visited[value]:
            visited[value] = True
            parent[value]  = templet
            level[value]   = level[templet]+1
            queue.put(value)
    

print(visited) 
print(level) 
print(parent) 
print(bfs_traversal_output)


# In[ ]:





# In[ ]:




