Slot Machine Game with PyQt5 
Introduction 
This is a simple Slot Machine Game implemented using PyQt5. The game allows the user to place a 
bet, and a virtual slot machine will spin three symbols. The user wins or loses money based on whether 
the symbols match. 
Features: 
• User starts with 100$. 
• User can place a bet, and the game will display spinning symbols. 
• If all three symbols match, the user wins. 
• The game shows the result of the spin, and the user's balance is updated accordingly. 
• The game has two options: Play or Quit. 
Requirements 
To run this project, you need the following: 
• Python 3.x (preferably Python 3.6 or later) 
• PyQt5 library for creating the graphical user interface (GUI) 
Install PyQt5 
To install PyQt5, use the following command: 
pip install PyQt5 
How to Run 
1. Clone or download the project to your local machine. 
2. Make sure you have Python and PyQt5 installed. 
3. Run the script: 
4. python slot_machine_game.py 
5. The game window will open, and you can start playing. 
Gameplay 
1. Enter your bet number in the input box. 
By Eng.Marwan Ahmed Ibrahim 
2. Click the Play button to spin the slot machine. 
3. If all three symbols match, you win money. Otherwise, you lose the bet. 
4. You can click the Quit button to exit the game at any time. Your current balance will be 
displayed before quitting. 
Game Interface 
The graphical user interface (GUI) consists of: 
• A Label showing the current balance. 
• An Input field for entering the bet amount. 
• Two buttons: 
o Play: Starts the game and spins the slot machine. 
o Quit: Exits the game and displays the final balance. 
Slot Symbols: 
•       (Gold medal): Highest reward. 
•       (Silver medal): Medium reward. 
•       (Bronze medal): Lowest reward. 
Code Explanation 
The core of the game is as follows: 
• Window Setup: The window is created using QWidget and styled using QPalette for a black 
background. 
• Bet Input: The user inputs their bet in a QLineEdit field. 
• Spin Mechanism: Random symbols are chosen for each of the three slots, and they spin for a 
while before the final result is displayed. 
• Result Evaluation: If all three symbols are the same, the user wins a reward depending on the 
symbol. The money is updated after each round. 
• Quit Option: If the user clicks "Quit", the game closes, and the final balance is displayed in a 
message box.
