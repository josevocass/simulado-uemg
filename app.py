import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Simulado Oficial UEMG (48 Questões + Redação)", page_icon="📝", layout="centered")

# --- BANCO COMPLETO DE QUESTÕES (48 QUESTÕES - PADRÃO UEMG) ---
BANCO_QUESTOES = [
    # Português e Literatura (Q01 a Q10)
    {
        "id": "Q01", "materia": "Português",
        "enunciado": "Assinale a alternativa em que a regência do verbo 'aspirar' está correta segundo a norma-padrão:",
        "opcoes": [
            "O jovem aspirava o cargo de diretor.",
            "Aspiramos o perfume das flores no jardim.",
            "Ele aspira em passar no vestibular.",
            "O médico aspirou o paciente com cuidado."
        ],
        "gabarito": "Aspiramos o perfume das flores no jardim."
    },
    {
        "id": "Q02", "materia": "Português",
        "enunciado": "Identifique a opção em que a crase foi empregada incorretamente:",
        "opcoes": [
            "Fomos à festa de formatura.",
            "Ele entregou o documento à diretora.",
            "Começou a chover às duas horas.",
            "Prefiro passear a ficar em casa."
        ],
        "gabarito": "Prefiro passear a ficar em casa."
    },
    {
        "id": "Q03", "materia": "Literatura",
        "enunciado": "O Romantismo no Brasil teve fases distintas. Qual característica marca predominantemente a chamada 'Segunda Geração Romântica' (Mal do Século)?",
        "opcoes": [
            "Nacionalismo ufanista e exaltação do índio.",
            "Pessimismo profundo, tédio, angústia e culto à morte.",
            "Crítica social e combate à escravidão.",
            "Objetividade científica e parnasianismo."
        ],
        "gabarito": "Pessimismo profundo, tédio, angústia e culto à morte."
    },
    {
        "id": "Q04", "materia": "Português",
        "enunciado": "Na frase 'O livro que comprei é excelente', a palavra 'que' classifica-se morfologicamente como:",
        "opcoes": [
            "Conjunção integrante",
            "Pronome relativo",
            "Conjunção subordinativa causal",
            "Partícula expletiva"
        ],
        "gabarito": "Pronome relativo"
    },
    {
        "id": "Q05", "materia": "Literatura",
        "enunciado": "Autor mineiro de grande destaque, criador de obras como 'Grande Sertão: Veredas', que revolucionou a linguagem literária brasileira:",
        "opcoes": [
            "Machado de Assis",
            "Carlos Drummond de Andrade",
            "João Guimarães Rosa",
            "Lima Barreto"
        ],
        "gabarito": "João Guimarães Rosa"
    },
    {
        "id": "Q06", "materia": "Português",
        "enunciado": "Assinale a alternativa em que a concordância verbal está inteiramente de acordo com a norma-padrão:",
        "opcoes": [
            "Faltou coragem e determinação aos candidatos.",
            "Haviam muitos alunos na sala de aula.",
            "Devo fazer cerca de dois anos que não o vejo.",
            "Mais de um aluno faltaram à prova."
        ],
        "gabarito": "Faltou coragem e determinação aos candidatos."
    },
    {
        "id": "Q07", "materia": "Português",
        "enunciado": "A função da linguagem focada no próprio código utilizada na mensagem é denominada:",
        "opcoes": ["Emotiva", "Fática", "Metalinguística", "Conativa"],
        "gabarito": "Metalinguística"
    },
    {
        "id": "Q08", "materia": "Literatura",
        "enunciado": "O Modernismo em Minas Gerais teve forte expressão na segunda fase com a poesia de Carlos Drummond de Andrade. Qual obra marca sua estreia em 1930?",
        "opcoes": ["Claro Enigma", "Alguma Poesia", "A Rosa do Povo", "Sentimento do Mundo"],
        "gabarito": "Alguma Poesia"
    },
    {
        "id": "Q09", "materia": "Português",
        "enunciado": "Assinale a alternativa em que a pontuação separa incorretamente o sujeito do predicado:",
        "opcoes": [
            "Os alunos do cursinho estudaram bastante.",
            "A prova da UEMG, exigirá muita atenção dos candidatos.",
            "Com a chegada da chuva, a temperatura caiu.",
            "Meus amigos viajaram para Ouro Preto."
        ],
        "gabarito": "A prova da UEMG, exigirá muita atenção dos candidatos."
    },
    {
        "id": "Q10", "materia": "Português",
        "enunciado": "No trecho 'O vento sussurrava segredos à noite', a figura de linguagem presente é:",
        "opcoes": ["Metáfora", "Personificação (Prosopopeia)", "Antítese", "Hipérbole"],
        "gabarito": "Personificação (Prosopopeia)"
    },

    # Matemática (Q11 a Q18)
    {
        "id": "Q11", "materia": "Matemática",
        "enunciado": "Se 5 máquinas produzem 100 peças em 4 dias, quantas peças 3 máquinas produzirão em 6 dias?",
        "opcoes": ["90", "72", "80", "100"],
        "gabarito": "80"
    },
    {
        "id": "Q12", "materia": "Matemática",
        "enunciado": "O valor da expressão log₂(32) + log₃(81) é igual a:",
        "opcoes": ["7", "8", "9", "10"],
        "gabarito": "9"
    },
    {
        "id": "Q13", "materia": "Matemática",
        "enunciado": "Uma PA (Progressão Aritmética) tem primeiro termo a₁ = 3 e razão r = 4. O 10º termo dessa progressão é:",
        "opcoes": ["39", "43", "47", "51"],
        "gabarito": "39"
    },
    {
        "id": "Q14", "materia": "Matemática",
        "enunciado": "A área de um triângulo equilátero cujo lado mede 6 cm é:",
        "opcoes": ["9√3 cm²", "18√3 cm²", "36√3 cm²", "6√3 cm²"],
        "gabarito": "9√3 cm²"
    },
    {
        "id": "Q15", "materia": "Matemática",
        "enunciado": "Se lançarmos dois dados comuns de 6 faces simultaneamente, qual é a probabilidade de a soma dos resultados ser igual a 7?",
        "opcoes": ["1/6", "1/12", "5/36", "7/36"],
        "gabarito": "1/6"
    },
    {
        "id": "Q16", "materia": "Matemática",
        "enunciado": "Dada a função quadrática f(x) = -x² + 6x - 8, as coordenadas do vértice da parábola são:",
        "opcoes": ["(3, 1)", "(2, 0)", "(3, -1)", "(1, 3)"],
        "gabarito": "(3, 1)"
    },
    {
        "id": "Q17", "materia": "Matemática",
        "enunciado": "Um capital de R$ 2.000,00 aplicado a juros simples a uma taxa de 2% ao mês renderá quanto de juros em 5 meses?",
        "opcoes": ["R$ 100,00", "R$ 200,00", "R$ 400,00", "R$ 500,00"],
        "gabarito": "R$ 200,00"
    },
    {
        "id": "Q18", "materia": "Matemática",
        "enunciado": "O volume de um cilindro circular reto com raio da base igual a 3 cm e altura de 10 cm é (considere π = 3):",
        "opcoes": ["180 cm³", "270 cm³", "90 cm³", "540 cm³"],
        "gabarito": "270 cm³"
    },

    # História e Geografia (Q19 a Q26)
    {
        "id": "Q19", "materia": "História",
        "enunciado": "A Inconfidência Mineira (1789) teve como um de seus contextos:",
        "opcoes": [
            "O apoio irrestrito da coroa portuguesa.",
            "A insatisfação com a derrama e a influência iluminista.",
            "O fim imediato da escravidão no Brasil.",
            "A aliança militar com os jesuítas."
        ],
        "gabarito": "A insatisfação com a derrama e a influência iluminista."
    },
    {
        "id": "Q20", "materia": "Geografia",
        "enunciado": "Minas Gerais destaca-se nacionalmente na economia pelo complexo metalúrgico e extrativismo mineral, com ênfase principal na extração de:",
        "opcoes": ["Minério de ferro", "Petróleo bruto", "Carvão mineral hulha", "Gás natural"],
        "gabarito": "Minério de ferro"
    },
    {
        "id": "Q21", "materia": "História",
        "enunciado": "O Período Regencial brasileiro (1831-1840) foi marcado por diversas revoltas provinciais, entre as quais destaca-se em Minas Gerais:",
        "opcoes": ["Revolta dos Farrapos", "Revolta da Sabinada", "Revolta de Vila Rica (Filipe dos Santos)", "Revolta dos Liberais de 1842"],
        "gabarito": "Revolta dos Liberais de 1842"
    },
    {
        "id": "Q22", "materia": "Geografia",
        "enunciado": "O relevo do estado de Minas Gerais é bastante diversificado, destacando-se feições geomorfológicas importantes como:",
        "opcoes": ["A planície amazônica e igapós", "Depressões periféricas e mares de morros (planalto)", "Canyons basálticos do sul do país", "Tabuleiros costeiros nordestinos"],
        "gabarito": "Depressões periféricas e mares de morros (planalto)"
    },
    {
        "id": "Q23", "materia": "História",
        "enunciado": "A Proclamação da República no Brasil, em 1889, contou com a forte articulação dos militares liderados por:",
        "opcoes": ["Duque de Caxias", "Marechal Deodoro da Fonseca", "Barão do Rio Branco", "Getúlio Vargas"],
        "gabarito": "Marechal Deodoro da Fonseca"
    },
    {
        "id": "Q24", "materia": "Geografia",
        "enunciado": "A bacia hidrográfica que abrange a maior parte do território mineiro e escoa rumo ao litoral norte/nordeste do país é a Bacia do:",
        "opcoes": ["Rio Amazonas", "Rio Paraná", "Rio São Francisco", "Rio Paraguai"],
        "gabarito": "Rio São Francisco"
    },
    {
        "id": "Q25", "materia": "História",
        "enunciado": "A Era Vargas (1930-1945) caracterizou-se pela centralização política e impulso à industrialização de base. Qual empresa siderúrgica foi criada em Minas Gerais durante esse governo?",
        "opcoes": ["Vale (CVRD)", "CSN (Companhia Siderúrgica Nacional)", "Usiminas", "Petrobras"],
        "gabarito": "Vale (CVRD)"
    },
    {
        "id": "Q26", "materia": "Geografia",
        "enunciado": "O clima predominante no estado de Minas Gerais é o:",
        "opcoes": [
            "Equatorial úmido",
            "Tropical semiárido no sul",
            "Tropical com duas estações bem definidas (verão chuvoso e inverno seco)",
            "Subtropical frio"
        ],
        "gabarito": "Tropical com duas estações bem definidas (verão chuvoso e inverno seco)"
    },

    # Biologia, Química e Física (Q27 a Q40)
    {
        "id": "Q27", "materia": "Biologia",
        "enunciado": "Em uma cadeia alimentar, a energia disponível nos níveis tróficos:",
        "opcoes": [
            "Aumenta em direção aos consumidores terciários.",
            "Permanece constante.",
            "Diminui do nível dos produtores para os consumidores por dissipação de calor.",
            "É integralmente reaproveitada sem perdas."
        ],
        "gabarito": "Diminui do nível dos produtores para os consumidores por dissipação de calor."
    },
    {
        "id": "Q28", "materia": "Química",
        "enunciado": "Dada a reação de neutralização total entre NaOH e H₂SO₄, a proporção estequiométrica em mols de base para reagir com 1 mol de ácido é:",
        "opcoes": ["1 mol de NaOH", "2 mols de NaOH", "3 mols de NaOH", "4 mols de NaOH"],
        "gabarito": "2 mols de NaOH"
    },
    {
        "id": "Q29", "materia": "Física",
        "enunciado": "Um automóvel acelera uniformemente de 0 a 20 m/s em 4 segundos. A aceleração média desse veículo é:",
        "opcoes": ["2 m/s²", "4 m/s²", "5 m/s²", "80 m/s²"],
        "gabarito": "5 m/s²"
    },
    {
        "id": "Q30", "materia": "Biologia",
        "enunciado": "A organela celular responsável pela respiração celular e produção de ATP nas células eucarióticas é:",
        "opcoes": ["Complexo de Golgi", "Ribossomo", "Mitocôndria", "Lisossomo"],
        "gabarito": "Mitocôndria"
    },
    {
        "id": "Q31", "materia": "Química",
        "enunciado": "O pH de uma solução aquosa com concentração de íons hidrônio [H₃O⁺] = 10⁻⁴ mol/L é igual a:",
        "opcoes": ["4", "7", "10", "14"],
        "gabarito": "4"
    },
    {
        "id": "Q32", "materia": "Física",
        "enunciado": "A Primeira Lei da Termodinâmica é uma expressão do princípio de conservação de:",
        "opcoes": ["Quantidade de movimento", "Carga elétrica", "Energia", "Momento angular"],
        "gabarito": "Energia"
    },
    {
        "id": "Q33", "materia": "Biologia",
        "enunciado": "O processo de divisão celular que origina células gaméticas (espermatozoides e óvulos) com metade do número cromossômico é:",
        "opcoes": ["Mitose", "Meiose", "Fissão binária", "Gemulação"],
        "gabarito": "Meiose"
    },
    {
        "id": "Q34", "materia": "Química",
        "enunciado": "As ligações químicas encontradas nas moléculas de água (H₂O) são do tipo:",
        "opcoes": ["Iônicas", "Metálicas", "Covalentes polares", "Coordenadas puras"],
        "gabarito": "Covalentes polares"
    },
    {
        "id": "Q35", "materia": "Física",
        "enunciado": "Segundo a Segunda Lei de Newton, a força resultante aplicada sobre um corpo é igual ao produto da massa pela:",
        "opcoes": ["Velocidade", "Aceleração", "Posição", "Densidade"],
        "gabarito": "Aceleração"
    },
    {
        "id": "Q36", "materia": "Biologia",
        "enunciado": "A estrutura de ácidos nucleicos responsável por conter as instruções genéticas para o desenvolvimento e funcionamento dos seres vivos é o:",
        "opcoes": ["ATP", "DNA", "Amido", "Glicogênio"],
        "gabarito": "DNA"
    },
    {
        "id": "Q37", "materia": "Química",
        "enunciado": "Na tabela periódica, os elementos pertencentes ao Grupo 1 (exceto o hidrogênio) são conhecidos como:",
        "opcoes": ["Metais Alcalinos", "Metais Alcalino-Terrosos", "Halogênios", "Gases Nobres"],
        "gabarito": "Metais Alcalinos"
    },
    {
        "id": "Q38", "materia": "Física",
        "enunciado": "A energia associada ao movimento de um corpo dotado de massa é denominada energia:",
        "opcoes": ["Potencial gravitacional", "Cinética", "Potencial elástica", "Térmica interna"],
        "gabarito": "Cinética"
    },
    {
        "id": "Q39", "materia": "Biologia",
        "enunciado": "Relação ecológica interespecífica em que ambas as espécies associadas se beneficiam, sendo a relação obrigatória para a sobrevivência, chama-se:",
        "opcoes": ["Competição", "Mutualismo", "Comensalismo", "Parasitismo"],
        "gabarito": "Mutualismo"
    },
    {
        "id": "Q40", "materia": "Química",
        "enunciado": "Um sistema físico-químico que apresenta mais de uma fase visível é classificado como:",
        "opcoes": ["Mistura homogênea", "Solução verdadeira", "Mistura heterogênea", "Substância pura simples"],
        "gabarito": "Mistura heterogênea"
    },

    # Língua Estrangeira e Atualidades (Q41 a Q48)
    {
        "id": "Q41", "materia": "Língua Estrangeira",
        "enunciado": "In English, choose the alternative that correctly completes the sentence: 'If I ___ rich, I would travel around the world.'",
        "opcoes": ["am", "were", "will be", "have been"],
        "gabarito": "were"
    },
    {
        "id": "Q42", "materia": "Língua Estrangeira",
        "enunciado": "Identifique a tradução mais adequada para a expressão em inglês 'by the way':",
        "opcoes": ["Perto daqui", "A propósito / Por falar nisso", "De jeito nenhum", "No meio do caminho"],
        "gabarito": "A propósito / Por falar nisso"
    },
    {
        "id": "Q43", "materia": "Atualidades",
        "enunciado": "As discussões globais sobre transição energética e mudanças climáticas frequentemente abordam a necessidade de conter o aquecimento global reduzindo a emissão de:",
        "opcoes": ["Oxigênio puro", "Gás carbônico (CO₂)", "Vapor de água", "Hélio"],
        "gabarito": "Gás carbônico (CO₂)"
    },
    {
        "id": "Q44", "materia": "Atualidades",
        "enunciado": "O avanço acelerado da Inteligência Artificial Generativa levanta debates éticos, econômicos e sociais contemporâneos que afetam diretamente qual setor central na formação dos jovens?",
        "opcoes": [
            "A educação e o mercado de trabalho",
            "A extração primária de sal",
            "A navegação marítima a vela",
            "A indústria têxtil manual"
        ],
        "gabarito": "A educação e o mercado de trabalho"
    },
    {
        "id": "Q45", "materia": "Sociologia/Filosofia",
        "enunciado": "O conceito de 'Cidadania' envolve o gozo de direitos civis, políticos e sociais. Na história brasileira, a conquista do voto feminino foi garantida constitucionalmente em:",
        "opcoes": ["1822", "1889", "1932 (Código Eleitoral)", "1988"],
        "gabarito": "1932 (Código Eleitoral)"
    },
    {
        "id": "Q46", "materia": "Sociologia/Filosofia",
        "enunciado": "Filósofo contratualista que defendia que o Estado surge de um 'contrato social' para garantir a segurança e a propriedade privada dos cidadãos:",
        "opcoes": ["Platão", "John Locke", "Sócrates", "Aristóteles"],
        "gabarito": "John Locke"
    },
    {
        "id": "Q47", "materia": "Geografia",
        "enunciado": "A globalização intensificou os fluxos de informações, mercadorias e capitais. O fenômeno de encurtamento das distâncias temporais e espaciais devido aos meios de comunicação e transporte modernos é conhecido como:",
        "opcoes": ["Aldeia global ou compressão do tempo-espaço", "Isolamento regional", "Desindustrialização primária", "Autarquia econômica"],
        "gabarito": "Aldeia global ou compressão do tempo-espaço"
    },
    {
        "id": "Q48", "materia": "Língua Estrangeira",
        "enunciado": "Choose the correct antonym for the word 'ancient' in English:",
        "opcoes": ["Old", "Modern / New", "Historic", "Distant"],
        "gabarito": "Modern / New"
    }
]

# --- BANCO DE TEMAS E TEXTOS MOTIVADORES ---
PAINEL_REDACAO = {
    "Tema 1": {
        "tema": "O impacto da inteligência artificial nas relações de trabalho e na educação contemporânea.",
        "textos": [
            "**Texto I:** 'A automação impulsionada por algoritmos avançados e inteligência artificial generativa redefine as competências exigidas pelo mercado laboral, exigindo dos sistemas educacionais uma transição urgente para a criatividade, pensamento crítico e letramento digital.' (Relatório Global de Empregabilidade)",
            "**Texto II:** 'Se por um lado a tecnologia democratiza o acesso à informação e personaliza o ensino, por outro acentua desigualdades estruturais decorrentes da exclusão digital e da falta de infraestrutura nas escolas públicas do país.'"
        ]
    },
    "Tema 2": {
        "tema": "Os desafios para a preservação do patrimônio histórico e cultural no Brasil.",
        "textos": [
            "**Texto I:** 'O patrimônio cultural — material e imaterial — constitui a memória coletiva e a identidade de um povo. No Brasil, capitais históricas como Ouro Preto e centros urbanos seculares enfrentam pressões imobiliárias, escassez de recursos públicos para restauro e negligência na conservação.'",
            "**Texto II:** 'Preservar o passado não significa estagnar o presente, mas reconhecer nas raízes históricas o alicerce para a construção da cidadania e do pertencimento social nas próximas gerações.'"
        ]
    },
    "Tema 3": {
        "tema": "A questão do desperdício de alimentos e a segurança alimentar na sociedade moderna.",
        "textos": [
            "**Texto I:** 'Toneladas de alimentos perfeitamente próprios para o consumo são descartadas diariamente ao longo da cadeia de suprimentos, desde a colheita no campo até o descarte nas residências, contrastando frontalmente com índices alarmantes de insegurança alimentar.'",
            "**Texto II:** 'O combate ao desperdício alimentar exige uma revisão profunda dos hábitos de consumo contemporâneos, políticas públicas logísticas eficientes e campanhas de conscientização voltadas para a sustentabilidade e solidariedade social.'"
        ]
    },
    "Tema 4": {
        "tema": "O papel e a valorização da ciência no desenvolvimento social do Brasil.",
        "textos": [
            "**Texto I:** 'A produção científica nacional demonstra resiliência e impacto internacional notável em áreas como saúde pública, agricultura tropical e energias renováveis, muitas vezes operando sob severas restrições orçamentárias e cortes de financiamento.'",
            "**Texto II:** 'A valorização da ciência não se restringe ao reconhecimento acadêmico, mas traduz-se na garantia de soberania nacional, melhoria da qualidade de vida da população e no combate direto ao negacionismo científico.'"
        ]
    }
}

st.title("📝 Simulado Oficial UEMG (48 Questões + Redação)")
st.write("Esta é a simulação completa no formato idêntico ao vestibular da UEMG. Responda com atenção à prova objetiva e leia os textos motivadores antes de redigir sua dissertação.")

nome_aluna = st.text_input("Digite o seu nome completo ou apelido:")

if nome_aluna:
    if "questoes_sorteadas" not in st.session_state:
        q_sort = BANCO_QUESTOES.copy()
        random.shuffle(q_sort)
        for q in q_sort:
            # Embaralha as opções, mas mantém as letras A, B, C, D fixas e ordenadas
            opcoes_embaralhadas = q["opcoes"].copy()
            random.shuffle(opcoes_embaralhadas)
            q["opcoes_embaralhadas"] = opcoes_embaralhadas
            
        st.session_state.questoes_sorteadas = q_sort
        
        chave_tema_sorteado = random.choice(list(PAINEL_REDACAO.keys()))
        st.session_state.dados_redacao = PAINEL_REDACAO[chave_tema_sorteado]

    st.markdown("---")
    st.header("🎯 Prova Objetiva (48 Questões)")
    
    respostas_usuario = {}

    for i, q in enumerate(st.session_state.questoes_sorteadas):
        st.subheader(f"Questão {i+1} de 48 — [{q['materia']}]")
        st.write(q["enunciado"])
        
        # index=None garante que NENHUMA alternativa venha marcada previamente
        resp_escolhida = st.radio(
            "Escolha a alternativa:",
            options=q["opcoes_embaralhadas"],
            index=None,
            key=f"resp_{q['id']}"
        )
        
        certeza = st.radio("Qual o seu grau de certeza nesta resposta?", [
            "1 - Chutei / Não sei", 
            "2 - Em dúvida entre duas", 
            "3 - Certeza absoluta"
        ], index=None, key=f"cert_{q['id']}")
        
        respostas_usuario[q["id"]] = {"resposta": resp_escolhida, "certeza": certeza}
        st.markdown("---")

    st.header("✍️ Proposta de Redação & Textos Motivadores")
    st.info(f"**Tema Sorteado para você:** {st.session_state.dados_redacao['tema']}")
    
    st.markdown("#### 📚 Textos Motivadores de Apoio:")
    for t_motivo in st.session_state.dados_redacao["textos"]:
        st.markdown(t_motivo)
    
    st.markdown("---")
    st.write("*Instrução:* Com base na leitura dos textos motivadores e nos seus conhecimentos, elabore um texto dissertativo-argumentativo estruturado (Introdução, Desenvolvimento e Conclusão) em norma-padrão.")
    
    texto_redacao = st.text_area("Digite ou cole sua redação aqui:", height=350)

    if st.button("Finalizar Prova Oficial e Gerar Relatório"):
        # Valida se deixou alguma questão sem responder
        questoes_nao_respondidas = sum(1 for q_id in respostas_usuario if respostas_usuario[q_id]["resposta"] is None)
        
        if questoes_nao_respondidas > 0:
            st.warning(f"⚠️ Atenção: Você deixou {questoes_nao_respondidas} questão(ões) sem responder. Responda todas antes de finalizar!")
        elif len(texto_redacao.strip()) < 50:
            st.error("Sua redação está muito curta. Desenvolva o texto antes de finalizar!")
        else:
            st.success("Prova concluída com sucesso!")
            
            dados_relatorio = []
            acertos_totais = 0

            for q in st.session_state.questoes_sorteadas:
                r_user = respostas_usuario[q["id"]]["resposta"]
                c_user = respostas_usuario[q["id"]]["certeza"] or "Não informado"
                acertou = (r_user == q["gabarito"])
                if acertou:
                    acertos_totais += 1

                dados_relatorio.append({
                    "Aluna": nome_aluna,
                    "Questao_ID": q["id"],
                    "Materia": q["materia"],
                    "Resposta_Aluna": r_user,
                    "Gabarito": q["gabarito"],
                    "Acertou": 1 if acertou else 0,
                    "Grau_Certeza": c_user
                })

            df = pd.DataFrame(dados_relatorio)

            st.metric(label="Desempenho Final na Prova Objetiva", value=f"{acertos_totais} / 48")

            st.subheader("📊 Relatório Detalhado por Matéria")
            st.dataframe(df)

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Baixar arquivo de dados oficiais (CSV)",
                data=csv,
                file_name=f"simulado_oficial_uemg_{nome_aluna.lower().replace(' ', '_')}.csv",
                mime="text/csv"
            )

            st.markdown("### 📝 Redação Enviada:")
            st.write(texto_redacao)
            st.info("Baixe a tabela CSV ou copie o relatório e traga para cá junto com a redação para fazermos a análise detalhada de desempenho por disciplina e a correção completa do texto!")
