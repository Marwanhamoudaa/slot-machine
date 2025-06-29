import sys
import random
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette


class SlotMachineGame(QWidget):
    def __init__(self):
        super().__init__()

        self.money = 100  # Starting money
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Slot Machine Game")
        self.setFixedSize(450, 500)  # Increase the window size to make it more spacious

        # Set background color to black
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 0, 0))  # Black background
        self.setPalette(palette)

        # Create widgets
        self.money_label = QLabel(f"Your money: {self.money}$", self)
        self.money_label.setStyleSheet("font-size: 22px; color: white; font-weight: bold;")

        self.bet_input = QLineEdit(self)
        self.bet_input.setPlaceholderText("Enter your bet number")
        self.bet_input.setStyleSheet("""
            font-size: 18px;
            padding: 15px;
            background-color: white;
            color: black;
            border-radius: 8px;
            min-width: 250px;  /* Increase width of the input box */
            max-width: 300px;  /* Set max width */
        """)

        self.play_button = QPushButton("Play", self)
        self.play_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-size: 20px;
            padding: 15px;
            border-radius: 8px;
        """)

        self.quit_button = QPushButton("Quit", self)
        self.quit_button.setStyleSheet("""
            background-color: #f44336;
            color: white;
            font-size: 20px;
            padding: 15px;
            border-radius: 8px;
        """)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.money_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.bet_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.play_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.quit_button, alignment=Qt.AlignCenter)

        # Set spacing between widgets
        layout.setSpacing(20)

        self.setLayout(layout)

        # Connect signals
        self.play_button.clicked.connect(self.play_game)
        self.quit_button.clicked.connect(self.quit_game)

    def play_game(self):
        try:
            bet = int(self.bet_input.text())
            if bet > self.money:
                self.show_message("Sorry, you don't have enough money.")
                return
        except ValueError:
            self.show_message("Sorry, invalid bet number.")
            return

        # Simulate the slot machine
        symbols = ["🥇", "🥈", "🥉"]
        slots = ["-", "-", "-"]
        for i in range(10):
            slots[0] = random.choice(symbols)
            self.update_slots(slots)
            time.sleep(0.1)

        for i in range(20):
            slots[1] = random.choice(symbols)
            self.update_slots(slots)
            time.sleep(0.1)

        for i in range(20):
            slots[2] = random.choice(symbols)
            self.update_slots(slots)
            time.sleep(0.1)

        self.update_slots(slots)
        result = self.check_result(slots)

        if result == 0:
            self.money -= bet
            self.show_message("Sorry, you lost.")
        else:
            self.money += bet * result
            self.show_message(f"Congratulations! You won {bet * result}$.")

        self.money_label.setText(f"Your money: {self.money}$")

    def check_result(self, slots):
        if slots[0] == slots[1] == slots[2]:
            if slots[0] == "🥇":
                return 3
            elif slots[0] == "🥈":
                return 2
            else:
                return 1
        return 0

    def update_slots(self, slots):
        self.money_label.setText(f"Your money: {self.money}$\n| {slots[0]} | {slots[1]} | {slots[2]} |")
        QApplication.processEvents()

    def quit_game(self):
        self.show_message(f"Goodbye! Your final money is {self.money}$")
        self.close()

    def show_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Slot Machine Game")
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = SlotMachineGame()
    game.show()
    sys.exit(app.exec_())
