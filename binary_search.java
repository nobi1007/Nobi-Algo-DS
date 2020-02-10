import java.util.*;
import java.io.*;
import java.lang.*;

class binary_search{
    // this function will return where the item can be inserted if it is not present
    public static int binarySearch(int[] arr, int item, int low, int high){
        int mid = (low+high)/2;
        if(low>=high){
            System.out.println("Item not present but can be inserted at : ");
            if(low>=arr.length)
            return arr.length;
            else if(item>arr[low])
            return low+1;
            else
            return low;
        }
        else if(arr[mid]==item){
            return mid;
        }
        else{
            if(arr[mid]>item)
            return binarySearch(arr, item, low, mid);
            return binarySearch(arr, item, mid+1, high); 
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int arr[] = new int[n];

        String[] inp = br.readLine().split("\\s+");
        int i=0;
        for(String temp:inp){
            arr[i++] = Integer.parseInt(temp.trim());
        }

        // for(int x:arr){
        //     System.out.println(x);
        // }

        int item = Integer.parseInt(br.readLine());

        int pos = binarySearch(arr, item, 0, arr.length);

        System.out.println("Out --> "+pos);
    }
}
