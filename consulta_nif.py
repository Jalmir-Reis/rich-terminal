from rich import print
from rich.prompt import Prompt
from rich.progress import track
from rich.console import Console
from time import sleep
from rich.table import Table

console = Console()
prompt = Prompt()
continuar = True

while continuar == True:
    nif = int(prompt.ask('[green]digite seu [bold]NIF[/]: [/]'))
    resposta = prompt.ask(
        f'Você digitou [red]{nif}[/], este número está correto?')
    if resposta.lower() in ('s', 'sim'):
        print('ótimo')
        continuar = False
    elif resposta.lower() in ('n', 'não'):
        print('reiniciando...')
    else:
        print('Digite apenas [red]"s"[/] ou [red]"n"[/]')


def consultar_nif():
    console.log('NIF sem bloqueios')
    sleep(2)
    console.log('Sem multas em financiamentos')
    sleep(2)
    console.log('Nome não encontrado em divídas nas finanças')
    sleep(2)
    console.log('dados validados com sucesso')


with console.status('[green]Preenchendo formulário[/]') as status:
    consultar_nif()

print('[green]Seu NIF está pronto para um financiamento![/]')

table = Table(title='Financiamentos Disponíveis')
table.add_column("Meses")
table.add_column("Valor")
table.add_column("Taxa de juros")

table.add_row('12x', '€1750,00', '7.5%')
table.add_row('36x', '€560,00', '12.0%')
table.add_row('72x', '€360,00', '15.5%')

print(table)

tipo_financiamento = prompt.ask('Qual financiamento deseja contratar?',
                                choices=['12', '36', '72'])

nome = input('Digite seu nome para finalizar: ')

print(
    f'[on blue][black]Parabéns [white]{nome}[/], você escolheu o financiamento de [green]{tipo_financiamento} meses.[/][/][/]')
