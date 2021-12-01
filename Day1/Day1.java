import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day1 {
    public static void main(String[] args) throws FileNotFoundException {
        File input = new File("input.txt");
        Scanner scanner = new Scanner(input);
        int[] arr = new int[10000]; //array to hold the input
        int i =0;
        
        // reading input into array
        while(scanner.hasNext()){
        arr[i++] = scanner.nextInt();
        }
        
        int counter = 0;
        for(int j=0;j<arr.length-1;j++) {
            int current = arr[j];
             
            if(arr[j+1] > current){
                counter++;
            }
            
        }

        System.out.println(counter);
    }
}
