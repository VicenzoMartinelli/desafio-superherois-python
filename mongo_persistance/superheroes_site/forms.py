from django import forms

class CrudHeroesForm(forms.Form):

	name = forms.CharField(required=True)
	description = forms.CharField(required=False)

	def is_valid(self):

		valid = True

		if not super(CrudHeroesForm, self).is_valid():
			self.adiciona_erro('Por favor, verifique os dados informados')
			valid = False

		# user_exists = User.objects.filter(username=self.data['nome']).exists()
		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)