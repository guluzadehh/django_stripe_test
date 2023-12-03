# Test Django Stripe Project

<b>Использование:</b>

Сперва, заполните файл <i>.env</i> в папке <i>app/</i>

Далее, запустите следующую программу:
  
    cd app/ &&  docker compose up --build

С помощью админ панеля создайте модели <i>Item</i>, <i>Order</i>, <i>Discount</i>: http://localhost:8000/admin/

Чтобы проверить покупку <i>Item</i> или <i>Order</i>, зайдите на следующие ссылки, указав <b>id</b> моделя:

http://localhost:8000/items/{ITEM_ID}/

http://localhost:8000/orders/{ORDER_ID}/

Нажмите кнопку Buy и вы будете переведены на страницу покупки.
