from django.shortcuts import render, get_object_or_404
from .models import Produto


# Create your views here.
def index(request):
    """
    print(f'\nO QUE POSSO FAZER COM REQUEST: {dir(request)}\n')
    print(f'\n \033[36mCOOKIES:\033[m {request.COOKIES} \n')
    print(f'\n \033[36mFILES:\033[m {request.FILES} \n')
    print(f'\n \033[36mGET:\033[m {request.GET} \n')

    print('\n \033[36mMETA:\033[m \n')
    meta = request.META
    for chave, valor in meta.items():
        print(f'\033[36m{chave}:\033[m {valor}')

    print(f'\n \033[36mPOST:\033[m {request.POST} \n')
    print(f'\n \033[36mACCEPTED TYPES:\033[m {request.accepted_types} \n')
    print(f'\n \033[36mACCEPTS:\033[m {request.accepts} \n')
    print(f'\n \033[36mBODY:\033[m {request.body} \n')
    print(f'\n \033[36mCONTENT PARAMS:\033[m {request.content_params} \n')
    print(f'\n \033[36mCONTENT TYPE:\033[m {request.content_type} \n')
    print(f'\n \033[36mENCODING:\033[m {request.encoding} \n')
    print(f'\n \033[36mGET HOST:\033[m {request.get_host} \n')
    print(f'\n \033[36mGET PORT:\033[m {request.get_port} \n')

    print(f'\n \033[36mHEADERS:\033[m \n')
    header = request.headers
    for chave, valor in header.items():
        print(f'\033[36m{chave}:\033[m {valor}')

    print(f'\n \033[36mIS AJAX:\033[m {request.is_ajax} \n')
    print(f'\n \033[36mMETHOD:\033[m {request.method} \n')
    print(f'\n \033[36mPATH:\033[m {request.path} \n')
    print(f'\n \033[36mPATH INFO:\033[m {request.path_info} \n')
    print(f'\n \033[36mREAD:\033[m {request.read} \n')
    print(f'\n \033[36mSCHEME:\033[m {request.scheme} \n')
    print(f'\n \033[36mSESSION:\033[m {request.session} \n')
    print(f'\n \033[36mUPLOAD HANDLERS:\033[m {request.upload_handlers} \n')
    print(f'\n \033[36mUSER:\033[m {request.user} \n')
    """

    # nome do usuário logado:
    nome_usuario_logado = request.user

    # listando todos os objetos do banco
    produtos = Produto.objects.all()

    # pegando o primeiro / ultimo
    primeiro_produto = Produto.objects.first()
    ultimo_produto = Produto.objects.last()

    # contando quantos registros existem
    quantidade = Produto.objects.count()

    # ordenado pelo nome
    ordem = Produto.objects.order_by('nome')

    # lista inversa
    inversa = Produto.objects.reverse()

    context = {
        'curso': 'Django',
        'plataforma': 'Udemy',
        'nome_usuario': nome_usuario_logado,
        'produtos': produtos,
        'primeiro': primeiro_produto,
        'ultimo': ultimo_produto,
        'quantidade_de_produto': quantidade,
        'ordem': ordem,
        'inversa': inversa,
    }

    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, id):
    """
    Função que recebe id como parâmetro,
    Faz a consulta ao objeto do banco onde o id for igual ao id recebido na url,
    Variável recebe um objeto Produto,
    Converto para dicionário e retorno o mesmo para se acessado na página produto.html
    """
    # consultando no banco pelo id recebido
    #consulta_produto = Produto.objects.get(id=id)

    # faz a consulta usando o módulo get object 404, do tipo Produto, onde o id é igual ao recebido por parâmetro.
    # Se encontrar, retorna o objeto, se não, o objeto não existe e redirecione o usuário pra página 404.
    consulta_produto = get_object_or_404(Produto, id=id)

    # transformando resposta do id pra um dicionário
    context = {
        'produto': consulta_produto
    }
    return render(request, 'produto.html', context)
