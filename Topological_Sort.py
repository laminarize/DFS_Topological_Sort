from collections import deque

def add_node(graph, prereq, course):
    if prereq not in graph.keys():
        graph[prereq] = {course}
    else:
        graph[prereq].add(course)
    return graph


graph = dict()
schedule = deque()
visited = set()
node_children = dict()

graph = add_node(graph ,  None   , 'LA15' )
graph = add_node(graph ,  None   , 'LA22' )
graph = add_node(graph , 'LA15'  , 'LA16' )
graph = add_node(graph , 'LA15'  , 'LA31' )
graph = add_node(graph , 'LA16'  , 'LA32' )
graph = add_node(graph , 'LA31'  , 'LA32' )
graph = add_node(graph , 'LA22'  , 'LA126')
graph = add_node(graph , 'LA32'  , 'LA126')
graph = add_node(graph , 'LA16'  , 'LA127')
graph = add_node(graph , 'LA22'  , 'LA141')
graph = add_node(graph , 'LA16'  , 'LA141')
graph = add_node(graph , 'LA32'  , 'LA169')


for keys, values in graph.items():
    node_children[keys] = len(graph[keys])
    for value in graph[keys]:
        node_children[value] = 0


def build_schedule(graph, schedule, start_node):
    if start_node not in visited:
        if start_node in graph.keys():
            for pre_req in graph[start_node]:
                node_children[start_node] -= 1
                build_schedule(graph, schedule, pre_req)
                if node_children[start_node] == 0 and start_node != None:
                    print(f'Node has no more children safe to append: {start_node}')
                    schedule.appendleft(start_node)
        else:
            print(f'Node has no more children safe to append: {start_node}')
            schedule.appendleft(start_node)
        visited.add(start_node)
    if len(visited) == len(node_children):
        return schedule
    else:
        next_node= list(set(node_children.keys()).difference(visited))
        next_node = next_node[0]



print(build_schedule(graph, schedule, None))
