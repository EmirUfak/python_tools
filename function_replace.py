
x = " aşağıdan yukarıya yükseliyor , AŞAĞIDAN YUKARIYA YUKSELİYOR"

print("Önce:", x)

x = x.replace("ç","c")    # stringdeki karakteri belirlediğiniz diğer karakterle değiştirir. 
x = x.replace("Ç","C")    # Bu örnekte türkçe harflerden kurtulmak için kullanılmış.
x = x.replace("ö","o")
x = x.replace("Ö","O")
x = x.replace("ü","u")
x = x.replace("Ü","U")
x = x.replace("ı","i")
x = x.replace("İ","I")
x = x.replace("ğ","g")
x = x.replace("ş","s")
x = x.replace("Ş","S")

print("Sonra:", x)
