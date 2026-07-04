import random, time, emoji

jokenpo = {'pedra': emoji.emojize(':punho_levantado:', language = 'pt' ) ,
         'papel': emoji.emojize(':mão_aberta_com_os_dedos_separados:', language = 'pt' ),
         'tesoura': emoji.emojize(':mão_em_v_de_vitória:', language = 'pt' ) }


print('=' * 60)
print('Vamos jogar jokenpô?')
print('=' * 60)

escolha = input('Escolha pedra, papel ou tesoura!!!\n').lower().strip()
computador = random.choice(['pedra', 'papel', 'tesoura'])

if escolha in ['pedra', 'papel', 'tesoura']:
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!!')
    time.sleep(1)

    match escolha:
        case 'pedra':
            if computador == 'pedra':
                print(f'Eu joguei {jokenpo['pedra']} e você jogou {jokenpo['pedra']}! Deu empate!!!')
            elif computador == 'papel':
                print(f'Eu joguei {jokenpo['papel']} e você jogou {jokenpo['pedra']}! EU VENCI!!!')
            else:
                print(f'Eu joguei {jokenpo['tesoura']} e você jogou {jokenpo['pedra']}! VOCÊ VENCEU!!!')

        case 'papel':
            if computador == 'pedra':
                print(f'Eu joguei {jokenpo['pedra']} e você jogou {jokenpo['papel']}! VOCÊ VENCEU!!!')
            elif computador == 'papel':
                print(f'Eu joguei {jokenpo['papel']} e você jogou {jokenpo['papel']}! DEU EMPATE!!!')
            else:
                print(f'Eu joguei {jokenpo['tesoura']} e você jogou {jokenpo['papel']}! EU VENCI!!!')

        case 'tesoura':
            if computador == 'pedra':
                print(f'Eu joguei {jokenpo['pedra']} e você jogou {jokenpo['tesoura']}! EU VENCI!!!')
            elif computador == 'papel':
                print(f'Eu joguei {jokenpo['papel']} e você jogou {jokenpo['tesoura']}! VOCÊ VENCEU!!!')
            else:
                print(f'Eu joguei {jokenpo['tesoura']} e você jogou {jokenpo['tesoura']}! DEU EMPATE!!!')

else:
    print('Opção invalida! Digite pedra, papel ou tesoura!!!')


