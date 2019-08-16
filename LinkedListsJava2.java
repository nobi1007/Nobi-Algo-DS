/*
Following methods are covered in the following code:
1 - Adding the data at last of the list
2 - Adding the value infront of the list
3 - Adding the value at the specfic location
4 - Reversing the linked list and returning the head node
5 - Deleting the value from the list at the specified location
6 - Printing the Linked List from the provided head
7 - MORE TO ADD
*/

import java.util.*;

class LinkedListJava2{
    static class Node{
        public int data;
        public Node next;
        public Node(int value){
            this.data = value;
            this.next = null;
        }
    }

    //the append method adds the new value at the last of the list.
    public static Node append(Node head, int value){
        if(head==null){
            head = new Node(value);
        }
        else{
            Node temp = head;
            while(temp.next!=null){
                temp = temp.next;
            }
            Node node = new Node(value);
            temp.next = node;
        }
        return head;
    }

    //the lappend method adds the new value in front of the list.
    public static Node lappend(Node head, int value){
        if(head == null){
            head = new Node(value);
            return head;
        }
        else{
            Node temp = new Node(value);
            temp.next = head;
            return temp;
        }
    }

    //printList method prints all the values starting from the provided head.
    public static void printList(Node head){
        if(head!=null){
            while(head!=null){
                System.out.println(head.data);
                head = head.next;
            }
        }
    }

    public static void main(String args[]){
        Node head = new Node(1);
        head = append(head,2);
        head = append(head,3);
        head = append(head,4);
        head = lappend(head,5);
        head = lappend(head,6);
        head = append(head,7);
        printList(head);

        /*
        Output of the following code:
        6
        5
        1
        2
        3
        4
        7
        */

    }
}

