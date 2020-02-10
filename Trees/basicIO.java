import java.util.*;
import java.io.*;
import java.lang.*;

class Node{
    Node left,right;
    int data;
    Node(int data){
        this.data = data;
        this.left = this.right = null;
    }
}

class basicIO{
    public static Node insert(Node root,int data){
        if(root==null){
            return new Node(data);
        }
        else{
            Node curr;
            if(root.data < data){
                curr = insert(root.right,data);
                root.right = curr;
            }
            else{
                curr = insert(root.left,data);
                root.left = curr;
            }
            return root;
        }
    }

    public static void main(String args[])throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // System.out.println("Enter n: ");
        // int n = Integer.parseInt(br.readLine());
        
        Node root=null;
        root = insert(root,4);
        root = insert(root,1);
        root = insert(root,3);
        root = insert(root,5);
        root = insert(root,7);
        
        System.out.println(root.data);
        System.out.println(root.right.data);
        System.out.println(root.right.right.data);
        System.out.println(root.left.data);
        System.out.println(root.left.right.data);
        
        
        // for(int i=0;i<n-1;i++){
        //     // String temp[] = br.readLine().split("\\s+");
        //     int x = Integer.parseInt(br.readLine());
        //     // int y = Integer.parseInt(temp[0]);
            
        // }
    }
}

