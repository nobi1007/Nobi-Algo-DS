import java.util.*;
class Trees{
    static class Node{
        public int data;
        public Node left = right = null;
        public Node(int value){
            this.data = value;
            this.left = this.right = null;
        }
    }

    public static Node insert(Node root, int value){
        if(root == null){
            root = new Node(value);
        }
        if(value<root.left.data){
            
        }
    }
}
