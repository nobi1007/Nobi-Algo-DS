import java.util.*;
class Main{

    private static void printArr(int[][] x){
        int n = x.length;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                System.out.print(x[i][j]+" ");
            }
            System.out.println();
        }
    }

    private static void printList(HashMap<Integer,ArrayList<Integer>> map){
        Set<Integer> keys = map.keySet();
        for(Integer key: keys){
            System.out.println(key+" -> "+map.get(key));
        }
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int ver = sc.nextInt();
        int edg = sc.nextInt();
        int adgMat[][] = new int[ver][ver];
        HashMap<Integer,ArrayList<Integer>> adgList = new HashMap<>();

        for(int i=0;i<edg;i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            adgMat[x-1][y-1] = 1;
            if(adgList.containsKey(x)){
                adgList.get(x).add(y);
            }
            else{
                adgList.put(x,new ArrayList<>(Arrays.asList(y)));
            }
        }
        printArr(adgMat);
        printList(adgList);
    }
}