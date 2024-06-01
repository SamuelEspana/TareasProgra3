import tkinter as tk
import random
import graphviz

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_winner = None
        self.states = {}

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def get_board_state(self):
        return ''.join(self.board)

    def add_state(self, state):
        if state not in self.states:
            self.states[state] = {move: 0 for move in range(9)}

    def update_weights(self, move):
        for state in self.states:
            if move in self.states[state]:
                self.states[state][move] += 10

class TicTacToeGUI:
    def __init__(self, root):
        self.game = TicTacToe()
        self.root = root
        self.root.title("Proyecto Programación 3")
        self.buttons = [tk.Button(root, text=' ', font='normal 20 bold', height=3, width=6, command=lambda i=i: self.player_move(i)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)
        self.reset_button = tk.Button(root, text='Reiniciar', command=self.reset_game, font='normal 15 bold', bg='yellow')
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
        self.show_weights_button = tk.Button(root, text='Ver Ponderaciones', command=self.show_weights, font='normal 15 bold', bg='lightgreen')
        self.show_weights_button.grid(row=4, column=0, columnspan=3, sticky='nsew')
        self.graph_weights_button = tk.Button(root, text='Graficar Ponderaciones', command=self.graph_weights, font='normal 15 bold', bg='lightblue')
        self.graph_weights_button.grid(row=5, column=0, columnspan=3, sticky='nsew')
        self.credits_button = tk.Button(root, text='Créditos', command=self.show_credits, font='normal 15 bold', bg='lightgrey')
        self.credits_button.grid(row=6, column=0, columnspan=3, sticky='nsew')
        self.status_label = tk.Label(root, text="Tu turno", font='normal 15 bold', bg='lightblue')
        self.status_label.grid(row=7, column=0, columnspan=3, sticky='nsew')
        self.game_history = []

    def player_move(self, index):
        if self.game.board[index] == ' ' and not self.game.current_winner:
            self.game.make_move(index, 'X')
            self.buttons[index].config(text='X', state='disabled')
            self.game_history.append((self.game.get_board_state(), index))
            self.game.update_weights(index)
            if self.game.current_winner:
                self.status_label.config(text="¡Ganaste!")
                self.disable_all_buttons()
            elif not self.game.available_moves():
                self.status_label.config(text="¡Es un empate!")
            else:
                self.ai_move()

    def ai_move(self):
        state = self.game.get_board_state()
        self.game.add_state(state)
        available_moves = self.game.available_moves()
        if available_moves:
            move = random.choice(available_moves)
            self.game.make_move(move, 'O')
            self.buttons[move].config(text='O', state='disabled')
            self.game_history.append((self.game.get_board_state(), move))
            self.game.update_weights(move)
            if self.game.current_winner:
                self.status_label.config(text="La máquina ganó.")
                self.disable_all_buttons()
            elif not self.game.available_moves():
                self.status_label.config(text="¡Es un empate!")

    def disable_all_buttons(self):
        for button in self.buttons:
            button.config(state='disabled')

    def reset_game(self):
        self.game = TicTacToe()
        for button in self.buttons:
            button.config(text=' ', state='normal')
        self.status_label.config(text="Tu turno")

    def show_weights(self):
        weights_window = tk.Toplevel(self.root)
        weights_window.title("Ponderaciones de Movimientos")
        row = 0
        for state, moves in self.game.states.items():
            tk.Label(weights_window, text=f"Estado: {state}").grid(row=row, column=0, sticky='w')
            for move, weight in moves.items():
                tk.Label(weights_window, text=f"Mov: {move} -> Peso: {weight}").grid(row=row, column=1, sticky='w')
                row += 1

    def graph_weights(self):
        dot = graphviz.Digraph(comment='Ponderaciones de Tic Tac Toe')
        for state, moves in self.game.states.items():
            dot.node(state, state)
            for move, weight in moves.items():
                move_state = state[:move] + 'X' + state[move+1:]
                dot.node(move_state, move_state)
                dot.edge(state, move_state, label=str(weight))
        dot.render('tic_tac_toe_weights', format='png', view=True)

    def show_credits(self):
        credits_window = tk.Toplevel(self.root)
        credits_window.title("Créditos")
        credits = [
            "Jonathan Herrera 9490-22-11551",
            "Mario Culajay 9490-225771",
            "Segrio Sanchez 9490-21-1077",
            "Samuel España 9490-22-11789"
        ]
        for i, credit in enumerate(credits):
            tk.Label(credits_window, text=credit, font='normal 15 bold').grid(row=i, column=0, sticky='w')

if __name__ == '__main__':
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.mainloop()
