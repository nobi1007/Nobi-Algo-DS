import java.util.*;
import java.io.*;
import java.lang.*;

class KMP_substring_search{
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String pattern = "cabc";
        // String str = "acacabacacabacacac";
        // String str = "aabaabaaa";
        char[] arr = pattern.toCharArray();
        int j=0;

        String string = "abxabbcaabcabc";
        char str[] = string.toCharArray();

        int common[] = new int[arr.length];
        common[0] = 0;
        for(int i=1;i<arr.length;){
            if(arr[i]==arr[j]){
                common[i] = j+1;
                j++;
                i++;
            }
            else{
                if(j==0){
                    common[i] = 0;
                    i++;
                }
                else{
                    j--;
                    j = common[j];
                }
            }
        }
        System.out.println(Arrays.toString(common));
        j = 0;
        for(int i=0;i<str.length;){
            if(str[i]==arr[j]){
                i++;
                j++;
            }
            else{
                if(j==0){
                    i++;
                }
                else{
                    j--;
                    j = common[j];
                }
            }
            if(j==arr.length){
                j--;
                System.out.println("Match found at "+(i-arr.length));
            }
        }        
        // j = 0;
        // int common[] = new int[pattern.length()];
        // common[0] = 0;


        // for(int i=1;i<pattern.length();){
        //     if(arr[j]==arr[i]){
        //         common[i] = ++j;
        //         i++;
        //     }
        //     else{
        //         if(j==0){
        //             common[i] = 0;
        //             i++;
        //         }
        //         else{
        //             j--;
        //             j = common[j];
        //         }
        //     }
        // }


        // j=0;
        // for(int i=0;i<string.length() && j<pattern.length();){
        //     if(str[i]==arr[j]){
        //         i++;
        //         j++;
        //     }
        //     else{
        //         if(j!=0){
        //             j--;
        //             j = common[j];   
        //         }
        //         else{
        //             i++;
        //         }
        //     }
        //     if(j==pattern.length()){
        //         System.out.println("Found at "+(i-pattern.length()));
        //         j--;
        //     }
        // }

        // System.out.println(Arrays.toString(common));
    }
}