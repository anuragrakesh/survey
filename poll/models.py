from django.db import models


class Register(models.Model):
    rid = models.AutoField
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    e_mail = models.EmailField()
    m_no = models.IntegerField(null=False, default=False)
    sex = models.CharField(max_length=20, choices=(('f', 'female'),
                                                   ('m', 'male')))
    dob = models.DateField()

    def __str__(self):
        return self.f_name


class Question(models.Model):
    ques_no = models.AutoField
    ques_desc = models.CharField(max_length=100)
    opa = models.CharField(max_length=100, default='')
    opb = models.CharField(max_length=100, default='')
    opc = models.CharField(max_length=100, default='')
    opd = models.CharField(max_length=100, default='')
    ans = models.CharField(max_length=100, default='')

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.ques_desc, self.opa, self.opb, self.opc, self.opd, self.ans)









