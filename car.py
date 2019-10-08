class Cart_items():
    def __init__(self,book,count):
        # book是从数据库书籍详情表中查出来的QuerySet对象
        self.book = book
        self.count = count

class Cart():
    def __init__(self):
        self.total_price = 0
        self.save_price = 0
        # 列表存放的是Car_items对象
        self.cart_items = []
        self.del_items = []

    # 计算总价
    def sums(self):
        self.total_price = 0
        self.save_price = 0
        for i in self.cart_items:
            self.total_price += i.book.dprice * i.count
            self.save_price += (i.book.price-i.book.dprice)*i.count

    #增加商品
    def add_car(self,bookid):
        for i in self.cart_items:
            if i.book.booid == bookid:
                i.count += 1
                self.sums()
                return
        self.cart_items.append(Cart_items(Tbook.object.filter(bookid=bookid),1))
        self.sums()

    #删除商品
    def del_car(self,bookid):
        for i in self.cart_items:
            if i.book.bookid == bookid:
                self.cart_items.remove(i)
                self.del_items.append(Tbook.object.filter(bookid=bookid),i.count)
                self.sums()

    #修改商品
    def change_nums(self,bookid,nums):
        for i in self.cart_items:
            if i.book.bookid == bookid:
                i.count = nums
                self.sums()


    def index(self):
        pass

