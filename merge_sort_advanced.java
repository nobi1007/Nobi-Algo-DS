// This program will find the number of inversions

import java.io.*;
import java.lang.*;
import java.util.*;

class merge_sort_advanced{

    // static int swaps;

    // static{
    //     swaps = 0;
    // }

    public static int merge(int[] arr, int left, int mid, int right){
        int n1 = mid - left + 1;
        int n2 = right - mid;
        
        int temp1[] = new int[n1];
        int temp2[] = new int[n2];


        for(int i=0;i<n1;i++){
            temp1[i] = arr[i+left];
        }

        int midv = mid+1;
        for(int i=0;i<n2;i++){
            temp2[i] = arr[i+midv];
        }
        
        // System.out.println("part 1");
        // for(int x:temp1)
        // System.out.println(x);

        // System.out.println("part 2");
        // for(int x:temp2)
        // System.out.println(x);

        int i=0;int j=0;
        int swaps = 0;

        int k=left;
        while(i<n1 && j<n2){
            if(temp1[i]<=temp2[j]){
                arr[k] = temp1[i];
                // k+;
                // total++;
                i++;
            }
            else{
                arr[k] = temp2[j];
                // k++;
                swaps += (mid+1)- (left+i);
                j++;
            }
            k++;
        }

        while(i<n1){
            arr[k] = temp1[i];
            k++;
            i++;
        }

        while(j<n2){
            arr[k] = temp2[j];
            k++;
            j++;
        }

        // for(int temp:arr){
        //     System.out.print(temp+" ");
        // }

        // System.out.println();
        return swaps;

    }

    public static int mergeSort(int[] arr, int left, int right){
        int count = 0;
        if(right>left){
            // int count = 0;
            int mid = (left+right)/2;
            // int n = right-left+1;
            count += mergeSort(arr, left, mid);
            count += mergeSort(arr, mid+1, right);
            count += merge(arr,left,mid,right);    
        }
        return count;
        
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        while(t-->0){
            int n = Integer.parseInt(br.readLine());
            String inp[] = br.readLine().split("\\s+");
            int arr[] = new int[n];
            int pos=0;
            for(String temp:inp){
                arr[pos++] = Integer.parseInt(temp);
            }
            int total = mergeSort(arr, 0, arr.length-1);
            // merge(arr, 0, (int)arr.length/2, arr.length);
            // System.out.println("After sorting - ");
            // for(int x:arr){
            //     System.out.println(x);
            // }
            // System.out.println("Inversions - ");
            System.out.println(total);
            
        }
    }
}