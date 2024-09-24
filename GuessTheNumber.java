import java.util.Random;
import java.util.Scanner;

public class GuessTheNumber{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        boolean playAgain = true;
        int totalRounds = 0;
        int totalScore = 0;

        System.out.println("Welcome to Hari vamsi's Number Guessing Game!");

        while (playAgain) {
            int numberToGuess = random.nextInt(100) + 1;
            int attempts = 0;
            int maxAttempts = 10;
            boolean hasGuessedCorrectly = false;

            System.out.println("I have generated a number between 1 and 100,Try to guess it!");
            System.out.println("You have " + maxAttempts + " attempts left.");

            while (attempts < maxAttempts && !hasGuessedCorrectly) {
                System.out.print("Enter your guess: ");
                int userGuess = scanner.nextInt();
                attempts++;

                if (userGuess == numberToGuess) {
                    hasGuessedCorrectly = true;
                    System.out.println("Congratulations! You guessed the number in " + attempts + " attempts.");
                    totalScore += maxAttempts - attempts + 1;
                } else if (userGuess > numberToGuess) {
                    System.out.println("Too high! Try again.Guess a bit lower");
                } else {
                    System.out.println("Too low! Try again.Guess a bit higher");
                }
            }

            if (!hasGuessedCorrectly) {
                System.out.println("Sorry, you've used up all of your attempts. The correct number was : " + numberToGuess);
            }

            totalRounds++;
            System.out.println("Your current score: " + totalScore);

            System.out.print("Do you wanna play another round? (yes/no) : ");
            String response = scanner.next();
            if (!response.equalsIgnoreCase("yes")) {
                playAgain = false;
            }
        }

        System.out.println("Game over! You played " + totalRounds + " round(s) with a total score of " + totalScore);
        scanner.close();
    }
}
