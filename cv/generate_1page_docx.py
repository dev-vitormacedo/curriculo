import docx
from docx.shared import Pt, Inches, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def add_hyperlink(paragraph, url, text, color='004B91', underline=True):
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('r:id'), r_id)
    new_run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    if color:
        c = OxmlElement('w:color')
        c.set(qn('w:val'), color)
        rPr.append(c)
    if underline:
        u = OxmlElement('w:u')
        u.set(qn('w:val'), 'single')
        rPr.append(u)
    new_run.append(rPr)
    new_run.text = text
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)

doc = docx.Document()

# Adjust margins to 0.35 in top/bottom, 0.45 in left/right
for s in doc.sections:
    s.top_margin = Inches(0.35)
    s.bottom_margin = Inches(0.35)
    s.left_margin = Inches(0.45)
    s.right_margin = Inches(0.45)

# Normal style font
style_normal = doc.styles['Normal']
style_normal.font.name = 'Calibri'
style_normal.font.size = Pt(8.5)
style_normal.paragraph_format.line_spacing = 1.05
style_normal.paragraph_format.space_before = Pt(0)
style_normal.paragraph_format.space_after = Pt(1)

# Name
p_name = doc.add_paragraph()
r_name = p_name.add_run('Vitor Moraes Macedo')
r_name.bold = True
r_name.font.size = Pt(13)
p_name.paragraph_format.space_before = Pt(0)
p_name.paragraph_format.space_after = Pt(1)

# Contact links line 1
p_c1 = doc.add_paragraph()
add_hyperlink(p_c1, 'https://www.linkedin.com/in/o-vitormoraes/', 'https://www.linkedin.com/in/o-vitormoraes/')
p_c1.paragraph_format.space_before = Pt(0)
p_c1.paragraph_format.space_after = Pt(1)

# Contact links line 2
p_c2 = doc.add_paragraph()
p_c2.add_run('Novo Hamburgo, RS (disponível para mudança) | ')
add_hyperlink(p_c2, 'https://wa.me/5551986288741', '(51) 98628-8741')
p_c2.add_run(' | ')
add_hyperlink(p_c2, 'mailto:vitor.macedo.cs@outlook.com', 'vitor.macedo.cs@outlook.com')
p_c2.paragraph_format.space_before = Pt(0)
p_c2.paragraph_format.space_after = Pt(3.5)

def add_sec_title(title):
    p = doc.add_paragraph()
    r = p.add_run(title)
    r.bold = True
    r.font.size = Pt(9.5)
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(1)

# Resumo
add_sec_title('Resumo')
p_res = doc.add_paragraph()
p_res.add_run('Tenho mais de 18 anos de experiência na área comercial e de operações, com foco recente em Excelência Operacional, Treinamento & Desenvolvimento (T&D) e Sucesso do Cliente. Aplico Inteligência Artificial (IA) de forma contínua para acelerar a roteirização de treinamentos, síntese de POPs e automação de fluxos. Na Easybuilder e na Appmax reduzi o tempo de resolução de chamados de 2 dias para 4 horas (redução de 50% de SLA), estruturei mais de 5 POPs com apoio de IA, conduzi +20 monitorias ao vivo e reverti mais de 75% dos casos de churn e chargeback. Busco posições de Analista de Excelência Operacional e T&D.')
p_res.paragraph_format.space_before = Pt(0)
p_res.paragraph_format.space_after = Pt(3)

# Experiência
add_sec_title('Experiência')

jobs = [
    {
        'title': 'Analista de Excelência Operacional Pleno | Gerente de Comunidade - Easybuilder.com.br (EdTech e Plataforma No-Code)',
        'date': 'julho de 2026 - o momento (4 meses)',
        'bullets': [
            'Responsável pela coordenação do Bootcamp Setup Builder (180+ alunos), gestão de mentorias mensais, plantões semanais e +20 monitorias ao vivo via Google Meet e padronização de POPs operacionais;',
            'Utilizava Inteligência Artificial generativa, ClickUp (+400 tasks gerenciadas), Google Meet, Hotmart Club, Discord, WhatsApp e relatórios analíticos de dados;',
            'Consegui mediar tentativas de churn e chargeback com mais de 75% de êxito na reversão, elaborei +5 POPs operacionais com auxílio de IA e atuei com TI na ferramenta v2.0 validando mais de 50 melhorias contínuas.'
        ]
    },
    {
        'title': 'Analista de Treinamento e Desenvolvimento (T&D) | Customer Success - Easybuilder.com.br (EdTech e Plataforma No-Code)',
        'date': 'março de 2026 - julho de 2026 (4 meses)',
        'bullets': [
            'Responsável pelo mapeamento pedagógico, reformulação da grade de aulas dos produtos principais, roteirização com IA e gravação de aulas didáticas e onboarding de alunos;',
            'Utilizava IA generativa (ChatGPT/Claude/Gemini) para design instrucional ágil, Hotmart Club, softwares de gravação/edição de vídeo e planilhas de indicadores;',
            'Consegui gravar e editar mais de 30 aulas didáticas práticas com roteiros apoiados por IA, atender mais de 100 alunos com NPS >80% e gerar +300% de engajamento orgânico em desafio com 112 alunos.'
        ]
    },
    {
        'title': 'Analista de Qualidade e Sucesso do Cliente | Key Account Manager - Appmax (Fintech de Pagamentos e E-commerce)',
        'date': 'fevereiro de 2023 - janeiro de 2024 (1 ano)',
        'bullets': [
            'Responsável pela reestruturação do fluxo de chamados no Intercom entre Vendas, CS e Back Office e gestão high-touch de 20 a 30 Key Accounts e carteira com mais de 100 clientes;',
            'Utilizava Intercom Helpdesk, HubSpot CRM, plataformas de e-commerce (Shopify, Nuvemshop, Yampi) e dashboards de métricas;',
            'Consegui reduzir o tempo de solução de chamados de 2 dias para 4 horas (redução de 50% de SLA), zerar backlog de 100+ tickets, elevar NPS e CSAT, reduzir o churn em 20% e escalar faturamento de cliente de R$ 100k para R$ 1M/mês.'
        ]
    },
    {
        'title': 'Supervisor de Vendas e Operações Comerciais - Appmax (Fintech de Pagamentos e E-commerce)',
        'date': 'novembro de 2018 - fevereiro de 2023 (4 anos e 4 meses)',
        'bullets': [
            'Responsável pela supervisão, capacitação contínua, aplicação de feedbacks e acompanhamento de metas da equipe comercial (30 vendedores) e vendas consultivas;',
            'Utilizava CRM de vendas, planilhas de KPIs comerciais, Intercom e Discord;',
            'Consegui aumentar o desempenho da equipe em 40% com mais de 30 feedbacks mensais aplicados e atingi faturamento total de R$ 2.215.414,15 em vendas consultivas.'
        ]
    },
    {
        'title': 'Account Manager Key Account | Product Owner - Escola DNC & Saipos (Tecnologia, SaaS e Educação)',
        'date': 'fevereiro de 2025 - novembro de 2025 (10 meses)',
        'bullets': [
            'Responsável pela liderança de equipe de 5 pessoas na DNC na estruturação de processos de aquisição com OKRs, e gestão de Key Accounts na Saipos com diagnósticos operacionais;',
            'Utilizava Figma, frameworks Scrum/Kanban, Trello e ferramentas de benchmarking competitivo;',
            'Consegui mapear mais de 10 gargalos operacionais em clientes com mais de 50 unidades e atuar em parceria estratégica com o iFood para captação de grandes franquias.'
        ]
    }
]

for job in jobs:
    p_jt = doc.add_paragraph()
    r_jt = p_jt.add_run(job['title'])
    r_jt.bold = True
    r_jt.font.size = Pt(8.5)
    p_jt.paragraph_format.space_before = Pt(2.5)
    p_jt.paragraph_format.space_after = Pt(0)
    
    p_jd = doc.add_paragraph()
    r_jd = p_jd.add_run(job['date'])
    r_jd.font.size = Pt(7.8)
    r_jd.italic = True
    p_jd.paragraph_format.space_before = Pt(0)
    p_jd.paragraph_format.space_after = Pt(0.5)
    
    for b in job['bullets']:
        p_b = doc.add_paragraph()
        r_bullet = p_b.add_run('• ')
        r_bullet.bold = True
        r_b = p_b.add_run(b)
        r_b.font.size = Pt(7.8)
        p_b.paragraph_format.space_before = Pt(0)
        p_b.paragraph_format.space_after = Pt(0.5)
        p_b.paragraph_format.left_indent = Inches(0.12)

# Formação acadêmica e Cursos
add_sec_title('Formação acadêmica e Cursos')

edus = [
    {
        'title': 'Especialização / Formação em Growth e Métricas - Escola DNC',
        'date': 'fevereiro de 2025 - abril de 2025',
        'desc': 'Aprendi análise de dados, métricas de crescimento, testes A/B, OKRs e melhoria contínua de processos operacionais e quero colocar em prática esse conhecimento para ajudar na minha próxima empresa.'
    },
    {
        'title': 'Graduação em Marketing (CST) - Estácio',
        'date': 'março de 2018 - outubro de 2021',
        'desc': 'Aprendi sobre comportamento do cliente, estratégia de mercado e processos comerciais. Isso foi essencial para mim, quando na Appmax e na Easybuilder eu pude reestruturar processos de atendimento e treinamentos elevando os índices de NPS e retenção.'
    }
]

for edu in edus:
    p_et = doc.add_paragraph()
    r_et = p_et.add_run(edu['title'])
    r_et.bold = True
    r_et.font.size = Pt(8.5)
    p_et.paragraph_format.space_before = Pt(2)
    p_et.paragraph_format.space_after = Pt(0)
    
    p_ed = doc.add_paragraph()
    r_ed = p_ed.add_run(edu['date'])
    r_ed.font.size = Pt(7.8)
    r_ed.italic = True
    p_ed.paragraph_format.space_before = Pt(0)
    p_ed.paragraph_format.space_after = Pt(0)
    
    p_ex = doc.add_paragraph()
    r_ex = p_ex.add_run(edu['desc'])
    r_ex.font.size = Pt(7.8)
    p_ex.paragraph_format.space_before = Pt(0)
    p_ex.paragraph_format.space_after = Pt(1)

# Idiomas
add_sec_title('Idiomas')
langs = [
    'Inglês intermediário (entendo bem, leio documentações técnicas e consigo escrever)',
    'Espanhol básico (entendo conceitos básicos, mas não tenho facilidade de falar e escrever)',
    'Português fluente (nativo)'
]
for lang in langs:
    p_l = doc.add_paragraph()
    r_l_bullet = p_l.add_run('• ')
    r_l_bullet.bold = True
    r_l = p_l.add_run(lang)
    r_l.font.size = Pt(7.8)
    p_l.paragraph_format.space_before = Pt(0)
    p_l.paragraph_format.space_after = Pt(0.5)
    p_l.paragraph_format.left_indent = Inches(0.12)

try:
    doc.save(r'H:\Skills e repositórios\ai-job-search\cv\curriculo_vitor_macedo_1pagina.docx')
    print('Salvo em cv/curriculo_vitor_macedo_1pagina.docx')
except PermissionError:
    alt_path = r'H:\Skills e repositórios\ai-job-search\cv\curriculo_vitor_macedo_1pagina_atualizado.docx'
    doc.save(alt_path)
    print(f'Arquivo original em uso. Salvo com sucesso em: {alt_path}')
print('Script finished successfully')
