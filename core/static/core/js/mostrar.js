var myButton = document.getElementById("btn-opcion");
var myOption = document.getElementById("myOption");
myButton.addEventListener("click", function(){
if (myOption.style.display === "none") {
    myOption.style.display = "block";
} else {
    myOption.style.display = "none";
}
});

var myButton2 = document.getElementById("btn-opcion2");
var myOption2 = document.getElementById("myOption2");
myButton2.addEventListener("click", function(){
    if (myOption2.style.display === "none") {
        myOption2.style.display = "block";
    } else {
        myOption2.style.display = "none";
    }
});
