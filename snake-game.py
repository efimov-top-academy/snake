from tkinter import font
import pygame
import time
import random
import tkinter

colorRed = (255, 0, 0)
colorBlue = (0, 0, 255)
colorWhite = (255, 255, 255)
colorGreen = (0, 255, 0)
colorYellow = (255, 255, 0)

cellSize = 20
winWidth = 40
winHeight = 30

colorText = colorRed
colorField = colorWhite
colorSnake = colorBlue
colorSnakeHead = colorGreen
colorFood = colorYellow

pygame.init()
win = pygame.display.set_mode((winWidth * cellSize, winHeight * cellSize))
pygame.display.set_caption("Snake | Game")

clock = pygame.time.Clock()
snakeSpeed = 10

def SettingsSave():
    pass

def SettingsView():
    ws = tkinter.Tk()
    ws.geometry("400x300")
    ws.title("Game settings")

    for c in range(2): 
        ws.columnconfigure(index=c, weight=1)
    for r in range(10): 
        ws.rowconfigure(index=r, weight=1)

    lblWidth = tkinter.Label(ws, 
                             text="Width of game field",
                             font="Arial 20",
                             padx=10, pady=10)
    lblWidth.grid(row = 0, column = 0)

    txtWidth = tkinter.Entry(ws, 
                             font="Arial 20",
                             width=4)
    txtWidth.grid(row = 0, column = 1)

    btnSave = tkinter.Button(ws, 
                             text="Save",
                             font="Arial 20",
                             command=SettingsSave)
    btnSave.grid(row=5, column=0, columnspan=2)

    ws.mainloop()

def ScoreView(score):
    fontStyle = pygame.font.SysFont(None, 2 * cellSize)
    scoreRend = fontStyle.render(str(score), True, colorRed)
    win.blit(scoreRend, [10, 10])

def Message(msg, color):
    fontStyle = pygame.font.SysFont(None, 2 * cellSize)
    msgRend = fontStyle.render(msg, True, color)
    win.blit(msgRend, [(cellSize * winWidth - msgRend.get_width()) // 2, cellSize * winHeight // 2])

def SnakeView(snake):
    head = len(snake) - 1
    for s in snake:
        if snake.index(s) == head:
            pygame.draw.rect(win, colorYellow, [s[0] * cellSize, s[1] * cellSize, cellSize, cellSize])
        else:
            pygame.draw.rect(win, colorBlue, [s[0] * cellSize, s[1] * cellSize, cellSize, cellSize])

def GameLoop():
    snakeX = winWidth // 2
    snakeY = winHeight // 2
    dx = 0
    dy = 0
    foodX = random.randint(0, winWidth)
    foodY = random.randint(0, winHeight)
    isGameOver = False
    isGameQuit = False

    snake = []
    snakeLength = 1

    while not isGameOver:
        while isGameQuit:
            win.fill(colorWhite)
            Message("You lost! Press Q - Quit, Press P - Play again", colorRed)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        isGameOver = True
                        isGameQuit = False
                    elif event.key == pygame.K_p:
                        GameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -1
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = 1
                    dy = 0
                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -1
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = 1
                elif event.key == pygame.K_o:
                    SettingsView()

        if snakeX >= winWidth or snakeX < 0 or snakeY >= winHeight or snakeY < 0:
            isGameQuit = True

        snakeX += dx #snakeX = snakeX + dx
        snakeY += dy
        win.fill(colorWhite)

        snakeHead = []
        snakeHead.append(snakeX)
        snakeHead.append(snakeY)
        snake.append(snakeHead)

        if len(snake) > snakeLength:
            del snake[0]
        
        for s in snake[:-1]:
            if s == snakeHead:
                isGameQuit = True
        
        SnakeView(snake)
        ScoreView(snakeLength - 1)
        
        pygame.draw.rect(win, colorGreen, [foodX * cellSize, foodY * cellSize, cellSize, cellSize])
        pygame.display.update()
        
        if snakeX == foodX and snakeY == foodY:
            foodX = random.randint(0, winWidth - 1)
            foodY = random.randint(0, winHeight - 1)
            snakeLength += 1

        clock.tick(snakeSpeed)
    pygame.quit()
    quit()


GameLoop()