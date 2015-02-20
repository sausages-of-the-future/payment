(function() {
	var selectCard = document.getElementById('select-card');
	selectCard.addEventListener("change", function(){
		var show_card = (selectCard.value == "card");
		var inputs = document.getElementsByClassName('form-control');
		for (var i = 0; i < inputs.length; i++) {
			inputs[i].style.display = show_card ? 'none' : 'block';
		}
		var labels = document.getElementsByClassName('control-label');
		for (var i = 0; i < labels.length; i++) {
			labels[i].style.display = show_card ? 'none' : 'block';
		}
	});
})();
