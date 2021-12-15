def simple_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        if not request.path == "confirm":
            try:
                print(Cliente.objects.get(usuario_id=request.user.id))
            except Cliente.DoesNotExist:
                return redirect('login')
        return response
    return middleware