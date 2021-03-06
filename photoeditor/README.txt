Endpoints list:

'list/' - список всех редактированных изображений

'resize/' - изменяет размеры загруженного изображения
в поле image загружается фотография, width, height -
ширина и высота которые приобретет исходная фотограяи

'scale/' - меняет размер изображения, сохраняя пропорции.
масштабирует изображение до максимально возможного
размера, который не превосходит заданные значения width и height.

'scale/<str:scaling>' - увеличивает или уменьшает изображение.
Если scaling = 2, то картина увеличится в два раза,
если scaling = 0.5, то картина уменьшится в два раза

'crop/' - обрезает изображение
left, upper, right, lower - разность соответствующих сторон
между исходным изображением и полученным. Например,
left обозначает на сколько пикселей нужно обрезать
изображение от ее левой стороны, upper - верхней и т.д
Если с какой стороны обрезать не нужно, то ее значение
ставится равным 0.

'reverse/' - зеркально отображает изоюражение по горизонтали

'rotate/<int:angle>' - поворачивает изображение на angle градусов влево

'filters/' - накладывает фильтр на изображение в зависимости
от введенного значение filter.
filter принимает следующие значеия:
    'white-black': to_white_black,
    'blue': to_blue,
    'negative': negative,
    'blur': blur, можно задать атрибут 'radius' (целое число), который отвечает за радиус размытия
    'contour': contour,
    'detail': detail,
    'emboss': emboss,
    'edge_enhance': edge_enhance,
    'find_edges': find_edges,
    'cartoonize': cartoonize,
    'oil_painting': oil_painting,  можно задать атрибут 'dst' (целое число), который отвечает за ясность деталей изображения

Значениями ключей являются функции производящие фильтрацию

Пример запроса к API:
(Запрос генерирован приложением Postman)

curl --location --request POST 'http://127.0.0.1:8000/api/filters/' \
--form 'image=@"7tHwD-evN/bwEhW3D3Gsw.jpg"' \
--form 'width="500"' \
--form 'height="800"' \
--form 'filter="oil_painting"' \
--form 'left="200"' \
--form 'upper="200"' \
--form 'right="200"' \
--form 'lower="200"'

Перед тем как тестировать выполните следующие команды:

python3 manage.py makemigrations
python3 manage.py migrate
