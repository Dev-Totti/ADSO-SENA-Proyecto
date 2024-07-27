from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe

from userauths.models import User


def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.address


class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat")
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="category", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe(f'<img src="{self.image.url}" height="50" width="50">')

    def __str__(self):
        return self.name


class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="prd")

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="product", null=True, blank=True)

    price = models.DecimalField(decimal_places=0, max_digits=10)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(decimal_places=0, max_digits=10, null=True, blank=True)

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)

    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def product_image(self):
        return mark_safe(f'<img src="{self.image.url}" height="50" width="50">')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images")

    class Meta:
        verbose_name_plural = "Product Images"

    def product_image(self):
        return mark_safe(f'<img src="{self.image.url}" height="50" width="50">')

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Carrito de {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = "Cart Items"

    def __str__(self):
        return f"{self.product.name} en el carrito de {self.cart.user.username}"

    def total_price(self):
        return self.product.price * self.quantity


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(decimal_places=0, max_digits=10)
    shipping = models.DecimalField(decimal_places=0, max_digits=10)
    tax = models.DecimalField(decimal_places=0, max_digits=10)
    total = models.DecimalField(decimal_places=0, max_digits=10)

    def __str__(self):
        return f"Orden de {self.user.username}"

    def calculate_total(self):
        self.total = self.subtotal + self.shipping + self.tax
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=0, max_digits=10)

    class Meta:
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"{self.product.name} en la orden de {self.order.user.username}"
