def save():
    ve = int(input("\nDeseja ver? (1 = SIM / 2 = NÃO): "))
    if ve == 1:
        print('\n')
        ve = open('save.txt', 'r')
        txtve = ve.read()
        print(txtve)
        ve.close()

        print("Obrigado por jogar!")
        sair1 = int(input("Digite um número menor que 10 para SAIR\n"))
        if sair1 < 10:
            return 0
    if ve == 2:
        return 0


def jogatina():
    def intro():
        print('\nINTRODUÇÃO')
        arquivoi = open('intro.txt', 'r')
        texto1 = arquivoi.read()
        print(texto1)
        arquivoi.close()
    intro()

    def cena0():
        print('\n')
        arquivo0 = open('cena0.txt', 'r')
        texto2 = arquivo0.read()
        print(texto2)
        arquivo0.close()
        print('\nO que você faz?')
        op = ('1: DÁ A VOLTA E IR EMBORA', '2: VAI ATÉ A CASA DE GUARDA', '3: PROSSEGUE ATÉ AS ÁRVORES')
        print(op)

        save0 = int(input('...: '))

        if save0 == 1:
            # salvando escolha cena 0
            arquivasave0 = open('save.txt', 'a+')
            arquivasave0.write('\nESCOLHA: 1) Dá a volta e vai embora\n')
            arquivasave0.close()

            print('\n')
            print('OK, ficou claro que você se importa com seu filho. Melhor mãe... ಠ_ಠ\nFlw vlw')
            print('FIM DO JOGO')
            print('Sua trajetótia durante o jogo foi salva na pasta do jogo')

            save()

        if save0 == 2:
            # salvando escolha cena 0
            arquivasave3 = open('save.txt', 'a+')
            arquivasave3.write('\nESCOLHA: 2) Vai até a cada de guarda\n')
            arquivasave3.close()

            def cena1():
                print('\n')
                arquivo1 = open('cena1.txt', 'r')
                texto3 = arquivo1.read()
                print(texto3)
                arquivo1.close()

                print('\nO que você faz?')
                op1 = ('1: CONTINUA ANDANDO EM DIREÇÃO AO CHEIRO', '2: VAI ATÉ AO BALANÇO')
                print(op1)

                save1 = int(input('...: '))

                if save1 == 1:
                    # salvando escolha cena 1
                    arquivasave1 = open('save.txt', 'a+')
                    arquivasave1.write('\nESCOLHA FINAL: 1) Continua andando em direção ao cheiro\n'+'FINAL RUIM')
                    arquivasave1.close()

                    def finalc():
                        print('\n')
                        arquivoc = open('finalC.txt', 'r' )
                        texto4 = arquivoc.read()
                        print(texto4)
                        arquivoc.close()
                        print('FIM DO JOGO')
                        print('Sua trajetótia durante o jogo foi salva na pasta do jogo')

                        save()
                    finalc()

                if save1 == 2:
                    # salvando escolha cena 1
                    arquivasave2 = open('save.txt', 'a+')
                    arquivasave2.write('\nESCOLHA FINAL: 2) Vai até ao balanço\n' + 'FINAL BOM')
                    arquivasave2.close()

                    def finald():
                        print('\n')
                        arquivod = open('finalD.txt', 'r')
                        texto5 = arquivod.read()
                        print(texto5)
                        arquivod.close()
                        print('FIM DO JOGO')
                        print('Sua trajetótia durante o jogo foi salva na pasta do jogo')

                        save()
                    finald()
            cena1()

        if save0 == 3:
            # salvando escolha cena 0
            arquivasave4 = open('save.txt', 'a+')
            arquivasave4.write('PRIMEIRA ESCOLHA: 3) PROSSEGUE ATÉ AS ÁRVORES\n')
            arquivasave4.close()

            def cena2():
                print('\n')
                arquivo2 = open('cena2.txt', 'r')
                texto6 = arquivo2.read()
                print(texto6)
                arquivo2.close()

                print('\nO que você faz?')
                op2 = ('1: SEGUE O CHEIRO QUE ESTÁ INSUPORTÁVEL', '2: PEGA O CELULAR PRIMEIRO ANTES DE IR')
                print(op2)

                save2 = int(input('...: '))

                if save2 == 1:
                    # salvando escolha cena 2
                    arquivasave5 = open('save.txt', 'a+')
                    arquivasave5.write('ESCOLHA FINAL: 1) Segue o cheiro que está insuportável\n'+'FINAL RUIM')
                    arquivasave5.close()

                    def finala():
                        print('\n')
                        arquivoa = open('finalA.txt', 'r')
                        textoa = arquivoa.read()
                        print(textoa)
                        arquivoa.close()
                        print('FIM DO JOGO')
                        print('Sua trajetótia durante o jogo foi salva na pasta do jogo')

                        save()
                    finala()

                if save2 == 2:
                    # salvando escolha cena 2
                    arquivasave6 = open('save.txt', 'a+')
                    arquivasave6.write('ESCOLHA FINAL: 2) Pega o celular primeiro antes de ir\n'+'FINAL BOM')
                    arquivasave6.close()

                    def finalb():
                        print('\n')
                        arquivob = open('finalB.txt', 'r')
                        textob = arquivob.read()
                        print(textob)
                        arquivob.close()
                        print('FIM DO JOGO')
                        print('Sua trajetótia durante o jogo foi salva na pasta do jogo')

                        save()
                    finalb()
            cena2()
    cena0()


def jogador():
    nome = input('INFORME NOME...: ')
    idade = input('INFORME IDADE...: ')
    arqsave = open('save.txt', 'a+')
    arqsave.write(nome)
    arqsave.write('\n')
    arqsave.write(idade)
    arqsave.write('\n')
    arqsave.close()


def menu():
    print('MENU')
    menu1 = ('1 - INICIAR', '2 - INTRUÇÕES', '3 - SAIR')
    print(menu1)
    op1 = input('ESCOLHA UMA OPÇÃO: ')

    if op1 == '1':
        jogador()
        jogatina()

    if op1 == '2':
        print('BLACKWOOD é um jogo simples baseado em texto.\n ')
        print('COMO JOGAR:\n')

        arquivoj = open('como-jogar.txt', 'r')
        textoj = arquivoj.read()
        print(textoj)
        arquivoj.close()

        def voltar():
            op = int(input('\nDESEJA VOLTAR AO MENU? (1 = SIM / 2 = NÃO): '))

            if op == 1:
                menu()

            if op == 2:
                return 0
        voltar()

    if op1 == '3':
        return 0


def main():
    print("  __   _        __       __                         __      __      __")
    print("||__\  ||     ||__||   ||     ||_/   ||      ||   ||  ||  ||  ||  ||  \ ")
    print("||__/  ||__   ||  ||   ||__   || \   ||_/--\_||   ||__||  ||__||  ||__/ ")

    print('\nBLACKWOOD\n by larissa_georgina\n')
    menu()
main()
