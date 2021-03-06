#coding:utf-8
from collections import deque

# dict表示图
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def is_mongo_seller(name):
    return name[-1] == 'm'

def find_seller(name):
    # 队列保存todos
    search_q = deque()
    search_q.append(name)
    # 保存分析过的节点
    searched = []

    while search_q:
        n = search_q.popleft()
        if n not in searched:
            if is_mongo_seller(n):
                print n + " is mongo seller"
                return True
            else:
                search_q += graph[n]
                searched.append(n)
    return False

find_seller('you')
