def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # вызовем inner_function внутри test_function, здесь ничего не происходит

# вызовем inner_function()
inner_function()
# выводит ошибку name 'inner_function' is not defined. Did you mean: 'test_function'?
# вызовем test_function()
test_function()   # только так работает