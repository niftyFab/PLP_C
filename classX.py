print("I am a software engineer")
def sum_n(n):
     """Return the sum of the first n natural numbers using recursion."""
     if n == 0:
         return 0
     else:
         return n + sum_n(n - 1)
# Test the recursive sum against the formula: n(n+1)/2
for i in range(1, 11):
     recursive_sum = sum_n(i)
     formula_sum = i * (i + 1) // 2
     print(f"n = {i}: Recursive Sum = {recursive_sum}, Formula Sum = {formula_sum}")

# Define two sets

A = {1, 2, 3, 4}

B = {3, 4, 5, 6}
# Set operations in action

union_set = A.union(B)              # Alternatively: A | B

intersection_set = A.intersection(B) # Alternatively: A & B

difference_set = A.difference(B)     # Alternatively: A - B
print("Set A:", A)
print("Set B:", B)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (A - B):", difference_set)

import itertools
elements = ['a', 'b', 'c']

# All permutations of the list:
permutations = list(itertools.permutations(elements))

print("Permutations of ['a', 'b', 'c']:", permutations)

# All combinations of 2 elements:
combinations = list(itertools.combinations(elements, 2))

print("Combinations of 2 from ['a', 'b', 'c']:", combinations)


from collections import deque
# Sample graph represented as an adjacency list

graph = {
     'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']

}
# DFS using recursion

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)
        return visited
print("DFS Traversal starting from A:")
dfs(graph, 'A')
print("\n")

# BFS using a queue
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            queue.extend([n for n in graph[vertex] if n not in visited])
    print()
    
print("BFS Traversal starting from A:")
bfs(graph, 'A')


def add(a, b):
    print("Sum:", a + b)

def subtract(a, b):
    print("Difference:", a - b)

def multiply(a, b):
    print("Product:", a * b)

def divide(a, b):
    print("Quotient:", a / b)

# user input
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

add(x, y)
subtract(x, y)
multiply(x, y)
divide(x, y)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose operation (1/2/3/4): ")

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if choice == "1":
    print("Answer:", add(x, y))
elif choice == "2":
    print("Answer:", subtract(x, y))
elif choice == "3":
    print("Answer:", multiply(x, y))
elif choice == "4":
    print("Answer:", divide(x, y))
else:
    print("Invalid choice")

