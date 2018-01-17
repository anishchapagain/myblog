function login(event) {
	event.preventDefault()
	form = document.getElementById('login-form')

	url = form.action

	form_data = new FormData(form)

	var xhr = new XMLHttpRequest()
	xhr.open('POST', url)
	xhr.send(form_data)
}