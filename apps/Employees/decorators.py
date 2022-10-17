from django.http import HttpResponse
from django.shortcuts import redirect

# Función o decorador que no permite a los usuarios logueados acceder a la página de login
def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('welcomePage')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

# Función o decorador que solo permite a ciertos grupos de usuarios acceder a ciertas páginas
def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator