(function() {
    var selectCard = document.getElementById('select-card');
    selectCard.addEventListener("change", function(){
        var show_card = (selectCard.value == "card");
        var new_card_fields = document.getElementById('new-card')
        new_card_fields.style.display = show_card ? 'none' : 'block';
    });
})();
