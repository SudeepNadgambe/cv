import java.util.Scanner;
public class KBC 
{
    public static void main(String args []){
        Scanner scan = new Scanner (System.in);
        
        //KEYBOARD INPUT
        String mcq [][] = new String [10][3];
        
        //QUESTION
        
        mcq [0][0] = "Where was corona virus originated ?";
        mcq [1][0] = "Where is Gokuldham society situated ?";
        mcq [2][0] = "For what agency do the team scorpion work ?";
        mcq [3][0] = "Walter O'brien has an IQ of _?";
        mcq [4][0] = "WHO is an organization related to ?";
        mcq [5][0] = "In what language did I wrote this game ?";
        mcq [6][0] = "Will you watch JOHN WICK 4 ?";
        mcq [7][0] = "Was einstein a player(:/) ?";
        mcq [8][0] = "Will Rahul gandhi ever be a Prime minister of INDIA ?";
        mcq [9][0] = "What is the popular slang of Sheldon cooper ?";
        
        //OPTIONS
        mcq [0][1] = "<A> India. \n<B> China. \n<C> Africa.";
        mcq [1][1] = "<A> Andheri. \n<B> Borivali. \n<C> Goregaon.";
        mcq [2][1] = "<A> NASA. \n<B> CIA. \n<C> Homeland.";
        mcq [3][1] = "<A> 197. \n<B> 198. \n<C> 199.";
        mcq [4][1] = "<A> Sports. \n<B> Health. \n<C> Military.";
        mcq [5][1] = "<A> C++. \n<B> Python. \n<C> Java.";
        mcq [6][1] = "<A> Yes. \n<B> Absolutely Yes. \n<C> No way.";
        mcq [7][1] = "<A> How would i know. \n<B> Yes. \n<C> No,he's a genius.";
        mcq [8][1] = "<A> Yes. \n<B> Humans will fly. \n<C> No.";
        mcq [9][1] = "<A> Bazinga!!. \n<B> oh no . \n<C> Hello!! .";
        
        //ANSWERS
        mcq [0][2] = "b";
        mcq [1][2] = "c";
        mcq [2][2] = "c";
        mcq [3][2] = "a";
        mcq [4][2] = "b";
        mcq [5][2] = "c";
        mcq [6][2] = "a";
        mcq [7][2] = "b";
        mcq [8][2] = "c";
        mcq [9][2] = "a";
        
        //INTERFACE
        int money = 100;
        System.out.println("Welcome to KBC game ");
        System.out.println("You currently have : " +money+"$\nFor every correct answer you win 50$\nHowever for every incorrect answer you lose 50$\n\tGOOD LUCK!!!\n\n");
        
        int i;
        for(i=0; i<mcq.length; i++){
            if(money > 0){
                System.out.println("Question"+(i+1)+":");
                System.out.println(mcq[i][0]);
                System.out.println(mcq[i][1]);
                String answer = scan.next();
                if(answer.equals(mcq[i][2])){
                    money+=50;
                    System.out.println("Good Job !!\nYou win 50$ !!\nCurrently you have :"+money+"$");
                    
                }
                else{
                    money-=50;
                    System.out.println("Sorry you chose incorrect option ...\nCurrently you have : "+money+"$");
                    
                    
                }
                
            }
            else{
                    i = mcq.length;
                    System.out.println("GAME OVER");
            }
            
        }
        if(money==600){
            System.out.println("CONGRATULATIONS!! YOU ARE THE WINNER");
        }
    }
        
        
        
        
       
        
       
        
}

