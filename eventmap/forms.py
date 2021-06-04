from django import forms
from django.forms.forms import Form
from.models import Visit
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=54,
        help_text='※有効なメールアドレスを入力してください。',
        label='Eメールアドレス'
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1',)

class UserForm(forms.Form):
    prefect = (
        ('北海道', '北海道'),
        ('青森県','青森県'),
        ('岩手県', '岩手県'),
        ('宮城県', '宮城県'),
        ('秋田県', '秋田県'),
        ('山形県', '山形県'),
        ('福島県', '福島県'),
        ('茨城県', '茨城県'),
        ('栃木県', '栃木県'),
        ('群馬県', '群馬県'),
        ('埼玉県', '埼玉県'),
        ('千葉県', '千葉県'),
        ('東京都', '東京都'),
        ('神奈川県', '神奈川県'),
        ('新潟県', '新潟県'),
        ('富山県', '富山県'),
        ('石川県', '石川県'),
        ('福井県', '福井県'),
        ('山梨県', '山梨県'),
        ('長野県', '長野県'),
        ('岐阜県', '岐阜県'),
        ('静岡県', '静岡県'),
        ('愛知県', '愛知県'),
        ('三重県', '三重県'),
        ('滋賀県', '滋賀県'),
        ('京都府', '京都府'),
        ('大阪府', '大阪府'),
        ('兵庫県', '兵庫県'),
        ('奈良県', '奈良県'),
        ('和歌山県', '和歌山県'),
        ('鳥取県', '鳥取県'),
        ('島根県', '島根県'),
        ('岡山県', '岡山県'),
        ('広島県', '広島県'),
        ('山口県', '山口県'),
        ('徳島県', '徳島県'),
        ('香川県', '香川県'),
        ('愛媛県', '愛媛県'),
        ('高知県', '高知県'),
        ('福岡県', '福岡県'),
        ('佐賀県', '佐賀県'),
        ('長崎県', '長崎県'),
        ('熊本県', '熊本県'),
        ('大分県', '大分県'),
        ('宮崎県', '宮崎県'),
        ('鹿児島県', '鹿児島県'),
        ('沖縄県', '沖縄県'),
    )

    prefecture = forms.ChoiceField(
        label='都道府県',
        widget=forms.Select,
        choices=prefect

    )
    place = forms.CharField(
        label='寄った名所、地名など',
        max_length=50,
    )
    startrip = forms.DateField(widget=forms.SelectDateWidget(years=[x for x in range(2000, 2028)]),label='旅行開始日')
    endtrip = forms.DateField(widget=forms.SelectDateWidget(years=[x for x in range(2000, 2028)]),label='旅行終了日')
    photo = forms.ImageField(label='お気に入りの一枚')
    comment = forms.CharField(
        label='コメント',
        widget=forms.Textarea,
        max_length=200,
    )
    
    def url(self):
        return self.photo.url

class ConectForm(forms.Form):
    subject = forms.CharField(label='件名', max_length=10)
    name = forms.CharField(label='name')
    mail = forms.EmailField(label='mail', help_text="※ご確認のうえ、正しく入力してください")
    text = forms.CharField(label='text',widget=forms.Textarea)

