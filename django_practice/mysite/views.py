from django.shortcuts import render, redirect
from .models import Memo


def memo_list(request):
    # メモの一覧を表示するビュー
    memos = Memo.objects.all().order_by('id')
    return render(request, 'memo_list.html', {'memos': memos})

