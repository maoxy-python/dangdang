from car import Cart as C

def car(request):
    bookid = request.GET.get('bookid')
    cart = request.Session.get('cart')
    if cart:
        cart.add_car(bookid)
        request.Session['cart']=cart
    else:
        cart = C()
        cart.add_car(bookid)
        request.Session['cart']=cart


def demo(request):

    print("123")
    print("11111")
    print("11111")
    print("11111")

def demo2(request):

    pass

