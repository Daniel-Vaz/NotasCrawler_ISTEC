#!python3
# Este ficheiro tem a função responsável pela Tradução da Sigla no URL para o nome completo do Módulo.
# Script em v.1.2 - Ter em conta que o código pode e deverá ser melhorado.


#É a nossa "Base de Dados" caso seja necessário mudar alguma disciplina e\ou adicionar uma nova é aqui que fazemos as alterações.
Cadeiras_Nomes = [
    "MAT","HI","RC","RCA","ANRO","ACS","SR","ISO","CLP","IT","EMP","AH","MH","DA","HRC","IRL",
    "SR","SD","CASOS","PS","SCE","CSSL","SOC","SOS","SOOS","SOSOS","PT","FC","PC","CSSL","PETD","POO",
    "EDECD","ASEBD","CEBDSQL","PSQL","MP","RI","PDM","A3D","AED","BD","ADM","IDM","FG","UXUI","PW",
    "MD","GAMING","Projeto","SO","AG","CF","FC","MKT","AR","HST","DFE","ICC","RCD","ASI","GP","CVFG",
    "PCAI","AMV","PMDM","3D","TDWD","CTDFSV","SIMD","FAM",
    ]

#Função Tradutora
def Cadeira(link):
    nome_texto = str(link)
    if nome_texto in Cadeiras_Nomes:
        if nome_texto == Cadeiras_Nomes[0]:
            nome_texto = "Matemática"
        elif nome_texto == Cadeiras_Nomes[1]:
            nome_texto = "História de Informática"
        elif nome_texto == Cadeiras_Nomes[2]:
            nome_texto = "Redes de Computadores"
        elif nome_texto == Cadeiras_Nomes[3]:
            nome_texto = "Redes de Computadores Avançadas"           
        elif nome_texto == Cadeiras_Nomes[4]:
            nome_texto = "Avaliação das Necessidades de Rede numa Organização"
        elif nome_texto == Cadeiras_Nomes[5]:
            nome_texto = "Arquitetura Cliente – Servidor"
        elif nome_texto == Cadeiras_Nomes[6]:
            nome_texto = "Serviços de Rede"
        elif nome_texto == Cadeiras_Nomes[7]:
            nome_texto = "Introdução aos Sistemas Operativos"
        elif nome_texto == Cadeiras_Nomes[8]:
            nome_texto = "Comunicar em Língua Portuguesa"
        elif nome_texto == Cadeiras_Nomes[9]:
            nome_texto = "Inglês Técnico"
        elif nome_texto == Cadeiras_Nomes[10]:
            nome_texto = "Empreendedorismo"
        elif nome_texto == Cadeiras_Nomes[11]:
            nome_texto = "Arquitetura de Hardware"
        elif nome_texto == Cadeiras_Nomes[12]:
            nome_texto = "Montagem de Hardware"
        elif nome_texto == Cadeiras_Nomes[13]:
            nome_texto = "Detecção de Avarias"
        elif nome_texto == Cadeiras_Nomes[14]:
            nome_texto = "Hardware e Redes de Computadores"
        elif nome_texto == Cadeiras_Nomes[15]:
            nome_texto = "Instalação de Redes Locais"
        elif nome_texto == Cadeiras_Nomes[16]:
            nome_texto = "Servidor de Dados"
        elif nome_texto == Cadeiras_Nomes[17]:
            nome_texto = "Configuração Avançada de Sistemas Operativos Servidores"
        elif nome_texto == Cadeiras_Nomes[18]:
            nome_texto = "Políticas de Segurança"
        elif nome_texto == Cadeiras_Nomes[19]:
            nome_texto = "Servidor de Correio Eletrónico"
        elif nome_texto == Cadeiras_Nomes[20]:
            nome_texto = "Configuração de Serviços num Servidor Linux"
        elif nome_texto == Cadeiras_Nomes[21]:
            nome_texto = "Sistema Operativo Cliente"
        elif nome_texto == Cadeiras_Nomes[22]:
            nome_texto = "Sistema Operativo Servidor"
        elif nome_texto == Cadeiras_Nomes[23]:
            nome_texto = "Sistemas Operativos Open Source"
        elif nome_texto == Cadeiras_Nomes[24]:
            nome_texto = "Sistema Operativo Servidor Open Source"
        elif nome_texto == Cadeiras_Nomes[25]:
            nome_texto = "Gestão e Manipulação Avançada de Aplicações Informáticas de Processamento de Texto"
        elif nome_texto == Cadeiras_Nomes[26]:
            nome_texto = "Gestão e Manipulação Avançada de Aplicações Informáticas de Folha de Cálculo"
        elif nome_texto == Cadeiras_Nomes[27]:
            nome_texto = "Primeiros Conceitos de Programação e Algoritmia e Estruturas de Controlo num Programa Informático"
        elif nome_texto == Cadeiras_Nomes[28]:
            nome_texto = "Programação Estruturada e Tipos de Dados"
        elif nome_texto == Cadeiras_Nomes[29]:
            nome_texto = "Programação Orientada a Objetos – Introdução"
        elif nome_texto == Cadeiras_Nomes[30]:
            nome_texto = "Estrutura de Dados Estática, Composta e Dinâmica"
        elif nome_texto == Cadeiras_Nomes[31]:
            nome_texto = "Análise de Sistemas e Estruturação de Bases de Dados"
        elif nome_texto == Cadeiras_Nomes[32]:
            nome_texto = "Criação de Estrutura de Base de Dados em SQL"
        elif nome_texto == Cadeiras_Nomes[33]:
            nome_texto = "Programação em SQL"
        elif nome_texto == Cadeiras_Nomes[34]:
            nome_texto = "Metodologia de Projecto"
        elif nome_texto == Cadeiras_Nomes[35]:
            nome_texto = "Redes Informáticas"
        elif nome_texto == Cadeiras_Nomes[36]:
            nome_texto = "Programação para Dispositivos Móveis I"
        elif nome_texto == Cadeiras_Nomes[37]:
            nome_texto = "Animação 3D"
        elif nome_texto == Cadeiras_Nomes[38]:
            nome_texto = "Algoritmos e Estruturas de Dados"
        elif nome_texto == Cadeiras_Nomes[39]:
            nome_texto = "Bases de Dados"
        elif nome_texto == Cadeiras_Nomes[40]:
            nome_texto = "Arquitetura de Dispositivos Móveis"
        elif nome_texto == Cadeiras_Nomes[41]:
            nome_texto = "Interação com Dispositivos Móveis"
        elif nome_texto == Cadeiras_Nomes[42]:
            nome_texto = "Ferramentas Gráficas"
        elif nome_texto == Cadeiras_Nomes[43]:
            nome_texto = "UX/UI Design"
        elif nome_texto == Cadeiras_Nomes[44]:
            nome_texto = "Programação Web"
        elif nome_texto == Cadeiras_Nomes[45]:
            nome_texto = "Marketing Digital"
        elif nome_texto == Cadeiras_Nomes[46]:
            nome_texto = "Gaming"
        elif nome_texto == Cadeiras_Nomes[47]:
            nome_texto = "Projeto"
        elif nome_texto == Cadeiras_Nomes[48]:
            nome_texto = "Sociologia das Organizações"
        elif nome_texto == Cadeiras_Nomes[49]:
            nome_texto = "Aplicações de Gestão"
        elif nome_texto == Cadeiras_Nomes[50]:
            nome_texto = "Cálculo Financeiro"
        elif nome_texto == Cadeiras_Nomes[51]:
            nome_texto = "Aplicações Informáticas de Folha de Cálculo"
        elif nome_texto == Cadeiras_Nomes[52]:
            nome_texto = "Marketing"
        elif nome_texto == Cadeiras_Nomes[53]:
            nome_texto = "Administração de Redes"
        elif nome_texto == Cadeiras_Nomes[54]:
            nome_texto = "Higiene e Segurança no Trabalho"
        elif nome_texto == Cadeiras_Nomes[55]:
            nome_texto = "Direito e Fiscalidade das Empresas"
        elif nome_texto == Cadeiras_Nomes[56]:
            nome_texto = "Introdução à Ciência dos Computadores"
        elif nome_texto == Cadeiras_Nomes[57]:
            nome_texto = "Redes e Comunicação de Dados"
        elif nome_texto == Cadeiras_Nomes[58]:
            nome_texto = "Auditoria e Segurança Informática"
        elif nome_texto == Cadeiras_Nomes[59]:
            nome_texto = "Gestão de Projetos"
        elif nome_texto == Cadeiras_Nomes[60]:
            nome_texto = "Comunicação, Visualização e Ferramentas Gráficas"
        elif nome_texto == Cadeiras_Nomes[61]:
            nome_texto = "Programação Criativa e Artes Interativas"
        elif nome_texto == Cadeiras_Nomes[62]:
            nome_texto = "Animação Multimédia e Videojogos"
        elif nome_texto == Cadeiras_Nomes[63]:
            nome_texto = "Programação Multimédia e de Dispositivos Móveis"
        elif nome_texto == Cadeiras_Nomes[64]:
            nome_texto = "Computação Gráfica e Animação 3D"
        elif nome_texto == Cadeiras_Nomes[65]:
            nome_texto = "Técnicas de Design e Web Design"
        elif nome_texto == Cadeiras_Nomes[66]:
            nome_texto = "Criação e Tratamento Digital de Fotografia, Som e Vídeo"
        elif nome_texto == Cadeiras_Nomes[67]:
            nome_texto = "Sistemas de Informação e Marketing Digital"
        elif nome_texto == Cadeiras_Nomes[68]:
            nome_texto = "Ferramentas de Autor Multimédia"
        else:
            nome_texto = "<Módulo não Identificado>"
    else:
        nome_texto = "<Módulo não Identificado>"
    return nome_texto
    