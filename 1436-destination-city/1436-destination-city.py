class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = {}
        for start_city, end_city in paths:
            graph[start_city] = end_city
        ans = paths[0][0]
        while True:
            try:
                ans = graph[ans]
            except:
                return ans