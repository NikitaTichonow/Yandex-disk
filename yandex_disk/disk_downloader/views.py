from django.core.cache import cache
from django.shortcuts import render

from .api import get_public_files
from .forms import PublicKeyForm
from .utils import get_file_type


# Функция получения списка файлов с Яндекс.Диска
def file_list_view(request):
    form = PublicKeyForm(request.POST or None)
    files = []

    if request.method == "POST" and form.is_valid():
        public_key = form.cleaned_data["public_key"]
        cache_key = f"yandex_disk_files_{public_key}"
        files = cache.get(cache_key)

        if files is None:
            data = get_public_files(public_key)
            if data and "_embedded" in data:  # Проверка на наличие файлов в публичной ссылке
                files = data["_embedded"]["items"]
                # Сохраняем список файлов в кэш на 10 минут
                cache.set(cache_key, files, timeout=600)


    return render(
        request,
        "disk/base.html",
        {"form": form, "files": files},
    )
