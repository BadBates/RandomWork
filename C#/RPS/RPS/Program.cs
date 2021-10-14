using System;

namespace RPS //Rock, Paper, Scissors
{
    class Program
    {
        static void Main(string[] args)
        {
            string pGuess, cpuGuess;
            int randomInt;
            bool playAgain = true;

            

            Random rnd = new Random();

            while (playAgain == true) {
                int playerScore = 0, cpuScore = 0;

                while (playerScore <= 7 && cpuScore <= 7)
                {
                    //Player's choice or input
                    Console.Write("Chooise  between Rock, Paper, and Scissors: ");
                    pGuess = Console.ReadLine();
                    pGuess = pGuess.ToUpper();
                    
                    
                    //"Computer AI PLAYER"
                    randomInt = rnd.Next(1, 3);
                    switch (randomInt)
                    {
                        case 1:
                            cpuGuess = "Rock";
                            Console.WriteLine("Computer choose Rock.");
                            if (pGuess == "Rock")
                                Console.WriteLine("It's a draw");
                            else if (pGuess == "Paper")
                            {
                                playerScore++;
                                Console.WriteLine("You win this one.", playerScore.ToString());
                            }
                            else if (pGuess == "Scissors")
                            {
                                cpuScore++;
                                Console.WriteLine("I win this one.", cpuScore.ToString());
                            }
                            break;
                        case 2:
                            cpuGuess = "Paper";
                            Console.WriteLine("Computer choose Paper.");
                            if (pGuess == "Paper")
                                Console.WriteLine("It's a draw");
                            else if (pGuess == "Scissors")
                            {
                                playerScore++;
                                Console.WriteLine("You win this one.", playerScore.ToString());
                            }
                            else if (pGuess == "Rock")
                            {
                                cpuScore++;
                                Console.WriteLine("You win this one.", cpuScore.ToString());
                            }
                            break;
                        case 3:
                            cpuGuess = "Scissors";
                            Console.WriteLine("Computer choose Scissors.");
                            if (pGuess == "Scissors")
                                Console.WriteLine("It's a draw");
                            else if (pGuess == "Rock")
                            {
                                playerScore++;
                                Console.WriteLine("You win this one.", playerScore.ToString());
                            }
                            else if (pGuess == "Paper")
                            {
                                cpuScore++;
                                Console.WriteLine("I win this one.", cpuScore.ToString());
                            }
                            break;

                        default:
                            Console.WriteLine("Invalid Object");
                            break;

                    }
                    if (playerScore == 7)
                        Console.WriteLine("You Win!!!");
                    else if (cpuScore == 7)
                        Console.WriteLine("Computer Wins");
                }
                Console.WriteLine("Do you want to play again?  Answer(y/n)");
                string loop = Console.ReadLine();
                if (loop == "y")
                    playAgain = true;
                else if(loop == "n")
                    playAgain = false;
            }
        }
    }
}