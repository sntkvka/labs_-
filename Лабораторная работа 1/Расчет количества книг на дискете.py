# TODO Найдите количество книг, которое можно разместить на дискете
disk_volume = 1.44
page_number = 100
string_number = 50
symb_number = 25
symb_stor = 4 #in bites
book_stor = symb_number*string_number*page_number*symb_stor
book_stor_mb = book_stor/1024/1024
book_number = disk_volume//book_stor_mb
print("Количество книг, помещающихся на дискету:", int(book_number))
