from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Usuario  
from .form import UsuarioForm  
from django.contrib.auth.models import User



# Vista para la página principal (home)
def home(request):
    return render(request, 'home.html')

# crear un nuevo usuario
def signup(request):
    if request.method == "POST":
        # Obtener datos del formulario
        username = request.POST.get('username', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '').strip()
        name = request.POST.get('name', '').strip()
        surname = request.POST.get('surname', '').strip()
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()

        # Validar que todos los campos obligatorios estén completos
        if not username:
            return render(request, 'signup.html', {
                'form': UsuarioForm(),
                'error': 'El campo "username" es obligatorio.'
            })
        
        if not email:
            return render(request, 'signup.html', {
                'form': UsuarioForm(),
                'error': 'El campo "email" es obligatorio.'
            })

        # Validar que las contraseñas coincidan
        if password1 != password2:
            return render(request, 'signup.html', {
                'form': UsuarioForm(),
                'error': 'Las contraseñas no coinciden.'
            })

        try:
            # Crear usuario en el modelo User de Django
            user = User.objects.create_user(username=username, password=password1, email=email)
            user.save()

            # Crear registro en el modelo Usuario
            Usuario.objects.create(
                email=email,
                name=name,
                surname=surname,
                phone=phone,
                address=address,
            )

            return redirect('login')  # Redirige al login después de registrar el usuario
        except Exception as e:
            return render(request, 'signup.html', {
                'form': UsuarioForm(),
                'error': f'Ocurrió un error: {str(e)}'
            })

    return render(request, 'signup.html', {
        'form': UsuarioForm()
    })

# perfil del usuario
#@login_required
def perfil_usuario(request):
    return render(request, 'perfil_usuario.html', {'usuario': request.user})

# editar los datos del perfil del usuario
@login_required
def editar_perfil(request):
    usuario = request.user  # Obtener el usuario logueado

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)  # Usar el formulario de UsuarioForm para editar
        if form.is_valid():
            form.save()  # Guardar los cambios en el modelo Usuario
            return redirect('perfil_usuario')  # Redirigir al perfil después de guardar
    else:
        form = UsuarioForm(instance=usuario)  # Cargar el formulario con los datos actuales del usuario

    return render(request, 'editar_perfil.html', {'form': form})

# eliminar el usuario
@login_required
def eliminar_usuario(request):
    if request.method == 'POST':
        usuario = request.user  # Obtener el usuario logueado
        usuario.delete()  # Eliminar al usuario
        logout(request)  # Desloguear al usuario después de eliminar su cuenta
        return redirect('home')  # Redirigir a la página principal después de eliminar la cuenta

    return render(request, 'eliminar_usuario.html')



"""def get_all_usuarios():
    usuarios = Usuario.objects.all().order_by('')
    usuario_serializers = UsuarioSerializer(usuarios, many=True)
    return usuario_serializers.data


def index(request):
    usuarios = get_all_usuarios()
    return render(request, 'index_usuario.html', {'usuarios': usuarios})


def usuarios_rest(request):
    usuarios = get_all_usuarios()
    return JsonResponse(usuarios, safe=False)


def users_rest(request):
    return JsonResponse("Ok", safe=False)


def add_usuario_view(request):
    
     if request.method == 'POST':
         usuario_form = UsuarioForm(request.POST)
         if usuario_form.is_valid():
             usuario = usuario_form.save()
             return redirect('usuarios')
     if request.method == 'GET':
         usuario_form = UsuarioForm()
         csrf_token = get_token(request)
         html_form = f
             <form method="post">
             <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                 {usuario_form.as_p()}
                 <button type="submit">Submit</button>
             </form>
         
         return HttpResponse(html_form)

class NewUsuarioView(CreateView):
    form_class = UsuarioForm
    template_name = 'form_usuario.html'
    success_url = '/index_usuario/'


class NewUserView(CreateView):
    form_class = UsuarioForm
    template_name = 'form_usuario.html'
    success_url = '/'
"""