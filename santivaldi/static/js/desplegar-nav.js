document.addEventListener('DOMContentLoaded', function () {
	var menuIcon = document.getElementById('menuIcon');
	var menu = document.querySelector('.menu');
		
	menuIcon.addEventListener('click', function () {
	menu.classList.toggle('active');
				});
	});
		