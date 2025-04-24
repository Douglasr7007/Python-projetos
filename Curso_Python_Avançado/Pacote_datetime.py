import datetime as dt

# Obtém a data e hora atual (completo, incluindo hora, minuto e segundo)

dia_hoje = dt.datetime.today()
print(dia_hoje)

# Verifica o tipo do objeto 'dia_hoje', que é um datetime completo

print(type(dia_hoje))

# Obtém apenas a data atual (sem hora)

dia_atual = dt.datetime.today().date()
print(dia_atual)

# Extrai o ano, mês e dia da data atual

ano = dia_atual.year
mes = dia_atual.month
dia = dia_atual.day
print(dia,mes,ano)


# Obtém a data e hora atual (completo) novamente, mas agora com o método 'now

dia_atual = dt.datetime.now()

# Extrai as horas, minutos e segundos da data e hora atual

horas = dia_atual.hour
minutos = dia_atual.minute
secundos = dia_atual.second
print(horas,minutos,secundos)


# Define uma data específica (20 de abril de 2024)

data_antiga = dt.date(2024,4,20)
print(data_antiga)

# Calcula a diferença entre a data atual e a data antiga

dias_restantes = dia_hoje.date() - data_antiga
print(dias_restantes)

# Verifica o tipo da variável 'dias_restantes', que é uma diferença entre datas (timedelta)

print(type(dias_restantes))

# Adiciona 30 dias à diferença de dias (dias_restantes) e imprime a nova data

print(dias_restantes + dt.timedelta(days=30))
