# from django.forms import ModelForm
# from .models import Review


# class ReviewForm(ModelForm):
#     class Meta:
#         model = Review
#         fields = ['body']
#
#         labels = {
#             'body': 'Добавьте комментарий'
#         }
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         for field in self.fields.items():
#             field.widget.attrs.update({'class': 'input'})
