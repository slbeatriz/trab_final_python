from fpdf import FPDF

class PDF(FPDF):

    def doc_title(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln()

    def doc_text(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 7, text)
        self.ln()

    def doc_img(self, img, x, y, w, h):
        self.image(img, x, y, w, h)

pdf = PDF()
pdf.add_page()

pdf.doc_title("Breve Análise das Desigualdades Sociais na Educação")

pdf.doc_text("A educação superior no Brasil reflete não apenas o acesso ao conhecimento avançado, mas também espelha as profundas desigualdades presentes na sociedade. Ao explorar as instituições de ensino superior, uma divisão clara emerge entre as instituições públicas e privadas, destacando disparidades em diversos aspectos. As instituições públicas, muitas vezes, enfrentam uma demanda significativamente maior do que a capacidade de oferta de vagas. Isso resulta em processos seletivos altamente competitivos, onde apenas uma parcela dos candidatos consegue acesso. Por outro lado, instituições privadas, embora variem em prestígio, geralmente têm mais flexibilidade para aumentar o número de vagas e atender a uma demanda maior, o que justifica em partes o grande número de instituições privadas existentes, como podemos visualizar no gráfico abaixo, onde 84.4% das instituições de ensino superior no Brasil se concentram na categoria de privadas com fins lucrativos:")

pdf.doc_img("instituicoes.png", 80, 115, 60, 60)

pdf.ln(65)

pdf.doc_text("O grande número de instituições de ensino superior privadas no Brasil pode ser justificado por uma série de fatores históricos, sociais e econômicos. O Brasil passou por um crescimento populacional significativo nas últimas décadas. O aumento da população geralmente resulta em uma maior demanda por oportunidades educacionais, o que estimula a criação de mais instituições. As universidades públicas, apesar de oferecerem uma educação de qualidade, têm recursos limitados e enfrentam desafios financeiros recorrentes. O setor privado, então, surge para preencher essa lacuna, proporcionando mais vagas e opções de cursos. As instituições privadas muitas vezes têm mais flexibilidade para diversificar sua oferta de cursos e programas, adaptando-se rapidamente às mudanças nas demandas do mercado de trabalho. E outra questão relacionada a justificativa ao grande número e ingresso às instituições privadas tem conexão com ensino a distância que ganhou popularidade como uma opção flexível e acessível. Muitas instituições privadas investiram significativamente em programas de EaD para atender a um público mais amplo, especialmente em um país de dimensões continentais como o Brasil. ")

pdf.doc_text("É importante observar que, embora as instituições privadas desempenhem um papel vital na expansão do acesso à educação superior, é fundamental garantir que haja padrões de qualidade e fiscalização adequadas para garantir que todos os estudantes recebam uma educação de qualidade. O equilíbrio entre instituições públicas e privadas é crucial para um sistema educacional eficaz e equitativo. ")

pdf.doc_text("O aumento do número de ingresso de alunos em instituições de ensino superior na modalidade de tecnólogo no Brasil pode ser atribuído a vários fatores que refletem mudanças nas demandas do mercado de trabalho e nas preferências dos estudantes. No gráfico a seguir podemos observar uma grande concentração de alunos ingressados nos cursos de grau Tecnológico, ocupando uma porcentagem de 51%:")

pdf.ln(45)

pdf.doc_img("grau.png", 80, 115, 60, 60)

pdf.ln(45)

pdf.doc_text("O aumento do número de ingresso de alunos em instituições de ensino superior na modalidade de tecnólogo no Brasil pode ser atribuído a vários fatores que refletem mudanças nas demandas do mercado de trabalho e nas preferências dos estudantes. Algumas justificativas incluem o foco na Empregabilidade: onde os cursos tecnólogos são projetados para preparar os alunos para o mercado de trabalho de forma mais rápida e específica. Eles geralmente têm uma abordagem prática e orientada para as habilidades necessárias em setores específicos, o que atrai estudantes que buscam uma formação mais direcionada para a empregabilidade. Menor Duração do Curso que em comparação com cursos de bacharelado, os tecnólogos têm uma duração mais curta, geralmente entre dois e três anos. Isso atrai estudantes que desejam entrar no mercado de trabalho mais rapidamente. Especialização em Áreas em Crescimento onde muitos cursos tecnólogos são oferecidos em áreas específicas que estão em crescimento e têm demanda no mercado, como tecnologia da informação, gestão, logística, design, entre outros. Os estudantes veem essas áreas como promissoras em termos de oportunidades de emprego. A flexibilidade e Adaptação: os cursos tecnólogos são conhecidos por serem mais flexíveis em termos de estrutura curricular e podem se adaptar mais rapidamente às mudanças nas necessidades do mercado em comparação com cursos mais tradicionais. ")

pdf.doc_text("Aumento da Oferta na Educação a Distância EaD: muitos cursos tecnólogos são oferecidos na modalidade de educação a distância EaD, proporcionando uma opção flexível para estudantes que trabalham ou têm outras responsabilidades. As parcerias com o Setor Empresarial onde alguns cursos tecnólogos estabelecem parcerias diretas com empresas, proporcionando oportunidades de estágio e contato próximo com as demandas reais do mercado de trabalho. Isso atrai estudantes que valorizam experiências práticas. Também temos adaptação à Economia Digital com a crescente importância da economia digital, cursos tecnólogos relacionados à tecnologia da informação, ciência de dados, marketing digital e outros ganharam destaque devido à necessidade de profissionais qualificados nessas áreas. E por fim o reconhecimento do Mercado: gradualmente, o mercado de trabalho passou a reconhecer e valorizar mais os diplomas de tecnólogos, contribuindo para uma maior aceitação e demanda por esses profissionais em setores diversos. Esses fatores combinados refletem uma mudança nas preferencias dos estudantes e nas exigências do mercado de trabalho, levando a um aumento no número de ingresso de alunos em cursos tecnológicos no Brasil. Essa modalidade de ensino continua a evoluir para atender às necessidades dinâmicas de uma economia em transformação. ") 


pdf.output("educacao2.pdf")