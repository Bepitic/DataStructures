#include <vector>;
using namespace std;

class dikjstra
{
private:
    /* data */
    int size_graph = 0;
    vector<int> distance;
    vector<int> prev;
    vector<int> node_unvisited;
    vector<int> node_visited;

public:
    dikjstra(vector<vector<int>> graph, int source);
    ~dikjstra();
};

dikjstra::dikjstra(vector<vector<int>> graph, int source)
{
    this->size_graph = (graph.size() * graph[0].size() );
    this->distance = vector<int>(size_graph,-1);
    this->prev = vector<int>(size_graph,-1);
    
}

dikjstra::~dikjstra()
{
}
