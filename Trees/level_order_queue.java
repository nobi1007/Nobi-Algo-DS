import java.util.*;
import java.io.*;
import java.lang.*;

class Node{
    Node left,right;
    int data;
    Node(int data){
        this.left = this.right = null;
        this.data = data;
    }
}

class level_order_queue{
    public static Node insert(Node root, int data){
        if(root==null){
            return new Node(data);
        }
        else{
            Node cur;
            if(root.data>data){
                cur = insert(root.left,data);
                root.left = cur;
            }
            else{
                cur = insert(root.right,data);
                root.right = cur;
            }
            return root;
        }
    }

    public static void levelOrder(Node root){
        Queue<Node> queue = new LinkedList<Node>();
        if(root==null){
            return;
        }
        queue.add(root);
        while(!queue.isEmpty()){
            Node temp = queue.remove();
            System.out.println(temp.data);
            if(temp.left!=null){
                queue.add(temp.left);
            }
            if(temp.right!=null){
                queue.add(temp.right);
            }
        }
    }

    public static void main(String args[])throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Node root = new Node(3);
        root = insert(root,1);
        root = insert(root,2);
        root = insert(root,5);
        root = insert(root,4);


        // System.out.println(root.data);
        // System.out.println(root.left.data);
        // System.out.println(root.right.data);
        // System.out.println(root.left.right.data);
        // System.out.println(root.right.left.data);

        levelOrder(root);
    }
}