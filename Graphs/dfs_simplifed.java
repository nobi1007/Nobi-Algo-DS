import java.io.*;
import java.util.*;

class dfs_simplified{
    static LinkedList<Integer> adjMat[];
    static boolean checker[];
    static Stack<Integer> st;

    static void dfs(int root, boolean[] checker){
        checker[root] = true;
        st.add(root);

        for(int i=0;i<adjMat[root].size();i++){
            if(!checker[adjMat[root].get(i)]){
                dfs(adjMat[root].get(i),checker);
            }
        }
        System.out.println(st);
        if(!st.isEmpty()){
            st.pop();
        }
    }

    public static void main(String args[]){
        int n = 4;      // number of vertices
        int v = 6;      // number of edges
        adjMat = new LinkedList[n];
        for(int i=0;i<n;i++){
            adjMat[i] = new LinkedList<Integer>();
        }
        adjMat[0].add(1);
        adjMat[0].add(2);
        adjMat[1].add(2);
        adjMat[2].add(0);
        adjMat[2].add(3);
        adjMat[3].add(3);
        int root = 0;
        checker = new boolean[n];
        st = new Stack<Integer>();
        dfs(root,checker);
    }

}