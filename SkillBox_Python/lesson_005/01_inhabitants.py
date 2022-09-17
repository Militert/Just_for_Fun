# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks as f1
from room_2 import folks as f2

for name in f1:
    print(f'В комнате room_1 живут: {name}')

for name in f2:
    print(f'В комнате room_2 живут: {name}')
