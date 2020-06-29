'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. 
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. 
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.

Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
'''
#Solution:

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        # Create a graph for each airport and keep list of airport reachable from it
        for src, dst in tickets:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]
        print(graph)

        for src in graph.keys():
            graph[src].sort(reverse=True)
            # Sort children list in descending order so that we can pop last element 
            # instead of pop out first element which is costly operation
        print(graph)
        stack = []
        res = []
        stack.append("JFK")
        # Start with JFK as starting airport and keep adding the next child to traverse 
        # for the last airport at the top of the stack. If we reach to an airport from where 
        # we can't go further then add it to the result. This airport should be the last to go 
        # since we can't go anywhere from here. That's why we return the reverse of the result
        # After this backtrack to the top airport in the stack and continue to traaverse it's children

        while len(stack) > 0:
            elem = stack[-1]
            if elem in graph and len(graph[elem]) > 0: 
                # Check if elem in graph as there may be a case when there is no out edge from an airport 
                # In that case it won't be present as a key in graph
                stack.append(graph[elem].pop())
            else:
                res.append(stack.pop())
                # If there is no further children to traverse then add that airport to res
                # This airport should be the last to go since we can't anywhere from this
                # That's why we return the reverse of the result
            print(stack,res)
        return res[::-1]
        
        
        
        
        
