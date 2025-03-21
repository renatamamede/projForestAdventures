# O jogo vai ser executado na classe Game, que está no pacote 'code'. Aqui no main, vamos chamar Game

from code.game import Game  # Precisamos importar a classe lá do code

game = Game()  # Aqui usamos a classe importada
game.run()  # Aqui chamamos a função run da classe Game para executar o jogo
