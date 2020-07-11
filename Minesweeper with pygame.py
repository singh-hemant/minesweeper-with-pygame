import pygame
import random
import sys


class Minesweeper:
    def __init__(self, size=20):
        self.size = size
        self.matrix = []
        self.list = []
        for i in range(self.size):
            rows= []
            rows2 = []
            for j in range(self.size):
                rows.append(' ')
                rows2.append(0)
            self.matrix.append(rows)
            self.list.append(rows2)

    def put_mines(self, mines_count =20):
        for _ in range(mines_count):
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)
            self.matrix[x][y] = "X"

    def check_mines(self):
        for i in range(self.size):
            for j in range(self.size):
                count = 0
                if self.matrix[i][j] != "X":
                    if i == 0:
                        if j == 0:
                            if self.matrix[i][j+1] == "X":
                                count += 1
                            if self.matrix[i+1][j+1] == "X":
                                count += 1
                            if self.matrix[i+1][j] == "X":
                                count += 1
                        elif j == self.size - 1:
                            if self.matrix[i][j-1] == "X":
                                count += 1
                            if self.matrix[i+1][j-1] == "X":
                                count += 1
                            if self.matrix[i+1][j] == "X":
                                count += 1
                        else:
                            if self.matrix[i][j-1] == "X":
                                count += 1
                            if self.matrix[i+1][j-1] == "X":
                                count += 1
                            if self.matrix[i+1][j] == "X":
                                count += 1
                            if self.matrix[i+1][j+1] == "X":
                                count += 1
                            if self.matrix[i][j+1] == "X":
                                count += 1
                    elif i == self.size - 1:
                        if j == 0:
                            if self.matrix[i-1][j] == "X":
                                count += 1
                            if self.matrix[i-1][j+1] == "X":
                                count += 1
                            if self.matrix[i][j+1] == "X":
                                count += 1
                        elif j == self.size - 1:
                            if self.matrix[i-1][j] == "X":
                                count += 1
                            if self.matrix[i-1][j-1] == "X":
                                count += 1
                            if self.matrix[i][j-1] == "X":
                                count += 1
                        else:
                            if self.matrix[i][j-1] == "X":
                                count += 1
                            if self.matrix[i-1][j-1] == "X":
                                count += 1
                            if self.matrix[i-1][j] == "X":
                                count += 1
                            if self.matrix[i-1][j+1] == "X":
                                count += 1
                            if self.matrix[i][j+1] == "X":
                                count += 1
                    else:
                        if j == 0:
                            if self.matrix[i-1][j] == "X":
                                count += 1
                            if self.matrix[i-1][j+1] == "X":
                                count += 1
                            if self.matrix[i][j+1] == "X":
                                count += 1
                            if self.matrix[i+1][j+1] == "X":
                                count += 1
                            if self.matrix[i+1][j] == "X":
                                count += 1

                        elif j == self.size - 1:
                            if self.matrix[i-1][j] == "X":
                                count += 1
                            if self.matrix[i-1][j-1] == "X":
                                count += 1
                            if self.matrix[i][j-1] == "X":
                                count += 1
                            if self.matrix[i+1][j-1] == "X":
                                count += 1
                            if self.matrix[i+1][j] == "X":
                                count += 1

                        else:
                            if self.matrix[i-1][j-1] == "X":
                                count += 1
                            if self.matrix[i-1][j] == "X":
                                count += 1
                            if self.matrix[i-1][j+1] == "X":
                                count += 1
                            if self.matrix[i][j+1] == "X":
                                count += 1
                            if self.matrix[i+1][j+1] == "X":
                                count += 1
                            if self.matrix[i+1][j] == "X":
                                count += 1
                            if self.matrix[i+1][j-1] == "X":
                                count += 1
                            if self.matrix[i][j-1] == "X":
                                count += 1

                    if count > 0:
                        self.matrix[i][j] = count

    # For console printing+
    def printing(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.matrix[i][j], end="  ")
            print()


def main():
    minesweeper = Minesweeper(20)
    minesweeper.put_mines()
    minesweeper.check_mines()
    minesweeper.printing()


# Game Loop Pygame
class Game:
    def __init__(self):
        # game properties
        self.width = 750
        self.height = 600
        self.matrix_size = 15
        self.font_size = 24
        self.ith_padding = 15
        self.jth_padding = 5
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (0, 200, 0)
        self.red = (150, 20, 0)
        self.mines_count =  20

        self.no_of_boxes_left = self.matrix_size**2 - self.mines_count
        #self.score = 0
        # ---------end ----------

        # for Handling background logic
        self.minesweeper = Minesweeper(self.matrix_size)
        self.minesweeper.put_mines(self.mines_count)
        self.minesweeper.check_mines()
        self.save = []


        # create a window
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface((self.width, self.height))
        pygame.display.set_caption("MineSweeper")
        self.font = pygame.font.SysFont("Arial", self.font_size, "bold")
        self.clock = pygame.time.Clock()

        self.start_game()

    def gameloop(self):
        self.sizeb = self.height/self.minesweeper.size
        run = True
        x, y, a, b = 0, 0, 0, 0
        self.window.fill((255, 255, 255))
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.save.append((x, y))
            for i in range(self.minesweeper.size):
                for j in range(self.minesweeper.size):
                    if (x, y) in self.save:
                        if (x > i*self.sizeb) and (x < i*self.sizeb + self.sizeb) and (y > j*self.sizeb) and (y < j*self.sizeb + self.sizeb):

                            # Game over finding X
                            if self.minesweeper.matrix[i][j] == "X":
                                self.rect = pygame.draw.rect(self.window, self.red, (
                                                            i * self.sizeb + 2, j * self.sizeb + 2, self.sizeb - 2, self.sizeb - 2))
                                self.window.blit(self.font.render(str(self.minesweeper.matrix[i][j]), True, self.black), (i*self.sizeb+self.ith_padding, j*self.sizeb+self.jth_padding))
                                run = False
                                pygame.display.update()
                                pygame.time.wait(500)
                                self.game_over()
                            elif self.minesweeper.matrix[i][j] == ' ':
                                self.minesweeper.list[i][j] = 10
                                self.auto_blank_fill(i, j)
                            else:
                                self.minesweeper.list[i][j] = int(self.minesweeper.matrix[i][j])
                                self.rect = pygame.draw.rect(self.window, self.green, (i*self.sizeb+2, j*self.sizeb+2, self.sizeb-2, self.sizeb-2))
                                self.window.blit(self.font.render(str(self.minesweeper.matrix[i][j]), True, self.black), (i*self.sizeb+self.ith_padding, j*self.sizeb+self.jth_padding))

                    else:
                        pygame.draw.rect(self.window, (0, 100, 100), (i*self.sizeb+2, j*self.sizeb+2, self.sizeb-2, self.sizeb-2))

            self.scoring()
            if self.no_of_boxes_left == 0:
                self.you_win()
            pygame.display.update()

    def auto_blank_fill(self, i, j):
        self.rect = pygame.draw.rect(self.window, self.green,(i * self.sizeb + 2, j * self.sizeb + 2, self.sizeb - 2, self.sizeb - 2))
        self.window.blit(self.font.render(str(self.minesweeper.matrix[i][j]), True, self.black),(i * self.sizeb + self.ith_padding, j * self.sizeb + self.jth_padding))

        if self.minesweeper.matrix[i][j]:
            if i == 0:
                if j == 0:
                    if self.minesweeper.matrix[i][j + 1] == ' ':# and self.minesweeper.list[i][j+1] == 0:
                        self.auto_blank_fill(i, j + 1)
                    if self.minesweeper.matrix[i + 1][j + 1] == ' ':# and self.minesweeper.list[i][j+1] == 0:
                        self.auto_blank_fill(i+1, j+1)
                    if self.minesweeper.matrix[i + 1][j] == ' ':# and self.minesweeper.list[i][j+1] == 0:
                        self.auto_blank_fill(i+1, j)
                elif j == self.minesweeper.size - 1:
                    if self.minesweeper.matrix[i][j - 1] == ' ':
                        self.auto_blank_fill(i, j-1)
                    if self.minesweeper.matrix[i + 1][j - 1] == ' ':
                        self.auto_blank_fill(i+1, j-1)
                    if self.minesweeper.matrix[i + 1][j] == ' ':
                        self.auto_blank_fill(i+1, j)
                # else:
                #     if self.minesweeper.matrix[i][j - 1] == ' ':
                #         self.auto_blank_fill(i, j-1)
                #     if self.minesweeper.matrix[i + 1][j - 1] == ' ':
                #         self.auto_blank_fill(i+1, j-1)
                #     if self.minesweeper.matrix[i + 1][j] == ' ':
                #         self.auto_blank_fill(i+1, j)
                #     if self.minesweeper.matrix[i + 1][j + 1] == ' ':
                #         self.auto_blank_fill(i+1, j+1)
                #     if self.minesweeper.matrix[i][j + 1] == ' ':
                #         self.auto_blank_fill(i, j+1)
            # elif i == self.minesweeper.size - 1:
            #     if j == 0:
            #         if self.minesweeper.matrix[i - 1][j] == ' ':
            #             self.auto_blank_fill(i-1, j)
            #         if self.minesweeper.matrix[i - 1][j + 1] == ' ':
            #             self.auto_blank_fill(i-1, j+1)
            #         if self.minesweeper.matrix[i][j + 1] == ' ':
            #             self.auto_blank_fill(i, j+1)
            #     elif j == self.minesweeper.size - 1:
            #         if self.minesweeper.matrix[i - 1][j] == ' ':
            #             self.auto_blank_fill(i-1, j)
            #         if self.minesweeper.matrix[i - 1][j - 1] == ' ':
            #             self.auto_blank_fill(i-1, j-1)
            #         if self.minesweeper.matrix[i][j - 1] == ' ':
            #             self.auto_blank_fill(i, j-1)
            #     else:
            #         if self.minesweeper.matrix[i][j - 1] == ' ':
            #             self.auto_blank_fill(i, j-1)
            #         if self.minesweeper.matrix[i - 1][j - 1] == ' ':
            #             self.auto_blank_fill(i-1, j-1)
            #         if self.minesweeper.matrix[i - 1][j] == ' ':
            #             self.auto_blank_fill(i-1, j)
            #         if self.minesweeper.matrix[i - 1][j + 1] == ' ':
            #             self.auto_blank_fill(i-1, j+1)
            #         if self.minesweeper.matrix[i][j + 1] == ' ':
            #             self.auto_blank_fill(i, j+1)
            # else:
            #     if j == 0:
            #         if self.minesweeper.matrix[i - 1][j] == ' ':
            #             self.auto_blank_fill(i-1, j)
            #         if self.minesweeper.matrix[i - 1][j + 1] == ' ':
            #             self.auto_blank_fill(i-1, j+1)
            #         if self.minesweeper.matrix[i][j + 1] == ' ':
            #             self.auto_blank_fill(i, j+1)
            #         if self.minesweeper.matrix[i + 1][j + 1] == ' ':
            #             self.auto_blank_fill(i+1, j+1)
            #         if self.minesweeper.matrix[i + 1][j] == ' ':
            #             self.auto_blank_fill(i+1, j)
            #     elif j == self.minesweeper.size - 1:
            #         if self.minesweeper.matrix[i - 1][j] == ' ':
            #             self.auto_blank_fill(i-1, j)
            #         if self.minesweeper.matrix[i - 1][j - 1] == ' ':
            #             self.auto_blank_fill(i-1, j-1)
            #         if self.minesweeper.matrix[i][j - 1] == ' ':
            #             self.auto_blank_fill(i, j-1)
            #         if self.minesweeper.matrix[i + 1][j - 1] == ' ':
            #             self.auto_blank_fill(i+1, j-1)
            #         if self.minesweeper.matrix[i + 1][j] == ' ':
            #             self.auto_blank_fill(i+1, j)
            #
            #     else:
            #         if self.minesweeper.matrix[i - 1][j - 1] == ' ':
            #             self.auto_blank_fill(i-1, j-1)
            #         if self.minesweeper.matrix[i - 1][j] == ' ':
            #             self.auto_blank_fill(i-1, j)
            #         if self.minesweeper.matrix[i - 1][j + 1] == ' ':
            #             self.auto_blank_fill(i-1, j+1)
            #         if self.minesweeper.matrix[i][j + 1] == ' ':
            #             self.auto_blank_fill(i, j+1)
            #         if self.minesweeper.matrix[i + 1][j + 1] == ' ':
            #             self.auto_blank_fill(i+1, j+1)
            #         if self.minesweeper.matrix[i + 1][j] == ' ':
            #             self.auto_blank_fill(i+1, j)
            #         if self.minesweeper.matrix[i + 1][j - 1] == ' ':
            #             self.auto_blank_fill(i+1, j-1)
            #         if self.minesweeper.matrix[i][j - 1] == ' ':
            #             self.auto_blank_fill(i, j-1)

    def scoring(self):
        # reset to initial state
        self.score = 0
        self.no_of_boxes_left = self.matrix_size ** 2 - self.mines_count

        for i in range(self.minesweeper.size):
            for j in range(self.minesweeper.size):
                if 0 < self.minesweeper.list[i][j]:
                    self.no_of_boxes_left -= 1
                if self.minesweeper.list[i][j] != 10:
                    self.score += self.minesweeper.list[i][j]

        self.button(120, 40, 620, 50, "Boxes Left :", 18, font_paddingx=10)
        self.button(120, 100, 620, 100, str(self.no_of_boxes_left), 32, font_paddingx=40, font_paddingy=20)
        self.button(120, 100, 620, 250, "Score :", 18, font_paddingx=10)
        self.button(120, 100, 620, 300, str(self.score), 32, font_paddingx=40, font_paddingy=20)

    def game_over(self):
        self.background.fill((0, 200, 200))
        self.window.blit(self.background,(0, 0))
        running = True
        x, y = 0, 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

            self.button(250, 80, 240, 140, "GAME OVER", 32,font_paddingx=30,font_paddingy=20)
            self.button(150, 50, 180, 380, "PLAY AGAIN", 24)
            self.button(150, 50, 380, 380, "QUIT", 24, font_paddingx=40)

            if 380 < x < 380 + 150 and 380 < y < 380 + 50:
                self.button(150, 50, 380, 380, "QUIT", 24, font_paddingx=40, color=(10, 10, 10))
                pygame.display.update()
                pygame.time.wait(10)
                pygame.quit()
                sys.exit()

            if 180 < x < 180 + 150 and 380 < y < 380 + 50:
                self.button(150, 50, 180, 380, "PLAY AGAIN", 24,color=(10, 10, 10))

                #reset counts
                self.no_of_boxes_left = self.matrix_size ** 2 - self.mines_count
                self.score = 0
                for i in range(self.minesweeper.size):
                    for j in range(self.minesweeper.size):
                        self.minesweeper.list[i][j] = 0
                pygame.display.update()
                pygame.time.wait(10)
                self.gameloop()
            pygame.display.update()

    def you_win(self):
        self.background.fill((0, 200, 200))
        self.window.blit(self.background,(0, 0))
        running = True
        x, y = 0, 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

            self.button(250, 80, 240, 140, "YOU WIN!!!", 32, font_paddingx=40, font_paddingy=20)
            self.button(150, 50, 180, 380, "PLAY AGAIN", 24)
            self.button(150, 50, 380, 380, "QUIT", 24, font_paddingx=40)
            if 380 < x < 380 + 150 and 380 < y < 380 + 50:

                # For button animation
                self.button(150, 50, 380, 380, "QUIT", 24, font_paddingx=40, color=(10, 10, 10))
                pygame.display.update()
                pygame.time.wait(10)

                pygame.quit()
                sys.exit()
            if 180 < x < 180 + 150 and 380 < y < 380 + 50:

                # For button animation
                self.button(150, 50, 180, 380, "PLAY AGAIN", 24,color=(10, 10, 10))
                pygame.display.update()
                pygame.time.wait(10)

                #reset counts
                self.minesweeper.put_mines(self.mines_count)
                self.no_of_boxes_left = self.matrix_size ** 2 - self.mines_count
                self.score = 0
                for i in range(self.minesweeper.size):
                    for j in range(self.minesweeper.size):
                        self.minesweeper.list[i][j] = 0
                self.gameloop()
            pygame.display.update()

    def button(self, size_x, size_y, x, y, text, font_size, color=(255, 255, 255), font_color=(0, 150, 0), font_paddingx=10, font_paddingy=10):
        font2 = pygame.font.SysFont("Arial", font_size, "bold")
        self.rect = pygame.draw.rect(self.window, (100, 0, 0), (x-10, y-10, size_x+20, size_y+20))
        self.rect = pygame.draw.rect(self.window, color, (x, y, size_x, size_y))
        self.window.blit(font2.render(text, True, font_color), (x + font_paddingx, y + font_paddingy))

    def start_game(self):
        start = True
        x, y = 0, 0
        while start:
            last = pygame.time.get_ticks()
            self.background.fill((0, 200, 200))
            self.window.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

            self.button(500, 100, 130, 100, "MINESWEEPER", 64, font_paddingx=25, font_paddingy=15, color=(200, 150, 100), font_color=(120, 120, 120))
            self.button(260, 80, 240, 280, "START GAME", 36, font_paddingx=25, font_paddingy=15)

            if 240 < x < 240 + 260 and 280 < y < 280 + 80:
                self.button(260, 80, 240, 280, "START GAME", 32, font_paddingx=25, font_paddingy=15, color=(0, 0, 0))
                pygame.display.update()
                pygame.time.wait(10)
                self.gameloop()
                start = False

            pygame.display.update()


if __name__ == "__main__":
    Game()
    pygame.quit()
    sys.exit()
