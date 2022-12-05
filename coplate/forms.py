from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        # fields를 리스트업하지 않고 하나씩 추가해주면 마지막 fields만 뜨게 되므로 주의! (ex_ address 필드만 뜨게 됨)
        fields = ["nickname", "kakao_id", "address"]

    def signup(self, request, user): # form으로 입력받는 데이터를 유저 인스턴스에 저장
        user.nickname = self.cleaned_data["nickname"]
        user.kakao_id = self.cleaned_date["kakao_id"]
        user.address = self.cleaned_data["address"]
        
        user.save()