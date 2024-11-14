from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create the adjacency list from the flight data
        graph = {i: [] for i in range(n)}
        for u, v, price in flights:
            graph[u].append((v, price))
        
        # Priority Queue to store (cost, current city, number of stops)
        pq = [(0, src, 0)]  # Starting with 0 cost at src and 0 stops
        # Array to store the minimum cost to reach each city with a certain number of stops
        min_cost = [[float('inf')] * (k + 2) for _ in range(n)]
        min_cost[src][0] = 0
        
        while pq:
            cost, city, stops = heapq.heappop(pq)
            
            # If we have reached the destination within the allowed stops, return the cost
            if city == dst:
                return cost
            
            # Skip paths that exceed the maximum allowed stops
            if stops > k:
                continue
            
            # Explore all neighbors (destinations reachable from the current city)
            for neighbor, price in graph[city]:
                new_cost = cost + price
                # Check if reaching 'neighbor' with stops+1 is cheaper than previously known
                if stops + 1 <= k + 1 and new_cost < min_cost[neighbor][stops + 1]:
                    min_cost[neighbor][stops + 1] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, stops + 1))
        
        # If no valid path is found, return -1
        return -1
