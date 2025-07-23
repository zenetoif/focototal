# Script para popular dados de exemplo no Django
# Execute no shell: python manage.py shell < popular_dados.py

from app.models import Dica, MaterialApoio

# Criar algumas dicas de exemplo
dicas_exemplo = [
    {
        'titulo': 'Técnica Pomodoro',
        'conteudo': 'Divida seu tempo de estudo em blocos de 25 minutos com pausas de 5 minutos. Após 4 pomodoros, faça uma pausa maior de 15-30 minutos.'
    },
    {
        'titulo': 'Ambiente de Estudo',
        'conteudo': 'Mantenha seu local de estudo organizado, bem iluminado e livre de distrações. Um ambiente adequado aumenta significativamente a concentração.'
    },
    {
        'titulo': 'Revisão Espaçada',
        'conteudo': 'Revise o conteúdo em intervalos crescentes: 1 dia, 3 dias, 1 semana, 2 semanas. Esta técnica fortalece a memória de longo prazo.'
    }
]

for dica_data in dicas_exemplo:
    dica, created = Dica.objects.get_or_create(
        titulo=dica_data['titulo'],
        defaults={'conteudo': dica_data['conteudo']}
    )
    if created:
        print(f"Dica criada: {dica.titulo}")
    else:
        print(f"Dica já existe: {dica.titulo}")

# Criar alguns materiais de apoio de exemplo
materiais_exemplo = [
    {
        'titulo': 'Khan Academy - Matemática',
        'descricao': 'Plataforma gratuita com vídeos e exercícios de matemática para todos os níveis.',
        'link': 'https://pt.khanacademy.org/math',
        'imagem': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Khan_Academy_logo_2018.svg/200px-Khan_Academy_logo_2018.svg.png'
    },
    {
        'titulo': 'Coursera - Cursos Online',
        'descricao': 'Cursos online de universidades renomadas em diversas áreas do conhecimento.',
        'link': 'https://www.coursera.org',
        'imagem': 'https://about.coursera.org/static/whiteCoursera-23ec484f7a9925e5d248c0eb47eb6895.svg'
    },
    {
        'titulo': 'Duolingo - Idiomas',
        'descricao': 'Aprenda idiomas de forma divertida e gamificada com lições curtas e eficazes.',
        'link': 'https://www.duolingo.com',
        'imagem': 'https://d35aaqx5ub95lt.cloudfront.net/images/splash/owl.svg'
    }
]

for material_data in materiais_exemplo:
    material, created = MaterialApoio.objects.get_or_create(
        titulo=material_data['titulo'],
        defaults={
            'descricao': material_data['descricao'],
            'link': material_data['link'],
            'imagem': material_data['imagem']
        }
    )
    if created:
        print(f"Material criado: {material.titulo}")
    else:
        print(f"Material já existe: {material.titulo}")

print("Dados de exemplo criados com sucesso!")
