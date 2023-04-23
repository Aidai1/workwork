from django.db import models




class Organizations(models.Model):
    group = models.CharField(max_length=100, verbose_name='Организация')
    email = models.EmailField(max_length=50, verbose_name='Почта')
    qrcode = models.ImageField()

    def __str__(self) -> str:
        return self.group
    def __str__(self) -> str:
        return self.email

class User_work(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Имя')
    organization = models.ForeignKey(Organizations, on_delete=models.CASCADE, related_name='user_organizations', blank=True, null=True, verbose_name='Организация ')
    login = models.EmailField(max_length=70, verbose_name='Логин')
    passvord = models.CharField(max_length=50, verbose_name='Пароль')

    def __str__(self) -> str:
        return self.name
    def __str__(self) -> str:
        return self.last_name
    def __str__(self) -> str:
        return self.organization
    def __str__(self) -> str:
        return self.login


class Organization_defaulr_wt(models.Model):
    description = models.TextField()
    name = models.ForeignKey(Organizations, on_delete=models.CASCADE )
    start_time = models.DateField(auto_created=True,verbose_name='Время посешение' )
    end_time = models.DateField(auto_created=True,verbose_name='Время выхода' )

    def __str__(self) -> str:
        return self.name
    


    
class Work_time(models.Model):
    user = models.ForeignKey(User_work, on_delete=models.CASCADE, related_name='user_work', blank=True, null=True, verbose_name='USER')
    organization = models.ForeignKey(Organizations, on_delete=models.CASCADE,  blank=True, verbose_name='Организация')
    start_time = models.DateField(auto_now_add=True,verbose_name='Время посещение')
    end_time = models.DateField(auto_now_add=True, verbose_name='Время выхода')
    created_ad = models.DateField(auto_now_add=True, verbose_name='Время добовление')

    def __str__(self) -> str:
        return self.start_time
    def __str__(self) -> str:
        return self.end_time


class UserList(models.Model):
    name = models.CharField(max_length=70, verbose_name='Имя', unique=True, null=True, blank=True)
    last_name = models.CharField(max_length=70, verbose_name='Фамилия')  
    organization = models.ForeignKey(Organizations,on_delete=models.CASCADE, max_length=70)
    salary = models.CharField(max_length=100, verbose_name='Зарплата') 

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена' 



