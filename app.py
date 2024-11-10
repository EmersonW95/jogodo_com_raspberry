from time import sleep
import RPi.GPIO as GPIO
from random import randint

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_PIN1 = 14
led_PIN2 = 15
led_PIN3 = 18
led_PIN4 = 4
led_PIN5 = 5
led_PIN6 = 1
led_PIN7 = 3
led_PIN8 = 6

GPIO.setup(led_PIN1, GPIO.OUT)
GPIO.setup(led_PIN2, GPIO.OUT)
GPIO.setup(led_PIN3, GPIO.OUT)
GPIO.setup(led_PIN4, GPIO.OUT)
GPIO.setup(led_PIN5, GPIO.OUT)
GPIO.setup(led_PIN6, GPIO.OUT)
GPIO.setup(led_PIN7, GPIO.OUT)
GPIO.setup(led_PIN8, GPIO.OUT)

numero_pin1 = randint(1,8)
numero_pin2 = randint(1,8)
numero_pin3 = randint(1,8)
numero_pin4 = randint(1,8)
numero_pin5 = randint(1,8)
numero_pin6 = randint(1,8)
numero_pin7 = randint(1,8)
numero_pin8 = randint(1,8)
dente_errado = randint(1,8)

botao_pin1 = 21
botao_pin2 = 22
botao_pin3 = 23
botao_pin4 = 24
botao_pin5 = 25
botao_pin6 = 26
botao_pin7 = 27
botao_pin8 = 28

GPIO.setup(botao_pin1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(botao_pin2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(botao_pin3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(botao_pin4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(botao_pin5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(botao_pin6, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(botao_pin7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(botao_pin8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

numero_botao_pin1 = 1
numero_botao_pin2 = 2
numero_botao_pin3 = 3
numero_botao_pin4 = 4
numero_botao_pin5 = 5
numero_botao_pin6 = 6
numero_botao_pin7 = 7
numero_botao_pin8 = 8

while numero_pin1 == numero_pin2 or numero_pin1 == numero_pin3 or numero_pin1 == numero_pin4 or numero_pin1 == numero_pin5 or numero_pin1 == numero_pin6 or numero_pin1 == numero_pin7 or numero_pin1 == numero_pin8:
    numero_pin1 = randint(1,8)

while numero_pin2 == numero_pin1 or numero_pin2 == numero_pin3 or numero_pin2 == numero_pin4 or numero_pin2 == numero_pin5 or numero_pin2 == numero_pin6 or numero_pin2 == numero_pin7 or numero_pin2 == numero_pin8:
    numero_pin2 = randint(1,8)

while numero_pin3 == numero_pin1 or numero_pin3 == numero_pin2 or numero_pin3 == numero_pin4 or numero_pin3 == numero_pin5 or numero_pin3 == numero_pin6 or numero_pin3 == numero_pin7 or numero_pin3 == numero_pin8:
    numero_pin3 = randint(1,8)

while numero_pin4 == numero_pin1 or numero_pin4 == numero_pin2 or numero_pin4 == numero_pin3 or numero_pin4 == numero_pin5 or numero_pin4 == numero_pin6 or numero_pin4 == numero_pin7 or numero_pin4 == numero_pin8:
    numero_pin4 = randint(1,8)

while numero_pin5 == numero_pin1 or numero_pin5 == numero_pin2 or numero_pin5 == numero_pin3 or numero_pin5 == numero_pin4 or numero_pin5 == numero_pin6 or numero_pin5 == numero_pin7 or numero_pin5 == numero_pin8:
    numero_pin5 = randint(1,8)

while numero_pin6 == numero_pin1 or numero_pin6 == numero_pin2 or numero_pin6 == numero_pin3 or numero_pin6 == numero_pin4 or numero_pin6 == numero_pin5 or numero_pin6 == numero_pin7 or numero_pin6 == numero_pin8:
    numero_pin6 = randint(1,8)

while numero_pin7 == numero_pin1 or numero_pin7 == numero_pin2 or numero_pin7 == numero_pin3 or numero_pin7 == numero_pin4 or numero_pin7 == numero_pin5 or numero_pin7 == numero_pin6 or numero_pin7 == numero_pin8:
    numero_pin7 = randint(1,8)

while numero_pin8 == numero_pin1 or numero_pin8 == numero_pin2 or numero_pin8 == numero_pin3 or numero_pin8 == numero_pin4 or numero_pin8 == numero_pin5 or numero_pin8 == numero_pin6 or numero_pin8 == numero_pin7:
    numero_pin8 = randint(1,8)

print('CARREGANDO', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
botao = input('CLIQUE (ENTER) PARA COMEÇAR:').strip()
sleep(0.5)

if botao == '':

    print('-'*28)
    print('BEM-VINDO AO JOGO DO JACARÉ')
    print('-'*28)
    print('''REGRAS:
    DIGITE NÚMEROS ENTRE 1 E 8
    VOCÊ TEM 7 TENTATIVAS
    SE O DENTE ESCOLHIDO FOR O ERRADO VOCÊ PERDE\n''')

    tentativas = 0
    acertos = 0

    while tentativas <= 7:

        GPIO.output(led_PIN1, GPIO.LOW)
        GPIO.output(led_PIN2, GPIO.LOW)
        GPIO.output(led_PIN3, GPIO.LOW)
        GPIO.output(led_PIN4, GPIO.LOW)
        GPIO.output(led_PIN5, GPIO.LOW)
        GPIO.output(led_PIN6, GPIO.LOW)
        GPIO.output(led_PIN7, GPIO.LOW)
        GPIO.output(led_PIN8, GPIO.LOW)

        if GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1    

        if GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin3:
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1
        
        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if acertos == 7:
            print('-'*36)
            print('PARABÉNS VOCÊ GANHOU')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.10)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.20)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.40)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.80)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.160)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.320)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.640)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.10)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.20)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.40)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.80)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.160)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.320)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.640)
            break

    if acertos < 7:
        print('FIM DE JOGO')
        GPIO.output(led_PIN1, GPIO.HIGH)
        GPIO.output(led_PIN2, GPIO.HIGH)
        GPIO.output(led_PIN3, GPIO.HIGH)
        GPIO.output(led_PIN4, GPIO.HIGH)
        GPIO.output(led_PIN5, GPIO.HIGH)
        GPIO.output(led_PIN6, GPIO.HIGH)
        GPIO.output(led_PIN7, GPIO.HIGH)
        GPIO.output(led_PIN8, GPIO.HIGH)

else:
    print('OPS...ALGO DEU ERRADO!')

while True:
    
    nova_tentativa = int(input('''NOVA CHANCE
    (1) SIM
    (2) NÃO
    DIGITE AQUI:'''))

    if nova_tentativa == 2:
        print('SAINDO', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('SAIU')
        break

    elif 2 != nova_tentativa != 1:
        print('OPS... ALGO DEU ERRADO')
        continue

    elif nova_tentativa == 1:

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        led_PIN1 = 14
        led_PIN2 = 15
        led_PIN3 = 18
        led_PIN4 = 4
        led_PIN5 = 5
        led_PIN6 = 1
        led_PIN7 = 3
        led_PIN8 = 6

        GPIO.setup(led_PIN1, GPIO.OUT)
        GPIO.setup(led_PIN2, GPIO.OUT)
        GPIO.setup(led_PIN3, GPIO.OUT)
        GPIO.setup(led_PIN4, GPIO.OUT)
        GPIO.setup(led_PIN5, GPIO.OUT)
        GPIO.setup(led_PIN6, GPIO.OUT)
        GPIO.setup(led_PIN7, GPIO.OUT)
        GPIO.setup(led_PIN8, GPIO.OUT)

        numero_pin1 = randint(1,8)
        numero_pin2 = randint(1,8)
        numero_pin3 = randint(1,8)
        numero_pin4 = randint(1,8)
        numero_pin5 = randint(1,8)
        numero_pin6 = randint(1,8)
        numero_pin7 = randint(1,8)
        numero_pin8 = randint(1,8)
        dente_errado = randint(1,8)

        botao_pin1 = 21
        botao_pin2 = 22
        botao_pin3 = 23
        botao_pin4 = 24
        botao_pin5 = 25
        botao_pin6 = 26
        botao_pin7 = 27
        botao_pin8 = 28

        GPIO.setup(botao_pin1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(botao_pin2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(botao_pin3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(botao_pin4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(botao_pin5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(botao_pin6, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(botao_pin7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(botao_pin8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        numero_botao_pin1 = 1
        numero_botao_pin2 = 2
        numero_botao_pin3 = 3
        numero_botao_pin4 = 4
        numero_botao_pin5 = 5
        numero_botao_pin6 = 6
        numero_botao_pin7 = 7
        numero_botao_pin8 = 8

        while numero_pin1 == numero_pin2 or numero_pin1 == numero_pin3 or numero_pin1 == numero_pin4 or numero_pin1 == numero_pin5 or numero_pin1 == numero_pin6 or numero_pin1 == numero_pin7 or numero_pin1 == numero_pin8:
            numero_pin1 = randint(1,8)

        while numero_pin2 == numero_pin1 or numero_pin2 == numero_pin3 or numero_pin2 == numero_pin4 or numero_pin2 == numero_pin5 or numero_pin2 == numero_pin6 or numero_pin2 == numero_pin7 or numero_pin2 == numero_pin8:
            numero_pin2 = randint(1,8)

        while numero_pin3 == numero_pin1 or numero_pin3 == numero_pin2 or numero_pin3 == numero_pin4 or numero_pin3 == numero_pin5 or numero_pin3 == numero_pin6 or numero_pin3 == numero_pin7 or numero_pin3 == numero_pin8:
            numero_pin3 = randint(1,8)

        while numero_pin4 == numero_pin1 or numero_pin4 == numero_pin2 or numero_pin4 == numero_pin3 or numero_pin4 == numero_pin5 or numero_pin4 == numero_pin6 or numero_pin4 == numero_pin7 or numero_pin4 == numero_pin8:
            numero_pin4 = randint(1,8)

        while numero_pin5 == numero_pin1 or numero_pin5 == numero_pin2 or numero_pin5 == numero_pin3 or numero_pin5 == numero_pin4 or numero_pin5 == numero_pin6 or numero_pin5 == numero_pin7 or numero_pin5 == numero_pin8:
            numero_pin5 = randint(1,8)

        while numero_pin6 == numero_pin1 or numero_pin6 == numero_pin2 or numero_pin6 == numero_pin3 or numero_pin6 == numero_pin4 or numero_pin6 == numero_pin5 or numero_pin6 == numero_pin7 or numero_pin6 == numero_pin8:
            numero_pin6 = randint(1,8)

        while numero_pin7 == numero_pin1 or numero_pin7 == numero_pin2 or numero_pin7 == numero_pin3 or numero_pin7 == numero_pin4 or numero_pin7 == numero_pin5 or numero_pin7 == numero_pin6 or numero_pin7 == numero_pin8:
            numero_pin7 = randint(1,8)

        while numero_pin8 == numero_pin1 or numero_pin8 == numero_pin2 or numero_pin8 == numero_pin3 or numero_pin8 == numero_pin4 or numero_pin8 == numero_pin5 or numero_pin8 == numero_pin6 or numero_pin8 == numero_pin7:
            numero_pin8 = randint(1,8)


        print('CARREGANDO', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
        botao = input('CLIQUE (ENTER) PARA COMEÇAR:').strip()
        sleep(0.5)

    if botao == '':

        print('-'*28)
        print('BEM-VINDO AO JOGO DO JACARÉ')
        print('-'*28)
        print('''REGRAS:
        VOCÊ TEM 7 TENTATIVAS
        SE O DENTE ESCOLHIDO FOR O ERRADO VOCÊ PERDE\n''')

    tentativas = 0
    acertos = 0

    while tentativas <= 7:

        GPIO.output(led_PIN1, GPIO.LOW)
        GPIO.output(led_PIN2, GPIO.LOW)
        GPIO.output(led_PIN3, GPIO.LOW)
        GPIO.output(led_PIN4, GPIO.LOW)
        GPIO.output(led_PIN5, GPIO.LOW)
        GPIO.output(led_PIN6, GPIO.LOW)
        GPIO.output(led_PIN7, GPIO.LOW)
        GPIO.output(led_PIN8, GPIO.LOW)

        if GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin1) == GPIO.HIGH and numero_botao_pin1 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1    

        if GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break
        
        if GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin3:
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin2) == GPIO.HIGH and numero_botao_pin2 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin3) == GPIO.HIGH and numero_botao_pin3 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin4) == GPIO.HIGH and numero_botao_pin4 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin5) == GPIO.HIGH and numero_botao_pin5 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin6) == GPIO.HIGH and numero_botao_pin6 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin7) == GPIO.HIGH and numero_botao_pin7 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == dente_errado:
            print('VOCÊ ERROU')
            print('VOCÊ PERDEU')
            tentativas += 1
            acertos -=1
            break

        if GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin1:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin2:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin3:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin4:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin5:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin6:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin7:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        elif GPIO.input(botao_pin8) == GPIO.HIGH and numero_botao_pin8 == numero_pin8:
            print('PARABÉNS VOCÊ ACERTOU UM DENTE')
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            
            tentativas += 1
            acertos += 1

        if acertos == 7:
            print('PARABÉNS VOCÊ GANHOU')
            GPIO.output(led_PIN1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_PIN2, GPIO.HIGH)
            sleep(0.10)
            GPIO.output(led_PIN3, GPIO.HIGH)
            sleep(0.20)
            GPIO.output(led_PIN4, GPIO.HIGH)
            sleep(0.40)
            GPIO.output(led_PIN5, GPIO.HIGH)
            sleep(0.80)
            GPIO.output(led_PIN6, GPIO.HIGH)
            sleep(0.160)
            GPIO.output(led_PIN7, GPIO.HIGH)
            sleep(0.320)
            GPIO.output(led_PIN8, GPIO.HIGH)
            sleep(0.640)
            GPIO.output(led_PIN8, GPIO.LOW)
            sleep(0.5)
            GPIO.output(led_PIN7, GPIO.LOW)
            sleep(0.10)
            GPIO.output(led_PIN6, GPIO.LOW)
            sleep(0.20)
            GPIO.output(led_PIN5, GPIO.LOW)
            sleep(0.40)
            GPIO.output(led_PIN4, GPIO.LOW)
            sleep(0.80)
            GPIO.output(led_PIN3, GPIO.LOW)
            sleep(0.160)
            GPIO.output(led_PIN2, GPIO.LOW)
            sleep(0.320)
            GPIO.output(led_PIN1, GPIO.LOW)
            sleep(0.640)
            break

    if acertos < 7:
        print('FIM DE JOGO')
        GPIO.output(led_PIN1, GPIO.HIGH)
        GPIO.output(led_PIN2, GPIO.HIGH)
        GPIO.output(led_PIN3, GPIO.HIGH)
        GPIO.output(led_PIN4, GPIO.HIGH)
        GPIO.output(led_PIN5, GPIO.HIGH)
        GPIO.output(led_PIN6, GPIO.HIGH)
        GPIO.output(led_PIN7, GPIO.HIGH)
        GPIO.output(led_PIN8, GPIO.HIGH)

GPIO.cleanup()