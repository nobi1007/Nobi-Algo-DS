import java.util.*;
class Main2{
    public static void main(String[] args) {
        HashMap<Integer,ArrayList<Integer>> dic = new HashMap<>();
        dic.put(2,new ArrayList<>(Arrays.asList(2,3)));
        System.out.println(dic); 
        System.out.println(dic.containsKey(3));
    }
}