$(document).ready(function(){
 $('.header').height($(window).height());
})
function check(){
  if (document.form1.nick.value =='')
  {
	alert('Введите ник!');
	return false;
  }
  if (document.form1.contact.value =='')
  {
	alert('Введите контакт!');
	return false;
  }
  if (document.getElementById('a').checked==false) {
	  alert('Вы не согласны с правилами сервера!');
  }
}