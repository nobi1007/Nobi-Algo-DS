import java.util.*;
import java.io.*;

class dfs_again{
    static LinkedList<Integer> adj[];
    static int size;
    public static class Graph{
        Graph(int n){

            adj = new LinkedList[n];
            size = n;

            for(int i=0;i<n;i++){
                adj[i] = new LinkedList<>();
            }
        }

        void addEdge(int v1, int v2){
            adj[v1].add(v2);        
            // adj[v2].add(v1);        // add in case of undirected graph
        }

        Stack<Integer> st = new Stack<Integer>();

        void dfs(int root){
            int n = size;
            boolean[] bm = new boolean[n];

            DFS(root,bm);
        }

        void DFS(int root, boolean bm[]){
            bm[root] = true;
            st.push(root);

            for(int i=0;i<adj[root].size();i++){
                if(!bm[adj[root].get(i)]){
                    DFS(adj[root].get(i),bm);
                }
            }
            System.out.println(st);
            if (!st.isEmpty())
            st.pop();
        }
    }

    public static void main(String args[]){
        Graph g1 = new Graph(8);
        g1.addEdge(0,1);
        g1.addEdge(0,2);
        g1.addEdge(1,3);
        g1.addEdge(3,5);
        g1.addEdge(3,6);
        g1.addEdge(2,4);
        g1.addEdge(2,7);
        
        g1.dfs(0);
    }
}