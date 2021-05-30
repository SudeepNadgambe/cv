import java.util.Scanner;
public class Rockpaperscissors
{
    public static void main(String args[]){
        int randnum = (int)(Math.random() * 2);
        
        Scanner scan = new Scanner(System.in);
        //System.out.println(randnum);
        System.out.println("chose from the following options:\n<1>=rock\n<2>=paper\n<3>=scissor");
        int choice = scan.nextInt();
        
        if(choice == 1){
            if(randnum == 2){
                System.out.println("you lose:paper covers rock.");
                
            }
            else{
                System.out.println("you win:rock breaks scissor.");
            }
        }
        if(choice == 2){
            if(randnum == 3){
                System.out.println("you lose:scissor cuts paper.");
            }
            else{
                System.out.println("you win:paper covers rock.");
            }
        }
        if(choice == 3){
            if(randnum == 1){
                System.out.println("you lose:rock breaks scissor.");
            }
            else{
                System.out.println("you win:scissor cuts paper.");
            }
        }
        else{
            System.out.println("you should choose number only between 1-3");
            
        }
    }
}
