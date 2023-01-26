#include <vector>;
#include <queue>;
using namespace std;

template <typename T>
class bfs
{
private:
    vector<vector<T>> Graph;
    vector<bool> explored(false);
    vector<int> parent();

public:
    bfs(vector<vector<T>> graph);
    ~bfs();

    bfs(vector<vector<T>> graph, int src, int final)
    {
       queue<int> q;
       q.push(src);
       while(!q.empty())
       {
        int node = q.pop();
        if(node == final)
        {return node;}
          for(auto edge:graph[node])
          {
            if(explored[edge] == false)
            {
              explored[edge] = true;
              parent[edge] = node;
              q.push(edge);
            }
          }

       }


    }

    bfs::~bfs()
    {
    }
};