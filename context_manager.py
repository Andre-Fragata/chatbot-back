def process_input(user_input, context):
    user_input = user_input.strip().lower()

    if context['step'] == 0:  # Identificar o tipo de compressor
        if 'pistão' in user_input or 'pistao' in user_input:
            context['compressor_type'] = 'pistão'
            context['step'] = 1
            return "Você escolheu compressor a pistão. Há quantos dias foi trocado o óleo do compressor?"

        elif 'parafuso' in user_input:
            context['compressor_type'] = 'parafuso'
            context['step'] = 7
            return "Você escolheu compressor a parafuso. O seu compressor está atingindo a pressão máxima desejada sem dificuldades?"

    # ---------------- Compressor a Pistão -------------------------- #
    elif context['step'] == 1:  # Resposta óleo + Pergunta sobre troca filtro de ar
        try:
            oil_change = int(user_input)
            context['oil_change_days'] = oil_change
            context['step'] = 2
            return "Quando foi realizada a troca do filtro de ar pela última vez?"
        except ValueError:
            return "Por favor, informe a quantidade de dias em um formato numérico."

    elif context['step'] == 2:  # Resposta filtro de ar + Pergunta esgotamento de água compressor
        try:
            air_change = int(user_input)
            context['air_change_days'] = air_change
            context['step'] = 3
            return "Há quantos dias foi esgotada a água do compressor?"
        except ValueError:
            return "Por favor, informe a quantidade de dias em um formato numérico."

    elif context['step'] == 3:  # Resposta esgotamento de água compressor + Pergunta tempo de funcionamento diário
        try:
            scape_water = int(user_input)
            context['scape_water_days'] = scape_water
            context['step'] = 4
            return "Qual é o tempo de funcionamento diário do compressor?"
        except ValueError:
            return "Por favor, informe a quantidade de horas em um formato numérico."

    elif context['step'] == 4:  # Resposta tempo de funcionamento diário + Pergunta vazamento óleo
        try:
            daily_operation = int(user_input)
            context['daily_op'] = daily_operation
            context['step'] = 5
            return "Há algum vazamento de óleo no compressor? (Responda 'sim' ou 'não')"
        except ValueError:
            return "Por favor, responda com 'sim' ou 'não'."

    elif context['step'] == 5:  # Resposta vazamento óleo + Pergunta nível de ruído
        try:
            oil_escape = str(user_input.lower())
            context['oil_leak'] = oil_escape
            if oil_escape not in ['sim', 'não', 'nao']:
                raise ValueError("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
            context['step'] = 6
            return "Você percebeu algum aumento no nível de ruído do compressor? (Responda 'sim' ou 'não')"
        except ValueError:
            return "Por favor, responda com 'sim' ou 'não'."

    elif context['step'] == 6:  # Resposta ruído
        try:
            noise = str(user_input.lower())
            context['weird_noises'] = noise
            if noise not in ['sim', 'não', 'nao']:
                raise ValueError("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
            return generate_diagnosis_pistao(context)
        except ValueError:
            return "Por favor, responda com 'sim' ou 'não'."

    # ---------------- Compressor a Parafuso -------------------------- #
    elif context['step'] == 7:  # Resposta máxima capacidade + Pergunta monitoramento nível do compressor
        try:
            capacity = str(user_input.lower())
            context['max_capacity'] = capacity
            if capacity not in ['sim', 'não', 'nao']:
                raise ValueError("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
            context['step'] = 8
            return "Há um monitoramento constante no nível de óleo do compressor? (Responda 'sim' ou 'não')"
        except ValueError:
            return "Por favor, responda com 'sim' ou 'não'."

    elif context['step'] == 8:  # Resposta nivel óleo + Pergunta filtros de ar e óleo
        try:
            oil_monitor = str(user_input.lower())
            context['oil_level'] = oil_monitor
            if oil_monitor not in ['sim', 'não', 'nao']:
                raise ValueError("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
            context['step'] = 9
            return "Os filtros de ar e óleo foram trocados recentemente? (Responda 'sim' ou 'não')"
        except ValueError:
            return "Por favor, responda com 'sim' ou 'não'."

    elif context['step'] == 9:  # Resposta filtros de ar e óleo + Pergunta separador de óleo
        try:
            air_oil = str(user_input.lower())
            context['air_oil_filter'] = air_oil
            if air_oil not in ['sim', 'não', 'nao']:
                raise ValueError("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
            context['step'] = 10
            return "O separador de óleo está funcionando corretamente? (Responda 'sim' ou 'não')"
        except ValueError:
            return "Por favor, responda com 'sim' ou 'não'."

    elif context['step'] == 10:  # Resposta separador de óleo + Pergunta perf comp
        try:
            separator = str(user_input.lower())
            context['oil_separator'] = separator
            if separator not in ['sim', 'não', 'nao']:
                raise ValueError("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
            context['step'] = 11
            return "Você notou alguma queda no desempenho do compressor? (Responda 'sim' ou 'não')"
        except ValueError:
            return "Por favor, responda com 'sim' ou 'não'."

    elif context['step'] == 11:  # Resposta desempenho compressor + Pergunta vazamento de óleo
        try:
            perfomance = str(user_input.lower())
            context['comp_perf'] = perfomance
            if perfomance not in ['sim', 'não', 'nao']:
                raise ValueError("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
            context['step'] = 12
            return "Há algum vazamento de óleo no compressor? (Responda 'sim' ou 'não')"
        except ValueError:
            return "Por favor, responda com 'sim' ou 'não'."

    elif context['step'] == 12:  # Resposta vazamento de óleo + Pergunta temperatura compressor
        try:
            oil_escape = str(user_input.lower())
            context['oil_leak'] = oil_escape
            if oil_escape not in ['sim', 'não', 'nao']:
                raise ValueError("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
            context['step'] = 13
            return "A temperatura de operação do compressor parece mais alta do que o normal? (Responda 'sim' ou 'não')"
        except ValueError:
            return "Por favor, responda com 'sim' ou 'não'."

    elif context['step'] == 13:  # Resposta temperatura compressor
        try:
            temp = str(user_input.lower())
            context['comp_temp'] = temp
            if temp not in ['sim', 'não', 'nao']:
                raise ValueError("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
            return generate_diagnosis_parafuso(context)
        except ValueError:
            return "Por favor, responda com 'sim' ou 'não'."

def generate_diagnosis_pistao(context):
    diagnosis = "Relatório do Compressor a pistão:\n"

    if context['oil_change_days'] >= 30:
        diagnosis += "- O compressor precisa de troca de óleo imediatamente.\n"
    else:
        diagnosis += "- O óleo do compressor está dentro do período recomendado.\n"

    if context['air_change_days'] >= 90:
        diagnosis += "- O filtro de ar precisa ser trocado.\n"
    else:
        diagnosis += "- O filtro de ar está em dia.\n"

    if context['scape_water_days'] >= 7:
        diagnosis += "- É necessário esgotar a água do seu compressor.\n"
    else:
        diagnosis += "- A água do compressor está ok.\n"

    if context['daily_op'] >= 8:
        diagnosis += "- É necessário realizar uma manutenção preventiva por conta do tempo alto de operação do compressor.\n"
    else:
        diagnosis += "- O tempo de operação do compressor está dentro do recomendado.\n"

    if context['oil_leak'] == 'sim':
        diagnosis += "- Vazamento de óleo detectado. Verifique e repare imediatamente.\n"
    else:
        diagnosis += "- Não há vazamento de óleo detectado.\n"

    if context['weird_noises'] == 'sim':
        diagnosis += "- Ruído anormal detectado. Verifique o compressor.\n"
    else:
        diagnosis += "- O nível de ruído está normal.\n"

    diagnosis += "Obrigado por utilizar nosso sistema de diagnóstico! Entre em contato com a Arpress para obter um relatório mais detalhado ou para agendar a sua manutenção."
    return diagnosis

def generate_diagnosis_parafuso(context):
    diagnosis = "Relatório do Compressor a Parafuso:\n"

    if context['max_capacity'] == 'não' or context['max_capacity'] == 'nao':
        diagnosis += "- O compressor não está atingindo a pressão máxima. Verifique o sistema.\n"
    else:
        diagnosis += "- O compressor está atingindo a pressão máxima normalmente.\n"

    if context['oil_level'] == 'não' or context['oil_level'] == 'nao':
        diagnosis += "- Monitoramento de nível de óleo inadequado. Ajuste o monitoramento.\n"
    else:
        diagnosis += "- O monitoramento de nível de óleo está em dia.\n"

    if context['air_oil_filter'] == 'não' or context['air_oil_filter'] == 'nao':
        diagnosis += "- Troque os filtros de ar e óleo imediatamente.\n"
    else:
        diagnosis += "- Os filtros de ar e óleo estão em boas condições.\n"

    if context['oil_separator'] == 'não' or context['oil_separator'] == 'nao':
        diagnosis += "- O separador de óleo não está funcionando corretamente. Verifique-o.\n"
    else:
        diagnosis += "- O separador de óleo está funcionando normalmente.\n"

    if context['comp_perf'] == 'não' or context['comp_perf'] == 'nao':
        diagnosis += "- Desempenho do compressor abaixo do esperado. Realize a manutenção.\n"
    else:
        diagnosis += "- O desempenho do compressor está dentro do esperado.\n"

    if context['oil_leak'] == 'sim':
        diagnosis += "- Vazamento de óleo detectado. Verifique e repare imediatamente.\n"
    else:
        diagnosis += "- Não há vazamento de óleo detectado.\n"

    if context['comp_temp'] == 'sim':
        diagnosis += "- Temperatura do compressor alta. Verifique o sistema de resfriamento.\n"
    else:
        diagnosis += "- A temperatura de operação está normal.\n"

    diagnosis += "Obrigado por utilizar nosso sistema de diagnóstico! Entre em contato com a Arpress para obter um relatório mais detalhado ou para agendar a sua manutenção."
    return diagnosis

