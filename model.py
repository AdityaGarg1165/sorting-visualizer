import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame")


def gen_list(max_val,min_value):
    return [random.randint(min_value, max_val) for _ in range(80)]
font = pygame.font.Font("font.ttf", 30)
text = font.render("Python Sorting Visualizer", True, (0, 255, 0))
text2 = font.render("Press spacebar to continue", True, (0, 255, 0))
text3 = font.render(" I-insertion sort and B - bubble sort", True, (0, 255, 0))
text4 = font.render(" Press R to reset", True, (0, 255, 0))

def generate_rects(window,random_list,start,iteration_key,completed):
    if start:
        pygame.draw.rect(window, (0,0,0), (0, 0, 800, 600))
        screen.blit(text, (400 - text.get_width() // 2, 30))
        pass
    rect_width = 7
    if iteration_key == -1:
        for i,height in enumerate(random_list):
            pygame.draw.rect(window, (0,255,0), (i* 10, 600 - height, rect_width, height))
    else:
        for i,height in enumerate(random_list):
            if i == iteration_key or i == iteration_key + 1:
                pygame.draw.rect(window, (255,255,255), (i* 10, 600 - height, rect_width, height))
                
            else:
                pygame.draw.rect(window, (0,255,0), (i* 10, 600 - height, rect_width, height))
        pygame.time.delay(3)

    
    if start:
        pygame.display.update()
    
    if completed:
        for i,height in enumerate(random_list):
            pygame.draw.rect(window, (255,255,255), (i* 10, 600 - height, rect_width, height))
        pygame.display.update()






def bubble_sort(arr,sorting):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                generate_rects(screen,arr,True,arr.index(arr[i]),False)

    generate_rects(screen,arr,True,arr.index(arr[i]),True)

def insertion_sort(arr,sorting):
    for i in range(1,len(arr)):
        current = arr[i]
        while True:
            random_var = i > 0 and arr[i - 1] > current
            if not random_var:
                break
            arr[i] = arr[i-1]
            i= i-1
            arr[i] = current
            generate_rects(screen,arr,True,arr.index(arr[i]),False)

    generate_rects(screen,arr,True,arr.index(arr[i]),True)




def start(algo_name):
    if algo_name == "insertion_sort":
        insertion_sort(generated_list,sorting)
    else:
        bubble_sort(generated_list,sorting)

    # bubble_sort(generated_list,sorting)

sorting = True
running = True
generated_list = gen_list(400,0)
generate_rects(screen,generated_list,False,-1,False)
pygame.display.update()
algo_name = "bubble_sort"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                # print("Space pressed")
                start(algo_name)
            elif pygame.key.get_pressed()[pygame.K_i]:
                algo_name = "insertion_sort"
            elif pygame.key.get_pressed()[pygame.K_b]:
                algo_name = "bubble_sort"
            elif pygame.key.get_pressed()[pygame.K_r]:
                generated_list = gen_list(400,0)
                pygame.draw.rect(screen, (0,0,0), (0, 0, 800, 600))
                generate_rects(screen,generated_list,False,-1,False)

    screen.blit(text, (400 - text.get_width() // 2, 30))
    screen.blit(text2, (400 - text2.get_width() // 2, 60))
    screen.blit(text3, (50, 90))
    screen.blit(text3, (50, 90))
    screen.blit(text4, (250, 120))
    pygame.display.update()
pygame.quit()
