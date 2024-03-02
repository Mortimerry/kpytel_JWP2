class OX:


    def __init__(self):

        self.ALL_SPACES = list('123456789')
        self.currentPlayer = 'X'
        self.nextPlayer = 'O'

    def getBlankBoard(self):
        """Tworzy nową, pustą planszę gry w kółko i krzyżyk."""
        board = {}  # Plansza jest reprezentowana przez słownik Pythona.
        for space in self.ALL_SPACES:
            board[space] = ' '  # Wszystkie pola na początku są puste.
        return board


    def getBoardStr(self):
        """Zwraca tekstową reprezentację planszy."""
        return f'''
                {self.gameBoard['1']}|{self.gameBoard['2']}|{self.gameBoard['3']} 1 2 3 
                -+-+- 
                {self.gameBoard['4']}|{self.gameBoard['5']}|{self.gameBoard['6']} 4 5 6 
                -+-+- 
                {self.gameBoard['7']}|{self.gameBoard['8']}|{self.gameBoard['9']} 7 8 9'''


    def isValidSpace(self, move):
        """Zwraca True, jeśli pole na planszy ma prawidłowy numer i pole jest puste."""
        if move is None:
            return False
        return move in self.ALL_SPACES or self.self.gameBoard[move] == ' '

    def updateBoard(self, space):
        """Ustawia pole na planszy na podany znak."""
        self.gameBoard[space] = self.currentPlayer

    def isWinner(self):
        """Zwraca True, jeśli gracz jest zwycięzcą tej planszy KIK."""
        b, p = self.gameBoard, self.currentPlayer  # Krótsze nazwy jako "składniowy cukier".
        # Sprawdzenie, czy trzy takie same znaki występują w wierszach, kolumnach i po przekątnych.
        return ((b['1'] == b['2'] == b['3'] == p) or  # poziomo na górze
                (b['4'] == b['5'] == b['6'] == p) or  # poziomo w środku
                (b['7'] == b['8'] == b['9'] == p) or  # poziomo u dołu
                (b['1'] == b['4'] == b['7'] == p) or  # pionowo z lewej
                (b['2'] == b['5'] == b['8'] == p) or  # pionowo w środku
                (b['3'] == b['6'] == b['9'] == p) or  # pionowo z prawej
                (b['3'] == b['5'] == b['7'] == p) or  # przekątna 1
                (b['1'] == b['5'] == b['9'] == p))  # przekątna 2

    def isBoardFull(self,space):
        """Zwraca True, jeśli wszystkie pola na planszy są zajęte."""
        for space in self.ALL_SPACES:
            if self.gameBoard[space] == ' ':
                return False  # Jeśli nawet jedno pole jest puste, zwracaj False.
        return True  # Nie ma wolnych pól, zatem zwróć True.
    def play(self):

        self.gameBoard = self.getBlankBoard()  # Utwórz słownik planszy KIK.

        while True:
            print(self.getBoardStr())  # Wyświetl planszę na ekranie.

            # Zadawaj graczowi pytanie, aż wprowadzi prawidłową liczbę od 1 do 9:
            move = None
            while not self.isValidSpace(move):
                print(f'Jaki jest ruch gracza {self.currentPlayer}? (1-9)')
                move = input()
            self.updateBoard(move)  # Wykonanie ruchu.
            # Sprawdzenie, czy gra jest zakończona:
            if self.isWinner():  # Sprawdzenie, kto wygrał.
                print(self.getBoardStr())
                print(self.currentPlayer + ' wygrał grę!')
                break
            elif self.isBoardFull():  # Sprawdzenie remisu.
                print(self.getBoardStr())
                print('Gra zakończyła się remisem!')
                break
            self.currentPlayer, self.nextPlayer = self.nextPlayer, self.currentPlayer  # Zmiana gracza.
        print('Dziękuję za grę!')



#Test gry

gra = OX()

gra.play()