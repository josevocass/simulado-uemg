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
        "alternativas": ["A) O jovem aspirava o cargo de diretor.", "B) Aspiramos o perfume das flores no jardim.", "C) Ele aspira em passar no vestibular.", "D) O médico aspirou o paciente com cuidado."],
        "gabarito": "B) Aspiramos o perfume das flores no jardim."
    },
    {
        "id": "Q02", "materia": "Português",
        "enunciado": "Identifique a opção em que a crase foi empregada incorretamente:",
        "alternativas": ["A) Fomos à festa de formatura.", "B) Ele entregue o documento à diretora.", "C) Começou a chover às duas horas.", "D) Prefiro passear a ficar em casa."],
        "gabarito": "D) Prefiro passear a ficar em casa."
    },
    {
        "id": "Q03", "materia": "Literatura",
        "enunciado": "O Romantismo no Brasil teve fases distintas. Qual característica marca predominantemente a chamada 'Segunda Geração Romântica' (Mal do Século)?",
        "alternativas": ["A) Nacionalismo ufanista e exaltação do índio.", "B) Pessimismo profundo, tédio, angústia e culto à morte.", "C) Crítica social e combate à escravidão.", "D) Objetividade científica e parnasianismo."],
        "gabarito": "B) Pessimismo profundo, tédio, angústia e culto à morte."
    },
    {
        "id": "Q04", "materia": "Português",
        "enunciado": "Na frase 'O livro que comprei é excelente', a palavra 'que' classifica-se morfologicamente como:",
        "alternativas": ["A) Conjunção integrante", "B) Pronome relativo", "C) Conjunção subordinativa causal", "D) Partícula expletiva"],
        "gabarito": "B) Pronome relativo"
    },
    {
        "id": "Q05", "materia": "Literatura",
        "enunciado": "Autor mineiro de grande destaque, criador de obras como 'Grande Sertão: Veredas', que revolucionou a linguagem literária brasileira:",
        "alternativas": ["A) Machado de Assis", "B) Carlos Drummond de Andrade", "C) João Guimarães Rosa", "D) Lima Barreto"],
        "gabarito": "C) João Guimarães Rosa"
    },
    {
        "id": "Q06", "materia": "Português",
        "enunciado": "Assinale a alternativa em que a concordância verbal está inteiramente de acordo com a norma-padrão:",
        "alternativas": ["A) Faltou coragem e determinação aos candidatos.", "B) Haviam muitos alunos na sala de aula.", "C) Devo fazer cerca de dois anos que não o vejo.", "D) Mais de um aluno faltaram à prova."],
        "gabarito": "A) Faltou coragem e determinação aos candidatos."
    },
    {
        "id": "Q07", "materia": "Português",
        "enunciado": "A função da linguagem focada no próprio código utilizada na mensagem é denominada:",
        "alternativas": ["A) Emotiva", "B) Fática", "C) Metalinguística", "D) Conativa"],
        "gabarito": "C) Metalinguística"
    },
    {
        "id": "Q08", "materia": "Literatura",
        "enunciado": "O Modernismo em Minas Gerais teve forte expressão na segunda fase com a poesia de Carlos Drummond de Andrade. Qual obra marca sua estreia em 1930?",
        "alternativas": ["A) Claro Enigma", "B) Alguma Poesia", "C) A Rosa do Povo", "D) Sentimento do Mundo"],
        "gabarito": "B) Alguma Poesia"
    },
    {
        "id": "Q09", "materia": "Português",
        "enunciado": "Assinale a alternativa em que a pontuação separa incorretamente o sujeito do predicado:",
        "alternativas": ["A) Os alunos do cursinho estudaram bastante.", "B) A prova da UEMG, exigirá muita atenção dos candidatos.", "C) Com a chegada da chuva, a temperatura caiu.", "D) Meus amigos viajaram para Ouro Preto."],
        "gabarito": "B) A prova da UEMG, exigirá muita atenção dos candidatos."
    },
    {
        "id": "Q10", "materia": "Português",
        "enunciado": "No trecho 'O vento sussurrava segredos à noite', a figura de linguagem presente é:",
        "alternativas": ["A) Metáfora", "B) Personificação (Prosopopeia)", "C) Antítese", "D) Hipérbole"],
        "gabarito": "B) Personificação (Prosopopeia)"
    },

    # Matemática (Q11 a Q18)
    {
        "id": "Q11", "materia": "Matemática",
        "enunciado": "Se 5 máquinas produzem 100 peças em 4 dias, quantas peças 3 máquinas produzirão em 6 dias?",
        "alternativas": ["A) 90", "B) 72", "C) 80", "D) 100"],
        "gabarito": "C) 80"
    },
    {
        "id": "Q12", "materia": "Matemática",
        "enunciado": "O valor da expressão $log_2(32) + log_3(81)$ é igual a:",
        "alternativas": ["A) 7", "B) 8", "C) 9", "D) 10"],
        "gabarito": "C) 9"
    },
    {
        "id": "Q13", "materia": "Matemática",
        "enunciado": "Uma PA (Progressão Aritmética) tem primeiro termo $a_1 = 3$ e razão $r = 4$. O 10º termo dessa progressão é:",
        "alternativas": ["A) 39", "B) 43", "C) 47", "D) 51"],
        "gabarito": "A) 39"
    },
    {
        "id": "Q14", "materia": "Matemática",
        "enunciado": "A área de um triângulo equilátero cujo lado mede $6\\text{ cm}$ é:",
        "alternativas": ["A) $9\\sqrt{3}\\text{ cm}^2$", "B) $18\\sqrt{3}\\text{ cm}^2$", "C) $36\\sqrt{3}\\text{ cm}^2$", "D) $6\\sqrt{3}\\text{ cm}^2$"],
        "gabarito": "A) $9\\sqrt{3}\\text{ cm}^2$"
    },
    {
        "id": "Q15", "materia": "Matemática",
        "enunciado": "Se lançarmos dois dados comuns de 6 faces simultaneamente, qual é a probabilidade de a soma dos resultados ser igual a 7?",
        "alternativas": ["A) 1/6", "B) 1/12", "C) 5/36", "D) 7/36"],
        "gabarito": "A) 1/6"
    },
    {
        "id": "Q16", "materia": "Matemática",
        "enunciado": "Dada a função quadrática $f(x) = -x^2 + 6x - 8$, as coordenadas do vértice da parábola são:",
        "alternativas": ["A) $(3, 1)$", "B) $(2, 0)$", "C) $(3, -1)$", "D) $(1, 3)$"],
        "gabarito": "A) $(3, 1)$"
    },
    {
        "id": "Q17", "materia": "Matemática",
        "enunciado": "Um capital de R$ 2.000,00 aplicado a juros simples a uma taxa de 2% ao mês renderá quanto de juros em 5 meses?",
        "alternativas": ["A) R$ 100,00", "B) R$ 200,00", "C) R$ 400,00", "D) R$ 500,00"],
        "gabarito": "B) R$ 200,00"
    },
    {
        "id": "Q18", "materia": "Matemática",
        "enunciado": "O volume de um cilindro circular reto com raio da base igual a $3\\text{ cm}$ e altura de $10\\text{ cm}$ é (considere $\\pi = 3$):",
        "alternativas": ["A) $180\\text{ cm}^3$", "B) $270\\text{ cm}^3$", "C) $90\\text{ cm}^3$", "D) $540\\text{ cm}^3$"],
        "gabarito": "B) $270\\text{ cm}^3$"
    },

    # História e Geografia (Q19 a Q26)
    {
        "id": "Q19", "materia": "História",
        "enunciado": "A Inconfidência Mineira (1789) teve como um de seus contextos:",
        "alternativas": ["A) O apoio irrestrito da coroa portuguesa.", "B) A insatisfação com a derrama e a influência iluminista.", "C) O fim imediato da escravidão no Brasil.", "D) A aliança militar com os jesuítas."],
        "gabarito": "B) A insatisfação com a derrama e a influência iluminista."
    },
    {
        "id": "Q20", "materia": "Geografia",
        "enunciado": "Minas Gerais destaca-se nacionalmente na economia pelo complexo metalúrgico e extrativismo mineral, com ênfase principal na extração de:",
        "alternativas": ["A) Minério de ferro", "B) Petróleo bruto", "C) Carvão mineral hulha", "D) Gás natural"],
        "gabarito": "A) Minério de ferro"
    },
    {
        "id": "Q21", "materia": "História",
        "enunciado": "O Período Regencial brasileiro (1831-1840) foi marcado por diversas revoltas provinciais, entre as quais destaca-se em Minas Gerais:",
        "alternativas": ["A) Revolta dos Farrapos", "B) Revolta da Sabinada", "C) Revolta de Vila Rica (Filipe dos Santos)", "D) Revolta dos Liberais de 1842"],
        "gabarito": "D) Revolta dos Liberais de 1842"
    },
    {
        "id": "Q22", "materia": "Geografia",
        "enunciado": "O relevo do estado de Minas Gerais é bastante diversificado, destacando-se feições geomorfológicas importantes como:",
        "alternativas": ["A) A planície amazônica e igapós", "B) Depressões periféricas e mares de morros (planalto)", "C) Canyons basálticos do sul do país", "D) Tabuleiros costeiros nordestinos"],
        "gabarito": "B) Depressões periféricas e mares de morros (planalto)"
    },
    {
        "id": "Q23", "materia": "História",
        "enunciado": "A Proclamação da República no Brasil, em 1889, contou com a forte articulação dos militares liderados por:",
        "alternativas": ["A) Duque de Caxias", "B) Marechal Deodoro da Fonseca", "C) Barão do Rio Branco", "D) Getúlio Vargas"],
        "gabarito": "B) Marechal Deodoro da Fonseca"
    },
    {
        "id": "Q24", "materia": "Geografia",
        "enunciado": "A bacia hidrográfica que abrange a maior parte do território mineiro e escoa rumo ao litoral norte/nordeste do país é a Bacia do:",
        "alternativas": ["A) Rio Amazonas", "B) Rio Paraná", "C) Rio São Francisco", "D) Rio Paraguai"],
        "gabarito": "C) Rio São Francisco"
    },
    {
        "id": "Q25", "materia": "História",
        "enunciado": "A Era Vargas (1930-1945) caracterizou-se pela centralização política e impulso à industrialização de base. Qual empresa siderúrgica foi criada em Minas Gerais durante esse governo?",
        "alternativas": ["A) Vale (CVRD)", "B) CSN (Companhia Siderúrgica Nacional)", "C) Usiminas", "D) Petrobras"],
        "gabarito": "A) Vale (CVRD)"
    },
    {
        "id": "Q26", "materia": "Geografia",
        "enunciado": "O clima predominante no estado de Minas Gerais é o:",
        "alternativas": ["A) Equatorial úmido", "B) Tropical semiárido no sul", "C) Tropical com duas estações bem definidas (verão chuvoso e inverno seco)", "D) Subtropical frio"],
        "gabarito": "C) Tropical com duas estações bem definidas (verão chuvoso e inverno seco)"
    },

    # Biologia, Química e Física (Q27 a Q40)
    {
        "id": "Q27", "materia": "Biologia",
        "enunciado": "Em uma cadeia alimentar, a energia disponível nos níveis tróficos:",
        "alternativas": ["A) Aumenta em direção aos consumidores terciários.", "B) Permanece constante.", "C) Diminui do nível dos produtores para os consumidores por dissipação de calor.", "D) É integralmente reaproveitada sem perdas."],
        "gabarito": "C) Diminui do nível dos produtores para os consumidores por dissipação de calor."
    },
    {
        "id": "Q28", "materia": "Química",
        "enunciado": "Dada a reação de neutralização total entre NaOH e $H_2SO_4$, a proporção estequiométrica em mols de base para reagir com 1 mol de ácido é:",
        "alternativas": ["A) 1 mol de NaOH", "B) 2 mols de NaOH", "C) 3 mols de NaOH", "D) 4 mols de NaOH"],
        "gabarito": "B) 2 mols de NaOH"
    },
    {
        "id": "Q29", "materia": "Física",
        "enunciado": "Um automóvel acelera uniformemente de 0 a 20 m/s em 4 segundos. A aceleração média desse veículo é:",
        "alternativas": ["A) 2 m/s²", "B) 4 m/s²", "C) 5 m/s²", "D) 80 m/s²"],
        "gabarito": "C) 5 m/s²"
    },
    {
        "id": "Q30", "materia": "Biologia",
        "enunciado": "A organela celular responsável pela respiração celular e produção de ATP nas células eucarióticas é:",
        "alternativas": ["A) Complexo de Golgi", "B) Ribossomo", "C) Mitocôndria", "D) Lisossomo"],
        "gabarito": "C) Mitocôndria"
    },
    {
        "id": "Q31", "materia": "Química",
        "enunciado": "O pH de uma solução aquosa com concentração de íons hidrônio $[H_3O^+] = 10^{-4}\\text{ mol/L}$ é igual a:",
        "alternativas": ["A) 4", "B) 7", "C) 10", "D) 14"],
        "gabarito": "A) 4"
    },
    {
        "id": "Q32", "materia": "Física",
        "enunciado": "A Primeira Lei da Termodinâmica é uma expressão do princípio de conservação de:",
        "alternativas": ["A) Quantidade de movimento", "B) Carga elétrica", "C) Energia", "D) Momento angular"],
        "gabarito": "C) Energia"
    },
    {
        "id": "Q33", "materia": "Biologia",
        "enunciado": "O processo de divisão celular que origina células gaméticas (espermatozoides e óvulos) com metade do número cromossômico é:",
        "alternativas": ["A) Mitose", "B) Meiose", "C) Fissão binária", "D) Gemulação"],
        "gabarito": "B) Meiose"
    },
    {
        "id": "Q34", "materia": "Química",
        "enunciado": "As ligações químicas encontradas nas moléculas de água ($H_2O$) são do tipo:",
        "alternativas": ["A) Iônicas", "B) Metálicas", "C) Covalentes polares", "D) Coordenadas puras"],
        "gabarito": "C) Covalentes polares"
    },
    {
        "id": "Q35", "materia": "Física",
        "enunciado": "Segundo a Segunda Lei de Newton, a força resultante aplicada sobre um corpo é igual ao produto da massa pela:",
        "alternativas": ["A) Velocidade", "B) Aceleração", "C) Posição", "D) Densidade"],
        "gabarito": "B) Aceleração"
    },
    {
        "id": "Q36", "materia": "Biologia",
        "enunciado": "A estrutura de ácidos nucleicos responsável por conter as instruções genéticas para o desenvolvimento e funcionamento dos seres vivos é o:",
        "alternativas": ["A) ATP", "B) DNA", "C) Amido", "D) Glicogênio"],
        "gabarito": "B) DNA"
    },
    {
        "id": "Q37", "materia": "Química",
        "enunciado": "Na tabela periódica, os elementos pertencentes ao Grupo 1 (exceto o hidrogênio) são conhecidos como:",
        "alternativas": ["A) Metais Alcalinos", "B) Metais Alcalino-Terrosos", "C) Halogênios", "D) Gases Nobres"],
        "gabarito": "A) Metais Alcalinos"
    },
    {
        "id": "Q38", "materia": "Física",
        "enunciado": "A energia associada ao movimento de um corpo dotado de massa é denominada energia:",
        "alternativas": ["A) Potencial gravitacional", "B) Cinética", "C) Potencial elástica", "D) Térmica interna"],
        "gabarito": "B) Cinética"
    },
    {
        "id": "Q39", "materia": "Biologia",
        "enunciado": "Relação ecológica interespecífica em que ambas as espécies associadas se beneficiam, sendo a relação obrigatória para a sobrevivência, chama-se:",
        "alternativas": ["A) Competição", "B) Mutualismo", "C) Comensalismo", "D) Parasitismo"],
        "gabarito": "B) Mutualismo"
    },
    {
        "id": "Q40", "materia": "Química",
        "enunciado": "Um sistema físico-químico que apresenta mais de uma fase visível é classificado como:",
        "alternativas": ["A) Mistura homogênea", "B) Solução verdadeira", "C) Mistura heterogênea", "D) Substância pura simples"],
        "gabarito": "C) Mistura heterogênea"
    },

    # Língua Estrangeira e Atualidades (Q41 a Q48)
    {
        "id": "Q41", "materia": "Língua Estrangeira",
        "enunciado": "In English, choose the alternative that correctly completes the sentence: 'If I ___ rich, I would travel around the world.'",
        "alternativas": ["A) am", "B) were", "C) will be", "D) have been"],
        "gabarito": "B) were"
    },
    {
        "id": "Q42", "materia": "Língua Estrangeira",
        "enunciado": "Identifique a tradução mais adequada para a expressão em inglês 'by the way':",
        "alternativas": ["A) Perto daqui", "B) A propósito / Por falar nisso", "C) De jeito nenhum", "D) No meio do caminho"],
        "gabarito": "B) A propósito / Por falar nisso"
    },
    {
        "id": "Q43", "materia": "Atualidades",
        "enunciado": "As discussões globais sobre transição energética e mudanças climáticas frequentemente abordam a necessidade de conter o aquecimento global reduzindo a emissão de:",
        "alternativas": ["A) Oxigênio puro", "B) Gás carbônico ($CO_2$)", "C) Vapor de água", "D) Hélio"],
        "gabarito": "B) Gás carbônico ($CO_2$)"
    },
    {
        "id": "Q44", "materia": "Atualidades",
        "enunciado": "O avanço acelerado da Inteligência Artificial Generativa levanta debates éticos, econômicos e sociais contemporâneos que afetam diretamente qual setor central na formação dos jovens?",
        "alternativas": ["A) A educação e o mercado de trabalho", "B) A extração primária de sal", "C) A navegação marítima a vela", "D) A indústria têxtil manual"],
        "gabarito": "A) A educação e o mercado de trabalho"
    },
    {
        "id": "Q45", "materia": "Sociologia/Filosofia",
        "enunciado": "O conceito de 'Cidadania' envolve o gozo de direitos civis, políticos e sociais. Na história brasileira, a conquista do voto feminino foi garantida constitucionalmente em:",
        "alternativas": ["A) 1822", "B) 1889", "C) 1932 (Código Eleitoral)", "D) 1988"],
        "gabarito": "C) 1932 (Código Eleitoral)"
    },
    {
        "id": "Q46", "materia": "Sociologia/Filosofia",
        "enunciado": "Filósofo contratualista que defendia que o Estado surge de um 'contrato social' para garantir a segurança e a propriedade privada dos cidadãos:",
        "alternativas": ["A) Platão", "B) John Locke", "C) Sócrates", "D) Aristóteles"],
        "gabarito": "B) John Locke"
    },
    {
        "id": "Q47", "materia": "Geografia",
        "enunciado": "A globalização intensificou os fluxos de informações, mercadorias e capitais. O fenômeno de encurtamento das distâncias temporais e espaciais devido aos meios de comunicação e transporte modernos é conhecido como:",
        "alternativas": ["A) Aldeia global ou compressão do tempo-espaço", "B) Isolamento regional", "C) Desindustrialização primária", "D) Autarquia econômica"],
        "gabarito": "A) Aldeia global ou compressão do tempo-espaço"
    },
    {
        "id": "Q48", "materia": "Língua Estrangeira",
        "enunciado": "Choose the correct antonym for the word 'ancient' in English:",
        "alternativas": ["A) Old", "B) Modern / New", "C) Historic", "D) Distant"],
        "gabarito": "B) Modern / New"
    }
]

# --- BANCO DE TEMAS E TEXTOS MOTIVADORES (PADRÃO UEMG) ---
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
            alt = q["alternativas"].copy()
            random.shuffle(alt)
            q["alternativas_embaralhadas"] = alt
        st.session_state.questoes_sorteadas = q_sort
        
        # Sorteia um dos temas do painel de redação com seus respectivos textos motivadores
        chave_tema_sorteado = random.choice(list(PAINEL_REDACAO.keys()))
        st.session_state.dados_redacao = PAINEL_REDACAO[chave_tema_sorteado]

    st.markdown("---")
    st.header("🎯 Prova Objetiva (48 Questões)")
    
    respostas_usuario = {}

    for i, q in enumerate(st.session_state.questoes_sorteadas):
        st.subheader(f"Questão {i+1} de 48 — [{q['materia']}]")
        st.write(q["enunciado"])
        
        resp = st.radio("Escolha a alternativa:", q["alternativas_embaralhadas"], key=f"resp_{q['id']}")
        certeza = st.radio("Qual o seu grau de certeza nesta resposta?", [
            "1 - Chutei / Não sei", 
            "2 - Em dúvida entre duas", 
            "3 - Certeza absoluta"
        ], key=f"cert_{q['id']}")
        
        respostas_usuario[q["id"]] = {"resposta": resp, "certeza": certeza}
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
        if len(texto_redacao.strip()) < 50:
            st.error("Sua redação está muito curta. Desenvolva o texto antes de finalizar!")
        else:
            st.success("Prova concluída com sucesso!")
            
            dados_relatorio = []
            acertos_totais = 0

            for q in st.session_state.questoes_sorteadas:
                r_user = respostas_usuario[q["id"]]["resposta"]
                c_user = respostas_usuario[q["id"]]["certeza"]
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
