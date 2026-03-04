function setBlind(image, id){
    var blind = document.getElementById("blind");
    blind.src = image;
    var inp = document.getElementById("textile-id")
    inp.value = id
}
function setKant(image, id){
    var kant = document.getElementById("kant");
    kant.src = image;
    var inp = document.getElementById("kant-id")
    inp.value = id
}
function updateLabelHeight(height){
    var label = document.getElementById('height-label');
    label.textContent = "Высота: " + height; 
}
function updateLabelWidth(width){
    var label = document.getElementById('width-label');
    label.value = "Ширина: " + width; 
}

